apt-get install -y python3-pip
apt-get update -y
apt-get install git -y
apt-get install wget -y
apt-get install curl -y
apt-get install --no-cache python3 py3-pip
apt-get install --virtual build-deps gcc bash \
    python3-dev musl-dev \
    openssl-dev libffi-dev libsodium-dev build-base
apt-get update


wget -O - https://gist.githubusercontent.com/fredhsu/f3d927d765727181767b3b13a3a23704/raw/3c2c55f185e23268f7fce399539cb6f1f3c45146/ubuntudocker.sh | bash

sudo apt-get update && sudo apt-get install -y apt-transport-https gnupg2
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg |sudo  apt-key add -
echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
apt-get update
apt-get install -y kubectl
apt-get update