## BASE IMAGE
FROM python:3.8.2-slim-buster AS builder
RUN apt-get update && apt-get upgrade -y
WORKDIR /app

## IMAGE DEPENDENCIES
FROM builder AS dependencies

## APPLICATION DEPENDENCIES
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app

## PRODUCTION IMAGE
FROM dependencies AS production
ENV FLASK_ENV=production
EXPOSE 8080
CMD ["celery", "-A", "app.app", "worker", "--loglevel=info"]
#celery, worker, --app=worker.app, --pool=gevent, --concurrency=20, --loglevel=INFO