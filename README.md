# bus-station-application

Small web application with a backend/API built with Django, using Celery to run tasks and tested with pytest.

The user interface is a html page using pure JavaScript for DOM manipulation and tested using mocha.

## .env example
```
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
SECRET_KEY=
DEBUG=
ALLOWED_HOSTS=
CELERY_BROKER_URL=
POSTGRES_HOST=
POSTGRES_PORT=
```

The .env should be inside the repo directory.

## To run
```bash
docker compose up
```

