FROM goforbroke1006/face-detect

MAINTAINER Sergey Cherkesov <sergey.cherkesov.1006@gmail.com>

WORKDIR /opt/application/
CMD [ "python", "/opt/application/server.py", "8080" ]
EXPOSE 80 8080
