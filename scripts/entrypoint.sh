#!/bin/sh

set -o errexit

python /app/manage.py migrate
python /app/manage.py collectstatic --noinput

exec "$@"
