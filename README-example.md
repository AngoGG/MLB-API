# README

## Introduction

XXX

## Installation

To install the production version, proceed as follow:

```bash
$ cd directory/of/project/
$ python3 -m venv venv     # py instead of python3 on windows
$ ./venv/bin/activate      # .\venv\Scripts\activate on windows
(venv) $ python -m pip install --upgrade pip
(venv) $ pip install -r requirements.txt
```

## Configuration

For this website to work, some environment variables are expected:

- `ENVVAR_EXAMPLE`: XXX
- `DJANGO_KEY`: security key, to generate key with `django.core.management.utils.get_random_secret_key()`

XXX

## Running dev web server

Django has an internal web server used for development purpose only.

```bash
$ cd directory/of/project/
$ ./venv/bin/activate      # .\venv\Scripts\activate on windows
(venv) $ python manage.py runserver
```
And it should be up and running \o/

## Workflow

XXX

## Development

For those who want to use this repository for development purpose, it is required to install the packages listed in the dedicated file. So, please do

```bash
$ cd directory/of/project/
$ ./venv/bin/activate      # .\venv\Scripts\activate on windows
(venv) $ pip install -r requirements-dev.txt
```

XXX


### Testing

XXX