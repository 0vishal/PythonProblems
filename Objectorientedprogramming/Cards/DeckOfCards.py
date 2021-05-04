'''
@Author: Vishal Salaskar
@Date: 2021-04-05 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-04-05
@Title : To get 9 cards to 4 players using random 
'''

import random, itertools

class DeckOfCards:

    def __init__(self):
        self.suit = [ "Heart", "Spades", "Diamonds", "Clubs" ]
        self.numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


    def randomShuffle(self,player):
         """
        Description:
        A function to get 9 cards to 4 players using random 
        Parameter:
        player for the number name of player
        """  
        self.player = player
        
        print("You got:")
        for i in range(0,9):
          deck = list(itertools.product(self.numbers,self.suit))
          random.shuffle(deck)
          self.player.append(([deck[i][0], deck[i][1]]))  
        print(self.player)  

            
if __name__=="__main__":
    deck = DeckOfCards()
    player1 = []
    player2 = []
    player3 = []
    player4 = []
    
    deck.randomShuffle(player1)
    deck.randomShuffle(player2)
    deck.randomShuffle(player3)
    deck.randomShuffle(player4)
    