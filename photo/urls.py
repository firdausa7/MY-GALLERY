from django.conf.urls import url
from . import views

urlpatterns=[
    #index path
    url('^$', views.index,name='index'),
    url('location/', views.category, name='location'),
    url('category', views.category, name='category'),
    url('search/', views.search_results, name='search_results'),
]