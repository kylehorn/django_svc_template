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

if [[ ! -s "$HOME/.bash_profile" && -s "$HOME/.profile" ]] ; then
  profile_file="$HOME/.profile"
else
  profile_file="$HOME/.bash_profile"
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

    source ~/.bashrc

fi

echo 'virtualenvwrapper installed'

echo '**************************'
echo '** VIRTUALENV INSTALLED **'
echo '**************************'


echo '** run the following command **'
echo 'mkvirtualenv {{ cookiecutter.repo_name }} -r requirements.txt'
