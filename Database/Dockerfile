## BASE IMAGE
FROM redis:6.0-rc-buster AS builder
LABEL Maintainer="Peter Keech <pkeech@ngds.com>"
RUN apt-get update && apt-get upgrade -y

## IMAGE DEPENDENCIES
FROM builder AS dependencies

## DEV IMAGE
FROM dependencies AS development
CMD ["redis-server", "--requirepass Pa55w0rd!"]

## TEST IMAGE
FROM dependencies AS test

## PRODUCTION IMAGE
FROM dependencies AS production
CMD ["redis-server", "--requirepass Pa55w0rd!"]