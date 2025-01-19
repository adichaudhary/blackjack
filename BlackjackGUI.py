#Pygame Init
import pygame, sys, random
from pygame.locals import *

pygame.init()

#Pygame Constants
FPS = 15
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 100, 0)
PLAYER_X = 100
PLAYER_Y = 250

#Display Init
DISPLAY = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAY.fill(GREEN)
pygame.display.set_caption("Blackjack")

#Game Variables
playerHand = []
playerValue = 0
dealerHand = []
dealerValue = 0
suits = ["hearts", "diamonds", "clubs", "spades"]
ranks = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
discardDeck = []
playerTurn = True
roundCount = 1
deck = []
for suit in suits:
    for rank in ranks:
        deck.append(f"{rank}_of_{suit}.png")

class Card:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = None
        self.rect = None
        self.load_card()
        self.fullName = None
        self.printName = None

    def load_card(self):
        self.fullName = random.choice(deck)
        self.printName = self.fullName.split("_")[0].capitalize() + " " + self.fullName.split("_")[1] + " " + self.fullName.split("_")[2].split(".")[0].capitalize()
        random_image = pygame.image.load(rf"c:\Users\kumar\Desktop\Adi\CodingProjects\Python\blackjack\cards\{self.fullName}").convert_alpha()
        self.image = pygame.transform.scale(random_image, (100, 150))
        self.rect = self.image.get_rect()

    def draw(self, surface, x, y):
        self.rect.topleft = (x, y)
        surface.blit(self.image, self.rect)

def playerDraw(x, y):
    global playerValue
    card = Card()
    card.load_card()
    card.draw(DISPLAY, x, y)
    discardDeck.append(card.fullName)
    deck.remove(card.fullName)
    name = card.printName
    print("Your card: " + name)
    if "Ace" in name and playerValue <= 10:
        playerValue += 11
    elif "Ace" in name and playerValue > 10:
        playerValue += 1
    elif "Jack" in name or "Queen" in name or "King" in name:
        playerValue += 10
    else:
        playerValue += int(name.split()[0])
    print("Your deck value:",playerValue)

def dealerDraw(x, y):
    global dealerValue
    global dealerHand
    card = Card()
    card.load_card()
    card.draw(DISPLAY, x, y)
    discardDeck.append(card.fullName)
    dealerHand.append(card.printName)
    deck.remove(card.fullName)
    name = card.printName
    if "Ace" in name and dealerValue <= 10:
        dealerValue += 11
    elif "Ace" in name and dealerValue > 10:
        dealerValue += 1
    elif "Jack" in name or "Queen" in name or "King" in name:
        dealerValue += 10
    else:
        dealerValue += int(name.split()[0])

def dealerReveal():
    print("Dealer's card: " + dealerHand[-1])
    print("Dealer's deck value:",dealerValue)


# def dealerDraw():
#     global dealerValue
#     global dealerCount
#     card = random.choice(deck)
#     discardDeck.append(card)
#     deck.remove(card)
#     dealerHand.append(card)
#     dealerValueAssigner(card)
        


# def dealerValueAssigner(card):
#     global dealerValue
#     if "Ace" in card and dealerValue <= 10:
#         dealerValue += 11
#     elif "Ace" in card and dealerValue > 10:
#         dealerValue += 1
#     elif "Jack" in card or "Queen" in card or "King" in card:
#         dealerValue += 10
#     else:
#         dealerValue += int(card.split()[0])

playerDraw(350, 400)
dealerDraw(0, 0)
dealerReveal()
playerDraw(450, 400)

while True:     
    #Ensures Quit Functionality
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Drawing Execution
    pygame.display.flip()