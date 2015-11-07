from django.conf.urls import include, url
from django.contrib import admin

# 시작패키지 urls.py

from v1.urls import urlpatterns as v1_urls

urlpatterns = [
    url(r'^v1/', include(v1_urls, namespace='gb')),
    url(r'^admin/', include(admin.site.urls)),
]
