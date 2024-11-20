# Currency exchange API

Simple REST API for viewing currency exchange rates fetched from `Yahoo!
Finance`.

## Setup

Follow the steps below to set up the project.

Install dependencies.

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Apply migrations.

```bash
python manage.py migrate
```

Fetch data from the external database.

```bash
python manage.py load_data
```

## Running

Before running the server make sure that you have activated `venv`.

```bash
source venv/bin/activate
```

To run the server, execute the following command:

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api`

### Updating the data

You can always update the currency rated by running:

```bash
python manage.py load_data
```

If you wish to fetch the latest data on server start, you can use the `run.sh`
script:

```bash
./run.sh
```

## Documentation

You can access the project's documentation at the following URLs:

- `http://localhost:8000/api/swagger.json`: JSON view of Swagger
- `http://localhost:8000/api/swagger.yaml`: YAML view of Swagger
- `http://localhost:8000/api/swagger/`: Swagger UI
- `http://localhost:8000/api/redoc/`: Redoc
