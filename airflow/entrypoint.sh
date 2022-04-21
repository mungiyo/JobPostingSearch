#!/bin/sh

echo "10 seconds waiting..."
sleep 10

airflow db init && \
airflow users create \
--username admin \
--password admin \
--firstname admin \
--lastname admin \
--role Admin \
--email admin@gmail.com && \
airflow webserver --port 8080 & airflow scheduler