#!/bin/bash
set -e

#cp -r /var/www/truegreatproject/admin_panel/static_2/ /var/www/truegreatproject/admin_panel/static/
#rm -rf /var/www/truegreatproject/admin_panel/static_2/
python manage.py collectstatic --noinput
python manage.py migrate
gunicorn project_name.wsgi -b 0.0.0.0:${BIND_PORT:-8000}