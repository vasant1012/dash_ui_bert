FROM python:3.9-slim-buster
RUN set -xe && apt-get cleanall && apt-get update && apt-get upgrade -y
RUN apt-get install vim wget elinks python3-pip openssl curl libssl-dev && rm -rf /var/lib/apt/lists/*
 
RUN mkdir /opt/dash-ui/
WORKDIR /opt/dash-ui/

COPY requirements.txt /tmp/requirements.txt
COPY . /opt/dash-ui/

RUN pip install -r /tmp/requirements.txt && rm -f /tmp/requirements.txt && rm -f /opt/dash-ui/requirements.txt

#CMD [ "gunicorn", "--workers=5", "--threads=1", "-b 0.0.0.0:80", "app:server"]
CMD [ "gunicorn", "--workers=5", "--threads=1", "-b 0.0.0.0:80", "--timeout 1800", "--access-logfile access.log", "--error-logfile error.log", "--log-level debug", "app:server" ]
