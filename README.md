# Guideline for installing a Manga online store on your computer


## Requirements 

Installed python version 3+

## Installation 
* Install virtual environment 'python3 -m venv name_of_env'
* Create virtual environment 'virtalenv name_of_env'
* Activate virtual environment 'source name_of_env/bin/activate'
* Install all packages to your virtual environment 'pip install -r requirements.txt'

Installation complete
## Open project in your IDE
Go to file MangaProject/MangaProject/settings.py and look for Database settings. In this project I used **postgres**.
Install database with configurations in settings.

In terminal with activated environment type

'python manage.py makemigrations'

''python manage.py migrate''

'''python manage.py runserver'''

## Test in Postman

Install postman and use my postman collection to test all functionality
link to postman collection: 'https://www.getpostman.com/collections/cb0e9d96ddd593319d9d'


##View logs
<<<<<<< HEAD
* In terminal you can logs or in file test_manga.log
=======
* In terminal you can logs or in file test_manga.log
>>>>>>> 6882f6a705029e3ca92e6178e355c4ee2a76dcf4
