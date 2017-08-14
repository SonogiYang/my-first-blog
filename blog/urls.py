from django.conf.urls import url
from . import views
#we don't have this yet, will make soon

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
