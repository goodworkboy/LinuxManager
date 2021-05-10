#基础镜像
FROM centos:7

#作者和邮箱
MAINTAINER liugx<2423136704@qq.com>

#linux执行的命令
RUN set -eux\
    \
    && groupadd students \
    && mkdir -p /src/experiences \
    && chgrp students /src/experiences

#暴露端口
EXPOSE 8888
#环境变量
ENV MYPATH /src/experiences
#初始工作目录
WORKDIR $MYPATH
#容器运行时的命令
CMD /bin/bash