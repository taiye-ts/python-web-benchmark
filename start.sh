#!/bin/bash

if [ "$DB" = "postgres" ]
then
  cd /app
  sleep 10
  python postgres.py
fi

gunicorn -b 0.0.0.0:8042 --max-requests 1000 --timeout 30 ${FRAMEWORK}-${DB}:app
