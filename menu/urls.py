from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.pet_list, name = "pet_list")
]
