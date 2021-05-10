# LinuxManager
毕设（基于Docker的Linux实验管理平台的设计
#environment
centos7
python3.8.9
docker 20.10.9

#import execl
url  https://blog.csdn.net/weixin_30064143/article/details/111968084


#docker build
docker build -f /home/liugx/graduation/project/dockerfile_centos7 -t mycentos7 .


#docker run
<<<<<<< HEAD
docker run -it --name=centos7  -p 8888:8888 -p 8889:22 -v /home/liugx/graduation/test/experiences:/src/experiences mycentos7
=======
docker run -it -p 8888:8888 -v /home/liugx/graduation/experiences:/src/experiences mycentos7
>>>>>>> temp

#docker remove image
docker rmi -f mycentos7


#在docker容器内安装sshd
yum -y install openssh-server
生成公钥私钥对
ssh-keygen -q -t rsa -b 2048 -f /etc/ssh/ssh_host_rsa_key -N ''
ssh-keygen -q -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N ''
ssh-keygen -t dsa -f /etc/ssh/ssh_host_ed25519_key -N ''

运行 /usr/sbin/sshd -D &
#安装sshpass
yum -y install sshpass

#使用sshpass 远程登陆docker容器内linux系统
前置条件：docker内容器运行sshd服务，并且暴露22端口
sshpass -p XXX ssh -l liugx 127.0.0.1 -p 22

