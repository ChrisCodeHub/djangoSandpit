# djangoSandpit
Sandpit project to explore django and various databases

The aim is to 

Create a basic docker compose based project that spins up django in 1 container and an SQL data base in another
Then try some toy porjects to experiment with the models and how they interact with the ORM of Django


The basis of the Docker Compose file was inspired by...
https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/
and the free harvard course https://cs50.harvard.edu   https://cs50.harvard.edu/web/2020/weeks/4/



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

so far so good
Django is structured as a series of apps.  So - create an app

# following the Harvard lectures
python manage.py startapp flights

This creates teh app directories.  To be useful

                - add the app to the project settings.py  into INSTALLED_APPS  so Django knows about it
                - in urls.py    
                    - add import include to from django.urls import line
                    - to urlpatterns[] add path("flights/", include("flights.urls"))
                    - this adds the url paths for the app to the base router
                    - then in flights add a urls.py since the above just pointed to it... so it better exist
                    - inside flights.urls add the below text to act as teh routing from the api to teh views

                    - create a model to define a table that we care about
                         - a simple model is in the flights.models.py

                    - once you have a model... you need a migration to update/create a database table
                       - python manage.py makemigrations
                       - python manage.py migrate

                       you could enter a django shell by
                           - python manage.py shell  # 
                           - this is a command line, that has your django model in it
                           - import model, create one, add, save and see the database grow...
                           - call filter funcs to experiment with recalling lines
                        f = Flight...
                        f.save()
                        flight = Flight.object.all()

                    - to access all of this - 
                        you need a view (as in views.py) that picks up the url and calls the model
                        model gets the data, views then formats and returns

files that get chanegd to bring to life
app/proj1/settings.py   - extend INSTALLED_APPS = []  to know about flights app
app/proj1/urls.py - extend urlpatterns = [] to direct suitable urls to flights app
create the flights.urls and add some views to it
add a model to define a database table
add a view that access the model and returns some information
shell into the django project and explore the operations available on models



# useful from command line 
```
docker compose up -d
docker exec -it djangosandpit-web-1 bash
docker compose down
```

#useful inside the container
```
django-admin startproject proj1 .    --> create a djano project
python manage.py startapp flights    --> create an app inside the project
python manage.py shell               --> in you jump to the django

python manage.py makemigrations  --> every time you add a new model
python manage.py migrate         --> every time you add a new model
python manage.py loaddata initial_data   --> allows a preload for a table, setting Primary Keys in the fixture is a good idea
```

sometimes its useful to preload some static data into a table, say an about-us.
You can do this with a fixture - put a json file in /fixtures, then preload with the loaddata command above