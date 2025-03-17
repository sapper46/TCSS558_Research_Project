# Method to initialize view.
def initialize_view(num_actuators_per_sector, num_sectors):
    sector_list = ['00', 'A', 'B', 'C', 'D', 'E', 'F','G', 'H'] 
    view = []
    for i in range(1, num_sectors + 1):
        for j in range(1, num_actuators_per_sector + 1):
                sector = str(sector_list[i])
                actuator = str(j)
                name_line = sector + actuator
                # create a key value pair for the actuator
                actuator_dict = {
                    "name": name_line,
                    "values": []
                }
                view.append(actuator_dict)
    return view

def update_view(db_letter, num_actuators_per_sector, num_sectors):
    sector_list = ['00', 'A', 'B', 'C', 'D', 'E', 'F','G', 'H'] 
    
    conn = connect_to_db(db_letter)
    if not conn:
        return

    cursor = conn.cursor()
    view = initialize_view(num_actuators_per_sector, num_sectors)

    try:
        for i in range(1, num_sectors + 1):
            for j in range(1, num_actuators_per_sector + 1):
                sector = str(sector_list[i])
                actuator = str(j)
                name_line = sector + actuator
                query = f"SELECT {sector} FROM view_table WHERE id = {j}"
                cursor.execute(query)
                result = cursor.fetchone()

                if result:
                    #view[name_line].append(result[0])
                    for item in view:
                        if item["name"] == name_line:
                            item["values"].append(result[0])
                            break
                    

    except Exception as error:
        print(f"Error updating view: {error}")
    finally:
        cursor.close()
        conn.close()

    return view