try:
    # django 3.0+
    from django.conf.urls import re_path
except ImportError:
    try:
        from django.conf.urls import url as re_path
        # django >1.6 <3.0
    except ImportError:
        # django <1.6
        from django.conf.urls.defaults import url as re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.DjangoVersionViewer.as_view(), name='django_version_viewer'),
    re_path(r'^csv/$', views.DjangoVersionViewerCSV.as_view(), name='django_version_viewer_csv'),
    re_path(r'^toolbar/$', views.DjangoVersionViewerToolBar.as_view(), name='django_version_viewer_toolbar'),  # noqa
]
