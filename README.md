cf-vLab-event
==========
An example Cloud Foundry django app for handling EMC's vLab autologinlinks for an event. Tested with Pivotal Web Services https://run.pivotal.io/ 

Requirements:
-------------
* a Cloud Foundry account (a 60-day free trial can be found here: https://run.pivotal.io/)
* a Cloud Foundry SQL Service (ClearDB Mysql or ElephantSQL PostgreSQL)
* Cloud Foundry cli (https://github.com/cloudfoundry/cli/releases)
* git cli (http://git-scm.com/downloads)

Configuration:
-------------

First clone the repository:

    $ git clone git://github.com/vchrisb/cf-vLab-event

Configure your app and service name and modify the ``SECRET_KEY`` in ``manifest.yml``:

    ---
    applications:
    - name: vLab
      instances: 1
      memory: 128M
      command: null
      services:
      - vLab_DB
      env:
        SECRET_KEY: 'aadc-t8j*i5a7^y9@d^$at#g0!j_h=h++5stj=nb7z8u#l_y#&'
        DEBUG: 'False'

Modify ``init_db.sh`` which will be run once to initialize the DB:

    #!/bin/sh
    echo "------ Create database tables ------"
    python manage.py migrate --noinput
    
    echo "------ import sample data ------"
    python manage.py loaddata vLab.json
    
    echo "------ create default admin user ------"
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@vlab.local', 'Passw0rd')" | python manage.py shell

    echo "------ starting gunicorn  ------"
    gunicorn emcforum.wsgi --workers 2

Deploy to Cloud Foundry:
-------------

Login to Pivtoal Web Services and create ElephantSQL service:

    cf login -a https://api.run.pivotal.io
    cf marketplace
    cf create-service elephantsql turtle vLab_DB

Push app and run database initialization script:

    cf push --no-route -c "bash ./init_db.sh"
    
Push app:

    cf push

Test App:
-------------

Get ``status`` and ``URL``:

    cf app vLab
    
Sample output:

    Showing health and status for app vLab in org ORG / space SPACE as user@example.com...
    OK
    
    requested state: started
    instances: 1/1
    usage: 128M x 1 instances
    urls: vlab.cfapps.io
    
         state     since                    cpu    memory          disk
    #0   running   2014-09-22 11:40:13 AM   0.0%   90.8M of 128M   168.8M of 1G


    
now you should be able to access the app by ``http://vlab.cfapps.io``
and the admin interface by ``http://vlab.cfapps.io/admin``
