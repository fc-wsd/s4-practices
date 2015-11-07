from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^(?P<pk>[\d]+)/$', views.show_post, name='show_post'
    ),
    url(r'^create/$', views.create_post, name='create'),
]
