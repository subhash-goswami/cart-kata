#!/bin/bash

# Run migrations
python src/manage.py migrate

# Collect static files
python src/manage.py collectstatic --noinput --clear

# Create a superuser if it doesn't exist
python src/manage.py createsuperuser --username admin --email noop@example.com --noinput || true

# Start the Django development server
exec python src/manage.py runserver 0.0.0.0:8000
