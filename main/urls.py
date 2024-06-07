from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path("", views.index, name="index"),
    path("results", views.results, name="results"),
    path("2022", views.info2022, name="info2022"),
    path("2023", views.info2023, name="info2023"),
]