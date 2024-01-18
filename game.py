import deckmodule
import handmodule
import handplayer

class Game():
    def __init__(self):
        name1 = input("p1 name: ")
        name2 = input("p2 name: ")
        self.deck = deckmodule.Deck()
        self.p1 = handplayer.Player(name1)
        self.p2 = handplayer.Player(name2)
    def draw(self):
        self.p1.hand.cards.append(self.deck.draw())
        self.p2.hand.cards.append(self.deck.draw())
    def round_win(self):
        a = self.p1.hand.cards[0]
        b = self.p2.hand.cards[0]
        print("{} drew a {}!".format(self.p1.name, a))
        print("{} drew a {}!".format(self.p2.name, b))
        if a > b:
            print("{} wins!".format(self.p1.name))
            self.p1.wins += 1
            
        else:
            print("{} wins!".format(self.p2.name))
            self.p2.wins += 1
        self.p1.hand.cards.pop()
        self.p2.hand.cards.pop()
    def winner(self):
        if self.p1.wins > self.p2.wins:
            return "{} wins!".format(self.p1.name)
        elif self.p1.wins < self.p2.wins:
            return "{} wins!".format(self.p2.name)
        else:
            return "It was a tie!"
    def play_game(self):
        print("beginning War!")
        while len(self.deck.cards) >= 2:
            m = "Press q to quit, or any other key to play a round."
            gameplayer = input(m)
            if gameplayer == "q":
                break
            self.draw()
            self.round_win()
        print(self.winner() + " War is over.")

game = Game()
game.play_game()



        
            
                
    

        
    

        
