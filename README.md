# Pip Package Version Viewer

The pip package version viewer plugin allows a queryable endpoint to display a list of dicts representing all installed pip packages in the environment that django is running in. It also allows the insertion of a template tag to any template to display a link which calls up a pop up modal displaying all installed pip packages. You may also configure which users have access to the link and endpoint.

---------------------------------------
## Installation
---------------------------------------

Add the following to `INSTALLED_APPS` in `settings.py`

	INSTALLED_APPS = [
		'version_viewer'
	]

Add `version_viewer` include to `urls.py`

	urlpatterns = [
		...
		url(r'^version_viewer/', include('version_viewer.urls')),
		...
	]

Choose the Accessor class that determins who can view/access the version_viewer template tag and route:

	# Version Viewer settings:
	# default class only allows superusers access
	ACCESSOR_CLASS_PATH = 'version_viewer.mxins.Accessor'


Override the `base.html` django Admin template (or the template of your choosing) by creating a `base.html` file  inside a `templates/admin` directory in your project.

Make sure you insert the necessary `src` and `link` blocks so that the popup modal works properly.

	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

Finally, load the template tags file and insert the template tag where ever you want the "Installed Versions" link to show up:

    {% load pip_version_viewer_tags %}
    {% show_pip_package_versions %}
