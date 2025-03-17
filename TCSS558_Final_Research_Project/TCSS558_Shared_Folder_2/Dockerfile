FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install OS dependencies and psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the Python script into the container
COPY op_db_manager.py .

# Install psycopg2
RUN pip install psycopg2-binary

# Run the Python script
CMD ["python", "op_db_manager.py"]