#!/bin/sh

set -o errexit

python /app/manage.py migrate

export GUNICORN_WORKERS=$((2 * $(nproc) + 1))
exec "$@"
