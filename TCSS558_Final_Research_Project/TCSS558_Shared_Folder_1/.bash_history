sudo apt-get update
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
docker --version
docker pull postgres
sudo docker pull postgres
docker start postgres-container
sudo docker start postgres-container
docker images
sudo docker images
docker run --test-container -e POSTGRES_USER=dave -e POSTGRES_PASSWORD=test_password -e POSTGRES_DB=testdb -p 5432:5432 -d postgres
docker run --test_container -e POSTGRES_USER=dave -e POSTGRES_PASSWORD=test_password -e POSTGRES_DB=testdb -p 5432:5432 -d postgres
docker run --name test_container -e POSTGRES_USER=dave -e POSTGRES_PASSWORD=test_password -e POSTGRES_DB=testdb -p 5432:5432 -d postgres
sudo docker run --name test_container -e POSTGRES_USER=dave -e POSTGRES_PASSWORD=test_password -e POSTGRES_DB=testdb -p 5432:5432 -d postgres
docker exec -it test_container psql -U dave -d testdb
sudo docker exec -it test_container psql -U dave -d testdb
history
exit
docker ps
sudo docker ps
sudo docker exec -it test_container psql -U dave -d testdb
exit
sudo docker exec -it test_container psql -U dave -d testdb
docker ps
sudo docker ps
sudo apt update
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
FROM ubuntu:latest
RUN apt-get update &&     apt-get install -y python3 python3-pip &&     apt-get clean
ubuntu:latest
nano Dockerfile
docker build -t ubuntu-python3 .
sudo docker build -t ubuntu-python3 .
history
sudo docker run -it --name test_reader ubuntu-python3
sudo docker ps
sudo docker ps -a
docker exec -it test_reader /bin/bash
sudo docker exec -it test_reader /bin/bsh
sudo docker exec -it test_reader /bin/bash
docker start test_reader
sudo docker start test_reader
sudo docker exec -it test_reader /bin/bash
groups
sudo usermod -aG docker $USER
groups
whoami
sudo usermod -aG docker ubuntu
groups
exit
groups
code
vscode
nano
docker ps
groups
psql -h ec2-3-145-12-148.us-east-2.compute.amazonaws.com -U dave -d testdb -p 5432
sudo docker exec -it test_container psql -U dave -d testdb
docker ps
docker logs test_reader
sudo systemctl restart docker
docker ps
docker ps -l
docker start test_reader
docker ps
docker start test_container
docker ps
pwd
ls
code
sudo snap install code
sudo docker exec -it test_reader
sudo docker exec -it test_reader /bin/bash
docker stop test_reader
docker ps
docker ps -a
pwd
ls
code
exit
pwd
ls
mkdir shared_file
ls
docker run -d --test_reader -v /home/ubuntu/shared_file:~/files ubuntu
docker run -d --name test_reader -v /home/ubuntu/shared_file:~/files ubuntu
code
vscode
docker stop test_reader
docker rm test_reader
docker run -d --name test_reader -v /home/ubuntu/shared_file:~/files ubuntu
docker run -d --name test_reader -v /home/ubuntu/shared_file:/files ubuntu
docker ps
docker exec -it test_reader /bin/bash
docker start test_container
docker ps
docker start test_reader
docker ps
docker ps -l
docker exec -it test_reader /bin/bash
docker ps -a
sudo docker exec -it test_reader /bin/bash
docker logs test_reader
sudo docker logs test_reader
sudo docker run -it --name test_reader -v /home/ubuntu/shared_file:/files ubuntu /bin/bash
sudo docker exec -it test_reader /bin/bash
docker stop test_reader
docker rm test_reader
docker run -d --name test_reader -v /home/ubuntu/shared_file:/files ubuntu /bin/bash

