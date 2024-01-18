import deckmodule
import cardmodule

class Hand():
    def __init__(self, o):
        self.cards = []
        self.owner = o

class Player():
    def __init__(self, name):
        self.wins = 0
        self.name = name
        self.hand = Hand(name)
    def show_hand(self):
        return (self.hand.cards)


        
    
