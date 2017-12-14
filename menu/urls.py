from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.pet_list, name = 'pet_list'),
    url(r'^bombei', views.bombei, name = 'bombei'),
    url(r'^chiwawa', views.chiwawa, name = 'chiwawa'),
    url(r'^cogi', views.cogi, name = 'cogi'),
    url(r'^shiam', views.shiam, name = 'shiam'),
    url(r'^siva', views.siva, name = 'siva'),
    url(r'^tabie', views.tabie, name = 'tabie'),
]
