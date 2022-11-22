#!/bin/bash

NAME_IMAGE="osm2xodr"

if [ ! "$(docker image ls -q "$NAME_IMAGE")" ]; then
    echo "Image ${NAME_IMAGE} not found."
    docker build -t ${NAME_IMAGE} .
fi

PWD=`pwd`
docker run -it --rm -v ${PWD}:/usr/app ${NAME_IMAGE} python main.py $@