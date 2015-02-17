#!/bin/bash
set -e

# move settings file
echo 'Creating local settings file'
mv {{cookiecutter.repo_name}}/local_settings_template.py {{cookiecutter.repo_name}}/local_settings.py
echo 'Local settings file created'

echo 'Collect static files'
python manage.py collectstatic --noinput
echo 'Static files collected'

echo 'Create database'
python manage.py migrate
echo 'Database created'

echo 'Start server'
python manage.py runserver_plus