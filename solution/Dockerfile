FROM python:3.6

RUN mkdir -p /usr/src/app

RUN apt-get update && apt-get -y install netcat && apt-get -y install cron && apt-get -y install vim && apt-get clean

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install requests[security]

COPY . /usr/src/app/

# ENTRYPOINT ["sh", "./entrypoint.sh"]

