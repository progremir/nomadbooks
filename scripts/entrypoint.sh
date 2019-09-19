#!/bin/sh

set -o errexit

python /app/manage.py migrate

if [ -z "$PORT" ]
then
    export PORT=5000
fi

exec "$@"
