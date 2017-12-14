from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name = 'main'),
    url(r'^main', views.main, name = 'main'),
    url(r'^new', views.new, name = 'new'),
    url(r'^bombei', views.bombei, name = 'bombei'),
    url(r'^chiwawa', views.chiwawa, name = 'chiwawa'),
    url(r'^cogi', views.cogi, name = 'cogi'),
    url(r'^shiam', views.shiam, name = 'shiam'),
    url(r'^siva', views.siva, name = 'siva'),
    url(r'^tabie', views.tabie, name = 'tabie'),
    url(r'^bierd', views.bierd, name = 'bierd'),
    url(r'^hedge', views.hedge, name = 'hedge'),
]
