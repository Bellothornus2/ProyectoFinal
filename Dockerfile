#FROM ubuntu:16.04
FROM python:3

RUN apt-get update -y && \
    apt-get install python3-pip python-dev -y

WORKDIR /usr/src/app

COPY ./requirements.txt ./requirements.txt



RUN useradd --shell /bin/bash --no-log-init --password 1234 --home-dir /usr/src/app flaskuser 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

USER flaskuser
#VOLUME [ "D:\Archivos\FP_Superior_DAW_1\Programacion\codigos\FlaskOllivanders\Dockerfile", "/usr/src/app"]


COPY . .
#no especifico un puerto porque por defecto usaré el 5000
CMD ["python", "app.py", "production"]