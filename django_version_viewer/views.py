import json
import csv

from pydoc import locate

from django.http import HttpResponse
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.views.generic import View

from pip_viewer import list_package_versions, get_pip_packages_csv

accessor_class = locate(
    getattr(settings, 'ACCESSOR_CLASS_PATH', 'django_version_viewer.mixins.Accessor'))
accessor = accessor_class()


class DjangoVersionViewer(View):

    def get(self, request, *args, **kwargs):
        if not accessor.allow_access(request):
            raise PermissionDenied
        packages = list_package_versions()
        return HttpResponse(json.dumps(packages), status=200, content_type="application/json")


class DjangoVersionViewerCSV(View):

    def get(self, request, *args, **kwargs):
        if not accessor.allow_access(request):
            raise PermissionDenied
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="pip_package_versions.csv"'

        fieldnames = ['Package Name', 'Package Version']
        writer = csv.writer(response)

        writer.writerow(fieldnames)
        get_pip_packages_csv(writer)
        return response
