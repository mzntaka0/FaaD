# FaaD
FastAPI as a Document

## Dependencies(See details in `pyproject.toml` file)
* fastAPI
* Pydantic
* Poetry
* SQLAlchemy



## Installation
clone

install dependencies
```
poetry install
```

set environment variables(see more details in .env.example file)
```
cp .env.example .env

vi .env
```

## Dev
first, going into virtual env
```
poetry shell
```

then run `main.py`
```
python app/main.py

---
INFO:     Started server process [63995]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
```

run on docker
```
docker-compose up --build
```


## Deploy
```
docker-compose up --build -d
```

## checking a document(automatically created by fastAPI)
get access to `/docs` on your hosting domain.  e.g.) https://localhost:8080/docs

## how to add packages
```
poetry add ${package_name}
```
