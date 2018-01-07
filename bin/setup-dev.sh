#!/usr/bin/env bash

sudo apt-get install -y python-pip

sudo apt-get install -y build-essential cmake
sudo apt-get install -y libgtk-3-dev
sudo apt-get install -y libboost-all-dev
sudo apt-get install -y python-opencv
sudo apt-get install -y python-tk

pip install --upgrade pip
sudo pip install -r requirements.txt