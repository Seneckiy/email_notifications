GEOAP: kubernetes notebook executer 
===============

Installable App
---------------

This app used for sending emails.

This app can be installed and used in your django project by:

.. code-block:: bash

    $ pip install git+https://{username}:{token}@github.com/QuantuMobileSoftware/email_notifications.git


Edit your `settings.py` file to include `'email_notifications'` in the `INSTALLED_APPS`
listing.

.. code-block:: python

    INSTALLED_APPS = [
        ...

        'email_notifications',
    ]
