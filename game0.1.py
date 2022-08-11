# Create PyGame screen and set title

import pygame

# initilize the game
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800,600))

# Set title
pygame.display.set_caption('Hangman')

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
