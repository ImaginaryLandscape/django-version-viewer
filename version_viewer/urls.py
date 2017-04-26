try:
    # django 1.6+
    from django.conf.urls import url
except ImportError:
    # django <1.6
    from django.conf.urls.defaults import url

from . import views

urlpatterns = [
    url(r'^$', views.PipPackageViewer.as_view(), name='version_viewer'),
    # url(r'^$', views.pip_package_viewer,
    #     None, name='pip_package_viewer'),
]
