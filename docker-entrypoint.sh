#!/bin/bash
set -e

#cp -r /var/www/project_50/static_2/* /var/www/project_50/static/
#rm -rf /var/www/project_50/static_2/

python manage.py collectstatic --noinput
python manage.py migrate
gunicorn project_name50.wsgi -b 0.0.0.0:${BIND_PORT:-8000}
