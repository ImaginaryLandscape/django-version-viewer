"""example22 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings

admin.site.index_template = 'admin/custom_index.html'
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('django_version_viewer/', include('django_version_viewer.urls')),
]

if settings.ENABLE_DJANGOCMS:
    print("CMS")
    urlpatterns += [
        path('', include('cms.urls')),
    ]
