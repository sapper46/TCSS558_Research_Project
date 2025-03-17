import psycopg2
import time

# Database connection parameters
DB_HOST = "ec2-3-145-12-148.us-east-2.compute.amazonaws.com"
DB_PORT = "5432"
DB_NAME = "testdb"
DB_USER = "dave"
DB_PASSWORD = "test_password"

# File to be monitored
FILE_NAME = "generated_file.txt"

def connect_to_db():
    try:
        connection = psycopg2.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME
        )
        return connection
    except Exception as error:
        print(f"Error connecting to database: {error}")
        return None

def get_latest_file_upload(connection):
    try:
        cursor = connection.cursor()
        query = '''
        SELECT filename, file_content FROM file_uploads
        ORDER BY upload_time DESC LIMIT 1;
        '''
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        return result
    except Exception as error:
        print(f"Error fetching latest file upload: {error}")
        return None

def update_report_table(connection, timestamp, target):
    try:
        cursor = connection.cursor()
        update_query = '''
        UPDATE report_table
        SET sensor = %s, time_stamp = %s, target = %s
        WHERE id = 1;
        '''
        cursor.execute(update_query, ("SENSOR1", timestamp, target))
        connection.commit()
        cursor.close()
        print("Report table updated successfully.")
    except Exception as error:
        print(f"Error updating report table: {error}")

def process_file_content(file_content):
    # Convert memoryview to bytes
    file_content_bytes = file_content.tobytes()
    lines = file_content_bytes.decode('utf-8').split('\n')
    if len(lines) >= 2:
        timestamp = lines[0]
        target = lines[1]
        return timestamp, target
    else:
        print("File does not contain enough lines.")
        return None, None

def main():
    connection = connect_to_db()
    if connection:
        last_processed_file = None
        while True:
            latest_file = get_latest_file_upload(connection)
            if latest_file and latest_file[0] == FILE_NAME and latest_file != last_processed_file:
                file_content = latest_file[1]
                timestamp, target = process_file_content(file_content)
                if timestamp and target:
                    update_report_table(connection, timestamp, target)
                    last_processed_file = latest_file
            time.sleep(10)  # Check for new uploads every 10 seconds
        connection.close()

if __name__ == "__main__":
    main()
    #good
    #good