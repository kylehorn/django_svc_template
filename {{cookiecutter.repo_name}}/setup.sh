#!/usr/bin/env bash
set -e

# pip is used for packagemanagement
echo 'Installing pip'

if [[ ! -x `which pip` ]]; then
    sudo easy_install pip
fi

echo 'pip installed'


# virtualenvwrapper is used to keep enviroments standard
echo 'Installing virtualenvwrapper'

if [[ -x `which pip` && ! -x `which mkvirtualenv` ]]; then
    pip install virtualenvwrapper
    export WORKON_HOME=~/.envs
    mkdir -p $WORKON_HOME
    source /usr/local/bin/virtualenvwrapper.sh
fi

echo 'virtualenvwrapper installed'


# set up virtualenv
echo 'Creating virtualenv for {{ cookiecutter.repo_name }}'

mkvirtualenv {{ cookiecutter.repo_name }} -r requirements.txt -a .
EOF

echo 'Virtualenv for {{ cookiecutter.repo_name }} created'

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