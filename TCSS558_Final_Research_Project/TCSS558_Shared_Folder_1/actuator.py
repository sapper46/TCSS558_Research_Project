import os
import psycopg2
import time
import argparse
from psycopg2 import extensions

# create an actuator class
class Actuator:
    def __init__(self, sector_letter, sector_number, actuator_script):
        
        # Get the sector letter and sector number so the actuator knows which database to access
        self.sector_letter = sector_letter
        self.sector_number = sector_number
        
        # Create the Actuator Name
        self.name=str(sector_letter)+str(sector_number)
        
        # Internalize the script for that sector
        self.actuator_script = actuator_script

        # Initialize the number of permissions at 0
        self.num_permissions = 0
        
        # Update the number of targets in sector from the script
        if actuator_script[0]=='.':
            self.num_targets=0
        elif actuator_script[0]=='T':
            self.num_targets=1
        # -------------- Update the text file
        self.update_sector_target_text_file()

        # Create the list to store the target time of presentation
        self.time_of_target_presentation_list = [] # when the target presented itself
        if self.num_targets == 1:
            # Store the time in seconds from epoch
            self.time_of_target_presentation_list.append(time.time())
        
        # Remove the first element of the actuator_script
        self.actuator_script.pop(0)

        # Initialize the permission list
        self.time_of_target_permission_list = []  

    def update_sector_target_text_file(self):
        # create the textfile self.name.txt
        with open(f"{self.name}.txt", "w") as file:
            # write self.num_targets to the file
            #file.write(f"{self.num_targets-self.num_permissions}\n")
            file.write(f"{self.num_targets}\n")
        # close the file
        file.close()        

    def update_sector_permissions(self):
        conn = connect_to_db(self.sector_letter)
        if not conn:
            return

        cursor = conn.cursor()

        try:
            query = f"SELECT {self.sector_letter} FROM permission_table WHERE id = {self.sector_number}"
            cursor.execute(query)
            result = cursor.fetchone()

            if result:
                print(f'Successfully queried sector permissions table and I read: {result[0]}')
                target_delta = result[0] - self.num_permissions
                if target_delta > 0:     
                    for x in range(target_delta):
                        # Store the time in seconds from epoch
                        self.time_of_target_permission_list.append(time.time())
                
                self.num_permissions = result[0]

        except Exception as error:
            print(f"Error updating sector permissions: {error}")
        finally:
            cursor.close()
            conn.close()
        
    def read_next_target_from_script(self):
        if self.actuator_script[0]=='.':
            pass
        elif self.actuator_script[0]=='T':
            self.num_targets+=1
            # -------------- Update the text file
            self.update_sector_target_text_file()
            # Store the time in seconds from epoch
            self.time_of_target_presentation_list.append(time.time())
        self.actuator_script.pop(0)    

    def report_statistics(self):
        print(f'Number of targets: {self.num_targets}')
        print(f'Number of targets destroyed: {self.num_permissions}')
        print(f'Time of target presentation: {self.time_of_target_presentation_list}')
        print(f'Time of target permission: {self.time_of_target_permission_list}')
        #calculate average time to destruction of target
        time_to_destruction = 0
        for x in range(len(self.time_of_target_permission_list)):  # permission list should be less than or equal to presentation list under all conditions
            print(f"X is equal to: {x}")
            time_to_destruction += self.time_of_target_permission_list[x] - self.time_of_target_presentation_list[x]
        average_time_to_destruction = time_to_destruction/len(self.time_of_target_presentation_list)
        print(f'Average time to destruction of target: {average_time_to_destruction}')
        return(self.num_targets, self.num_permissions, average_time_to_destruction)


        

