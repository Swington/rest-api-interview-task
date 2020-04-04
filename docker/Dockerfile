FROM python:3.8.1-slim-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app/

CMD gunicorn --bind 0.0.0.0:5000 app:app