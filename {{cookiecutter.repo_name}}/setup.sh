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
  profile_file="$HOME/.zprofile"
else
  profile_file="$HOME/.zshrc"
fi

if [[ -x `which pip` && ! -x `which mkvirtualenv` ]]; then
    pip install virtualenvwrapper

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
fi

echo 'virtualenvwrapper installed'

echo '**************************'
echo '** VIRTUALENV INSTALLED **'
echo '**************************'


echo '** run the following command **'
echo ' '
echo 'mkvirtualenv {{ cookiecutter.repo_name }} -r requirements.txt'
echo ' '