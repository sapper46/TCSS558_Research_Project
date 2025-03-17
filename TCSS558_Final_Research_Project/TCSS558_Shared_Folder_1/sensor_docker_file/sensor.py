import os
import psycopg2
import time
import argparse
import random

class Sensor:
    def __init__(self, sector_letter, sector_number, isolation_level, target_prioritization):
        self.sector_letter = sector_letter
        self.sector_number = sector_number
        self.isolation_level = isolation_level
        self.target_prioritization = target_prioritization

    def update_database_reports_and_views(self, observed_sector, file_size, isolation_level):
        # Connect to the database
        conn = connect_to_db(self.sector_letter)
        if not conn:
            return

        cursor = conn.cursor()

        # Set the isolation level
        if isolation_level == 1:
            cursor.execute("SET TRANSACTION ISOLATION LEVEL READ COMMITTED")
        elif isolation_level == 2:
            cursor.execute("SET TRANSACTION ISOLATION LEVEL REPEATABLE READ")
        elif isolation_level == 3:
            cursor.execute("SET TRANSACTION ISOLATION LEVEL SERIALIZABLE")

        try:
            # Update the report_table
            report_query = f"UPDATE report_table SET {self.sector_letter} = %s WHERE id = %s"
            file_content = self.read_file_content(file_size)
            cursor.execute(report_query, (file_content, observed_sector))

            # Update the view_table
            view_query = f"UPDATE view_table SET {self.sector_letter} = %s WHERE id = %s"
            current_time = time.time()
            cursor.execute(view_query, (current_time, observed_sector))

            # Commit the changes
            conn.commit()

        except Exception as error:
            print(f"Error updating database: {error}")
        finally:
            cursor.close()
            conn.close()

    def check_for_new_targets(self, observed_sector):
        # Connect to the database
        conn = connect_to_db(self.sector_letter)
        if not conn:
            return False, 0  # Return a tuple with a boolean and a default value

        cursor = conn.cursor()

        try:
            # Read the value from the permission_table
            permission_query = f"SELECT {self.sector_letter} FROM permission_table WHERE id = %s"
            cursor.execute(permission_query, (observed_sector,))
            num_permissions = cursor.fetchone()[0]
            print(f'I read {num_permissions} permissions from {self.sector_letter} {observed_sector}.')

            # Read the value from the text file
            file_name = f"host_files/{self.sector_letter}{observed_sector}.txt"
            try:
                with open(file_name, "r") as file:
                    num_targets = int(file.read().strip())
                    print(f'I read {num_targets} targets from file {file_name}.')
            except FileNotFoundError:
                print(f"File {file_name} not found.")
                return False, 0  # Return a tuple with a boolean and a default value

            # Calculate new_targets
            num_new_targets = num_targets - num_permissions

            print(f'I detect {num_new_targets} new targets in sector {observed_sector}.')
            print(f'I will update the target_table with {num_targets} total targets.')
            
            return num_new_targets > 0, num_targets 

        except Exception as error:
            print(f"Error checking for new targets: {error}")
            return False, 0  # Return a tuple with a boolean and a default value
        finally:
            cursor.close()
            conn.close()

    def update_database_target_numbers(self, num_observed_targets, observed_sector, file_size, isolation_level):
        # Connect to the database
        conn = connect_to_db(self.sector_letter)
        if not conn:
            return

        cursor = conn.cursor()

        # Set the isolation level
        if isolation_level == 1:
            cursor.execute("SET TRANSACTION ISOLATION LEVEL READ COMMITTED")
        elif isolation_level == 2:
            cursor.execute("SET TRANSACTION ISOLATION LEVEL REPEATABLE READ")
        elif isolation_level == 3:
            cursor.execute("SET TRANSACTION ISOLATION LEVEL SERIALIZABLE")

        try:
            # Update the target_table
            target_query = f"UPDATE target_table SET {self.sector_letter} = %s WHERE id = %s"
            cursor.execute(target_query, (num_observed_targets, observed_sector))

            # Update the report_table
            report_query = f"UPDATE report_table SET {self.sector_letter} = %s WHERE id = %s"
            file_content = self.read_file_content(file_size)
            cursor.execute(report_query, (file_content, observed_sector))

            # Commit the changes
            conn.commit()

        except Exception as error:
            print(f"Error updating database: {error}")
        finally:
            cursor.close()
            conn.close()

    def read_file_content(self, file_size):
        file_name = f"file_size_{file_size}mb.txt"
        try:
            with open(file_name, "r") as file:
                return file.read()
        except FileNotFoundError:
            print(f"File {file_name} not found.")
            return ""

# Function to connect to the PostgreSQL database
def connect_to_db(db_letter):
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
        return connection
    except Exception as error:
        print(f"Error connecting to database {db_letter}: {error}")
        return None
    
def read_environment_variables():
    return {
        "sector_letter": os.getenv('SECTOR_LETTER'),
        "sector_number": int(os.getenv('SECTOR_NUMBER')),
        "num_sectors_per_sector": int(os.getenv('NUM_ACTUATORS_PER_SECTOR')),
        "num_sectors": int(os.getenv('NUM_SECTORS')),
        "interval_in_seconds": int(os.getenv('INTERVAL_IN_SECONDS')),
        "num_intervals": int(os.getenv('NUM_INTERVALS')),
        "time_unit_pause": float(os.getenv('TIME_UNIT_PAUSE')),
        "file_size": int(os.getenv('FILE_SIZE')),
        "isolation_level": int(os.getenv('ISOLATION_LEVEL')),
        "target_prioritization": os.getenv('TARGET_PRIORITIZATION') == 'true'
    }

def main():
    print("Lets get started.")
    # Get environmental variables
    env_vars = read_environment_variables()
    
    # create a sensor object
    sensor = Sensor(env_vars["sector_letter"], env_vars["sector_number"], env_vars["isolation_level"], env_vars["target_prioritization"])
    target_prioritization = env_vars["target_prioritization"]
    # Begin Sensor Scanning Protocol
    while True:
        # randomly generate an integer 1- num_sectors_per_sector (this will correspond to the observed sector)
        observed_sector = random.randint(1, env_vars["num_sectors_per_sector"])
        # FOR TESTING WE SET OBSERVED SECTOR TO 3--------------------
        #observed_sector = 3
        sensor.update_database_reports_and_views(observed_sector, env_vars["file_size"], env_vars["isolation_level"])
        print("Made it here.")
        new_targets_boolean, num_targets = sensor.check_for_new_targets(observed_sector)
        print(f'New targets boolean: {new_targets_boolean}, num_targets: {num_targets}')
        
        if new_targets_boolean and not target_prioritization:
            print(f'I will update the database with {num_targets} total targets. Target prioritization is set to {target_prioritization}.')
            sensor.update_database_target_numbers(num_targets, observed_sector, env_vars["file_size"], env_vars["isolation_level"])
        elif new_targets_boolean and target_prioritization:
            while new_targets_boolean:
                print("I am looping until all targets are updated")
                new_targets_boolean, num_targets = sensor.check_for_new_targets(observed_sector)
                sensor.update_database_target_numbers(num_targets, observed_sector, env_vars["file_size"], env_vars["isolation_level"])

if __name__ == "__main__":
    main()