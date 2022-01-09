# Anime API

The project is about listing anime shows by a search by their name, initially intented to do it with django rest framework and VueJS
but decided it's best for this to be only Django (never worked only with django, so that's my best). I almost implemented and
a vertical histogram about showing how many shows are based on their rating, so for example rating is from 1-10,
if we search for naruto and there are 5 animes with rating above 9 that'll be **Rating 9 - 5 shows**, but only the 
backend part is implemented.

You can also go into a more detailed view and see a chart pie of liked/disliked ratio percentage.

## Commands to run the project
 
>  git clone git@github.com:angel-obretenov/anime.git

> cd anime

> virtualenv venv

> source venv/bin/activate # if using mac/linux

> venv\Scripts\activate # if using Windows

> pip install -r requirements.txt

> python manage.py migrate

> python manage.py runserver

Hit localhost:8000 or 127.0.0.1:8000 and that's it!
