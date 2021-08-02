FROM python:3.8

ADD . /app/
WORKDIR /app

RUN apt-get update && apt-get install -y git vim
RUN pip install -r requirements.txt
