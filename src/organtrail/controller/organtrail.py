from django.http import HttpResponse
from django.shortcuts import render_to_response
import random

available_players = range(1, 10)
npc_players = []

def home(request):
    return render_to_response('organtrail.html', 
                              { "player" : random.choice(available_players)})