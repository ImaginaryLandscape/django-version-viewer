from django.urls import path

from . import views

urlpatterns = [
    path('', views.DjangoVersionViewer.as_view(), name='django_version_viewer'),
    path('csv/', views.DjangoVersionViewerCSV.as_view(), name='django_version_viewer_csv'),
    path('toolbar/', views.DjangoVersionViewerToolBar.as_view(), name='django_version_viewer_toolbar'),  # noqa
]
