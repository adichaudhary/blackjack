import random

playerHand = []
playerValue = 0
dealerHand = []
dealerValue = 0
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
discardDeck = []
playerTurn = True
roundCount = 1

deck = []
for suit in suits:
    for rank in ranks:
        deck.append(rank + " of " + suit)

def playerDraw():
    global playerValue

    card = random.choice(deck)
    discardDeck.append(card)
    deck.remove(card)
    playerHand.append(card)
    
    print("Your card: " + card)
    playerValueAssigner(card)
    print("Your deck value:",playerValue)

def dealerDraw():
    global dealerValue
    global dealerCount
    card = random.choice(deck)
    discardDeck.append(card)
    deck.remove(card)
    dealerHand.append(card)
    dealerValueAssigner(card)
        
def playerValueAssigner(card):
    global playerValue
    if "Ace" in card and playerValue <= 10:
        playerValue += 11
    elif "Ace" in card and playerValue > 10:
        playerValue += 1
    elif "Jack" in card or "Queen" in card or "King" in card:
        playerValue += 10
    else:
        playerValue += int(card.split()[0])

def dealerValueAssigner(card):
    global dealerValue
    if "Ace" in card and dealerValue <= 10:
        dealerValue += 11
    elif "Ace" in card and dealerValue > 10:
        dealerValue += 1
    elif "Jack" in card or "Queen" in card or "King" in card:
        dealerValue += 10
    else:
        dealerValue += int(card.split()[0])

def playerBlackjackCheck():
    if playerValue == 21:
        print("Blackjack! You win 3:2!")
        game()

def dealerBlackjackCheck():
    if dealerValue == 21:
        dealerReveal()
        print("Dealer got Blackjack. You lose.")
        game()

def action():
    act = input("Would you like to hit or stand? ")
    if act.lower().strip() == "hit":
        playerDraw()
        if playerValue > 21:
            print("Bust. You lose.")
            game()
        elif playerValue == 21:
            print("You win!")
            game()
        action()
    dealerReveal()
    while dealerValue <= 17:
        print("Dealer hits 17 or lower.")
        dealerDraw()
        dealerReveal()
        winChecker()
    else:
        print("Dealer stands greater than 17.")
        winChecker()

def dealerReveal():
    print("Dealer's card: " + dealerHand[-1])
    print("Dealer's deck value:",dealerValue)

def winChecker():
    if playerValue == 21:
        print("You win!")
        game()
    elif playerValue > 21:
        print("Bust. You lose.")
        game()
    elif dealerValue == 21:
        print("Dealer wins.")
        game()
    elif dealerValue > 21:
        print("Dealer busted! You win!")
        game()
    elif playerValue < 22 and dealerValue > 17 and playerValue > dealerValue:
        print("You win!")
        game()
    elif dealerValue < 22 and playerValue < dealerValue:
        print("Dealer wins.")
        game()
    elif playerValue == dealerValue:
        print("Push. Keep your bet.")
        game()

def game():
    global roundCount
    global discardDeck
    global playerHand
    global playerValue
    global dealerHand
    global dealerValue
    global discardDeck
    global playerTurn
    for card in discardDeck:
        deck.append(card)
    playerHand = []
    playerValue = 0
    dealerHand = []
    dealerValue = 0
    discardDeck = []
    playerTurn = True
    print("\nWelcome to Blackjack. Round", roundCount, "\n")
    roundCount+=1
    playerDraw()
    dealerDraw()
    dealerReveal()
    playerDraw()
    dealerDraw()
    playerBlackjackCheck()
    dealerBlackjackCheck()
    action()
    game()

start = input("Enter E to start.")
if start.lower() == "e":
    game()