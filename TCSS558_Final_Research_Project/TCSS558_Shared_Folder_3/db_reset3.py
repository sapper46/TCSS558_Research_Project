import psycopg2

def reset_strategic_tables(conn_details, tables_info):
    """
    Connects to the strategic PostgreSQL database using the provided connection details,
    and resets every column (except the primary key) in each table listed in tables_info.
    
    For report_table (which holds text) the columns are set to '0' (as text),
    while for the other tables (which hold integers) the columns are set to 0.
    """
    try:
        conn = psycopg2.connect(**conn_details)
        cur = conn.cursor()
        for table, info in tables_info.items():
            columns = info["columns"]
            # Set value '0' for text columns and 0 for numeric columns
            if info["type"] == "text":
                values = tuple("RESET" for _ in columns)
            else:
                values = tuple(0 for _ in columns)
            
            # Build the UPDATE query
            set_clause = ", ".join(f"{col} = %s" for col in columns)
            query = f"UPDATE {table} SET {set_clause};"
            cur.execute(query, values)
            print(f"Reset table {table} in strategic database {conn_details['dbname']}.")
        conn.commit()
    except Exception as e:
        print(f"Error resetting tables in strategic database {conn_details['dbname']}: {e}")
    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()

def main():
    # Strategic database connection details
    strategic_conn_details = {
        'dbname': 'mydatabase_Strategic',
        'user': 'myuser_Strategic',
        'password': 'mypassword_Strategic',
        'host': 'localhost',
        'port': 5435
    }
    
    # Define table information. Adjust the columns as needed.
    tables_info = {
        "report_table": {"type": "text", "columns": ["A", "B", "C"]},
        "view_table": {"type": "int", "columns": ["A", "B", "C"]},
        "target_table": {"type": "int", "columns": ["A", "B", "C"]},
        "permission_table": {"type": "int", "columns": ["A", "B", "C"]}
    }
    
    print("Resetting all tables in strategic database...")
    reset_strategic_tables(strategic_conn_details, tables_info)

if __name__ == '__main__':
    main()

