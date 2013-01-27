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
        for definition in cls.raw_mechanics:
            cls.operations.append(cls(definition))
            
    
    @classmethod
    def get_mechanic(cls, move_id):
        if len(cls.operations) == 0:
            cls.load_mechanics()
        for mechanic in cls.operations:
            if mechanic.id == move_id:
                return mechanic
            
    @classmethod
    def new_day(cls):
        cls.day += 1
        
    def execute_move(self, player):
        print(str(player.cant_move_until) + " " + str(Mechanics.day))
        if player.cant_move_until <= Mechanics.day and player.money >= self.moneyCost:
            player.cant_move_until += self.timeCost
            player.money -= self.moneyCost
            dice = random.random()
            print(str(dice) + " " + str(self.successRate))
            if dice < self.successRate:
                Mechanics.donor_pool *= self.donorPoolImpact
                player.rank += self.recipientListImpact
                return "success"
            else:
                return "fail"
        else:
            return "fail"
        
    raw_mechanics = [{
                                "id" : 1,
                                "name" : "Get a Check-Up",
                                "description" : "Getting tested might show your condition worsening.",
                                "timeCost" : 1,
                                "moneyCost" : 40,
                                "successRate" : .8,
                                "donorPoolImpact" : 1,
                                "recipientListImpact" : 500
                            },
                                         {
                                "id" : 2,
                                "name" : "Make a Donation",
                                "description" : "Being friendly to the hospital could make the hospital be friendlier to you.",
                                "timeCost" : 1,
                                "moneyCost" : 1000,
                                "successRate" : .6,
                                "donorPoolImpact" : 1.2,
                                "recipientListImpact" : 1000
                            },
                            {
                                "id" : 3,
                                "name" : "Switch Doctors",
                                "description" : "Maybe a different doctor can give you a different assessment on your condition.",
                                "timeCost" : 3,
                                "moneyCost" : 100,
                                "successRate" : .5,
                                "donorPoolImpact" : 1,
                                "recipientListImpact" : 2000
                            },
                            {
                                "id" : 4,
                                "name" : "Get News Coverage",
                                "description" : "Getting public exposure could make people sympathetic to you problem, or even increase the number of donors.",
                                "timeCost" : 4,
                                "moneyCost" : 0,
                                "successRate" : .1,
                                "donorPoolImpact" : 1.3,
                                "recipientListImpact" : 100
                            },
                            {
                                "id" : 5,
                                "name" : "Try Experimental Treatment",
                                "description" : "Science keeps comping up with new treatments. Although risky, you might consider experimental treatment.",
                                "timeCost" : 8,
                                "moneyCost" : 40,
                                "successRate" : 0.1,
                                "donorPoolImpact" : 1.1,
                                "recipientListImpact" : 1000
                            },
                            {
                                "id" : 6,
                                "name" : "Try Homeopathic Medicine",
                                "description" : "Hey, you never know.",
                                "timeCost" : 1,
                                "moneyCost" : 200,
                                "successRate" : 0,
                                "donorPoolImpact" : 1,
                                "recipientListImpact" : 0
                            },
                            {
                                "id" : 7,
                                "name" : "Search for Organs Abroad",
                                "description" : "Maybe countries with different regulations might make it easier...",
                                "timeCost" : 78,
                                "moneyCost" : 0.2,
                                "successRate" : 0,
                                "donorPoolImpact" : 1,
                                "recipientListImpact" : 1000
                            },
                            {
                                "id" : 8,
                                "name" : "Go to the Illegal Market",
                                "description" : "You can try to buy an organ in the black market, but the risk is pretty high.",
                                "timeCost" : 78,
                                "moneyCost" : 0.2,
                                "successRate" : 0,
                                "donorPoolImpact" : 1,
                                "recipientListImpact" : 1000
                            },
                            {
                                "id" : 9,
                                "name" : "Organize an Organ Drive",
                                "description" : "If you can encourage friends and family to register as organ donors, it will increase the likelihood that organs will be available to patients on the list.",
                                "timeCost" : 6,
                                "moneyCost" : 100,
                                "successRate" : 0.7,
                                "donorPoolImpact" : 1.3,
                                "recipientListImpact" : 100
                            }]
