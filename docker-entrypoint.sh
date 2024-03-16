#!/bin/bash

set -e

FLAG_FILE=/app/.initialized

if [ ! -f "$FLAG_FILE" ]; then
  python manage.py migrate
  touch "$FLAG_FILE"
fi

exec "$@"
