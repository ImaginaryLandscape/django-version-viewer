# Django Version Viewer
[![Build Status](https://travis-ci.org/ImaginaryLandscape/django-version-viewer.svg?branch=master)](https://travis-ci.org/ImaginaryLandscape/django-version-viewer)


Version Viewer provides Django Admins (with appropriate permission)
the ability to view the Python packages and versions used within the project.

This tool can be used in several ways. It provides:

 - a template tag which inserts a link onto a template.
   Clicking that link opens up a pop up modal displaying installed
   Python packages.
 - a DjangoCMS toolbar entry. When clicked, a popup will display installed
   Python packages.
 - a CSV export of installed Python packages.
 - a queryable endpoint that displays installed Python packages.

You may also configure which users have access to the link and endpoint.

See .travis.yml for supported versions of Python and Django.

---------------------------------------
## Installation
---------------------------------------

To install the Django Version Viewer, simply:

    pip install django_version_viewer

Add the following to `INSTALLED_APPS` in `settings.py`

    INSTALLED_APPS = [
        'django_version_viewer'
    ]

## Add django_version_viewer urls and extend `admin/index.html`


Django Version Viewer needs to extend the `admin/index.html` and append it's urls to your `urls.py`. In your `urls.py` add:

    admin.site.index_template = 'admin/custom_index.html'
    admin.autodiscover()

    urlpatterns = [
        ...
        url(r'^django_version_viewer/', include('django_version_viewer.urls')),
        ...
    ]

    # Note that you can now make a GET request to the route `r'^django_version_viewer/'` to see
    # a list of your app's installed pip dependencies returned in JSON.

In your `templates/admin/` dir, create a `custom_index.html`.

    <!-- custom_index.html -->
    {% extends "admin/index.html" %}

    {% load i18n admin_static pip_version_viewer_tags %}

    {% block content %}
    {% show_pip_package_versions %}
    {{ block.super }}
    {% endblock %}

![Admin Integration](/images/version-viewer-admin-integration.jpg "Admin Integration")


## Django CMS integration

If Django CMS is installed, a new menu item will be added to the CMS Toolbar
Page Menu that will allow opening the version viewer popup.


![CMS Integration](/images/version-viewer-cms-integration.jpg "CMS Integration")

## Permissions

You can set your own access permissions on the template tag and route by
defining your own `Accessor` class. This class must have a `allow_access`
method that returns a `boolean`. By defualt, django_version_viewer only
allows superusers access to the route and template tag.

    # Django Version Viewer settings:
    ACCESSOR_CLASS_PATH = 'mypathto.my.AccessorClass'

    # the default class only allows superusers access
    django_version_viewer.mixins.SuperuserAccessor


## Running Tests

    # in a virtualenv
    pip install -e .[testing]
    pip install django==1.8
    flake8 .
    ENABLE_DJANGOCMS=False coverage run ./example18/manage.py test django_version_viewer


## Using the Example Project

An example project is provided to demonstrate the project.

    # in a virtualenv
    cd example18/
    pip install -r requirements.txt
    ./manage.py migrate
    ./manage.py createsuperuser
    ./manage.py runserver

    # Run without DjangoCMS
    ENABLE_DJANGOCMS=False ./manage.py runserver
