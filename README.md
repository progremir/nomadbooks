[![Build Status](https://travis-ci.com/progremir/nomadbooks.svg?token=fywMsTPcnkWZ7cZppNQo&branch=master)](https://travis-ci.com/progremir/nomadbooks)

![book](https://user-images.githubusercontent.com/17231674/65391212-687faf80-dd88-11e9-9741-040460668040.png)

## Getting Started

### Prerequisites

- python3.6
- Docker
- docker-compose
- virtualenv
- Postgres

### Environment variables

| NAME                  | EXAMPLE              | DESCRIPTION                                        |
| --------------------- | ---------            | -------------------------------------------------- |
| SECRET_KEY            | notasecret           | A secret key for a particular Django installation. |
| DEBUG                 | true                 | Flag that turns on debug mode. `true` or `false`   |
| DJANGO_SETTINGS_MODULE| project.settings.base| Name of the settings module                        |
| ALLOWED_HOSTS         | *                    | List of allowed hosts, separated by comma(,)       |
| DATABASE_URL          | postgres://postgres:postgres@localhost:5432/nomadbooks           | Database connection URI                           |
| FRONT_URL             | http://localhost:8080| URL of the front-end application                   |
| AWS_ACCESS_KEY_ID     |                 | AWS Key ID                                         |
| AWS_SECRET_ACCESS_KEY |                 | AWS Access Key                                     |
| AWS_STORAGE_BUCKET_NAME|                 | S3 bucket name                                   |
### Running with Docker

Declare environment variables. You can find this information in **ENVIRONMENT VARIABLES** section.

Start services  
```
docker-compose up --build
```

Server is up and running on port 5000

### Running with manage.py

Start postgres  
```
docker-compose up postgres
```

Create virtual environment  
```
virtualenv -p python3 venv
```

Activate your virtual environment  
```
source venv/bin/activate
```

Install requirements  
```
pip install -r requirements/dev.txt
```

Declare environment variables  
```
export <ENV_VAR>=<ENV_VALUE>
```

Apply new migrations if any  
```
python manage.py migrate
```

Start server  
```
python manage.py runserver 5000
```

Server is up and running on port 5000


## Basic commands

### Setting up your users

To create a superuser account, use this command:  
```
python manage.py createsuperuser
```

### Creating migrations
 
```
python manage.py makemigrations
```

### Applying migrations
 
```
python manage.py migrate
```

### If you are using docker to start the server, then you need to execute these commands

```
docker exec -it nomadbooks_django sh
```

inside docker terminal

```commandline
python manage.py createsuperser
```

### Test coverage

To run the tests, check your coverage, and generate an HTML coverage report:
```
coverage run --source='.' manage.py test
coverage html
```
Open `htmlcov/index.html` to see output

### Running linter

```
flake8 --format=html --htmldir=flake-report
```
Open `flake-report/index.html` to see linter output

### Running tests

```
python manage.py test
```
Open `test-report.xml` to see test output

### API Documentation

Swagger is running on `/swagger/`. If your port is 5000 then it's `localhost:5000/swagger/`