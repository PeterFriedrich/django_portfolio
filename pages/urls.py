# pages/urls.py
# ---------------
# path object, views module
# define a list of url patterns that correspond to the
# view functions

from django.urls import path
from pages import views

urlpatterns = [
        path("", views.home, name="home"),
    ]


