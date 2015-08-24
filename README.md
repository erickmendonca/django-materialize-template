# django-materialize-template

A starter template for projects in Django using Materialize and Bower.

## Requirements:

- PIP
- Bower
- Yuglify

## Dependencies on:

- requirements\base, dev, prod or test.txt
- bower.json

## To run

- virtualenv venv
- venv\bin\activate #on linux
- pip install -r requirements.txt
- bower install
- manage.py collectstatic
- manage.py migrate


# Configuration

Set these configurations on environments variables:
```['DEBUG', 'SECRET_KEY', 'ALLOWED_HOSTS', 'DATABASE_URL', 'MEDIA_ROOT', 'STATIC_ROOT']```


# Localization

- manage.py makemessages --ignore "venv/*" -l pt_BR
- manage.py compilemessages -l pt_BR


# Obs:

- Yuglify doesn`t work on Windows


# Heroku

- Run:
```
heroku buildpacks:set https://github.com/heroku/heroku-buildpack-nodejs
heroku buildpacks:add https://github.com/heroku/heroku-buildpack-python
```
- Set environment variables