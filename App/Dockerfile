## BASE IMAGE
FROM python:3.8.2-slim-buster AS Builder
RUN apt-get update && apt-get upgrade -y && apt-get install -y curl gnupg2 gcc
WORKDIR /app

## IMAGE DEPENDENCIES
FROM Builder AS Dependencies

## APPLICATION DEPENDENCIES
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

## DEV IMAGE
FROM Dependencies AS Development
LABEL Maintainer="Peter Keech <pkeech@ngds.com>"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_ENV=development 
ENV FLASK_RUN_PORT=80
CMD ["flask", "run", "--host=0.0.0.0"]

## TEST IMAGE
FROM Dependencies AS Test
LABEL Maintainer="Peter Keech <pkeech@ngds.com>"
RUN pip install flake8

## PRODUCTION IMAGE
FROM Dependencies AS Production
ENV FLASK_ENV=production
EXPOSE 8080
CMD ["uwsgi", "app.ini"] 