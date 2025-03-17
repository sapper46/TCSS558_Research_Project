import psycopg2
import time

# Database configurations for A, B, and C
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

def update_view_tables():
    # Get the current time in seconds since the epoch
    current_time = time.time()
    print(f"Updating view_table with current time: {current_time}")

    # SQL query to update columns A, B, and C for rows with id 1, 2, 3, and 4.
    query = "UPDATE view_table SET A = %s, B = %s, C = %s WHERE id IN (1, 2, 3, 4);"

    # Iterate over each database configuration and perform the update.
    for db_letter, config in db_config.items():
        try:
            conn = psycopg2.connect(**config)
            cur = conn.cursor()
            cur.execute(query, (current_time, current_time, current_time))
            conn.commit()
            print(f"Successfully updated view_table in database {db_letter}.")
        except Exception as e:
            print(f"Error updating view_table in database {db_letter}: {e}")
        finally:
            if 'cur' in locals():
                cur.close()
            if 'conn' in locals():
                conn.close()

if __name__ == "__main__":
    update_view_tables()
