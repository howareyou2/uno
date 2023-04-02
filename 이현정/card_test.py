import pygame
import random

# Initialize Pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("UNO Card Game")

# Set up the card images
CARD_WIDTH = 100
CARD_HEIGHT = 140
CARD_SPACING = 10
CARD_FONT = pygame.font.SysFont("Arial", 30)

card_images = {}
for color in ["red", "green", "blue", "yellow"]:
    for value in range(0, 10):
        card_images[f"{color}_{value}"] = pygame.image.load(f"small_cards/{color}_{value}.png")
    card_images[f"{color}_skip"] = pygame.image.load(f"small_cards/{color}_skip.png")
    card_images[f"{color}_reverse"] = pygame.image.load(f"small_cards/{color}_reverse.png")
    card_images[f"{color}_draw2"] = pygame.image.load(f"small_cards/{color}_draw2.png")
card_images["wild"] = pygame.image.load("small_cards/wild.png")
card_images["wild_draw4"] = pygame.image.load("small_cards/wild_draw4.png")

# Set up the deck of cards
deck = []
for color in ["red", "green", "blue", "yellow"]:
    for value in range(0, 10):
        deck.append(f"{color}_{value}")
        if value != 0:
            deck.append(f"{color}_{value}")
    deck.append(f"{color}_skip")
    deck.append(f"{color}_skip")
    deck.append(f"{color}_reverse")
    deck.append(f"{color}_reverse")
    deck.append(f"{color}_draw2")
    deck.append(f"{color}_draw2")
random.shuffle(deck)
draw_pile = deck[:]

# Set up the players
NUM_PLAYERS = 2
player_hands = [[] for i in range(NUM_PLAYERS)]
for i in range(NUM_PLAYERS):
    for j in range(7):
        player_hands[i].append(draw_pile.pop())

# Set up the discard pile
discard_pile = [draw_pile.pop()]

# Set up the game variables
current_player = 0
current_color = None
reverse_direction = False
draw_count = 0
game_over = False

# Helper function to draw a card
def draw_card(x, y, card, face_up=True):
    if face_up:
        screen.blit(card_images[card], (x, y))
    else:
        pygame.draw.rect(screen, WHITE, (x, y, CARD_WIDTH, CARD_HEIGHT))
        pygame.draw.rect(screen, BLACK, (x, y, CARD_WIDTH, CARD_HEIGHT), 2)
        text = CARD_FONT.render("UNO", True, BLACK)
        screen.blit(text, (x + 10, y + 10))

# Game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if draw_count == 0:
                if len(draw_pile) == 0:
                    draw_pile = discard_pile[:-1]
                   
