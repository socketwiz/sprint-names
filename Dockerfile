FROM python:3.8.6-buster

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_DEBUG=False
WORKDIR /code/sprint_names

RUN apt-get update && apt-get install nginx -y --no-install-recommends
RUN pip install pipenv gunicorn
RUN mkdir -p /code

COPY . /code/

RUN pipenv install --system --deploy --ignore-pipfile

