#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 10:56:38 2023

@author: mayurikaul
"""

import random

# Making a deck of cards

# Making a class

class Card(object) :
    def __init__(self,name,value,suit,symbol):   #Setting up the basic values in the class
        self.value = value
        self.suit = suit
        self.name = name
        self.symbol = symbol
        self.showing = False
    def __repr__(self): #how the object is represented
        if self.showing: 
            return self.symbol
        else:
            return "Card"


class Deck (object):
    def shuffle(self, times = 1):
        random.shuffle(self.cards)
        print("Deck shuffled")
        
    def deal(self):
        return self.cards.pop(0)
    
         

class StandardDeck (Deck):    
    def __init__(self):
        self.cards = []   # the class is aware of the cards variable
        suits = {"Hearts":"♡", "Spades":"♠", "Diamonds":"♢", "Clubs":"♣"}
        values = {"Two" : 2,
                  "Three":3,
                  "Four": 4,
                  "Five": 5,
                  "Six":6,
                  "Seven":7,
                  "Eight":8,
                  "Nine":9,
                  "Ten":10,
                  "Jack":11,
                  "Queen":12,
                  "King":13,
                  "Ace":14} #NOTE that ace can be used as 1 in straight
        
        for name in values:
            for suit in suits: 
                symbolIcon = suits[suit] 
                if values[name] < 11: 
                    symbol = str(values[name])+symbolIcon 
                else: 
                    symbol = name[0]+symbolIcon 
                
                self.cards.append( Card(name, values[name], suit, symbol) )

    def __repr__(self):
        return "Standard deck of cards: {0} remaining".format(len(self.cards))
    


class Player(object):
    def __init__(self):
        self.cards = []
    
    def cardCount(self):
        return len(self.cards)
    
    def addCard(self,card):
        self.cards.append(card)
        
    

class PokerScorer(object):
    def __init__(self, cards):
      
      #if not len(cards) == 5:
          #return "Error: Wrong number of cards"
      
      self.cards = cards

            
    
    def flush(self):
        suits = [card.suit for card in self.cards]
        if len (set (suits)) == 1: #turning into a set, as set cant have duplicates, then turning into a list
            return True
        else:
            return False
        
    
    def straight(self):
        values = [card.value for card in self.cards]
        values.sort()
        
        if not len(set(values)) == 5:
            return False
        
        if values[4] == 14 and values[3] == 5 and values[2] == 4 and values[1] == 3 and values[0] == 2:
            return 5 
        
        else:
            if not values[0] + 1 == values[1]: return False
            if not values[1] + 1 == values[2]: return False
            if not values[2] + 1 == values[3]: return False
            if not values[3] + 1 == values[4]: return False
                       
                
        return values[4]
    
    
    def highCard(self):
        values = [card.value for card in self.cards]
        highCard = None
        for card in self.cards:
            if highCard is None:
                highCard = card
            elif highCard.value < card.value:
                    highCard = card
        
        return highCard
    
    
    def highestCount(self):
        count = 0
        values = [card.value for card in self.cards]
        for value in values:
            if values.count(value) > count:
                count = values.count(value)
        
        return count
        
    
    
    def fourKind(self):
        values = [card.value for card in self.cards]
        for value in values:
            if values.count(value) == 4:
                return True
            
    def fullHouse(self):
        two = False
        three = False
        values = [card.value for card in self.cards]
        for value in values:
            if values.count(value) == 2:
                two  = True
            elif values.count(value) == 3:
                three = True
            
            if two and three:
                return True
                
            
    def Pairs(self):
        pairs = []
        values = [card.value for card in self.cards]
        for value in values:
            if values.count(value) == 2 and value not in pairs:
                pairs.append(value)
        
        return pairs
        
    
    
    #def pairs(self):
        #values = [card.value for card in self.cards]
        #if len(set(values)) == 5:
        #    return 0
        #else
  
        

def interpreterVideoPoker():
    
    player = Player()
    #Initial amount
    points = 100
    #cost per hand
    #handCost = 5
    
    
    #discard = []
    deck = StandardDeck()
    deck.shuffle()
    
    for i in range(5):
        player.addCard(deck.deal())
        
    
    for card in player.cards:
        card.showing = True

    
    print(player.cards)
    
    
    #Scorer
    
    score = PokerScorer(player.cards)
    straight = score.straight()
    flush = score.flush()
    highCount= score.highestCount()
    pairs = score.Pairs()
    
    #Royal Flush
    
    if straight and flush and straight == 14:
        print ("Royal Flush!")
        print("+2000")
        points += 2000
    
   
    #Straight Flush
    
    elif straight and flush:
        print ("Straight Flush!")
        print("+1000")
        points += 1000
        
    
    #Four of a Kind
    
    elif score.fourKind():
       print ("Four of a Kind!")
       print("+500")
       points += 500 
    
    
    #Full House
    
    elif score.fullHouse():
       print ("Full House!")
       print("+250")
       points += 250 
    
    #Flush
    
    elif flush:
        print("Flush!")
        print("+125")
        points += 125
        
        
    #Straight
    
    elif straight:
        print("Straight!")
        print("+75")
        points += 75
    
    
    
    #Three of a kind
    
    elif highCount == 3:
        print("Three of a Kind!")
        print("+50")
        points += 50
    
    #Two pair
    
    elif len(pairs) == 2:
        print("Two Pair!")
        print("+25")
        points += 25
        
    
    #Pair
    
    elif len(pairs) == 1:
        print("Pair!")
        print("+15")
        points += 15
    
    #High card
    
    elif score.highCard():
       print ("High Card!")
       print("+5")
       points += 5 
    
        
 
        
 # Notes: comparing straight flushes, four of a kinds etc (ace four of a kind better than 2 four of a kind)
 # How to improve/change
 # 1)  Add a dealer, flop, turn, river 
 # Deal out 2 cards instead of 5
 # Deal out 3 cards to dealer see what you've got
 # Deal out 1 more card to dealer, see what you've got (need to incorpate the fact that a hand is 5 cards)
 # Deal out 1 more card to dealer
 # Then take the 5 cards which give us the best hand
 # Then we can use the above to see what we have 
 
 # 2)  Multiplayer - in which case we need to compare hands and have a winner
 
 # 3) Add betting, folding 
    
interpreterVideoPoker() 
        
        
deck = StandardDeck()
deck 

deck.shuffle()


cody = Player()

cody.cards.append(deck.deal())

cody.cards


cody.cards[0].showing = True
cody.cards[1].showing = True
cody.cards[2].showing = True
cody.cards[3].showing = True
cody.cards[4].showing = True


cody.cards

cody.cards[0] = deck.deal()
cody.cards[0].showing = True
cody.cards

score = PokerScorer(cody.cards)
score
score.straight()
score.flush()
score.highCard()

randomcard = deck.deal()
randomcard
randomcard.showing = True
randomcard 