# create a View class
class View:
    def __init__(self, sector_letter, num_actuators_per_sector, num_sectors, interval_in_seconds, num_intervals):
        self.sector_letter = sector_letter
        self.num_actuators_per_sector = num_actuators_per_sector
        self.num_sectors = num_sectors
        self.interval_in_seconds = interval_in_seconds
        self.num_intervals = num_intervals
        self.sector_list = ['00', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.view = []
        self.time_stamps = []
        for i in range(1, self.num_sectors + 1):
            for j in range(1, self.num_actuators_per_sector + 1):
                sector = str(self.sector_list[i])
                actuator = str(j)
                name_line = sector + actuator
                # Create a key-value pair for the actuator
                actuator_dict = {
                    "name": name_line,
                    "values": []
                }
                self.view.append(actuator_dict)

    def update_view(self):
        current_time = time.time()
        self.time_stamps.append(current_time)
        conn = connect_to_db(self.sector_letter)
        if not conn:
            return

        cursor = conn.cursor()

        try:
            for i in range(1, self.num_sectors + 1):
                for j in range(1, self.num_actuators_per_sector + 1):
                    sector = str(self.sector_list[i])
                    actuator = str(j)
                    name_line = sector + actuator
                    query = f"SELECT {sector} FROM view_table WHERE id = {j}"
                    cursor.execute(query)
                    result = cursor.fetchone()

                    if result:
                        for item in self.view:
                            if item["name"] == name_line:
                                item["values"].append(result[0])
                                break

        except Exception as error:
            print(f"Error updating view: {error}")
        finally:
            cursor.close()
            conn.close()

        #return self.view

    def print_view(self):
        for item in self.view:
            print(f"{item['name']}: {item['values']}")

    def report_statistics(self):
        if not self.time_stamps:
            return 0, 0

        total_diff = 0
        count = 0
        count_stale_report = 0

        for item in self.view:
            values = item["values"]
            if len(values) != len(self.time_stamps):
                print("Length of values and time stamps do not match.")
                continue

            diff_sum = 0
            for i in range(len(self.time_stamps)):
                diff_sum += self.time_stamps[i] - values[i]
                if i > 0 and values[i] < values[i - 1]:
                    count_stale_report += 1

            avg_diff = diff_sum / len(self.time_stamps)
            total_diff += avg_diff
            count += 1

        if count == 0:
            return 0, count_stale_report

        overall_avg_diff = total_diff / count
        return overall_avg_diff, count_stale_report


# Function to connect to the PostgreSQL database
def connect_to_db(db_letter, isolation_level_in=None):

    isolation_levels = {
            "AUTOCOMMIT": extensions.ISOLATION_LEVEL_AUTOCOMMIT,
            "READ COMMITTED": extensions.ISOLATION_LEVEL_READ_COMMITTED,
            "REPEATABLE READ": extensions.ISOLATION_LEVEL_REPEATABLE_READ,
            "SERIALIZABLE": extensions.ISOLATION_LEVEL_SERIALIZABLE
        }

    isolation_level = isolation_levels.get(isolation_level_in)

    db_config = {
        'A': {
            'dbname': 'mydatabase_A',
            'user': 'myuser_A',
            'password': 'mypassword_A',
            'host': 'ec2-34-211-64-52.us-west-2.compute.amazonaws.com',
            'port': '5432'
        },
        'B': {
            'dbname': 'mydatabase_B',
            'user': 'myuser_B',
            'password': 'mypassword_B',
            'host': 'ec2-34-211-64-52.us-west-2.compute.amazonaws.com',
            'port': '5433'
        },
        'C': {
            'dbname': 'mydatabase_C',
            'user': 'myuser_C',
            'password': 'mypassword_C',
            'host': 'ec2-34-211-64-52.us-west-2.compute.amazonaws.com',
            'port': '5434'
        }
    }

    if db_letter not in db_config:
        print(f"Invalid database letter: {db_letter}")
        return None

    config = db_config[db_letter]

    try:
        connection = psycopg2.connect(
            dbname=config['dbname'],
            user=config['user'],
            password=config['password'],
            host=config['host'],
            port=config['port']
        )

        connection.set_isolation_level(isolation_level)           #################### setting isolation level

        return connection
    except Exception as error:
        print(f"Error connecting to database {db_letter}: {error}")
        return None

# Function to read command-line arguments
def read_command_line_args():
    parser = argparse.ArgumentParser(description='Initialize actuator script.')
    parser.add_argument('sector_letter', type=str, help='Sector letter')
    parser.add_argument('actuator_number', type=int, help='Actuator number')
    parser.add_argument('num_actuators_per_sector', type=int, help='Number of actuators per sector')
    parser.add_argument('num_sectors', type=int, help='Number of sectors')
    parser.add_argument('interval_in_seconds', type=int, help='Interval in seconds')
    parser.add_argument('target_probability', type=float, help='Target probability')
    parser.add_argument('num_intervals', type=int, help='Number of intervals')

    args = parser.parse_args()

    return {
        "sector_letter": args.sector_letter,
        "actuator_number": args.actuator_number,
        "num_actuators_per_sector": args.num_actuators_per_sector,
        "num_sectors": args.num_sectors,
        "interval_in_seconds": args.interval_in_seconds,
        "target_probability": args.target_probability,
        "num_intervals": args.num_intervals
    }

# Function to initialize the actuator script
def initialize_actuator_script(sector_letter, actuator_number):
    actuator_script = []
    try:
        with open("script.txt", "r") as file:
            for line in file:
                if line.startswith(f"{sector_letter}{actuator_number}"):
                    actuator_script = line.strip().split()[1:]
                    break
    except FileNotFoundError:
        print("script.txt file not found.")
    actuator_name = str(sector_letter)+str(actuator_number)
    
    # return the actuator_script list
    
    return actuator_script

# Function to read environment variables
def read_environment_variables():
    return {
        "sector_letter": os.getenv('SECTOR_LETTER'),
        "actuator_number": int(os.getenv('ACTUATOR_NUMBER')),
        "num_actuators_per_sector": int(os.getenv('NUM_ACTUATORS_PER_SECTOR')),
        "num_sectors": int(os.getenv('NUM_SECTORS')),
        "interval_in_seconds": int(os.getenv('INTERVAL_IN_SECONDS')),
        "num_intervals": int(os.getenv('NUM_INTERVALS')),
        "time_unit_pause": float(os.getenv('TIME_UNIT_PAUSE')),
        "isolation_level": str(os.getenv('ISOLATION_LEVEL'))                         ### Adding isolation level to the environment variables
    }
        
def main():
    #wait for a keyboard entery to start the simulation
    #input("Press Enter to start the simulation...")

    # Read the command-line arguments
    env_vars = read_environment_variables()
    print(f"Environmental Variables: {env_vars}")

    # Initialize the actuator script
    actuator_script = initialize_actuator_script(env_vars["sector_letter"], env_vars["actuator_number"])
    print(f"Actuator Script: {actuator_script}")

    # Initialize the actuator
    actuator = Actuator(env_vars["sector_letter"], env_vars["actuator_number"], actuator_script)

    # Initialize the view
    view = View(env_vars["sector_letter"], env_vars["num_actuators_per_sector"], env_vars["num_sectors"], env_vars["interval_in_seconds"], env_vars["num_intervals"])

    # Start the simulation
    num_intervals = env_vars["num_intervals"]
    interval_in_seconds = env_vars["interval_in_seconds"]
    interval_number = 1
    time_pause = env_vars["time_unit_pause"]
    current_time = time.time()
    start_of_simulation = time.time()
    while interval_number <= num_intervals:
        start_time = time.time()
        currrent_time = time.time()
        while current_time < start_time + interval_in_seconds:
            print(f'Interval: {interval_number}')
            current_time = time.time()
            actuator.update_sector_permissions()
            actuator.update_sector_target_text_file()
            view.update_view()
            time.sleep(time_pause)
            
        
        if interval_number < num_intervals:
            actuator.read_next_target_from_script()

        interval_number += 1
    
    end_of_simulation = time.time()
    print("Simulation completed.")
    print(f"Total simulation time: {end_of_simulation - start_of_simulation} seconds")

    report_latency, stale_reports = view.report_statistics()
    print(f"The reports were on average: {report_latency} seconds late.")
    print(f"Number of stale reports: {stale_reports}")

    num_targets, num_permissions, avg_time_to_destruction = actuator.report_statistics()
    print(f'Number of targets: {num_targets}')
    print(f'Number of targets destroyed: {num_permissions}')
    print(f'Average time to target destruction: {avg_time_to_destruction}')
    
    # Create a text file called "{sector_letter}{actuator_number}_simulation_report.txt"
    # Write the following information to the file in each line: report_latency, stale_reports, num_targets, num_permissions, avg_time_to_destruction
    with open(f"{env_vars['sector_letter']}{env_vars['actuator_number']}_simulation_report.txt", "w") as file:
        file.write(f"{env_vars['sector_letter']}{env_vars['actuator_number']}\n")
        file.write(f"{report_latency}\n")
        file.write(f"{stale_reports}\n")
        file.write(f"{num_targets}\n")
        file.write(f"{num_permissions}\n")
        file.write(f"{avg_time_to_destruction}\n")
        file.write(f'-----------------------------------\n')
        file.write(f"Total simulation time: {end_of_simulation - start_of_simulation} seconds\n")
        file.write(f"Number of intervals: {num_intervals}\n")
        file.write(f"Interval duration: {interval_in_seconds} seconds\n")
        file.write(f"Time unit pause: {time_pause} seconds\n")
        file.close()
    print("Simulation report written to file.")

    #input("Press Enter to end the simulation...")


if __name__ == "__main__":
    main()
