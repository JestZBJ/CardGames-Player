# create a Computer object that can have it's own hand and go through a series of ifs to decide what to do
# deal - deals one card
# deal_blackjack_hand - deals a hand for blackjack alternating from User to Comp

import random
import sys
import time
from dataclasses import dataclass

@dataclass
class Player:
    def __init__(self, hand):
        self.hand = hand

def new_standard_deck():
    deck = []
    suits = ["C", "H", "S", "D"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    for i in range(len(suits)):
        for j in range(len(values)):
            card = values[j] + suits[i]
            deck.append(card)
    
    return deck

    '''for i in range(4):
        for j in range(13):
            if len(deck) <= 12:
                c = str(j + 1) + "C"
                deck.append(c)
            elif len(deck) <= 25 and len(deck) > 12:
                h = str(j + 1) + "H"
                deck.append(h)
            elif len(deck) <= 38 and len(deck) > 25:
                s = str(j + 1) + "S"
                deck.append(s)
            elif len(deck) <= 52 and len(deck) > 38:
                d = str(j + 1) + "D"
                deck.append(d)'''

def new_uno_deck():
    deck = []
    suits = ["R", "G", "B", "Y"]
    values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "+2", "SKIP", "REV."]

    for i in range(len(suits)):
        card = suits[i] + "0"
        deck.append(card)
        for j in range(len(values)):
            for x in range(2):
                card = suits[i] + values[j]
                deck.append(card)
    
    for a in range(4):
        deck.append("WILD")
    
    for b in range(4):
        deck.append("+4")

    return deck

def new_custom_deck():
    deck = []

    # ask for suit and value input

    '''for i in range(len(suits)):
        for j in range(len(values)):
            card = suits[i] + values[j]
            deck.append(card)'''

def deal(players, deck):
    players.hand.append(deck[0])
    deck.pop(0)

