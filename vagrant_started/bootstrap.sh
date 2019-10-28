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
kubeadm join 192.168.2.227:6443 --token b2pud5.r9f6ed6tsl8p9np5 --discovery-token-ca-cert-hash sha256:bac98ae8311149666eb511472215b45cf9d1fbd3d2866b4083317b640b11786d 


