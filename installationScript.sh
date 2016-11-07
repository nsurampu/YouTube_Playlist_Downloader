#!/bin/bash
# this will install all the packages necessary for running this project

touch filePath.txt
sudo pip install --upgrade pip #installs pip
pip install --upgrade youtube-dl #installs youtube-dl
pip install pytube #installs pytube
pip install lxml #installs lxml
echo "Installation successful. You may now run the project."
