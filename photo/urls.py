from django.conf.urls import url
from . import views

urlpatterns=[
    #index path
    url('^$', views.index,name='index'),
]