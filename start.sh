#!/bin/bash

gunicorn -b 0.0.0.0:8042 --max-requests 1000 --timeout 30 ${FRAMEWORK}-${DB}:app
