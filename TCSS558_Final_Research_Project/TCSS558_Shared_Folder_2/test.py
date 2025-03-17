import os
import psycopg2

def update_tables(db_name, user, password, host, port, column, value):
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        cursor = connection.cursor()

        # Update report_table
        cursor.execute(f"UPDATE report_table SET {column} = %s", (value,))

        # Update view_table
        cursor.execute(f"UPDATE view_table SET {column} = %s", (value,))

        # Update target_table
        cursor.execute(f"UPDATE target_table SET {column} = %s", (value,))

        # Commit the changes
        connection.commit()

        print(f"Tables in {db_name} updated successfully.")

    except Exception as error:
        print(f"Error updating tables in {db_name}: {error}")

    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    # Database connection details for db_A
    db_A_details = {
        "db_name": "mydatabase_A",
        "user": "myuser_A",
        "password": "mypassword_A",
        "host": "localhost",
        "port": "5432"
    }

    # Database connection details for db_B
    db_B_details = {
        "db_name": "mydatabase_B",
        "user": "myuser_B",
        "password": "mypassword_B",
        "host": "localhost",
        "port": "5433"
    }

    # Database connection details for db_C
    db_C_details = {
        "db_name": "mydatabase_C",
        "user": "myuser_C",
        "password": "mypassword_C",
        "host": "localhost",
        "port": "5434"
    }

    # Update tables in db_A
    update_tables(**db_A_details, column="A", value="One")
    update_tables(**db_A_details, column="A", value=3)
    update_tables(**db_A_details, column="A", value=3)

    # Update tables in db_B
    update_tables(**db_B_details, column="B", value="One")
    update_tables(**db_B_details, column="B", value=2)
    update_tables(**db_B_details, column="B", value=2)

    # Update tables in db_C
    update_tables(**db_C_details, column="C", value="One")
    update_tables(**db_C_details, column="C", value=1)
    update_tables(**db_C_details, column="C", value=1)