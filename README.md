#django-template

.. _`Vagrant`: http://www.vagrantup.com/


Basic Django project
---

- web app files go in project/

==Heroku deploy setup
- update [app_info.json](app_info.json) with heroku app info

----

## vagrant/local setup

1. Install `Vagrant`_
2. Run ``vagrant up`` and you should be good to go.

## Django quickstart
1. vagrant ssh
2. fab vagrant.resetdb
3. fab runall


## Credentials
    admin username: admin
    admin password: pass

## Simple Django Project setup instructions

create a folder (this is the name of your app) in apps and add __init__.py models.py, admin.py, and api.py.

Set up your models in models.py first, then register them in the admin.py

register your app in LOCAL_APPS in base.py

run ``fab vagrant.resetdb`` to allow django to see your new model(s)

- at this point you can hop in to the REPL `./manage.py shell`, import your model from apps.yourappname.models and make sure it exists. its a good idea to check its existence, modify a field, and call save on it so we can check it in the admin later.

Now lets set up the api endpoint using tastypie so the front end can talk to the backend

- Head into your api.py file and create your model resource.

    - refer to the tastypie docs for nomenclature: http://django-tastypie.readthedocs.org/en/latest/resources.html

    - make sure you specify which authentication and authorization you will need for the project

- Now in urls.py, we have to set up the route by importing the resource so the frontend can recieve data from the backend.

    - refer to tastypie docs: http://django-tastypie.readthedocs.org/en/latest/api.html

    - you should now be able to hit the endpoint and get a return back with json

- Now we need to set up the front end to be able to send data to the backend:

    - use existing project or import your index.html (to the templates folder) and bring in your static folder, replacing bootstrapped file.

    - in your collection, you need to add a ``url: '/api/v1/yourmodelresource/'`` field

    - you will also need to make sure that whereever you are adding a new instance of the collection, you are also immediately calling fetch on that collection

    - since you are no longer using local storage, you can omit any ``save()`` calls in your views, just make sure to call create on your new model when adding it to your collection, vice add.
    ex: `` collection.create(foo) ``

- At this point, you will probably get a return from the server that is unreadable by marionette. the api will respond with an object, while marionette will need an array to be able to add it to the collection.

    - first, we need to add a parse function to the collection to override backbone's parse function when the ``fetch()`` is called:

    ``
        parse: function(data){
        return data.objects;
    },
    ``

    - next we need to tell django that we want to format the data coming from the server be defaulted to json. In your settings.py (base.py) file, you'll need to add

        ``TASTYPIE_DEFAULT_FORMATS = ['json']``

    under your url config block.


Now you're backend and frontend can communicate, storage is initiated, and we have a working app!

