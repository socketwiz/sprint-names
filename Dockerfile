FROM python:3.8.6-buster

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONUNBUFFERED=1
WORKDIR /code/sprint_names

RUN apt-get update && apt-get install -y --no-install-recommends
RUN pip install pipenv
RUN mkdir -p /code/sprint_names

COPY . /code/

RUN pipenv install --system --deploy --ignore-pipfile
