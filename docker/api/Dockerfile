FROM python:3.6
RUN mkdir /app
WORKDIR /app
ADD ./apiEndi/requirements.txt /app/api/

RUN pip install -r backend/requirements.txt

ADD ./docker /app/docker
ADD ./apiEndi /app/api

RUN python manage.py runserver 0:8000