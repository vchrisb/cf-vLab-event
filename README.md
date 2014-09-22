cf-vLab-event
==========
A Cloud Foundry django app for handling EMC's vLab autologinlinks for an event. Tested with Pivotal Web Services https://run.pivotal.io/ 

Requirements:
-------------
* a Cloud Foundry account
* a Cloud Foundry Mysql Service

Configuration:
-------------

First clone the repository:

    $ git clone git://github.com/vchrisb/cf-vLab-event

Change django ``SECRET_KEY`` in ``emcforum/settings.py``:

    SECRET_KEY = '&9cj-t8j*i5a7^y9@d^$at#g0!j_h=h++5stj=nb7z8u#l_y#&'

Configure your app and service name in ``manifest.yml``:

    ---
    applications:
    - name: vchrisb
      instances: 1
      memory: 128M
      command: null
      services:
      - vchrisb_mysql

Deploy to Cloud Foundry:
-------------

Login to Pivtoal Web Services and create MySQL service:

    cf login -a https://api.run.pivotal.io
    cf marketplace
    cf create-service cleardb spark vchrisb_mysql

Push app and run database initialization script:

    cf push --no-route -c "bash ./init_db.sh"
    
Push app:

    cf push

Test App:
-------------

Get ``status`` and ``URL``:

    cf app vchrisb
    
Sample output:

    Showing health and status for app vchrisb in org ORG / space SPACE as user@example.com...
    OK
    
    requested state: started
    instances: 1/1
    usage: 128M x 1 instances
    urls: vchrisb.cfapps.io
    
         state     since                    cpu    memory          disk
    #0   running   2014-09-22 11:40:13 AM   0.0%   90.8M of 128M   168.8M of 1G


    
now you should be able to access the app by ``http://vchrisb.cfapps.io/vLab``
and the admin interface by ``http://vchrisb.cfapps.io/admin``
