# coding: utf-8

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

import jazz.views as jazz


urlpatterns = [
    url(r'^$', jazz.index),
    url(r'^admin/', include(admin.site.urls)),
]# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
