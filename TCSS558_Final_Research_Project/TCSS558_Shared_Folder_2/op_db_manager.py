import psycopg2
import os
from psycopg2 import extensions

class Op_Manager_Class:
    def __init__(self, db_letter, isolation_level):
        
        self.sector_letter = db_letter

        isolation_level_in = isolation_level.upper()

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
            'host': 'db_A', # was 'db_A' before that 'localhost'
            'port': 5432 # was 5432
        }
        self.db_B_conn_details = {
            'dbname': 'mydatabase_B',
            'user': 'myuser_B',
            'password': 'mypassword_B',
            'host': 'db_B', # was 'db_B'
            'port': 5432 # was 5432
        }
        self.db_C_conn_details = {
            'dbname': 'mydatabase_C',
            'user': 'myuser_C',
            'password': 'mypassword_C',
            'host': 'db_C',  # was 'db_C'
            'port': 5432 # was 5432
        }
        self.db_Strategic_conn_details = {
            'dbname': 'mydatabase_Strategic',
            'user': 'myuser_Strategic',
            'password': 'mypassword_Strategic',
            'host': 'localhost',
            'port': 5435
        }

    def update_database(self):
        try:
            conn_A = psycopg2.connect(**self.db_A_conn_details)
            conn_A.set_isolation_level(self.isolation_level)####################
            cur_A = conn_A.cursor()
            conn_B = psycopg2.connect(**self.db_B_conn_details)
            conn_B.set_isolation_level(self.isolation_level)####################
            cur_B = conn_B.cursor()
            conn_C = psycopg2.connect(**self.db_C_conn_details)
            conn_C.set_isolation_level(self.isolation_level)####################
            cur_C = conn_C.cursor()

            # Print status of connections
            print(f"Connection A status: {conn_A}")
            print(f"Connection B status: {conn_B}")
            print(f"Connection C status: {conn_C}")

            # if self.sector_letter == 'A', pull data from db_B and db_C to update db_A--------------------
            if self.sector_letter == 'A':
                try:
                    print("I am A and I'm going to try")
                    # Step 1 (REPORT TABLE): Fetch data from each source database
                    cur_B.execute("SELECT id, B FROM report_table;")
                    data_B = cur_B.fetchall()
                    print(f"Data fetched from db_B report_table: {data_B}")

                    cur_C.execute("SELECT id, C FROM report_table;")
                    data_C = cur_C.fetchall()
                    print(f"Data fetched from db_C report_table: {data_C}")

                    # Step 2 (REPORT TABLE): Create dictionaries to map IDs to column values
                    dict_B = {row[0]: row[1] for row in data_B}
                    dict_C = {row[0]: row[1] for row in data_C}
                    print(f"Dictionary B: {dict_B}")
                    print(f"Dictionary C: {dict_C}")

                    # Step 3 (REPORT TABLE): Update db_Strategic with the new values
                    for id_key in dict_B.keys():
                        B_val = dict_B.get(id_key, None)
                        C_val = dict_C.get(id_key, None)
                        print(f"Updating id {id_key} with B_val: {B_val}, C_val: {C_val}")

                        cur_A.execute("""
                            UPDATE report_table 
                            SET B = %s, C = %s
                            WHERE id = %s;
                        """, (B_val, C_val, id_key))

                    # Step 1 (VIEW TABLE): Fetch data from each source database
                    cur_B.execute("SELECT id, B FROM view_table;")
                    data_B = cur_B.fetchall()
                    print(f"Data fetched from db_B view_table: {data_B}")

                    cur_C.execute("SELECT id, C FROM view_table;")
                    data_C = cur_C.fetchall()
                    print(f"Data fetched from db_C view_table: {data_C}")

                    # Step 2 (VIEW TABLE): Create dictionaries to map IDs to column values
                    dict_B = {row[0]: row[1] for row in data_B}
                    dict_C = {row[0]: row[1] for row in data_C}
                    print(f"Dictionary B: {dict_B}")
                    print(f"Dictionary C: {dict_C}")

                    # Step 3 (VIEW TABLE): Update db_Strategic with the new values
                    for id_key in dict_B.keys():
                        B_val = dict_B.get(id_key, None)
                        C_val = dict_C.get(id_key, None)
                        print(f"Updating id {id_key} with B_val: {B_val}, C_val: {C_val}")

                        cur_A.execute("""
                            UPDATE view_table 
                            SET B = %s, C = %s
                            WHERE id = %s;
                        """, (B_val, C_val, id_key))

                    # Step 1 (TARGET TABLE): Fetch data from each source database
                    cur_B.execute("SELECT id, B FROM target_table;")
                    data_B = cur_B.fetchall()
                    print(f"Data fetched from db_B target_table: {data_B}")

                    cur_C.execute("SELECT id, C FROM target_table;")
                    data_C = cur_C.fetchall()
                    print(f"Data fetched from db_C target_table: {data_C}")

                    # Step 2 (TARGET TABLE): Create dictionaries to map IDs to column values
                    dict_B = {row[0]: row[1] for row in data_B}
                    dict_C = {row[0]: row[1] for row in data_C}
                    print(f"Dictionary B: {dict_B}")
                    print(f"Dictionary C: {dict_C}")

                    # Step 3 (TARGET TABLE): Update db_Strategic with the new values
                    for id_key in dict_B.keys():
                        B_val = dict_B.get(id_key, None)
                        C_val = dict_C.get(id_key, None)
                        print(f"Updating id {id_key} with B_val: {B_val}, C_val: {C_val}")

                        cur_A.execute("""
                            UPDATE target_table 
                            SET B = %s, C = %s
                            WHERE id = %s;
                        """, (B_val, C_val, id_key))
                
                    # Commit the transaction
                    conn_A.commit()

                    print("Database A updated successfully (I think).")

                except Exception as e:
                    print(f"An error occurred updating DB A: {e}")
            
                finally:
                    # Close all cursors and connections
                    cur_A.close()
                    cur_B.close()
                    cur_C.close()
                    conn_A.close()
                    conn_B.close()
                    conn_C.close()

            # if self.sector_letter == 'B', pull data from db_A and db_C to update db_B--------------------
            if self.sector_letter == 'B':
                try:
                    # Step 1 (REPORT TABLE): Fetch data from each source database
                    cur_A.execute("SELECT id, A FROM report_table;")
                    data_A = cur_A.fetchall()
                    print(f"Data fetched from db_A report_table: {data_A}")

                    cur_C.execute("SELECT id, C FROM report_table;")
                    data_C = cur_C.fetchall()
                    print(f"Data fetched from db_C report_table: {data_C}")

                    # Step 2 (REPORT TABLE): Create dictionaries to map IDs to column values
                    dict_A = {row[0]: row[1] for row in data_A}
                    dict_C = {row[0]: row[1] for row in data_C}
                    print(f"Dictionary A: {dict_A}")
                    print(f"Dictionary C: {dict_C}")

                    # Step 3 (REPORT TABLE): Update db_Strategic with the new values
                    for id_key in dict_A.keys():
                        A_val = dict_A.get(id_key, None)
                        C_val = dict_C.get(id_key, None)
                        print(f"Updating id {id_key} with A_val: {A_val}, C_val: {C_val}")

                        cur_B.execute("""
                            UPDATE report_table 
                            SET A = %s, C = %s
                            WHERE id = %s;
                        """, (A_val, C_val, id_key))

                    # Step 1 (VIEW TABLE): Fetch data from each source database
                    cur_A.execute("SELECT id, A FROM view_table;")
                    data_A = cur_A.fetchall()
                    print(f"Data fetched from db_A view_table: {data_A}")

                    cur_C.execute("SELECT id, C FROM view_table;")
                    data_C = cur_C.fetchall()
                    print(f"Data fetched from db_C view_table: {data_C}")

                    # Step 2 (VIEW TABLE): Create dictionaries to map IDs to column values
                    dict_A = {row[0]: row[1] for row in data_A}
                    dict_C = {row[0]: row[1] for row in data_C}
                    print(f"Dictionary A: {dict_A}")
                    print(f"Dictionary C: {dict_C}")

                    # Step 3 (VIEW TABLE): Update db_Strategic with the new values
                    for id_key in dict_A.keys():
                        A_val = dict_A.get(id_key, None)
                        C_val = dict_C.get(id_key, None)
                        print(f"Updating id {id_key} with A_val: {A_val}, C_val: {C_val}")

                        cur_B.execute("""
                            UPDATE view_table 
                            SET A = %s, C = %s
                            WHERE id = %s;
                        """, (A_val, C_val, id_key))

                    # Step 1 (TARGET TABLE): Fetch data from each source database
                    cur_A.execute("SELECT id, A FROM target_table;")
                    data_A = cur_A.fetchall()
                    print(f"Data fetched from db_A target_table: {data_A}")

                    cur_C.execute("SELECT id, C FROM target_table;")
                    data_C = cur_C.fetchall()
                    print(f"Data fetched from db_C target_table: {data_C}")

                    # Step 2 (TARGET TABLE): Create dictionaries to map IDs to column values
                    dict_A = {row[0]: row[1] for row in data_A}
                    dict_C = {row[0]: row[1] for row in data_C}
                    print(f"Dictionary A: {dict_A}")
                    print(f"Dictionary C: {dict_C}")

                    # Step 3 (TARGET TABLE): Update db_Strategic with the new values
                    for id_key in dict_A.keys():
                        A_val = dict_A.get(id_key, None)
                        C_val = dict_C.get(id_key, None)
                        print(f"Updating id {id_key} with A_val: {A_val}, C_val: {C_val}")

                        cur_B.execute("""
                            UPDATE target_table 
                            SET A = %s, C = %s
                            WHERE id = %s;
                        """, (A_val, C_val, id_key))
                
                    # Commit the transaction
                    conn_B.commit()

                    print("Database B updated successfully (I think).")

                except Exception as e:
                    print(f"An error occurred updating DB B: {e}")
            
                finally:
                    # Close all cursors and connections
                    cur_A.close()
                    cur_B.close()
                    cur_C.close()
                    conn_A.close()
                    conn_B.close()
                    conn_C.close()

            # if self.sector_letter == 'C', pull data from db_A and db_C to update db_C--------------------
            if self.sector_letter == 'C':
                try:
                    # Step 1 (REPORT TABLE): Fetch data from each source database
                    cur_A.execute("SELECT id, A FROM report_table;")
                    data_A = cur_A.fetchall()
                    print(f"Data fetched from db_A report_table: {data_A}")

                    cur_B.execute("SELECT id, B FROM report_table;")
                    data_B = cur_B.fetchall()
                    print(f"Data fetched from db_B report_table: {data_B}")

                    # Step 2 (REPORT TABLE): Create dictionaries to map IDs to column values
                    dict_A = {row[0]: row[1] for row in data_A}
                    dict_B = {row[0]: row[1] for row in data_B}
                    print(f"Dictionary A: {dict_A}")
                    print(f"Dictionary B: {dict_B}")

                    # Step 3 (REPORT TABLE): Update db_Strategic with the new values
                    for id_key in dict_A.keys():
                        A_val = dict_A.get(id_key, None)
                        B_val = dict_B.get(id_key, None)
                        print(f"Updating id {id_key} with A_val: {A_val}, B_val: {B_val}")

                        cur_C.execute("""
                            UPDATE report_table 
                            SET A = %s, B = %s
                            WHERE id = %s;
                        """, (A_val, B_val, id_key))

                    # Step 1 (VIEW TABLE): Fetch data from each source database
                    cur_A.execute("SELECT id, A FROM view_table;")
                    data_A = cur_A.fetchall()
                    print(f"Data fetched from db_A view_table: {data_A}")

                    cur_B.execute("SELECT id, B FROM view_table;")
                    data_B = cur_B.fetchall()
                    print(f"Data fetched from db_B view_table: {data_B}")

                    # Step 2 (VIEW TABLE): Create dictionaries to map IDs to column values
                    dict_A = {row[0]: row[1] for row in data_A}
                    dict_B = {row[0]: row[1] for row in data_B}
                    print(f"Dictionary A: {dict_A}")
                    print(f"Dictionary B: {dict_B}")

                    # Step 3 (VIEW TABLE): Update db_Strategic with the new values
                    for id_key in dict_A.keys():
                        A_val = dict_A.get(id_key, None)
                        B_val = dict_B.get(id_key, None)
                        print(f"Updating id {id_key} with A_val: {A_val}, B_val: {B_val}")

                        cur_C.execute("""
                            UPDATE view_table 
                            SET A = %s, B = %s
                            WHERE id = %s;
                        """, (A_val, B_val, id_key))

                    # Step 1 (TARGET TABLE): Fetch data from each source database
                    cur_A.execute("SELECT id, A FROM target_table;")
                    data_A = cur_A.fetchall()
                    print(f"Data fetched from db_A target_table: {data_A}")

                    cur_B.execute("SELECT id, B FROM target_table;")
                    data_B = cur_B.fetchall()
                    print(f"Data fetched from db_B target_table: {data_B}")

                    # Step 2 (TARGET TABLE): Create dictionaries to map IDs to column values
                    dict_A = {row[0]: row[1] for row in data_A}
                    dict_B = {row[0]: row[1] for row in data_B}
                    print(f"Dictionary A: {dict_A}")
                    print(f"Dictionary B: {dict_B}")

                    # Step 3 (TARGET TABLE): Update db_Strategic with the new values
                    for id_key in dict_A.keys():
                        A_val = dict_A.get(id_key, None)
                        B_val = dict_B.get(id_key, None)
                        print(f"Updating id {id_key} with A_val: {A_val}, B_val: {B_val}")

                        cur_C.execute("""
                            UPDATE target_table 
                            SET A = %s, B = %s
                            WHERE id = %s;
                        """, (A_val, B_val, id_key))
                
                    # Commit the transaction
                    conn_C.commit()

                    print("Database C updated successfully (I think).")

                except Exception as e:
                    print(f"An error occurred updating DB C: {e}")
            
                finally:
                    # Close all cursors and connections
                    cur_A.close()
                    cur_B.close()
                    cur_C.close()
                    conn_A.close()
                    conn_B.close()
                    conn_C.close()

        except Exception as e:
            print(f"An error occurred connecting to the databases: {e}")

def main():
    # Create an instance of the Op_Manager_Class, importing the environmental variable for db_letter
    
    db_letter = os.environ.get('op_db_letter')
    isolation_level = os.environ.get('op_isolation_level')######################
    
    print(f'My db_letter is {db_letter}')
    print(f'My isolation level is {isolation_level}')
    op_manager = Op_Manager_Class(db_letter,isolation_level)
    while True:
        print(f'Updating database {db_letter} Database...')
        op_manager.update_database()

if __name__ == "__main__":
    main()
