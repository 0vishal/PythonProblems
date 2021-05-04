import itertools,random

def player1():
    for i in range(9):
        carddeck = list(itertools.product(range(1,14),["Spade", "Club", "Diamond", "Heart"]))
        random.shuffle(carddeck)
        player1 = []
        player1.append([carddeck[i][0],carddeck[i][1]]) 
        print("Player1:", player1)

player1()        