import cardmodule
from random import shuffle

class Deck():
    def __init__(self):
        self.cards = []
        for i in range(0, 13):
            for x in range(4):
                self.cards.append(cardmodule.Card(i + 2, x))
        shuffle(self.cards)
    def draw(self):
        a = self.cards[0]
        for i in range(len(self.cards) - 1):
            self.cards[i] = self.cards[i+1]
        self.cards.pop()
        return a

    
    
