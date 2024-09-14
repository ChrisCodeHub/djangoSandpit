# djangoSandpit
Sandpit project to explore django and various databases

The aim is to 

Create a basic docker compose based project that spins up django in 1 container and an SQL data base in another
Then try some toy porjects to experiment with the models and how they interact with the ORM of Django


The basis of the Docker Compose file was inspired by...
https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/


Note to help understand teh journey this code has taken

Start with a simple Dockerfile to get python and django inside a container
Then add bash to this container so that we can ssh into it and do stuff
Create a dockercompose yaml so that we can build and run the container
 - docker compose build                             --> to build the docker image
 - docker compose up                                --> to spin up an instance 
 - when you spin up a container it will build it of the image is out of date vs the dockerfile
 - to get the basic djano app running from scratch
     - docker compose up -d                         --> build and run, detach from container
     - docker exec -it djangosandpit-web-1 bash     --> start an ssh into the contaier
     - inside the container: 
              - django-admin startproject proj1 .    --> create a djano project
              - python manage.py runserver 0.0.0.0:8000      --> start django, serve test page on 127.0.0.1:8000