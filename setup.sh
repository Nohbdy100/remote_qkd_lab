#!/bin/bash

# update repos & update
sudo apt update && sudo apt upgrade

# install lib for python serial connections
sudo apt install python3-serial/stable

# add user to dialout
sudo usermod -a -G dialout $USER
#NOTE: ^ is this necessary?
