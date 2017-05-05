# Django Version Viewer

The pip package version viewer plugin allows a queryable endpoint to display a list of dicts representing all installed pip packages in the environment that django is running in. It also allows the insertion of a template tag to any template to display a link which calls up a pop up modal displaying all installed pip packages. You may also configure which users have access to the link and endpoint.

---------------------------------------
## Installation
---------------------------------------

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

In your `templates` dir, create a `custom_index.html`.

	<!-- custom_index.html -->
	{% extends "admin/index.html" %}

	{% load i18n admin_static pip_version_viewer_tags %}

	{% block content %}
	{% show_pip_package_versions %}
	{{ block.super }}
	{% endblock %}


## Permissions

You can set your own access permissions on the template tag and route by defining your own
`Accessor` class. This class must have a `allow_access` method that returns a `boolean`. By defualt,
django_version_viewer only allows superusers access to the route and template tag.

	# Django Version Viewer settings:
	# default class only allows superusers access
	ACCESSOR_CLASS_PATH = 'mypathto.my.AccessorClass'


## Running Tests

    cd example18/
		pip install -r requirements.txt
		flake8 ..
    ./manage.py test django_version_viewer
