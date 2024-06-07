import random
import os

from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Team, Player


def try_generate_teams():
    teams = []
    players = list(Player.objects.all())
    i = 0
    while players:
        player1_index = random.randrange(len(players))
        player2_index = random.randrange(len(players))
        if player2_index != player1_index and players[player2_index] not in players[player1_index].unwanted_teammates.all() and players[player1_index] not in players[player2_index].unwanted_teammates.all():
            player1 = players[player1_index]
            player2 = players[player2_index]
            players.pop(players.index(player1))
            players.pop(players.index(player2))
            team = Team(year=2024)
            team.save()
            team.players.set([player1, player2])
            teams.append(team)
            i = 0
        else:
            i += 1
        if i == 10:
            print("Failed selection, starting again")
            for team in teams:
                team.delete()
            teams = []
            break
    return teams


# Create your views here.
@login_required
@csrf_exempt
def generate_teams(request):
    if request.method == "POST":
        if 'generate_teams' in request.POST:
            upcoming_teams = Team.objects.filter(year=2024)
            if len(list(upcoming_teams)) > 0:
                messages.add_message(request, messages.INFO, "Teams have already been generated")
            else:
                for team in upcoming_teams:
                    team.delete()
                
                i = 0
                while i < 10:
                    teams = try_generate_teams()
                    if len(teams) > 0:
                        break
                    i += 1
                messages.add_message(request, messages.INFO, "New teams generated")
        elif 'show_next_team' in request.POST:
            upcoming_teams = list(Team.objects.filter(year=2024, show=False))
            if len(upcoming_teams) < 1:
                messages.add_message(request, messages.INFO, "All teams are already shown")
            else:
                upcoming_teams[0].show = True
                upcoming_teams[0].save()
                messages.add_message(request, messages.INFO, "New team shall now be showing")


    template = loader.get_template("teams/generate.html")
    upcoming_teams = Team.objects.filter(year=2024)
    context = {"upcoming_teams": upcoming_teams}
    return HttpResponse(template.render(context, request))

# Create your views here.
def draft(request):
    upcoming_teams = Team.objects.filter(year=2024, show=True)
    template = loader.get_template("teams/draft.html")
    context = {"upcoming_teams": upcoming_teams}
    return HttpResponse(template.render(context, request))