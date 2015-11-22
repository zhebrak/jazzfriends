# coding: utf-8

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

import jazz.views as jazz


urlpatterns = [
    url(r'^$', jazz.index, name='index'),
    url(r'^feedback/$', jazz.feedback, name='feedback'),

    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
