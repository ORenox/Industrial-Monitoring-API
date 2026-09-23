#!/bin/sh

set -e

echo "Applying database migrations..."

python manage.py migrate 

echo "start Django Server.."

exec "$@"

#exec "$@"

# ejecuta el comando que Docker le entregue.