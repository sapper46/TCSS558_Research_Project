import random
import argparse

def create_script(num_actuators_per_sector, num_sectors, interval_in_seconds, target_probability, num_intervals):
    # create a blank text file called "script.txt", or rewrite the old one
    file = open("script.txt", "w")

    sector_list = ['00', 'A', 'B', 'C', 'D', 'E', 'F','G', 'H']

    for i in range(1, num_sectors + 1):
        for j in range(1, num_actuators_per_sector + 1):
                sector = str(sector_list[i])
                actuator = str(j)
                name_line = sector + actuator
                # write name_line to the text file and add a space
                file.write(name_line + " ")
                # decide true or false for the target based on the target_probability
                for k in range(1, num_intervals + 1):
                    target = random.random() < target_probability
                    if target:
                        # write "1" to the text file and add a space
                        file.write("T ")
                    else:
                        file.write(". ")
                file.write("\n")

    # close the text file
    file.close()

def main():
    parser = argparse.ArgumentParser(description='Generate a script for actuators.')
    parser.add_argument('num_actuators_per_sector', type=int, help='Number of actuators per sector')
    parser.add_argument('num_sectors', type=int, help='Number of sectors')
    parser.add_argument('interval_in_seconds', type=int, help='Interval in seconds')
    parser.add_argument('target_probability', type=float, help='Target probability')
    parser.add_argument('num_intervals', type=int, help='Number of intervals')

    args = parser.parse_args()

    # initialize the actuator_script
    create_script(args.num_actuators_per_sector, args.num_sectors, args.interval_in_seconds, args.target_probability, args.num_intervals)
        
if __name__ == "__main__":
    main()



