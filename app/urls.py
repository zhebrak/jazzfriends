# coding: utf-8

from django.conf.urls import include, url
from django.contrib import admin

import jazz.views as jazz


urlpatterns = [
    url(r'', jazz.index),
    url(r'^admin/', include(admin.site.urls)),
]