sudo docker run -d --name test_reader -v /home/ubuntu/shared_file:/files ubuntu /bin/bash
docker run -it --test_reader ubuntu /bin/bash
docker run -it --name test_reader ubuntu /bin/bash
docker ps -a
sudo docker run -it --name test_reader -v /home/ubuntu/shared_file:/files ubuntu /bin/bash
docker start test_reader
docker ps -a
docker run test_reader /bin/bash
sudo docker run test_reader /bin/bash
docker start -i test_reader
docker ps -a
docker start -i test_reader /bin/bash
docker ps
docker start test_reader
docker exec -it test_reader /bin/bash
docker rm test_reader
docker ps- a
docker ps -a
sudo docker run -it --name test_reader2 -v /home/ubuntu/shared_file:/files ubuntu /bin/bash
ls
cd shared_file
ls
cd ..
ls
docker ps -a
sudo docker exec -it test_reader2 /bin/bash
docker stop test_reader2
docker ps -a
docker rm test_reader2
docker ps -a
sudo docker run --rm -it --name test_reader2 -v /home/ubuntu/shared_file:/files ubuntu /bin/bash
docker ps -a
docker ps
docker build -t container_reader
docker build -t ubuntu-python3
docker build -t container_reader .
sudo docker run --rm -it --name test_reader2 -v /home/ubuntu/shared_file:/files ubuntu /bin/bash
docker ps -a
ls
nano print_test.py
ls
sudo docker run --rm -it --name test_reader2 -v /home/ubuntu/shared_file:/files ubuntu /bin/bash
docker build -t container_reader .
sudo docker run --rm -it --name test_reader2 -v /home/ubuntu/shared_file:/files ubuntu /bin/bash
docker ps -a
sudo docker run --rm -it --name test_reader2 -v /home/ubuntu/shared_file:/files ubuntu /bin/bash
docker build -t container_reader .
sudo docker run --rm -it --name test_reader2 -v /home/ubuntu/shared_file:/files ubuntu /bin/bash
sudo docker run --rm -it --name test_reader2 -v /home/ubuntu/shared_file:/files container_reader
docker ps -a
docker build -t container_reader .
sudo docker run --rm -it --name test_reader2 -v /home/ubuntu/shared_file:/files container_reader
ls
cp ./shared_file/edge_reader_test.py .
ls
cd shared_file
rm edge_reader_test.py
ls
code
ls
cd ..
ls
rm shared_file
cd shared_file
ls
cd ..
cd shared_file
nano test_file.py
cd ..
rm -r shared_file
ls
ls
pwd
ls
nano Dockerfile
ls
nano print_test.py
nano Dockerfile
docker build -t container_reader .
sudo docker run --rm -it --name test_reader2 -v /home/ubuntu/:/files container_reader
docker build -t container_reader .
sudo docker run --rm -it --name test_reader2 -v /home/ubuntu/:/files container_reader
docker build -t container_reader .
sudo docker run --rm -it --name test_reader2 -v /home/ubuntu/:/files container_reader
docker build -t container_reader .
sudo docker run --rm -it --name test_reader2 -v /home/ubuntu/:/files container_reader
Docker ps -a
docker ps -a
docker rm laughing_payne
docker ps -a
docker rm adoring_hawking
docker rm mystifying_joliot
docker rm sharp_montalcini
docker rm fervent_solomon
docker ps -a
sudo docker run --rm -it --name test_reader2 -v /home/ubuntu/:/files container_reader
docker ps
docker ps -a
sudo docker run --rm -it --name test_reader2 -v /home/ubuntu/:/files container_reader
ls
nano edge_reader_test.py
sudo docker run --rm -it --name test_reader2 -v /home/ubuntu/:/files container_reader
nano edge_reader_test.py
ls
nano edge_reader_test.py
sudo docker run --rm -it --name test_reader2 -v /home/ubuntu/:/files container_reader
docker build -t container_reader .
docker ps -a
sudo docker run --rm -it --name test_reader2 -v /home/ubuntu/:/files container_reader
docker ps -a
sudo docker exec -it test_container psql -U dave -d testdb
ls
sudo sshfs -o allow_other -o IdentityFile=/home/dave/tcss558_project1.pem ubuntu@ec2-3-145-12-148.us-east-2.compute.amazonaws.com:/home/ubuntu/ /home/dave/TCSS558_Shared_Folder_1
ls
cd TCSS_Shared_Folder_1
cd TCSS558_Shared_Folder_1
ls
python3 script_builder.py
code script_builder.py
python3 script_builder.py 4 3 15 .02 8
nano script_builder.py
python3 script_builder.py 4 3 15 .02 8
ls
nano script.txt
ls
nano script.txt
python3 script_builder.py 4 3 15 .02 8
nano script.txt
python3 script_builder.py 4 3 15 .05 8
nano script.txt
python3 script_builder.py 4 3 15 .1 8
nano script.txt
python3 script_builder.py 4 3 15 .1 8
nano script.txt
ls
ls -lh file_size_25mb.txt
ls -lh file_size_20mb.txt
ls -lh file_size_15mb.txt
rm file_size_25mb.txt
ls
rm sensor.py
ls
nano script.txt
python3 actuator.py A 4 15 8
pip3 install psycopg2-binary
sudo apt install python3-pip
pip3 install psycopg2-binary
apt install python3-psycopg2-binary
sudo apt install python3-psycopg2-binary
python3 actuator.py A 4 15 8
nano script.txt
python3 actuator.py A 4 15 8
nano script.txt
python3 actuator.py A 4 15 8
ls
nano edge_reader_test.py
ls
python3 actuator.py
pip3 install psycopg2-binary
sudo apt install python3-psycopg2-binary
sudo pip3 install pyscopg2-binary
python3 -m venv myenv
apt install python3.12-venv
sudo apt-get install -y python3-pip python3-dev libpq-dev
pip3 install psycopg2-binary
sudo apt install python3-psycopg2-binary
sudo apt-get install python3-venv
ls
nano actuator.py
python3 -m venv myenv
source myenv/bin/activate
exit
python3 -m venv myenv
sudo apt-get install python3-venv
python3 -m venv myenv
sudo python3 -m venv myenv
source myenv/bin/activate
pip install psycopg2-binary
python3 actuator.py
psql -h ec2-18-216-135-214.us-east-2.compute.amazonaws.com -p 5432 -U myuser_A -d mydatabase_A
ls
python3 actuator.py
ls
python3 -m venv myenv
source myenv/bin/activate
pip install psycopg2-binary
python actuator.py
psql -h ec2-18-216-135-214.us-east-2.compute.amazonaws.com -U myuser_A -d mydatabase_A -p 5432
sudo apt install postgresql-client-common
psql -h ec2-18-216-135-214.us-east-2.compute.amazonaws.com -U myuser_A -d mydatabase_A -p 5432
sudo apt-get update
sudo agt-get install postgresql-client
sudo apt-get install postgresql-client
psql -h ec2-18-216-135-214.us-east-2.compute.amazonaws.com -U myuser_A -d mydatabase_A -p 5432
python3 actuator.py
python3 -m venv myenv
source myenv/bin/activate
python3 actuator.py
pwd
python3 actuator.py
ls
nano script.txt
python3 actuator.py
nano script.txt
ls
nano B3.txt
python3 actuator.py
ls
python3 actuator.py
ls
nano B3.txt
pwd
nano docker-compose.yml
ls
code docker-compose.yml
docker compose up --build -d
docker-compose up --build -d
sudo apt install docker-compose
docker-compose up --build -d
ls
nano Dockerfile
docker build -t acutator_container . 
nano docker-compose.yml
docker-compose up --build -d
docker compose down -v
docker-compose down -v
docker system prune -a --volumes
docker build -t actuator container .
docker build -t actuator_container .
docker-compose up --build -d
nano Dockerfile
docker-compose down -v
docker system prune -a --volumes
docker build -t actuator_container .
docker-compose down -v
docker system prune -a --volumes
docker build -t actuator_container .
docker-compose up --build -d
nano docker-compose.yml
docker-compose up --build -d
docker-compose down -v
docker system prune -a --volumes
docker build -t actuator_container .
docker-compose up --build -d
docker ps -a
docker rm -f $(docker ps -aq)
docker ps -a
docker-compose up --build -d
docker ps -a
ls
docker compose down -v
docker ps -a
docker rm -f $(docker ps -aq)
docker ps -a
docker-compose up --build -d
docker ps -a
ls
docker ps -a
docker compose down -v
docker rm -f $(docker ps -aq)
docker ps -a
docker run -it   -e SECTOR_LETTER=B   -e ACTUATOR_NUMBER=3   -e NUM_ACTUATORS_PER_SECTOR=5   -e NUM_SECTORS=5   -e INTERVAL_IN_SECONDS=5   -e NUM_INTERVALS=5   -e TIME_UNIT_PAUSE=1   actuator_container /bin/bash
ls
nano actuator.py
docker rm -f $(docker ps -aq)
docker ps -a
ls
docker run -it   -e SECTOR_LETTER=B   -e ACTUATOR_NUMBER=3   -e NUM_ACTUATORS_PER_SECTOR=5   -e NUM_SECTORS=5   -e INTERVAL_IN_SECONDS=5   -e NUM_INTERVALS=5   -e TIME_UNIT_PAUSE=1   actuator_container /bin/bash
docker ps -a
docker rm -f $(docker ps -aq)
docker ps -a
docker system prune -a --volumes
docker build -t actuator_container .
docker run -it   -e SECTOR_LETTER=B   -e ACTUATOR_NUMBER=3   -e NUM_ACTUATORS_PER_SECTOR=5   -e NUM_SECTORS=5   -e INTERVAL_IN_SECONDS=5   -e NUM_INTERVALS=5   -e TIME_UNIT_PAUSE=1   actuator_container /bin/bash
docker rm -f $(docker ps -aq)
docker run -it   -e SECTOR_LETTER=B   -e ACTUATOR_NUMBER=3   -e NUM_ACTUATORS_PER_SECTOR=5   -e NUM_SECTORS=5   -e INTERVAL_IN_SECONDS=5   -e NUM_INTERVALS=5   -e TIME_UNIT_PAUSE=1   actuator_container /bin/bash
docker rm -f $(docker ps -aq)
docker build -t actuator_container .
docker run -it   -e SECTOR_LETTER=B   -e ACTUATOR_NUMBER=3   -e NUM_ACTUATORS_PER_SECTOR=5   -e NUM_SECTORS=5   -e INTERVAL_IN_SECONDS=5   -e NUM_INTERVALS=5   -e TIME_UNIT_PAUSE=1   actuator_container /bin/bash
docker rm -f $(docker ps -aq)
docker build -t actuator_container_name .
docker run -it   -e SECTOR_LETTER=B   -e ACTUATOR_NUMBER=3   -e NUM_ACTUATORS_PER_SECTOR=5   -e NUM_SECTORS=5   -e INTERVAL_IN_SECONDS=5   -e NUM_INTERVALS=5   -e TIME_UNIT_PAUSE=1   actuator_container /bin/bash
docker rm -f $(docker ps -aq)
docker system prune -a --volumes
docker build -t actuator_container .
docker run -it   -e SECTOR_LETTER=B   -e ACTUATOR_NUMBER=3   -e NUM_ACTUATORS_PER_SECTOR=5   -e NUM_SECTORS=5   -e INTERVAL_IN_SECONDS=5   -e NUM_INTERVALS=5   -e TIME_UNIT_PAUSE=1   actuator_container /bin/bash
docker rm -f $(docker ps -aq)
docker system prune -a --volumes
docker build -t actuator_container .
docker system prune -a --volumes
docker build -t actuator_container .
docker run -it   -e SECTOR_LETTER=B   -e ACTUATOR_NUMBER=3   -e NUM_ACTUATORS_PER_SECTOR=5   -e NUM_SECTORS=5   -e INTERVAL_IN_SECONDS=5   -e NUM_INTERVALS=5   -e TIME_UNIT_PAUSE=1   actuator_container /bin/bash
ls
SECTOR_LETTER=B ACTUATOR_NUMBER=3 NUM_ACTUATORS_PER_SECTOR=5 NUM_SECTORS=5 INTERVAL_IN_SECONDS=5 NUM_INTERVALS=5 TIME_UNIT_PAUSE=1 python3 actuator.py
source myenv/bin/activate
pip install psycopg2-binary
SECTOR_LETTER=B ACTUATOR_NUMBER=3 NUM_ACTUATORS_PER_SECTOR=5 NUM_SECTORS=5 INTERVAL_IN_SECONDS=5 NUM_INTERVALS=5 TIME_UNIT_PAUSE=1 python3 actuator.py
ls
nano B3_simulation_report.txt
rm B3.txt
rm B3_simulation_report.txt
docker rm -f $(docker ps -aq)
docker system prune -a --volumes
docker-compose up --build -d
docker build -t actuator_container .
docker-compose up --build -d
docker ps -a
ls
docker ps -a
ls
docker exec -it actuator /bin/bash
docker exec -it baa6a4fbd160 /bin/bash
docker ps -a
docker rm -f $(docker ps -aq)
docker run -it   -e SECTOR_LETTER=B   -e ACTUATOR_NUMBER=3   -e NUM_ACTUATORS_PER_SECTOR=5   -e NUM_SECTORS=5   -e INTERVAL_IN_SECONDS=5   -e NUM_INTERVALS=5   -e TIME_UNIT_PAUSE=1   actuator_container /bin/bash
ls
docker rm -f $(docker ps -aq)
docker system prune -a --volumes
docker build -t actuator_container .
docker-compose up --build -d
docker ps -a
ls
docker rm -f $(docker ps -aq)
rm B3.txt
rm B3_simulation_report.txt
ls
docker ps -a
docker compose down -v
docker-compose up --build -d
docker ps -a
ls
docker rm -f $(docker ps -aq)
rm B3.txt
rm B3_simulation_report.txt
docker compose down -v
docker system prune -a --volumes
docker build -t actuator_container .
docker-compose up --build -d
docker ps -a
docker exec -it 3b1fe1677200 /bin/bash
ls
docker ps -a
docker compose down -v
docker rm -f $(docker ps -aq)
docker system prune -a --volumes
docker build -t actuator_container .
ls
nano sensor.py
ls
nano B3.txt
ls
nano actuator.py
ls
exit
ls
exit
ls
nano docker-compose.yml
nano actuator.py
ls
nano actuator.py
ls
nano B3.txt
docker compose up --build -d
docker --version
docker compose version
sudo apt-get update
sudo apt-get install docker-compose-plugin  # Debian/Ubuntu
sudo apt-get install docker-compose-plugin
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose version
docker-compose up --build -d
docker ps -a
docker compose down -v
docker system prune -a --volumes
ls
docker compose up --build -d
docker-compose version
docker compose up --build -d
docker-compose up --build -d
docker ps -a
docker logs sensor_container
docker logs --tail 50 sensor_container
ls
cp file_size_1mb.txt file_size_5mb.txt file_size_2mb.txt sensor.py ./sensor_docker_file 
ls
cd sensor_docker_file
ls
cd ..
rm sensor.py
ls
nano B3.txt
docker compose down -v
docker system prune -a --volumes
docker-compose up --build -d
docker ps -a
docker logs --tail 50 sensor_container
pw
pwd
ls
cd sensor_docker_file
pwd
cd ..
docker compose down -v
docker system prune -a --volumes
docker-compose up --build -d
docker ps -a
docker logs --tail 50 sensor_container
ls
cd sensor_docker_file
ls
cd ..
docker compose down -v
docker system prune -a --volumes
docker-compose up --build -d
docker ps -a
docker-compose up --build -d
docker ps -a
nano B3.txt
docker ps -a
docker logs --tail 50 sensor_container
docker compose down -v
docker system prune -a --volumes
docker-compose up --build -d
docker ps -a
docker logs --tail 50 sensor_container
docker compose down -v
docker system prune -a --volumes
docker-compose up --build -d
docker ps -a
docker logs --tail 50 sensor_container
docker ps -a
docker exec -it sensor_container bash
docker logs -f sensor_container
docker compose down -v
docker-compose up --build -d
docker ps -a
docker logs sensor_container
docker compose down -v
docker-compose up --build -d
docker ps -a
docker logs -f sensor_container
docker logs --tail 50 sensor_container
docker compose down -v
docker system prune -a --volumes
docker compose up --build -d
docker-compose up --build -d
docker ps -a
docker logs --tail 50 sensor_container
docker logs -f sensor_container
ls
docker stop $(docker ps -q)
docker compose down -v
docker system prune -a --volumes
export SECTOR_LETTER=B && export SECTOR_NUMBER=3 && export NUM_ACTUATORS_PER_SECTOR=4 && export NUM_SECTORS=5 && export INTERVAL_IN_SECONDS=15 && export NUM_INTERVALS=5 && export TIME_UNIT_PAUSE=1 && export FILE_SIZE=2 && export ISOLATION_LEVEL=1 && export TARGET_PRIORITIZATION=false && python3 ./sensor_docker_file/sensor.py
source myenv/bin/activate
export SECTOR_LETTER=B && export SECTOR_NUMBER=3 && export NUM_ACTUATORS_PER_SECTOR=4 && export NUM_SECTORS=5 && export INTERVAL_IN_SECONDS=15 && export NUM_INTERVALS=5 && export TIME_UNIT_PAUSE=1 && export FILE_SIZE=2 && export ISOLATION_LEVEL=1 && export TARGET_PRIORITIZATION=false && python3 ./sensor_docker_file/sensor.py
docker stop $(docker ps -q)
docker compose down -v
docker system prune -a --volumes
y
pwd
ls
cd sensor_docker_file
ls
cd ..
docker-compose up --build -d
docker ps -a
docker exec -it sensor_container bash
docker compose down -v
docker system prune -a --volumes
docker-compose up --build -d
docker ps -a
docker exec -it sensor_container bash
docker compose down -v
docker system prune -a --volumes
docker compose up --build -d
docker-compose up --build -d
docker ps -a
docker exec -it sensor_container bash
docker compose down -v
docker system prune -a --volumes
docker-compose up --build -d
docker exec -it sensor_container bash
ls
nano B3.txt
l
ls
cd sensor_docker_file
ls
code sensor.py
cd ..
docker compose down -v
docker system prune -a --volumes
docker-compose up --build -d
docker ps -a
docker exec -it sensor_container bash
docker compose down -v
docker system prune -a --volumes
docker-compose up --build -d
docker exec -it sensor_container bash
docker compose down -v
docker system prune -a --volumes
docker-compose up --build -d
docker exec -it sensor_container bash
docker ps -a
docker logs --tail 50 sensor_container
docker compose down -v
docker system prune -a --volumes
docker-compose up --build -d
docker ps -a
docker exec -it sensor_container bash
docker stop $(docker ps -q)
docker compose down -v
docker system prune -a --volumes
docker-compose up --build -d
docker ps -a
docker compose down -v
docker system prune -a --volumes
docker-compose up --build -d
docker ps -a
docker exec -it actuator_container_b3 bash
docker compose down -v
docker system prune -a --volumes
docker-compose up --build -d
docker exec -it actuator_container_b3 bash
docker compose down -v
docker system prune -a --volumes
docker compose up --build -d
ls
code B3.txt
nano B3.txt
docker compose up --build -d
docker-compose up --build -d
docker exec -it actuator_container_b3 bash
ls
code prepare_view.py
ls
python3 prepare_view.py
source myenv/bin/activate
python3 prepare_view.py
docker-compose up --build -d
docker ps -a
docker stop $(docker ps -q)
docker compose down -v
docker system prune -a --volumes
docker ps -a
python3 prepare_view.py
docker-compose up --build -d
ls
source myenv/bin/activate
docker ps -a
docker compose down -v
docker system prune -a --volumes
docker ps -a
docker system prune -a --volumes
docker ps -a
docker stop $(docker ps -q)
docker system prune -a --volumes
docker ps -a
docker-compose up --build -d
docker compose down -v
docker system prune -a --volumes
docker-compose up --build -d
docker ps -a
docker compose down -v
docker system prune -a --volumes
docker ps -a
docker compose down -v
docker system prune -a --volumes
docker ps -a
docker stop $(docker ps -q)
docker system prune -a --volumes
docker ps -a
docker-compose up --build -d
docker ps -a
docker exec -it actuator_container_b3 /bin/bash
docker ps -a
docker logs actuator_container_b3
docker-compose stop
docker-compose up --force-recreate -d
docker-compose stop
ls
python3 script_builder.py
ls
code script.txt
python3 script_builder.py 4 3 15 0.2 20
python3 script_builder.py 4 3 15 0.3 20
python3 script_builder.py 4 3 15 0.4 20
ls
docker ps -a
docker compose down -v
docker system prune -a --volumes
docker ps -a
ls
source myenv/bin/activate
pythonx prepare_view.py
python3 prepare_view.py
docker-compose up --build -d
docker ps -a
docker logs sensor_container_c2
docker ps -a
docker logs actuator_container_c2
ls
code master_script.txt
code A1_simulation_report.txt
docker ps -a
docker stop $(docker ps -q)
docker ps -a
python3 prepare_view.py
docker start $(docker ps -a -q)
docker ps -a
docker stop $(docker ps -q)
source myenv/bin/activate
docker ps -a
docker stop $(docker ps -q)
ls
python3 prepare_view.py
docker start $(docker ps -a -q)
docker ps -a
python3 report_compiler.py
docker stop $(docker ps -q)
python3 prepare_view.py
docker start $(docker ps -a -q)
docker ps -a
docker compose down -v
docker-compose down -v
docker-compose up --build -d
docker-compose down -v
python3 prepare_view.py
docker-compose up --build -d
docker ps -a
ls
docker logs actuator_container_b2
docker ps -a
docker-compose down -v
ls
python3 replace_zeroes.py
ls -l A1.txt
chmod +w A1.txt
sudo python3 replace_zeroes.py
docker-compose down -v
sudo python3 replace_zeroes.py
python3 prepare_view.py
docker-compose up --build -d
docker logs actuator_container_b2
docker-compose down -v
sudo python3 replace_zeroes.py
python3 prepare_view.py
docker-compose up --build -d
docker logs actuator_container_b2
docker-compose down -v
sudo python3 replace_zeroes.py
ls
source myenv/bin/activate
docker-compose down -v
docker-compose down
docker compose down
docker ps -a
docker system prune -a --volumes
docker-compose up --build -d
docker-compose down -v
sudo python3 replace_zeroes.py
python3 prepare_view.py
docker-compose up --build -d
docker ps -a
docker logs actuator_container_b2
\exit
ls
docker ps -a
docker-compose down -v
sudo python3 replace_zeroes.py
ls
python3 prepare_view.py
source myenv/bin/activate
python3 prepare_view.py
ls
code actuator.py
docker-compose down -v
docker system prune -a --volumes
docker-compose up --build -d
docker-compose down -v
python3 prepare_view.py
sudo python3 replace_zeroes.py
python3 prepare_view.py
docker-compose up --build -d
docker ps -a
docker logs acutator_container_c2
docker logs actuator_container_c2
docker-compose down -v
sudo python3 replace_zeroes.py
python3 prepare_view.py
docker-compose up --build -d
docker ps -a
docker logs actuator_container_c2
docker ps -a
python3 report_compiler.py
python3 prepare_view.py
docker-compose down -v
python3 prepare_view.py
sudo python3 replace_zeroes.py
python3 prepare_view.py
docker-compose up --build -d
docker ps -a
docker-compose down -v
sudo python3 replace_zeroes.py
python3 prepare_view.py
docker-compose up --build -d
docker ps -a
docker logs actuator_container_b2
docker-compose down -v
sudo python3 replace_zeroes.py
python3 prepare_view.py
docker start ubuntu-op_db_manager_a-1 ubuntu-op_db_manager_b-1 ubuntu-op_db_manager_c-1
docker-compose up --build -d
docker ps -a
ls
nano script.txt
docker-compose down -v
ls
python3 report_compiler.py
docker ps -a
source myenv/bin/activate
sudo python3 replace_zeroes.py
python3 prepare_view.py
docker-compose up --build -d
docker ps -a
ls
nano A1_simulation_report.txt
docker-compose down -v
sudo python3 replace_zeroes.py
python3 prepare_view.py
source myenv/bin/activate
python3 prepare_view.py
docker-compose up --build -d
docker ps -a
docker-compose down -v
python3 report_compiler.py
sudo python3 replace_zeroes.py
python3 prepare_view.py
docker start ubuntu-op_db_manager_a-1 ubuntu-op_db_manager_b-1 ubuntu-op_db_manager_c-1
python3 prepare_view.py
docker-compose up --build -d
docker ps -a
docker-compose down -v
sudo python3 replace_zeroes.py
python3 prepare_view.py
sudo python3 replace_zeroes.py
python3 prepare_view.py
docker-compose up --build -d
docker ps -a
source myenv/bin/activate
docker ps -a
docker-compose down -v
sudo python3 replace_zeroes.py
python3 prepare_view.py
docker-compose up --build -d
docker ps -a
docker stop ubuntu-op_db_manager_a-1 ubuntu-op_db_manager_b-1 ubuntu-op_db_manager_c-1
docker-compose down -v
sudo python3 replace_zeroes.py
python3 prepare_view.py
docker-compose up --build -d
docker ps -a
docker-compose down -v
replace_zeroes.py
sudo python3 replace_zeroes.py
python3 prepare_view.py
docker-compose up --build -d
docker ps -a
docker-compose down -v
