try:
    # django 1.6+
    from django.conf.urls import url
except ImportError:
    # django <1.6
    from django.conf.urls.defaults import url

from . import views

urlpatterns = [
    url(r'^$', views.DjangoVersionViewer.as_view(), name='django_version_viewer'),
    url(r'^csv/$', views.DjangoVersionViewerCSV.as_view(), name='django_version_viewer_csv'),
    url(r'^toolbar/$', views.DjangoVersionViewerToolBar.as_view(), name='django_version_viewer_toolbar'),  # noqa
]
