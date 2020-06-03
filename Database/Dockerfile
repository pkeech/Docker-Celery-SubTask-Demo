## BASE IMAGE
FROM redis:6.0-rc-buster AS BUILDER
LABEL Maintainer="Peter Keech <pkeech@ngds.com>"
RUN apt-get update && apt-get upgrade -y

## IMAGE DEPENDENCIES
FROM Builder AS Dependencies

## DEV IMAGE
FROM Dependencies AS Development
CMD ["redis-server", "--requirepass Pa55w0rd!"]

## TEST IMAGE
FROM Dependencies AS Test

## PRODUCTION IMAGE
FROM Dependencies AS Production
CMD ["redis-server", "--requirepass Pa55w0rd!"]