import psycopg2

def reset_all_tables(conn_details, tables_info):
    """
    Connects to a PostgreSQL database and resets every column (except the primary key)
    in each table listed in tables_info.

    tables_info is a dict where the keys are table names and the values are dicts with:
      - "type": either "text" or "int" (for the data type of the columns)
      - "columns": a list of column names to reset (assumed to be all non-primary key columns)
    """
    try:
        conn = psycopg2.connect(**conn_details)
        cur = conn.cursor()
        for table, info in tables_info.items():
            columns = info["columns"]
            # Determine the value to update for each column:
            # use '0' (as text) if table is text type, otherwise integer 0.
            if info["type"] == "text":
                values = tuple("RESET" for _ in columns)
            else:
                values = tuple(0 for _ in columns)
            
            # Build the SET clause: "col1 = %s, col2 = %s, col3 = %s"
            set_clause = ", ".join(f"{col} = %s" for col in columns)
            query = f"UPDATE {table} SET {set_clause};"
            cur.execute(query, values)
            print(f"Reset table {table} in database {conn_details['dbname']}.")
        conn.commit()
    except Exception as e:
        print(f"Error resetting tables in database {conn_details['dbname']}: {e}")
    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()

def main():
    # Define connection details for each database
    db_A_conn_details = {
        'dbname': 'mydatabase_A',
        'user': 'myuser_A',
        'password': 'mypassword_A',
        'host': 'localhost',
        'port': 5432
    }
    db_B_conn_details = {
        'dbname': 'mydatabase_B',
        'user': 'myuser_B',
        'password': 'mypassword_B',
        'host': 'localhost',
        'port': 5433
    }
    db_C_conn_details = {
        'dbname': 'mydatabase_C',
        'user': 'myuser_C',
        'password': 'mypassword_C',
        'host': 'localhost',
        'port': 5434
    }
    
    # Define the table information.
    # Here we assume each table (except the primary key) has columns: A, B, and C.
    # For report_table, these columns are text; for the others they are integers.
    tables_info = {
        "report_table": {"type": "text", "columns": ["A", "B", "C"]},
        "view_table": {"type": "int", "columns": ["A", "B", "C"]},
        "target_table": {"type": "int", "columns": ["A", "B", "C"]},
        "permission_table": {"type": "int", "columns": ["A", "B", "C"]}
    }
    
    print("Resetting all tables in database A...")
    reset_all_tables(db_A_conn_details, tables_info)
    
    print("Resetting all tables in database B...")
    reset_all_tables(db_B_conn_details, tables_info)
    
    print("Resetting all tables in database C...")
    reset_all_tables(db_C_conn_details, tables_info)

if __name__ == '__main__':
    main()

