'''
Created on Jan 26, 2013

@author: dmitchell
'''
import random
from mechanics import Mechanics
import time

class Recipient(object):
    '''
    classdocs
    '''

    raw_players = [{
            "id" : 1,
            "name" : "Jim Devin",
            "lifeExpectancy" : 31,
            "description" : "John has had 2 coronary bypassess and now needs a new heart.<br/>" +
                "<p>He's active in several non-profits... He has 12 grandchildren: 3 of whom live with him...</p>",
            "age" : 78,
            "rejectionProbability" : 0.2,
            "doctor" : None,
            "rank" : 1,
            "money" : 1000
        },
        {
            "id" : 2,
            "name" : "Cindy McArthur",
            "lifeExpectancy" : 31,
            "description" : "Cindy's heart failed due to a severe illness.<br/>" +
                "<p>Cindy has 2 young children...</p>",
            "age" : 23,
            "rejectionProbability" : 0.1,
            "doctor" : None,
            "rank" : 2,
            "money": 1000
        },
        {
            "id" : 3,
            "name" : "Alan Merkel",
            "lifeExpectancy" : 31,
            "description" : "John has had 2 coronary bypassess and now needs a new heart.<br/>" +
                "<p>He's active in several non-profits... He has 12 grandchildren: 3 of whom live with him...</p>",
            "age" : 78,
            "rejectionProbability" : 0.2,
            "doctor" : None,
            "rank" : 3,
            "money" : 1000                 
        },
        {
            "id" : 4,
            "name" : "Julie Hunter",
            "lifeExpectancy" : 31,
            "description" : "Cindy's heart failed due to a severe illness.<br/>" +
                "<p>Cindy has 2 young children...</p>",
            "age" : 23,
            "rejectionProbability" : 0.1,
            "doctor" : None,
            "rank" : 5,
            "money" : 1000                 
        },
        {
            "id" : 5,
            "name" : "Steve Black",
            "lifeExpectancy" : 31,
            "description" : "John has had 2 coronary bypassess and now needs a new heart.<br/>" +
                "<p>He's active in several non-profits... He has 12 grandchildren: 3 of whom live with him...</p>",
            "age" : 78,
            "rejectionProbability" : 0.2,
            "doctor" : None,
            "rank" : 4,
            "money" : 1000                 
        },
        {
            "id" : 6,
            "name" : "Alana Daniels",
            "lifeExpectancy" : 31,
            "description" : "Cindy's heart failed due to a severe illness.<br/>" +
                "<p>Cindy has 2 young children...</p>",
            "age" : 23,
            "rejectionProbability" : 0.1,
            "doctor" : None,
            "rank" : 6,
            "money" : 1000                 
        },
        {
            "id" : 7,
            "name" : "Aaron Woods",
            "lifeExpectancy" : 31,
            "description" : "John has had 2 coronary bypassess and now needs a new heart.<br/>" +
                "<p>He's active in several non-profits... He has 12 grandchildren: 3 of whom live with him...</p>",
            "age" : 78,
            "rejectionProbability" : 0.2,
            "doctor" : None,
            "rank" : 7,
            "money" : 1000                 
        },
        {
            "id" : 8,
            "name" : "Lucy Diamonds",
            "lifeExpectancy" : 31,
            "description" : "Cindy's heart failed due to a severe illness.<br/>" +
                "<p>Cindy has 2 young children...</p>",
            "age" : 23,
            "rejectionProbability" : 0.1,
            "doctor" : None,
            "rank" : 9,
            "money" : 1000                 
        },
        {
            "id" : 9,
            "name" : "Calvin Hobbes",
            "lifeExpectancy" : 31,
            "description" : "John has had 2 coronary bypassess and now needs a new heart.<br/>" +
                "<p>He's active in several non-profits... He has 12 grandchildren: 3 of whom live with him...</p>",
            "age" : 78,
            "rejectionProbability" : 0.2,
            "doctor" : None,
            "rank" : 8,
            "money" : 1000                 
        },
        {
            "id" : 10,
            "name" : "Frida Heine",
            "lifeExpectancy" : 31,
            "description" : "Cindy's heart failed due to a severe illness.<br/>" +
                "<p>Cindy has 2 young children...</p>",
            "age" : 23,
            "rejectionProbability" : 0.1,
            "doctor" : None,
            "rank" : 10,
            "money" : 1000                 
        }]
    
    active_players = []
    former_patients = []
    day_start_time = None
    start_time_date = Mechanics.day
    
    def __init__(self, initdict):
        '''
        Constructor
        '''
        self.id = initdict.get('id', None)
        self.name = initdict.get('name', "")
        self.lifeExpectancy = initdict.get('lifeExpectancy', 31)
        self.description = initdict.get('description', "")
        self.age = initdict.get('age', 100)
        self.rejectionProbability = initdict.get('rejectionProbability', 0.2)
        self.doctor = initdict.get('doctor', None)
        self.rank = initdict.get('rank', 99)
        self.money = initdict.get('money', 1000)
        self.status = 'sick'
        self.date = 0
        self.cant_move_until = 0
            
    @classmethod
    def choose(cls):
        player = random.choice(cls.raw_players)
        cls.raw_players.remove(player)
        player_obj = cls(player)
        cls.active_players.append(player_obj)
        print("chose " + str(player_obj.id))
        return player_obj

    
    @classmethod
    def getRecipient(cls, provided_id):
        if provided_id is None:
            return None
        provided_id = int(provided_id)
        for player in cls.active_players:
            if player.id == provided_id:
                return player
        for player in cls.former_patients:
            if player.id == provided_id:
                return player
        return None

    
    @classmethod
    def updateRecipient(cls, provided_id, updated):
        player = cls.getRecipient(provided_id)
        for key, value in updated.items():
            setattr(player, key, value)
        return player
    
    def new_day(self):
        if self.status == 'sick':
            self.lifeExpectancy -= 1
            if self.lifeExpectancy == 0:
                self.status = 'dead'
                Recipient.active_players.remove(self)
                Recipient.former_patients.append(self)
        self.date += 1
        
    @classmethod
    def waiting_for_move(cls):
        for player in cls.active_players:
            if player.cant_move_until <= Mechanics.day and player.status == 'sick':
                return True
        return False
        
    def game_state(self):
        if Recipient.day_start_time is None:
            Recipient.day_start_time = time.time()
            
        if Mechanics.day < 0:
            if self.remaining_wait_time() <= 0 or len(Recipient.active_players) > 3:
                Recipient.end_day()
                return self.game_state()
            else:
                return "staging-room"
        elif Mechanics.day < self.cant_move_until:
            # see if we should trigger the day change
            if self.remaining_wait_time() <= 0 or not Recipient.waiting_for_move():
                Recipient.end_day()
                return self.game_state()
            else:
                return "day-wait"
        else:
            return "playing"

    def remaining_wait_time(self):
        if Mechanics.day < 0:
            return 45 - time.time() + Recipient.day_start_time
        else:
            return 30 - time.time() + Recipient.day_start_time
        
    @classmethod
    def end_day(cls):
        Mechanics.new_day()
        for player in Recipient.active_players:
            player.new_day()
        # anyone left?
        if len(Recipient.active_players) == 0:
            return
        # allocate organ
        factor = Mechanics.donor_pool * max(5, len(Recipient.active_players))/30.0
        if (random.random() <= factor):
            # sort recipients by recipientListImpact
            cls.sort_recipients()
            # HACK: tickets over first 5: 10, 6, 4, 2, 1 = 23
            ticket = random.randrange(23)
            if ticket < 10:
                selection = cls.active_players[0]
            elif len(Recipient.active_players) < 2:
                return
            elif ticket < 16:
                selection = cls.active_players[1]
            elif len(Recipient.active_players) < 3:
                return
            elif ticket < 20:
                selection = cls.active_players[2]
            elif len(Recipient.active_players) < 4:
                return
            elif ticket < 22:
                selection = cls.active_players[3]
            elif len(Recipient.active_players) < 5:
                return
            else:
                selection = cls.active_players[4]
            
            Recipient.active_players.remove(selection)
            Recipient.former_patients.append(selection)

            if (random.random() < selection.rejectionProbability):
                selection.status = 'transplant-dead'
            else:
                selection.status = 'transplant-healed'
                
    @classmethod
    def sort_recipients(cls):
        unsorted = cls.active_players
        cls.active_players = []
        for player in unsorted:
            index = 0
            while index < len(cls.active_players) and cls.active_players[index].recipientListImpact > player.recipientListImpact:
                index += 1
            else:
                cls.active_players.insert(index, player)