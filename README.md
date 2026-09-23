# Industrial Monitoring API

REST API for monitoring industrial machines, sensors, measurements, alerts and maintenance operations.

The project was designed as a backend and SDET portfolio project based on an industrial monitoring scenario.

## Architecture

The application is built with Django and Django REST Framework and uses PostgreSQL as its relational database.
## DB Schema

![alt text](image.png)

## Technologies
Python 3.13
Django
Django REST Framework
PostgreSQL
JWT Authentication
Swagger / OpenAPI
Pytest
pytest-django
pytest-cov
Docker
Docker Compose
GitHub Actions
## Features
Machine management
Sensor management
Industrial measurements
Alert management
Maintenance records
JWT authentication
Role-based permissions
REST API
OpenAPI / Swagger documentation
Autlistoomated tests
Dockerized development environment
Continuous Integration with GitHub Actions


## Requirements

- Python 3.13
- PostgreSQL 17
- Docker
- Docker Compose

## Local Setup

### 1. Clone the repository

git clone <repository-url>
cd industrial-monitoring

### 2. Create and activate the virtual environment

python -m venv .venv

Windows:

.venv\Scripts\activate

Linux/macOS:

source .venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Configure environment variables

Create a .env file based on .env.example.

Example:

DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

POSTGRES_DB=industrial_monitoring
POSTGRES_USER=django
POSTGRES_PASSWORD=django_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5433

### 5. Start PostgreSQL

docker compose up -d db


### 6. Run migrations

python manage.py migrate

### 7. Start Django

python manage.py runserver

The API will be available at:

http://localhost:8000/



## API

The API is available under the `/api/` prefix.

### Main endpoints

| Resource | Endpoint | Methods |
|---|---|---|
| Machines | `/api/machines/` | GET, POST, PUT, PATCH, DELETE |
| Sensors | `/api/sensors/` | GET, POST, PUT, PATCH, DELETE |
| Measurements | `/api/measurements/` | GET, POST, PUT, PATCH, DELETE |
| Alerts | `/api/alerts/` | GET, POST, PUT, PATCH, DELETE |
| Maintenance | `/api/maintenance/` | GET, POST, PUT, PATCH, DELETE |

### API Documentation

Swagger UI:

`http://localhost:8000/api/docs/`

OpenAPI schema:

`http://localhost:8000/api/schema/`


## Authentication

The API uses JWT authentication.

### Obtain access and refresh tokens

Send a POST request to:

`/api/token/`

Example:

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

## Permissions

The API implements role-based permissions for protected operations.

Regular authenticated users can perform read operations.

Staff users can perform write operations on protected resources.

For example, the Machine API allows:

- GET: available for unauthenticated and authenticated users
- POST: staff users only
- PUT: staff users only
- PATCH: staff users only
- DELETE: staff users only


## Measurement Filters

Measurements support query parameters for filtering.

### Filter by sensor

GET /api/measurements/?sensor=1

### Filter by minimum value

GET /api/measurements/?min_value=50

Filter by maximum value

GET /api/measurements/?max_value=100

Filters can also be combined:

GET /api/measurements/?max_value=100


## Testing

The project uses Pytest and pytest-django for automated testing.

Run the complete test suite:

### Run tests with coverage:

pytest --cov=apps --cov-report=term-missing

Generate an HTML coverage report:

pytest --cov=apps --cov-report=html

## Future Improvements

Potential future improvements include:

- Pagination for large datasets
- Advanced measurement filtering
- Alert automation based on sensor thresholds
- Production deployment
- Monitoring and logging
- Performance testing
- Additional API integration tests