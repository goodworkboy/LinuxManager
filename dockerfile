FROM centos:7

MAINTAINER liugx<2423136704@qq.com>





RUN set -eux\
    \
    && groupadd students \
    && mkdir -p /src/experiences \
    && chgrp students /src/experiences



EXPOSE 8888

ENV MYPATH /src/experiences
WORKDIR $MYPATH
CMD /bin/bash