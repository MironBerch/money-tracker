# Zadacnhic

## Technologies:
- Django 4
- Postgresql


## Configuration
Docker containers:
 1. server
 2. db

docker-compose files:
 1. `docker-compose-local.yml` - for local development

To run docker containers you have to create a `.env` file in the root directory.

### Example of `.env` file:

```dotenv
# Project
SECRET_KEY=
DEBUG=


# SMTP
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=


# Postgres
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=<db>
POSTGRES_PORT=

```

### Start project:

Local:
```shell
docker-compose -f docker-compose-local.yml up --build
```
