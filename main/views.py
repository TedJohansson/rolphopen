from django.http import HttpResponse
from django.template import loader

from teams.models import Team

def index(request):
    upcoming_teams = Team.objects.filter(year=2024, show=True)
    template = loader.get_template("main/index.html")
    context = {"upcoming_teams": upcoming_teams}
    return HttpResponse(template.render(context, request))


def results(request):
    template = loader.get_template("main/results.html")
    context = {}
    return HttpResponse(template.render(context, request))


def info2022(request):
    template = loader.get_template("main/year2022.html")
    context = {}
    return HttpResponse(template.render(context, request))


def info2023(request):
    template = loader.get_template("main/year2023.html")
    context = {}
    return HttpResponse(template.render(context, request))