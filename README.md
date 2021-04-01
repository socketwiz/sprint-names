# Sprint Names App

* Repository is divided into 2 sections
    1. app
       1. Contains source code for core sprint names app
       1. Docker container built from source code
    1. nginx
       1. Contains just the nginx config file to service static files and proxying to app

* Base directory of repository contains setup script to build contains and static assetts.  Please run `./setup`.
  * NOTE: You must have docker installed with the docker-compose binary in your path, and your user must be a part of the docker group on your system.

* To start the application after you ran the setup, please run `docker-compose up -d`.

* Then, browse to http://localhost
