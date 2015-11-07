from django.conf.urls import url

# v1/urls.py

# from . import views
from .views import list_posts

urlpatterns = [
    url(r'list/$', list_posts),
]
