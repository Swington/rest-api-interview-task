FROM python:3.8.1-slim-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements/. /app/
RUN pip install -r requirements.dev.txt

COPY . /app/

CMD pytest tests -vvv