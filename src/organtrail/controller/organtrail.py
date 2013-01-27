from django.http import HttpResponse
from django.shortcuts import render_to_response
import time
import json
from recipient import Recipient

waiting_room_start = -1
state = 'waiting-room'

def home(request):
    global waiting_room_start
    print('home')
    player = Recipient.choose()
    if waiting_room_start <= 0:
        waiting_room_start = time.time()
    return render_to_response('organtrail.html', 
                              { "player" : player.id,
                               "recipients" : json.dumps(Recipient.active_players, default=lambda o: o.__dict__, ensure_ascii=False)})
    
def waiting_room(request):
    # are we done waiting?
    if state != 'waiting-room' and (time.time() - waiting_room_start > 45 or len(Recipient.active_players) > 3):
        state = 'playing'
    return HttpResponse(json.dumps({ "state" : state,
                                    "players" : [json.dumps(player.__dict__) for player in Recipient.active_players],
                                    "donorPool" : 0.2
                                    }),
                        content_type = "application/json")
                                

def recipient(request, provided_id):
    if request.method == 'GET':
        return HttpResponse(json.dumps(Recipient.getRecipient(provided_id), default=lambda o: o.__dict__, ensure_ascii=False),
                        content_type = "application/json")
                     
    elif request.method == 'PUT' or request.method == 'POST':
        return HttpResponse(json.dumps(Recipient.updateRecipient(provided_id, json.loads(request.raw_post_data)), default=lambda o: o.__dict__, ensure_ascii=False),
                        content_type = "application/json")

