FROM python:3.12.8-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk update && apk add --no-cache \
    build-base \
    libffi-dev \
    postgresql-dev \
    python3-dev \
    musl-dev \
    jpeg-dev \
    zlib-dev \
    gcc \
    bash

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

# Collect static files
RUN python manage.py collectstatic --noinput

EXPORT 8000

# Run the app with gunicorn
CMD gunicorn config.wsgi:application --bind 0.0.0.0:8000
