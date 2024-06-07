from django.urls import path

from . import views

app_name = 'teams'
urlpatterns = [
    path("generate", views.generate_teams, name="generate"),
    path("draft", views.draft, name="draft")
]