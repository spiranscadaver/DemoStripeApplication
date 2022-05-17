#! /usr/bin/env bash

# Required environment variables
# STRIPE_PUBLISHABLE_KEY
# STRIPE_SECRET_KEY

if [[ -z "${STRIPE_PUBLISHABLE_KEY}" ]]; then
  echo "Environment variable STRIPE_PUBLISHABLE_KEY not exists!"
  exit 1
fi

if [[ -z "${STRIPE_SECRET_KEY}" ]]; then
  echo "Environment variable STRIPE_SECRET_KEY not exists!"
  exit 1
fi

python3 /app/src/manage.py migrate
python3 /app/src/manage.py runserver 0.0.0.0:"${DJANGO_PORT}"
