FROM python:3.12-slim

RUN apt update
RUN apt install -y postgresql-client

RUN mkdir -p /home/python/app
WORKDIR /home/python/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./server /home/python/app/
