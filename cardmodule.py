class Card():
    suits = ("spades", "hearts", "diamonds", "clubs")
    values = ("two", "three", "four", "five", "six", "seven", "eight",
                  "nine", "ten", "Jack", "Queen", "King", "Ace")
    def __init__(self, v, s):
        self.value = self.values[v-2]
        self.suit = self.suits[s]
    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)
    def __lt__(self, c2):
        if self.values.index(self.value) < self.values.index(c2.value):
            return True
        elif self.values.index(self.value) == self.values.index(c2.value):
            if self.suits.index(self.suit) < self.suits.index(c2.suit):
                return True
            else:
                return False
        else:
            return False
    def __gt__(self, c2):
        if self.values.index(self.value) > self.values.index(c2.value):
            return True
        elif self.values.index(self.value) == self.values.index(c2.value):
            if self.suits.index(self.suit) > self.suits.index(c2.suit):
                return True
            else:
                return False
        else:
            return False


                
                   
