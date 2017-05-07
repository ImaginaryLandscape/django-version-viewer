from pydoc import locate
from django.core import exceptions
from django.conf import settings


def get_accessor_class():
    accessor_class_str = getattr(
        settings, 'ACCESSOR_CLASS_PATH', 'django_version_viewer.mixins.SuperuserAccessor')
    accessor_class = locate(accessor_class_str)
    if not accessor_class or not accessor_class_str:
        raise exceptions.ImproperlyConfigured(
            "ACCESSOR_CLASS_PATH must be a valid class.  Was given '{}'".format(
                str(accessor_class_str)))
    return accessor_class()
