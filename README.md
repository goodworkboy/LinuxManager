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
docker run -it -p 8888:8888 -v /home/liugx/graduation/experiences:/src/experiences mycentos7

#docker remove image
docker rmi -f mycentos7