import json
import csv

from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.views.generic import View
from django.views.generic.base import TemplateView


from .pip_viewer import list_package_versions, get_pip_packages_csv
from .utils import get_accessor_class


accessor = get_accessor_class()


class DjangoVersionViewerToolBar(TemplateView):
    template_name = "toolbar.html"

    def dispatch(self, request, *args, **kwargs):
        if not accessor.allow_access(request):
            raise PermissionDenied
        return super(DjangoVersionViewerToolBar, self).dispatch(
            request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DjangoVersionViewerToolBar, self).get_context_data(**kwargs)
        packages = list_package_versions()
        context.update({'packages': packages})
        return context


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
