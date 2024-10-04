#Get the base image
FROM apache/airflow:2.7.1-python3.9

#Copy requirements into the docker container
COPY ./requirements.txt /opt/airflow

#Set user to root to install software
USER root

RUN apt-get update && apt-get install -y vim nano python3-dev openjdk-11-jdk && apt-get clean

# Set JAVA_HOME environment variable
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-arm64


USER airflow

RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt



