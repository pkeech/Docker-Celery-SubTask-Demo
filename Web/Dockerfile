## BASE IMAGE
FROM python:3.8.2-slim-buster AS builder
RUN apt-get update && apt-get upgrade -y && apt-get install -y curl gnupg2 gcc
WORKDIR /app

## IMAGE DEPENDENCIES
FROM builder AS dependencies

## APPLICATION DEPENDENCIES
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app

## DEV IMAGE
FROM dependencies AS development
LABEL Maintainer="Peter Keech <pkeech@ngds.com>"
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 FLASK_APP=run.py FLASK_ENV=development FLASK_RUN_PORT=80
CMD ["flask", "run", "--host=0.0.0.0"]

## TEST IMAGE
FROM dependencies AS test
LABEL Maintainer="Peter Keech <pkeech@ngds.com>"
RUN pip install flake8

## PRODUCTION IMAGE
FROM dependencies AS production
ENV FLASK_ENV=production
EXPOSE 8080
CMD ["uwsgi", "app.ini"] 