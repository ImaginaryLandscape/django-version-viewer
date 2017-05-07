from django import template
from ..utils import get_accessor_class


accessor = get_accessor_class()
register = template.Library()


@register.inclusion_tag('version_viewer.html', takes_context=True)
def show_pip_package_versions(context):
    request = context.get('request', None)
    results = {'allow': False}
    if request and accessor.allow_access(request=request):
        results = {'allow': True}
    return results
