{{cookiecutter.repo_name}}
^^^^^

Local
^^^^^

Run this app locally inside a virtualenv. To install virtualenvwrapper run:

.. code-block:: bash

    pip install virtualenvwrapper

The to get your application up and running, inside your new directory, run:

.. code-block:: bash

    mv {{cookiecutter.repo_name}}/local_settings_template.py {{cookiecutter.repo_name}}/local_settings.py
    pip install -r requirements.txt
    python manage.py collectstatic --noinput
    python manage.py syncdb
    python manage.py runserver_plus


Dokku
^^^^^

You need to make sure you have a server running Dokku with at least 1GB of RAM. Backing services are
added just like in Heroku however you must ensure you have the relevant Dokku plugins installed.

.. code-block:: bash

    cd /var/lib/dokku/plugins
    git clone https://github.com/rlaneve/dokku-link.git link
    git clone https://github.com/jezdez/dokku-postgres-plugin postgres
    dokku plugins-install

You can specify the buildpack you wish to use by creating a file name .env containing the following.

.. code-block:: bash

    export BUILDPACK_URL=<repository>

You can then deploy by running the following commands.

..  code-block:: bash

    git remote add dokku dokku@yourservername.com:{{cookiecutter.repo_name}}
    git push dokku master
    ssh -t dokku@yourservername.com dokku postgres:create {{cookiecutter.repo_name}}-postgres
    ssh -t dokku@yourservername.com dokku postgres:link {{cookiecutter.repo_name}}-postgres {{cookiecutter.repo_name}}
    ssh -t dokku@yourservername.com dokku config:set {{cookiecutter.repo_name}} DJANGO_CONFIGURATION=Production
    ssh -t dokku@yourservername.com dokku config:set {{cookiecutter.repo_name}} DJANGO_SECRET_KEY=RANDOM_SECRET_KEY_HERE
    ssh -t dokku@yourservername.com dokku run {{cookiecutter.repo_name}} python {{cookiecutter.repo_name}}/manage.py migrate
    ssh -t dokku@yourservername.com dokku run {{cookiecutter.repo_name}} python {{cookiecutter.repo_name}}/manage.py createsuperuser

When deploying via Dokku make sure you backup your database in some fashion as it is NOT done automatically.