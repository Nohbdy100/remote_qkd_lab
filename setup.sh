#!/bin/bash

# update repos & update
sudo apt update && sudo apt upgrade

# install lib for python serial connections
sudo apt install python3-serial/stable
sudo apt install python3-flask
sudo apt install python3-opencv #NOTE: might want headless if available

# add user to dialout
sudo usermod -a -G dialout $USER
#NOTE: ^ is this necessary?
