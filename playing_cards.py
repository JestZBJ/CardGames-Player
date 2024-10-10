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

    dealer = Player([])
    user = Player([])
    players = [user, dealer]

    for i in range(2):
        for j in players:
            deal(j, deck)
    
    userHandValue = 0
    dealerHandValue = 0
    userAce = False
    dealerAce = False
    
    for a in user.hand:
        if (a[0] == "2"):
            userHandValue += 2
        if (a[0] == "3"):
            userHandValue += 3
        if (a[0] == "4"):
            userHandValue += 4
        if (a[0] == "5"):
            userHandValue += 5
        if (a[0] == "6"):
            userHandValue += 6
        if (a[0] == "7"):
            userHandValue += 7
        if (a[0] == "8"):
            userHandValue += 8
        if (a[0] == "9"):
            userHandValue += 9
        if (a[0] == "1" or a[0] == "J" or a[0] == "Q" or a[0] == "K"):
            userHandValue += 10
        if (a[0] == "A"):
            userHandValue += 11
            userAce = True
        
        if (userHandValue > 21 and userAce == True):
            userHandValue -= 10
    
    for b in dealer.hand:
        if (b[0] == "2"):
            dealerHandValue += 2
        if (b[0] == "3"):
            dealerHandValue += 3
        if (b[0] == "4"):
            dealerHandValue += 4
        if (b[0] == "5"):
            dealerHandValue += 5
        if (b[0] == "6"):
            dealerHandValue += 6
        if (b[0] == "7"):
            dealerHandValue += 7
        if (b[0] == "8"):
            dealerHandValue += 8
        if (b[0] == "9"):
            dealerHandValue += 9
        if (b[0] == "1" or b[0] == "J" or b[0] == "Q" or b[0] == "K"):
            dealerHandValue += 10
        if (b[0] == "A"):
            dealerHandValue += 11
            dealerAce = True
        
        if (dealerHandValue > 21 and dealerAce == True):
            dealerHandValue -= 10

    print("Dealer's upcard: " + dealer.hand[0])

    if (dealer.hand[0][0] == "A"):
        if (dealer.hand[1][0] == "1" or dealer.hand[1][0] == "J" or dealer.hand[1][0] == "Q" or dealer.hand[1][0] == "K"):
            print("Dealer checks hole card:", dealer.hand[1])
            print("House wins")
            sys.exit()
        else:
            print("Dealer checks hole card: Round still in play\n")
    elif (dealer.hand[0][0] == "1" or dealer.hand[0][0] == "J" or dealer.hand[0][0] == "Q" or dealer.hand[0][0] == "K"):
        if (dealer.hand[1][0] == "A"):
            print("Dealer checks hole card:", dealer.hand[1])
            print("House wins")
            sys.exit()
        else:
            print("Dealer checks hole card: Round still in play\n")
    else:
        print()

    print("Your hand:", user.hand)
    print("Hand value:", userHandValue)
    print("Hit or Stand?")
    ans = input()

    while (ans.lower() != "stand"):
        deal(user, deck)       #why wont this work!!!!!#nvrmnd peter fixed it, just had to add the input

        dealtCard = user.hand[-1]
        if (dealtCard[0] == "2"):
            userHandValue += 2
        if (dealtCard[0] == "3"):
            userHandValue += 3
        if (dealtCard[0] == "4"):
            userHandValue += 4
        if (dealtCard[0] == "5"):
            userHandValue += 5
        if (dealtCard[0] == "6"):
            userHandValue += 6
        if (dealtCard[0] == "7"):
            userHandValue += 7
        if (dealtCard[0] == "8"):
            userHandValue += 8
        if (dealtCard[0] == "9"):
            userHandValue += 9
        if (dealtCard[0] == "1" or dealtCard[0] == "J" or dealtCard[0] == "Q" or dealtCard[0] == "K"):
            userHandValue += 10
        if (dealtCard[0] == "A"):
            userHandValue += 11
            userAce = True
        
        if (userHandValue > 21 and userAce == True):
            userHandValue -= 10
            userAce = False
        
        print("\nDealt:", dealtCard)
        print("Your hand:", user.hand)
        print("Hand value:", userHandValue)

        if (userHandValue > 21):
            print("Bust\nHouse wins")
            sys.exit()

        print("Hit or Stand?")
        ans = input()
    
    print("\nDealer's turn -\n")
    print("Dealer's hand:", dealer.hand)
    print("Hand value:", dealerHandValue)

    while ((dealerAce == False and dealerHandValue < 17 and dealerHandValue < userHandValue) or (dealerAce == True and dealerHandValue < userHandValue)):
        print("Dealer Hits")
        time.sleep(2)
        deal(dealer, deck)

        dealtCard = dealer.hand[-1]
        if (dealtCard[0] == "2"):
            dealerHandValue += 2
        if (dealtCard[0] == "3"):
            dealerHandValue += 3
        if (dealtCard[0] == "4"):
            dealerHandValue += 4
        if (dealtCard[0] == "5"):
            dealerHandValue += 5
        if (dealtCard[0] == "6"):
            dealerHandValue += 6
        if (dealtCard[0] == "7"):
            dealerHandValue += 7
        if (dealtCard[0] == "8"):
            dealerHandValue += 8
        if (dealtCard[0] == "9"):
            dealerHandValue += 9
        if (dealtCard[0] == "1" or dealtCard[0] == "J" or dealtCard[0] == "Q" or dealtCard[0] == "K"):
            dealerHandValue += 10
        if (dealtCard[0] == "A"):
            dealerHandValue += 11
            dealerAce = True
        
        if (dealerHandValue > 21 and dealerAce == True):
            dealerHandValue -= 10
            dealerAce = False
        
        print("\nDealt:", dealtCard)
        print("Dealer's hand:", dealer.hand)
        print("Hand value:", dealerHandValue)

        if (dealerHandValue > 21):
            print("Bust\nYou win")
            sys.exit()
    
    print("Dealer Stands\n")
    time.sleep(2)
    
    if (userHandValue > dealerHandValue):
        print("Results - You win")
    if (userHandValue < dealerHandValue):
        print("Results - Dealer wins")
    if (userHandValue == dealerHandValue):
        print("Results - Pushback")

print("Usually, I would ask what you want to play, but right now there's only one option.  Blackjack.")
print("It's also still in testing, soooo...  Anyways, here you go.\n")

play_blackjack()
