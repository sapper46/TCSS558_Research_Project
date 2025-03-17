import psycopg2
import os
from psycopg2 import extensions

class Strat_Manager_Class:
    def __init__(self, target_prioritization,isolation_level_str):
        self.target_prioritization = target_prioritization
        isolation_level_in = isolation_level_str.upper()

        isolation_levels = {
            "AUTOCOMMIT": extensions.ISOLATION_LEVEL_AUTOCOMMIT,
            "READ COMMITTED": extensions.ISOLATION_LEVEL_READ_COMMITTED,
            "REPEATABLE READ": extensions.ISOLATION_LEVEL_REPEATABLE_READ,
            "SERIALIZABLE": extensions.ISOLATION_LEVEL_SERIALIZABLE
        }

        self.isolation_level = isolation_levels.get(isolation_level_in)

        # Database connection details
        self.db_A_conn_details = {
            'dbname': 'mydatabase_A',
            'user': 'myuser_A',
            'password': 'mypassword_A',
            'host': 'ec2-34-211-64-52.us-west-2.compute.amazonaws.com',
            'port': 5432
        }
        self.db_B_conn_details = {
            'dbname': 'mydatabase_B',
            'user': 'myuser_B',
            'password': 'mypassword_B',
            'host': 'ec2-34-211-64-52.us-west-2.compute.amazonaws.com',
            'port': 5433
        }
        self.db_C_conn_details = {
            'dbname': 'mydatabase_C',
            'user': 'myuser_C',
            'password': 'mypassword_C',
            'host': 'ec2-34-211-64-52.us-west-2.compute.amazonaws.com',
            'port': 5434
        }
        self.db_Strategic_conn_details = {
            'dbname': 'mydatabase_Strategic',
            'user': 'myuser_Strategic',
            'password': 'mypassword_Strategic',
            'host': 'localhost',
            'port': 5435
        }

    def update_report_view_and_target(self):
        # Connect to the databases and set the correct isolation levels.
        conn_A = psycopg2.connect(**self.db_A_conn_details)
        conn_A.set_isolation_level(self.isolation_level) #######################
        conn_B = psycopg2.connect(**self.db_B_conn_details)
        conn_B.set_isolation_level(self.isolation_level) #######################
        conn_C = psycopg2.connect(**self.db_C_conn_details)
        conn_C.set_isolation_level(self.isolation_level) #######################
        conn_Strategic = psycopg2.connect(**self.db_Strategic_conn_details)
        conn_Strategic.set_isolation_level(self.isolation_level) ###############

        # If connections are successful, print the connection status in the terminal
        #print(f"Connected to {self.db_A_conn_details['dbname']} database!")
        #print(f"Connected to {self.db_B_conn_details['dbname']} database!")
        #print(f"Connected to {self.db_C_conn_details['dbname']} database!")
        #print(f"Connected to {self.db_Strategic_conn_details['dbname']} database!")

        try:
            # Create cursors
            cur_A = conn_A.cursor()
            cur_B = conn_B.cursor()
            cur_C = conn_C.cursor()
            cur_Strategic = conn_Strategic.cursor()

            # Begin transaction
            conn_Strategic.autocommit = False

            # Step 1 (REPORT TABLE): Fetch data from each source database
            cur_A.execute("SELECT id, A FROM report_table;")
            data_A = cur_A.fetchall()

            cur_B.execute("SELECT id, B FROM report_table;")
            data_B = cur_B.fetchall()

            cur_C.execute("SELECT id, C FROM report_table;")
            data_C = cur_C.fetchall()

            # Step 2 (REPORT TABLE): Create dictionaries to map IDs to column values
            dict_A = {row[0]: row[1] for row in data_A}
            dict_B = {row[0]: row[1] for row in data_B}
            dict_C = {row[0]: row[1] for row in data_C}

            # Step 3 (REPORT TABLE): Update db_Strategic with the new values
            for id_key in dict_A.keys():
                A_val = dict_A.get(id_key, None)
                B_val = dict_B.get(id_key, None)
                C_val = dict_C.get(id_key, None)

                cur_Strategic.execute("""
                    UPDATE report_table 
                    SET A = %s, B = %s, C = %s
                    WHERE id = %s;
                """, (A_val, B_val, C_val, id_key))

            # Step 1 (VIEW TABLE): Fetch data from each source database
            cur_A.execute("SELECT id, A FROM view_table;")
            data_A = cur_A.fetchall()

            cur_B.execute("SELECT id, B FROM view_table;")
            data_B = cur_B.fetchall()

            cur_C.execute("SELECT id, C FROM view_table;")
            data_C = cur_C.fetchall()

            # Step 2 (VIEW TABLE): Create dictionaries to map IDs to column values
            dict_A = {row[0]: row[1] for row in data_A}
            dict_B = {row[0]: row[1] for row in data_B}
            dict_C = {row[0]: row[1] for row in data_C}

            # Step 3 (VIEW TABLE): Update db_Strategic with the new values
            for id_key in dict_A.keys():
                A_val = dict_A.get(id_key, None)
                B_val = dict_B.get(id_key, None)
                C_val = dict_C.get(id_key, None)

                cur_Strategic.execute("""
                    UPDATE view_table 
                    SET A = %s, B = %s, C = %s
                    WHERE id = %s;
                """, (A_val, B_val, C_val, id_key))

            # Step 1 (TARGET TABLE): Fetch data from each source database
            cur_A.execute("SELECT id, A FROM target_table;")
            data_A = cur_A.fetchall()

            cur_B.execute("SELECT id, B FROM target_table;")
            data_B = cur_B.fetchall()

            cur_C.execute("SELECT id, C FROM target_table;")
            data_C = cur_C.fetchall()

            # Step 2 (TARGET TABLE): Create dictionaries to map IDs to column values
            dict_A = {row[0]: row[1] for row in data_A}
            dict_B = {row[0]: row[1] for row in data_B}
            dict_C = {row[0]: row[1] for row in data_C}

            # Step 3 (TARGET TABLE): Update db_Strategic with the new values
            for id_key in dict_A.keys():
                A_val = dict_A.get(id_key, None)
                B_val = dict_B.get(id_key, None)
                C_val = dict_C.get(id_key, None)

                cur_Strategic.execute("""
                    UPDATE target_table 
                    SET A = %s, B = %s, C = %s
                    WHERE id = %s;
                """, (A_val, B_val, C_val, id_key))
            
            # Check for new targets if target_prioritization is True
            if self.target_prioritization:
                print("Target prioritization is enabled.")
                while self.check_for_new_targets():
                    print("I dectected new targets. Updating permission tables.")
                    self.update_permissions()

            # Commit the transaction
            conn_Strategic.commit()

        except Exception as e:
            print(f"An error occurred: {e}")
            conn_Strategic.rollback()
        finally:
            # Close all cursors and connections
            cur_A.close()
            cur_B.close()
            cur_C.close()
            cur_Strategic.close()
            conn_A.close()
            conn_B.close()
            conn_C.close()
            conn_Strategic.close()

    def check_for_new_targets(self):
        # Connect to the strategic database and set isolation level
        conn_Strategic = psycopg2.connect(**self.db_Strategic_conn_details)
        conn_Strategic.set_isolation_level(self.isolation_level)################

        try:
            # Create cursors
            cur_Strategic1 = conn_Strategic.cursor()
            cur_Strategic2 = conn_Strategic.cursor()
            cur_Strategic3 = conn_Strategic.cursor()
            cur_Strategic4 = conn_Strategic.cursor()
            cur_Strategic5 = conn_Strategic.cursor()
            cur_Strategic6 = conn_Strategic.cursor()

            # Fetch data from target_table and permission_table in strategic database-----------------------Pulling A Column
            cur_Strategic1.execute("SELECT id, A FROM target_table")
            target_data_A = cur_Strategic1.fetchall()

            cur_Strategic2.execute("SELECT id, A FROM permission_table")
            permission_data_A = cur_Strategic2.fetchall()

            # Fetch data from target_table and permission_table in strategic database-----------------------Pulling B Column
            cur_Strategic3.execute("SELECT id, B FROM target_table")
            target_data_B = cur_Strategic3.fetchall()

            cur_Strategic4.execute("SELECT id, B FROM permission_table")
            permission_data_B = cur_Strategic4.fetchall()

            # Fetch data from target_table and permission_table in strategic database-----------------------Pulling C Column
            cur_Strategic5.execute("SELECT id, C FROM target_table")
            target_data_C = cur_Strategic5.fetchall()

            cur_Strategic6.execute("SELECT id, C FROM permission_table")
            permission_data_C = cur_Strategic6.fetchall()

            # Create dictionaries to map IDs to column values
            dict_target_A = {row[0]: row[1] for row in target_data_A}
            dict_permission_A = {row[0]: row[1] for row in permission_data_A}
            dict_target_B = {row[0]: row[1] for row in target_data_B}
            dict_permission_B = {row[0]: row[1] for row in permission_data_B}
            dict_target_C = {row[0]: row[1] for row in target_data_C}
            dict_permission_C = {row[0]: row[1] for row in permission_data_C}
            
            # Compare the data from the target_table and permission_table
            for id_key in dict_target_A.keys():
                target_val_A = dict_target_A.get(id_key, None)
                permission_val_A = dict_permission_A.get(id_key, None)
                target_val_B = dict_target_B.get(id_key, None)
                permission_val_B = dict_permission_B.get(id_key, None)
                target_val_C = dict_target_C.get(id_key, None)
                permission_val_C = dict_permission_C.get(id_key, None)

                if (target_val_A > permission_val_A) or (target_val_B > permission_val_B) or (target_val_C > permission_val_C):
                    return True

            # If all comparisons passed, return False
            return False

        except Exception as e:
            print(f"An error occurred in check for new targets: {e}")
            return False
        finally:
            # Close all cursors and connections
            cur_Strategic1.close()
            cur_Strategic2.close()
            cur_Strategic3.close()
            cur_Strategic4.close()
            cur_Strategic5.close()
            cur_Strategic6.close()
            conn_Strategic.close()

    def update_permissions(self):
        # Connect to the strategic database and set isolation level
        conn_Strategic = psycopg2.connect(**self.db_Strategic_conn_details)
        conn_Strategic.set_isolation_level(self.isolation_level) ###############

        try:
            # Create cursors
            cur_Strategic1 = conn_Strategic.cursor()
            cur_Strategic2 = conn_Strategic.cursor()

            # Gather the data from the strategic database-----------------------Updating A Column
            cur_Strategic1.execute("SELECT id, A FROM target_table;")
            data_target = cur_Strategic1.fetchall()

            cur_Strategic2.execute("SELECT id, A FROM permission_table;")
            data_permission = cur_Strategic2.fetchall()

            # Create dictionaries to map IDs to column values
            dict_target = {row[0]: row[1] for row in data_target}
            dict_permission = {row[0]: row[1] for row in data_permission}

            # Begin comparison
            for id_key in dict_target.keys():
                target_val = dict_target.get(id_key, None)
                permission_val = dict_permission.get(id_key, None)

                # Increment permission_table by 1 if target_table is greater
                if target_val > permission_val:
                    cur_Strategic2.execute("""
                        UPDATE permission_table 
                        SET A = A + 1
                        WHERE id = %s;
                    """, (id_key,))

            # Gather the data from the strategic database-----------------------Updating B Column
            cur_Strategic1.execute("SELECT id, B FROM target_table;")
            data_target = cur_Strategic1.fetchall()

            cur_Strategic2.execute("SELECT id, B FROM permission_table;")
            data_permission = cur_Strategic2.fetchall()

            # Create dictionaries to map IDs to column values
            dict_target = {row[0]: row[1] for row in data_target}
            dict_permission = {row[0]: row[1] for row in data_permission}

            # Begin comparison
            for id_key in dict_target.keys():
                target_val = dict_target.get(id_key, None)
                permission_val = dict_permission.get(id_key, None)

                # Increment permission_table by 1 if target_table is greater
                if target_val > permission_val:
                    cur_Strategic2.execute("""
                        UPDATE permission_table 
                        SET B = B + 1
                        WHERE id = %s;
                    """, (id_key,))

            # Gather the data from the strategic database-----------------------Updating C Column
            cur_Strategic1.execute("SELECT id, C FROM target_table;")
            data_target = cur_Strategic1.fetchall()

            cur_Strategic2.execute("SELECT id, C FROM permission_table;")
            data_permission = cur_Strategic2.fetchall()

            # Create dictionaries to map IDs to column values
            dict_target = {row[0]: row[1] for row in data_target}
            dict_permission = {row[0]: row[1] for row in data_permission}

            # Begin comparison
            for id_key in dict_target.keys():
                target_val = dict_target.get(id_key, None)
                permission_val = dict_permission.get(id_key, None)

                # Increment permission_table by 1 if target_table is greater
                if target_val > permission_val:
                    cur_Strategic2.execute("""
                        UPDATE permission_table 
                        SET C = C + 1
                        WHERE id = %s;
                    """, (id_key,))    

            # Commit the transaction
            conn_Strategic.commit()
            

        except Exception as e:
            print(f"An error occurred in updating permission tables: {e}")
            conn_Strategic.rollback()
            
        finally:
            # Close all cursors and connections
            cur_Strategic1.close()
            cur_Strategic2.close()
            conn_Strategic.close()

        self.update_permissions_lower() # Call the update_permissions_lower method to update the lower permissions table in the other EC2 instance
            
    def update_permissions_lower(self):
        
        print("I will now try to update the lower permissions table.")

        # Connect to the databases and set isolation levels
        conn_A = psycopg2.connect(**self.db_A_conn_details)
        conn_A.set_isolation_level(self.isolation_level) #######################
        conn_B = psycopg2.connect(**self.db_B_conn_details)
        conn_B.set_isolation_level(self.isolation_level) #######################
        conn_C = psycopg2.connect(**self.db_C_conn_details)
        conn_C.set_isolation_level(self.isolation_level) #######################
        conn_Strategic = psycopg2.connect(**self.db_Strategic_conn_details)
        conn_Strategic.set_isolation_level(self.isolation_level) ###############

        # If connections are successful, print the connection status in the terminal
        print(f"Connected to {self.db_A_conn_details['dbname']} database!")
        print(f"Connected to {self.db_B_conn_details['dbname']} database!")
        print(f"Connected to {self.db_C_conn_details['dbname']} database!")
        print(f"Connected to {self.db_Strategic_conn_details['dbname']} database!")

        try:
            # Create cursors
            cur_Strategic_A = conn_Strategic.cursor() # for A column
            cur_Strategic_B = conn_Strategic.cursor() # for B column
            cur_Strategic_C = conn_Strategic.cursor() # for C column
            cur_A = conn_A.cursor()
            cur_B = conn_B.cursor()
            cur_C = conn_C.cursor()

            # Step 1 (PERMISSION TABLE): Fetch data from the permission_table in strategic database
            cur_Strategic_A.execute("SELECT id, A FROM permission_table;")
            data_A = cur_Strategic_A.fetchall()

            cur_Strategic_B.execute("SELECT id, B FROM permission_table;")
            data_B = cur_Strategic_B.fetchall()

            cur_Strategic_C.execute("SELECT id, C FROM permission_table;")
            data_C = cur_Strategic_C.fetchall()

            # Step 2 (PERMISSION TABLE): Create dictionaries to map IDs to column values
            dict_A = {row[0]: row[1] for row in data_A}
            dict_B = {row[0]: row[1] for row in data_B}
            dict_C = {row[0]: row[1] for row in data_C}

            # Step 3A (LOWER PERMISSION TABLE): Update db_A with the new values
            for id_key in dict_A.keys():
                A_val = dict_A.get(id_key, None)
                B_val = dict_B.get(id_key, None)
                C_val = dict_C.get(id_key, None)
                
                #print(f'Updating lower permissions for id: {id_key} with A: {A_val}, B: {B_val}, C: {C_val}')

                cur_A.execute("""
                    UPDATE permission_table 
                    SET A = %s, B = %s, C = %s
                    WHERE id = %s;
                """, (A_val, B_val, C_val, id_key))

            # Commit the transaction
            conn_A.commit()

            # Step 3B (LOWER PERMISSION TABLE): Update db_B with the new values
            for id_key in dict_B.keys():
                A_val = dict_A.get(id_key, None)
                B_val = dict_B.get(id_key, None)
                C_val = dict_C.get(id_key, None)
                
                #print(f'Updating lower permissions for id: {id_key} with A: {A_val}, B: {B_val}, C: {C_val}')

                cur_B.execute("""
                    UPDATE permission_table 
                    SET A = %s, B = %s, C = %s
                    WHERE id = %s;
                """, (A_val, B_val, C_val, id_key))

            # Commit the transaction
            conn_B.commit()        

            # Step 3C (LOWER PERMISSION TABLE): Update db_C with the new values
            for id_key in dict_C.keys():
                A_val = dict_A.get(id_key, None)
                B_val = dict_B.get(id_key, None)
                C_val = dict_C.get(id_key, None)
                
                #print(f'Updating lower permissions for id: {id_key} with A: {A_val}, B: {B_val}, C: {C_val}')

                cur_C.execute("""
                    UPDATE permission_table 
                    SET A = %s, B = %s, C = %s
                    WHERE id = %s;
                """, (A_val, B_val, C_val, id_key))

            # Commit the transaction
            conn_C.commit()         


        except Exception as e:
            print(f"An error occurred in updating lower permissions: {e}")
            
        finally:
            # Close all cursors and connections
            cur_A.close()
            cur_B.close()
            cur_C.close()
            cur_Strategic_A.close()
            cur_Strategic_B.close()
            cur_Strategic_C.close()
            conn_A.close()
            conn_B.close()
            conn_C.close()
            conn_Strategic.close()  

    def test(self):
        # Connect to the database A
        conn_A = psycopg2.connect(**self.db_A_conn_details)
        try:
            # Create a cursor
            cur_A = conn_A.cursor()

            # Update the permission_table
            cur_A.execute("""
                UPDATE permission_table 
                SET A = %s
                WHERE id = %s;
            """, (9, 1))

            # Commit the transaction
            conn_A.commit()

            print("Update successful")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            # Close the cursor and connection
            cur_A.close()
            conn_A.close()   


def read_environment_variables():
    return {
        "target_prioritization": os.getenv('TARGET_PRIORITIZATION') == 'true',
        "isolation_level_str":os.getenv('ISOLATION_LEVEL')
    }

def main():
    # Read environment variables
    env_vars = read_environment_variables()

    # Initialize the Strat_Manager_Class
    strat_manager = Strat_Manager_Class(**env_vars)

    print("Starting the Strat Manager. Press ctrl+c to quit ...")

    #strat_manager.test()
    
    # Update report and view tables
    while True:
        print("I am updating report, view, and target tables.")
        strat_manager.update_report_view_and_target()
        print(f'Checking to see if there are new targets... check_for_new_targets: {strat_manager.check_for_new_targets()}')
        print("I am updating permission tables.")
        strat_manager.update_permissions()


if __name__ == "__main__":
    main()