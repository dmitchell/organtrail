'''
Created on Jan 26, 2013

@author: dmitchell
'''
import os
import json
import random

class Mechanics(object):
    '''
    classdocs
    '''
    operations = []
    donor_pool = 0.2
    day = -1  # not yet ready for day 1

    def __init__(self, params):
        '''
        Constructor
        '''
        for key, value in params.items():
            setattr(self, key, value)

    @classmethod
    def load_mechanics(cls):
        f = open(os.path.join(settings.PROJECT_DIR, "static/mechanics.json"))
        for definition in json.load(f):
            cls.operations.append(cls(definition))
            
    
    @classmethod
    def get_mechanic(cls, move_id):
        if len(cls.operations) == 0:
            cls.load_mechanics()
        for mechanic in cls.operations:
            if mechanic.id == move_id:
                return mechanic
            
    def execute_move(self, player):
        if player.cant_move_until <= Mechanics.day and player.money >= self.moneyCost:
            player.cant_move_until += self.timeCost
            player.money -= self.moneyCost
            if random.random() < self.successRate:
                Mechanics.donor_pool *= self.donorPoolImpact
                player.rank += self.recipientListImpact
                return "success"
            else:
                return "fail"
        else:
            return "fail"