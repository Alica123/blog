from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
# pre danu url yavola metodu post_list ktora vrati html 
