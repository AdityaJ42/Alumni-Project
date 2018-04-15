from django.conf.urls import url
from . import views


urlpatterns = [ url(r'^addEvent/$', views.createEvent, name='addEvent'),
                url(r'^(?P<pk>[0-9]+)/$', views.eventDetails, name='details'),
                url(r'^(?P<pk>[0-9]+)/update/$', views.EventUpdateView.as_view(), name='update'),
                url(r'^(?P<pk>[0-9]+)/delete/$', views.EventDeleteView.as_view(), name='delete'),]
