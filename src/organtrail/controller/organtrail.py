from django.http import HttpResponse
from django.shortcuts import render_to_response
import random

available_players = range(1, 10)
npc_players = []
human_players = []

def home(request):
    player = random.choice(available_players)
    human_players.append(player)
    available_players.remove(player)
    return render_to_response('organtrail.html', 
                              { "player" : player})