#!/bin/sh
echo "------ Create database tables ------"
python manage.py migrate --noinput

echo "------ import sample data ------"
python manage.py loaddata vLab.json

echo "------ create default admin user ------"
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@vlab.local', 'Passw0rd')" | python manage.py shell
gunicorn emcforum.wsgi --workers 2