def play_blackjack():
    deck = new_standard_deck()
    random.shuffle(deck)

    print("How many players?  Please note that the standard 52 card deck can run out of cards and crash the game.")
    numPlayers = int(input())
    players = []

    for p in range(numPlayers):
        user = Player([])
        players.append(user)

    dealer = Player([])
    players.append(dealer)

    for i in range(2):
        for j in players:
            deal(j, deck)
    
    ace = []
    aceIndex = 0
    for q in players:
        ace.append(False)

        for a in q.hand:
            if (a[0] == "2"):
                q.handValue += 2
            if (a[0] == "3"):
                q.handValue += 3
            if (a[0] == "4"):
                q.handValue += 4
            if (a[0] == "5"):
                q.handValue += 5
            if (a[0] == "6"):
                q.handValue += 6
            if (a[0] == "7"):
                q.handValue += 7
            if (a[0] == "8"):
                q.handValue += 8
            if (a[0] == "9"):
                q.handValue += 9
            if (a[0] == "1" or a[0] == "J" or a[0] == "Q" or a[0] == "K"):
                q.handValue += 10
            if (a[0] == "A"):
                q.handValue += 11
                ace[aceIndex] = True
            
            if (q.handValue > 21 and ace[aceIndex] == True):
                q.handValue -= 10
        
        aceIndex = aceIndex + 1

    print("\n\nDealer's upcard: " + players[-1].hand[0])

    if (players[-1].hand[0][0] == "A"):
        if (players[-1].hand[1][0] == "1" or players[-1].hand[1][0] == "J" or players[-1].hand[1][0] == "Q" or players[-1].hand[1][0] == "K"):
            print("Dealer checks hole card:", players[-1].hand[1])
            print("House wins")
            sys.exit()
        else:
            print("Dealer checks hole card: Round still in play\n")
    elif (players[-1].hand[0][0] == "1" or players[-1].hand[0][0] == "J" or players[-1].hand[0][0] == "Q" or players[-1].hand[0][0] == "K"):
        if (players[-1].hand[1][0] == "A"):
            print("Dealer checks hole card:", players[-1].hand[1])
            print("House wins")
            sys.exit()
        else:
            print("Dealer checks hole card: Round still in play\n")
    else:
        print()

    for h in range(len(players) - 1):
        print("\nPlayer ", h + 1 , "hand:", players[h].hand)
        print("Hand value:", players[h].handValue)
    
    aceIndex = 0

    for t in range(len(players) - 1):
        print("\n\nPlayer", t + 1, "turn -\n")
        print("Your hand:", players[t].hand)
        print("Hand value:", players[t].handValue)
        print("Hit or Stand?")
        ans = input()

        while (ans.lower() != "stand"):
            deal(players[t], deck)       #why wont this work!!!!!#nvrmnd peter fixed it, just had to add the input

            dealtCard = players[t].hand[-1]
            if (dealtCard[0] == "2"):
                players[t].handValue += 2
            if (dealtCard[0] == "3"):
                players[t].handValue += 3
            if (dealtCard[0] == "4"):
                players[t].handValue += 4
            if (dealtCard[0] == "5"):
                players[t].handValue += 5
            if (dealtCard[0] == "6"):
                players[t].handValue += 6
            if (dealtCard[0] == "7"):
                players[t].handValue += 7
            if (dealtCard[0] == "8"):
                players[t].handValue += 8
            if (dealtCard[0] == "9"):
                players[t].handValue += 9
            if (dealtCard[0] == "1" or dealtCard[0] == "J" or dealtCard[0] == "Q" or dealtCard[0] == "K"):
                players[t].handValue += 10
            if (dealtCard[0] == "A"):
                players[t].handValue += 11
                ace[aceIndex] = True
            
            if (players[t].handValue > 21 and ace[aceIndex] == True):
                players[t].handValue -= 10
                ace[aceIndex] = False
            
            print("\nDealt:", dealtCard)
            print("Your hand:", players[t].hand)
            print("Hand value:", players[t].handValue)

            if (players[t].handValue > 21):
                print("Bust")
                break

            print("Hit or Stand?")
            ans = input()
        
        aceIndex = aceIndex + 1
    
    print("\nDealer's turn -\n")
    print("Dealer's hand:", players[-1].hand)
    print("Hand value:", players[-1].handValue)

    allBust = True
    highestHand = 0
    
    for g in range(len(players) - 1):
        if (players[g].handValue > 21):
            continue
        if (players[g].handValue <22):
            allBust = False
        if (players[g].handValue > highestHand):
            highestHand = players[g].handValue

    #did all bust; who's the hightest not bust
    while (players[-1].handValue < highestHand and not allBust and ((ace[-1] == False and players[-1].handValue < 17) or (ace[-1] == True))):
        print("Dealer Hits")
        time.sleep(2)
        deal(players[-1], deck)

        dealtCard = players[-1].hand[-1]
        if (dealtCard[0] == "2"):
            players[-1].handValue += 2
        if (dealtCard[0] == "3"):
            players[-1].handValue += 3
        if (dealtCard[0] == "4"):
            players[-1].handValue += 4
        if (dealtCard[0] == "5"):
            players[-1].handValue += 5
        if (dealtCard[0] == "6"):
            players[-1].handValue += 6
        if (dealtCard[0] == "7"):
            players[-1].handValue += 7
        if (dealtCard[0] == "8"):
            players[-1].handValue += 8
        if (dealtCard[0] == "9"):
            players[-1].handValue += 9
        if (dealtCard[0] == "1" or dealtCard[0] == "J" or dealtCard[0] == "Q" or dealtCard[0] == "K"):
            players[-1].handValue += 10
        if (dealtCard[0] == "A"):
            players[-1].handValue += 11
            ace[-1] = True
        
        if (players[-1].handValue > 21 and ace[-1] == True):
            players[-1].handValue -= 10
            ace[-1] = False
        
        print("\nDealt:", dealtCard)
        print("Dealer's hand:", players[-1].hand)
        print("Hand value:", players[-1].handValue)

        if (players[-1].handValue > 21):
            print("Bust")
            break
    
    if (players[-1].handValue < 22):
        print("Dealer Stands\n")
        time.sleep(2)
    
    for t in range(len(players) - 1):
        print("\nPlayer", t + 1, "Results: ")

        if ((players[t].handValue > players[-1].handValue or players[-1].handValue > 21) and players[t].handValue < 22):
            print(" - You win")
        if ((players[t].handValue < players[-1].handValue and players[-1].handValue < 22) or players[t].handValue > 21):
            print(" - Dealer wins")
        if (players[t].handValue == players[-1].handValue and players[t].handValue < 22):
            print(" - Pushback")

def play_crazy_eights():
    pass

print("Usually, I would ask what you want to play, but right now there's only one option.  Blackjack.")
print("It's also still in testing, soooo...  Anyways, here you go.\n")

play_blackjack()
