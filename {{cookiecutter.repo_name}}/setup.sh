#!/usr/bin/env bash
set -e

# pip is used for packagemanagement
echo 'Installing pip'

if [[ ! -x `which pip` ]]; then
    sudo easy_install pip
fi

# virtualenvwrapper is used to keep enviroments standard
echo 'Installing virtualenvwrapper'

if [[ -x `which pip` && ! -x `which virtualenvwrapper` ]]; then
    pip install virtualenvwrapper
    export WORKON_HOME=~/.envs
    mkdir -p $WORKON_HOME
    source /usr/local/bin/virtualenvwrapper.sh
    mkvirtualenv {{ cookiecutter.repo_name }}
fi

# pip install is used to install requirements
echo 'Installing requirements'

if [[ -x `which pip` ]]; then
    pip install -r requirements.txt
fi