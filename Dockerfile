FROM python:latest

RUN mkdir /project
WORKDIR /project
COPY requirements.txt /project
RUN pip3 install -r requirements.txt