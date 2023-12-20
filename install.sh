#!/bin/bash

# Update system repositories
sudo apt-get update
sudo apt-get install time

# Install jq and Python3 pip
sudo apt-get install -y jq python3-pip

# Install Go tools
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install github.com/lc/gau/v2/cmd/gau@latest
go install github.com/hakluke/hakrawler@latest
go install github.com/tomnomnom/qsreplace@latest
go install github.com/ferreiraklet/airixss@latest
go install github.com/hahwul/dalfox/v2@latest
go install github.com/ffuf/ffuf/v2@latest
go install github.com/003random/getJS@latest
go install github.com/jaeles-project/gospider@latest
go install github.com/shenwei356/rush@latest
go install github.com/KathanP19/Gxss@latest
go install -v github.com/tomnomnom/anew@latest
go install github.com/tomnomnom/assetfinder@latest
go install github.com/Emoe/kxss@latest
go install github.com/takshal/freq@latest
go install github.com/tomnomnom/gf@latest
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest

# Install Notify tools
wget https://github.com/projectdiscovery/notify/releases/download/v0.0.2/notify_0.0.2_linux_amd64.tar.gz
tar -xvf notify_0.0.2_linux_amd64.tar.gz
sudo mv -v notify /usr/local/bin/

# Move Go binaries to /usr/local/bin/
sudo mv -v $HOME/go/bin/* /usr/local/bin/

# Install Python packages
pip3 install uro
pip3 install bhedak

# Clone and build urldedupe
git clone https://github.com/ameenmaali/urldedupe.git
cd urldedupe
cmake CMakeLists.txt
make
sudo cp urldedupe /usr/bin/
cd ..

# Clone and install XSStrike
git clone https://github.com/s0md3v/XSStrike.git
cd XSStrike
sudo pip3 install -r requirements.txt
cd ..

# Clone and install tplmap
git clone https://github.com/epinna/tplmap.git
cd tplmap
sudo pip3 install -r requirements.txt
cd ..

# Clone and install log4j-scan
git clone https://github.com/adilsoybali/Log4j-RCE-Scanner.git
cd Log4j-RCE-Scanner
chmod +x log4j-rce-scanner.sh
cd ..

# Setup .gf directory and copy gf and Gf-Patterns
mkdir -p $HOME/.gf
git clone https://github.com/tomnomnom/gf.git
git clone https://github.com/1ndianl33t/Gf-Patterns.git
cp -r gf/examples/* $HOME/.gf
cp -r Gf-Patterns/* $HOME/.gf

# Update system repositories again (optional)
sudo apt-get update
