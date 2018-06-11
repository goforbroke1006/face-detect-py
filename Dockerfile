FROM debian:jessie

MAINTAINER Sergey Cherkesov <sergey.cherkesov.1006@gmail.com>

RUN apt-get update
RUN apt-get -y install git wget curl make cmake build-essential openssl
RUN apt-get -y install \
    libssl-dev libsqlite3-dev zlib1g-dev libncurses5-dev libgdbm-dev \
    libbz2-dev libssl-dev libdb-dev

RUN apt-get install -y build-essential checkinstall
RUN apt-get install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
RUN wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz
RUN tar -xzf Python-2.7.13.tgz
RUN cd Python-2.7.13 && ./configure && make && make altinstall
RUN wget https://bootstrap.pypa.io/get-pip.py && python2.7 get-pip.py

RUN apt-get -y install libgtk-3-dev libboost-all-dev python-opencv python-tk

#COPY ./ /app
#RUN cd /app && pip install -r requirements.txt
#
#WORKDIR /app

ADD requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

ADD . /app

EXPOSE 80 8080

CMD python web-app.py