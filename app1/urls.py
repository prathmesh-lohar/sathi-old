from django.contrib import admin
from django.urls import path
from app1 import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home , name="home"),
    path("login", views.login , name="login"),
    path("login1st", views.login1st , name="login1st"),

    path("logout", views.logout , name="logout"),
    path("register", views.register , name="register"),
    path("profile", views.profile , name="profile"),
    path("new_profile", views.new_profile , name="new_profile"),
    path("save_personal_detail", views.save_personal_detail , name="save_personal_detail"),

    path("family_details", views.family_details , name="family_details"),

    path("cdp", views.cdp , name="cdp"),
    path("all_profiles", views.all_profiles , name="all_profiles"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 