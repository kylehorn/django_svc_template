#!/bin/bash
set -e

# pip is used for packagemanagement
echo 'Installing pip'

if [[ ! -x `which pip` ]]; then
    sudo easy_install pip
fi

echo 'pip installed'


# virtualenvwrapper is used to keep enviroments standard
echo 'Installing virtualenvwrapper'

if [[ ! -s "$HOME/.zprofile" && -s "$HOME/.zshrc" ]] ; then
  profile_file="$HOME/.zshrc"
else
  profile_file="$HOME/.zprofile"
fi

if [[ -x `which pip` && ! -x `which mkvirtualenv` ]]; then
    pip install virtualenvwrapper

    { > ${profile_file} ; }
    if ! grep -q 'export WORKON_HOME=~/.envs' "${profile_file}" ; then
      echo "export WORKON_HOME=~/.envs" >> "${profile_file}"
    fi

    if ! grep -q 'mkdir -p $WORKON_HOME' "${profile_file}" ; then
      echo "mkdir -p $WORKON_HOME" >> "${profile_file}"
    fi

    if ! grep -q 'source /usr/local/bin/virtualenvwrapper.sh' "${profile_file}" ; then
      echo "Editing ${profile_file} to load ~/.git-completioin.bash on Terminal launch"
      echo "source /usr/local/bin/virtualenvwrapper.sh" >> "${profile_file}"
    fi

    source ${profile_file}
fi

echo 'virtualenvwrapper installed'

mkvirtualenv {{ cookiecutter.repo_name }} -r requirements.txt

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
