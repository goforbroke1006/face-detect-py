#!/usr/bin/env bash

DOCKER_ID_USER="goforbroke1006"
DOCKER_IMAGE="face-detect"

docker build --file=docker/Dockerfile-face-detect --tag=$DOCKER_ID_USER/$DOCKER_IMAGE .
#docker tag $DOCKER_IMAGE $DOCKER_ID_USER/$DOCKER_IMAGE
docker push $DOCKER_ID_USER/$DOCKER_IMAGE

docker-compose build
docker-compose down
docker-compose up -d