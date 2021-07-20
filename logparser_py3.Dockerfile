FROM ubuntu:16.04
LABEL author="Pad0y" github="github.com/pad0y"

WORKDIR /
RUN apt-get update \
    apt-get install -y wget bzip2 git \
    rm -rf /var/lib/apt/lists/*
