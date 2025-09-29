from django.urls import path
from . import views


urlpatterns = [
    path("", views.upload_view, name="home"),
    path("process/", views.process_view, name="process"),
]