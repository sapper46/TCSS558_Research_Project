#RUN apt-get update && apt-get install -y python3

#RUN pip3 install psycopg2

# Set the default command to run when the container starts
#COPY edge_reader_test.py edge_reader_test2.py
#CMD ["bash"]
#CMD ["python3", "/edge_reader_test2.py"]

#FROM debian:buster-slim
#ARG DEBIAN_FRONTEND=noninteractive
#RUN apt-get -y update && apt-get -y install python3 python3-pip curl nano procps
#RUN pip3 install --upgrade pip && pip3 install psycopg2-binary
#COPY edge_reader_test.py edge_reader_test2.py
#CMD ["python3", "actuator.py"]

# Use the official Debian image as the base image
FROM debian:buster-slim

# Set the environment variable to avoid prompts during package installation
ARG DEBIAN_FRONTEND=noninteractive

# Update the package list and install Python 3 and pip
RUN apt-get -y update && apt-get -y install \
    python3 \
    python3-pip \
    build-essential \
    libpq-dev \
    curl \
    nano \
    procps

# Install psycopg2-binary
RUN pip3 install psycopg2-binary

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Set the default command to run when the container starts
#CMD ["python3", "sensor.py"]