# syntax=docker/dockerfile:1

FROM debian:latest

FROM python:3.8-slim-buster

RUN mkdir -p /app/src

WORKDIR /app/src

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY start.sh /

RUN chmod +x /start.sh

COPY . .

CMD ["/start.sh"]



