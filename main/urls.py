from django.urls import path, include

from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [
path("", views.index, name="index" ),
path("volunteer/", views.volunteer, name="volunteer"),
path("volunteer/intercession", views.intercession, name="intercession"),
path("volunteer/tompkins", views.tompkins, name="tompkins"),
path("volunteer/calendar", views.calendar, name="tompkins"),
path("gethelp", views.help, name="help"),
path("register/", user_views.register, name="register"),
path("", include("django.contrib.auth.urls"))



]