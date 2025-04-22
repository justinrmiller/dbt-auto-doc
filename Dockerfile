FROM python:3.11-slim

RUN apt-get -y update
RUN apt-get -y install git

RUN pip install dbt-postgres openai typer

WORKDIR /usr/app
