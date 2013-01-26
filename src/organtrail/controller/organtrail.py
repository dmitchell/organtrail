from django.http import HttpResponse
from django.shortcuts import render_to_response
import random
import time
import json

available_players = range(1, 10)
npc_players = []
waiting_room_start = -1
human_players = []
state = 'waiting-room'

def home(request):
    global waiting_room_start
    player = random.choice(available_players)
    if waiting_room_start <= 0:
        waiting_room_start = time.time()
    human_players.append(player)
    available_players.remove(player)
    return render_to_response('organtrail.html', 
                              { "player" : player})
    
def waiting_room(request):
    # are we done waiting?
    if state != 'waiting-room' and (time.time() - waiting_room_start > 45 or len(human_players) > 3):
        state = 'playing'
    return HttpResponse(json.dumps({ "state" : state,
                                    "players" : [],
                                    "donorPool" : 0.2
                                    }),
                        content_type = "application/json")
                                
