from django.urls import path

from . import views

urlpatterns = [
    path("sections/", views.index, name="index"),
    path("sections/<int:num>", views.section, name="section")
]
