from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^wishitems/$', views.wishitems, name='wishitems'),
    url(r'^newitem/$', views.newitem, name='newitem'),
    url(r'^additem/(?P<id>\d+)$', views.additem, name='additem'),
    url(r'^inspect/(?P<id>\d+)$', views.inspect, name='inspect'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^remove/(?P<id>\d+)$', views.remove, name='remove')

]
