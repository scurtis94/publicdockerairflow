#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER airflow;
    ALTER USER airflow WITH PASSWORD 'airflow';
    CREATE DATABASE airflow;
    GRANT ALL PRIVILEGES ON DATABASE airflow TO airflow;
    ALTER ROLE airflow WITH LOGIN SUPERUSER INHERIT CREATEDB CREATEROLE NOREPLICATION;
    \c airflow;
    CREATE SCHEMA airflow;
    ALTER ROLE airflow IN DATABASE airflow SET search_path TO airflow;
EOSQL