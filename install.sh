#!/bin/bash

apt-get update
apt-get install -t unstable firefox -y
pip install beautifulsoup4
pip install selenium
pip install selenium-requests
wget "https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux32.tar.gz"
tar xvzf geckodriver-v0.24.0-linux32.tar.gz
mv geckodriver /usr/local/bin
