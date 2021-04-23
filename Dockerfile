FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Santiago

RUN apt-get update -y && \
    apt-get -y install build-essential python3-dev python3-pip python3-setuptools python3-wheel && \
    apt-get -y install python3-cffi

COPY . /app
WORKDIR /app
RUN python3 -m pip install -r requirements.txt

WORKDIR /app

EXPOSE 5010
ENTRYPOINT ["gunicorn", "-w", "4", "-b", "0.0.0.0:5010", "app:app"]