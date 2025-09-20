# Hello Ella Caching Service

This is a simple FastAPI micro-service that simulates the caching of responses
from another service.

## Installing Dependencies

Assuming you are in a Python virtualenv, install the required dependencies as
follows:

```bash
# For run-time dependencies
pip install -r requirements.txt

# For dev dependencies
pip install -r requirements-dev.txt
```

## Running the server

From the project root, run:

```bash
fastapi run --app app
```

## Running tests

```bash
PYTHONPATH=`pwd` pytest
```

## Running type-checking

```bash
mypy .
```

## Docker

### Building the Image

```bash
docker build -t cache-service .
```

### Running the container

```bash
docker run -d -p 8000:8000 --name cache-service cache-service
```

## Running the CLI Tool

```bash
PYTHONPATH=`pwd` python cli/main.py
```

## API Docs

API docs are available at [http://localhost:8000/docs](http://localhost:8000/docs).
