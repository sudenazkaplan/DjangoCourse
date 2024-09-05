#pull oficial base image
FROM python:3.10-slim

RUN apt-get update

# Install Tkinter and Tcl
RUN apt-get install -y tk tcl

RUN apt-get install libpq-dev -y
RUN apt-get install python3-dev build-essential -y
RUN apt-get install postgresql-client -y

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV VIRTUAL_ENV=/opt/venv

#pip requirements
RUN pip install --upgrade pip
RUN pip install virtualenv && python -m virtualenv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ADD ./requirements.txt tmpt/requirements.txt
RUN pip install -r tmpt/requirements.txt

RUN pip install psycopg2

COPY . /srv/app
WORKDIR /srv/app