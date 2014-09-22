vLab-event
==========
django app for handling EMC's vLab autologinlinks for an event

Requirements:
-------------
* Python (3)
* Django (1.7)
* django-environ (0.3.0)
* psycopg2 (2.5.4) for postgresql support

Installation:
-------------

First clone the repository:

    $ git clone git://github.com/vchrisb/vLab-event

create the environment fle ".env" in the "emcforum" directory

.env example:

    # as long as DEBUG=on you don't have to take care of 'static' files
    DEBUG=on
    
    # the SECRET_KEY should be unique and only known to you
    # https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
    SECRET_KEY='+_$1x@!s0z!n+ccemn#(jfc!eaw3$jq8^)m&4ys%@60002sq2d'
    
    # for sqlite database
    DATABASE_URL='sqlite:///my-local-sqlite.db'
    # for postgresql
    #DATABASE_URL='postgresql://User:Password@127.0.0.1:5432/emcforum'
    
    # The absolute path to the directory where collectstatic will collect static files for deployment.
    STATIC_ROOT='/var/www/vLab/static'

create database tables:

    $ python manage.py migrate

create admin user:

    $ python manage.py createsuperuser

Test application:
-----------------

start the django development server:

    $ python manage.py runserver 0.0.0.0:8000

now you should be able to access the app by ``http://<IP>:8000/vLab``
and the admin interface by ``http://<IP>:8000/admin``
