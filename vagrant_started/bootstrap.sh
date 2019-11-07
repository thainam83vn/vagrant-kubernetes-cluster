apt-get update -y
apt-get install docker.io -y
systemctl enable docker
apt-get install curl -y
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add
apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"
apt-get install kubeadm -y
kubeadm reset -f
echo "Joining Kubernete"
hostname
swapoff -a
kubeadm join 192.168.2.227:6443 --token neslbs.yars2oqeedtzsy1w --discovery-token-ca-cert-hash sha256:c8f42c63ffe6597d0b71678f1b89a7ff70ccf83ecd615ba7e5b4e5b498fce518 

