# dockerairflow


Docker repo containing containers for a fully independent airflow, postgres, and spark development environemnt. All containers are fully configured and setup has already been performed. All that is needed to do is pull and run docker compose commands. 

Airflow is configured using LocalExecutor mode. Still need to fix fernet key issue

Postgres is configured with default setup. Airflow db is created on entry script and necessary permissions added.

PGAdmin is configured with default setup and postgres server is already added to the server config file.

Spark is setup with one master node and two slave nodes. Config is already done. Will add instructions on how to submit spark jobs

# postgres

postgres default password is set in docker-compose file. Entry point script is located within postgres directory. Contains a shell script that runs upon container run. Script will create the necessary Airflow user with default password of airflow. Will also create db and grant permissions to airflow user, as well as create airflow schema and set default search path.

# PGAdmin

PGAdmin defualt email and password are set in docker-compose file. Default port exposed for webui is 80
The postgres server is already added to the servers.json file within the pgadmin directory 

# Airflow

Based on puckel-airflow with slight modifications. Using LocalExecutor. WebUI is accessible on port 8080. Airflow dockerfile also installs jdk8, htop, nano, wget, and pyspark. Will also create and share directories within the airflow parent directory. These include: data, scripts, and plugins. All are located within the /usr/local/airflow directory. This parent directory is also added to the PYTHONPATH, allowing for imports from subdirectories. 

# Spark

Spark is currently based on the jupyter notebook spark docker image. This may be modified in the future, as jupyter notebook is currently not configured, but can be set up if desired. Spark master webUI is exposed on port 8181. Two spark slave clients are also available on port 8081 and 8082 respectively. 

copy repo
 git bash into repo
 run docker-compose build
     docker-compose up -d
