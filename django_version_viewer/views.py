from pydoc import locate

from django.http import HttpResponse
from django.conf import settings
from django.core.exceptions import PermissionDenied
from pip_viewer import list_package_versions
from django.views.generic import View
import json

accessor_class = locate(settings.ACCESSOR_CLASS_PATH)
accessor = accessor_class()


class DjangoVersionViewer(View):

    def get(self, request, *args, **kwargs):
        if not accessor.allow_access(request):
            raise PermissionDenied
        packages = list_package_versions()
        return HttpResponse(json.dumps(packages), status=200, content_type="application/json")
