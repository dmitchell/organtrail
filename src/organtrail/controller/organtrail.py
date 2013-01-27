from django.http import HttpResponse
from django.shortcuts import render_to_response
import time
import json
from recipient import Recipient
from mechanics import Mechanics

waiting_room_start = -1
state = 'staging-room'

def home(request):
    global waiting_room_start
    player = Recipient.choose()
    if waiting_room_start <= 0:
        waiting_room_start = time.time()
    return render_to_response('organtrail.html', 
                              { "player" : player.id,
                               "donorPool" : int(Mechanics.donor_pool * 100),
                               "recipients" : json.dumps(Recipient.active_players, default=lambda o: o.__dict__, ensure_ascii=False)})
    
def waiting_room(request):
    # are we done waiting?
    global state
    if state == 'staging-room' and (time.time() - waiting_room_start > 45 or len(Recipient.active_players) > 3):
        state = 'playing'
    return HttpResponse(json.dumps({ "state" : state,
                                    "players" : Recipient.active_players,
                                    "donorPool" : int(Mechanics.donor_pool * 100),
                                    "timeRemaining" : 45 - time.time() + waiting_room_start
                                    }, default=lambda o: o.__dict__, ensure_ascii=False),
                        content_type = "application/json")
                                

def recipient(request, provided_id):
    if request.method == 'GET':
        return HttpResponse(json.dumps(Recipient.getRecipient(provided_id), default=lambda o: o.__dict__, ensure_ascii=False),
                        content_type = "application/json")
                     
    elif request.method == 'PUT' or request.method == 'POST':
        return HttpResponse(json.dumps(Recipient.updateRecipient(provided_id, json.loads(request.raw_post_data)), default=lambda o: o.__dict__, ensure_ascii=False),
                        content_type = "application/json")


def move(request, user_id, move_id):
    player = Recipient.getRecipient(int(user_id))
    mechanic = Mechanics.get_mechanic(int(move_id))
    response = mechanic.execute_move(player)
    # Determine if state should change (all players on same move # or time out or done)
    return HttpResponse(json.dumps({"state" : state,
                                    "players" : Recipient.active_players,
                                    "donorPool" : int(Mechanics.donor_pool * 100),
                                    "result" : response}))


