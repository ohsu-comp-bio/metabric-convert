#!/bin/bash

docker build -t metabric .

docker run -ti --rm -u `id -u` -e HOME=$HOME -v $HOME:$HOME -w `pwd` metabric /bin/bash