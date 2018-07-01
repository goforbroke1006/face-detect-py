FROM goforbroke1006/face-detect

MAINTAINER Sergey Cherkesov <sergey.cherkesov.1006@gmail.com>

WORKDIR /opt/application/
CMD [ "bash", "/opt/application/docker/run.sh" ]
EXPOSE 8001 8002
