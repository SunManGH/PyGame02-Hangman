# Set Labels and format

import pygame

# initilize the game
pygame.init()
pygame.font.init()

# Create the screen
screen = pygame.display.set_mode((800,600))

# Set title
pygame.display.set_caption('Hangman')

# Set word to guess
theWord = 'Welcome'

# Formatting text
def format_my_text(myText, fontName: str = 'Century',fontSize: int = 25,fontColor = (19,61,87)):
    f = pygame.font.SysFont(fontName, fontSize)
    fsurf = f.render("{}".format(myText), True, fontColor)
    return fsurf

# Set Labels
Heading_Label = format_my_text('HANGMAN',fontSize=50)
guessTheWord_Label = format_my_text('GUESS THE WORD')
tries_Label = format_my_text('Tries : ')
Word_Label = format_my_text('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')

# Game loop
running = True
while running:

    # Hangman background
    screen.fill((245,180,26))

    # font color
    screen.blit(Heading_Label,(250,200))
    screen.blit(guessTheWord_Label,(560,50))
    screen.blit(tries_Label,(30,50))
    screen.blit(Word_Label,(250,300))

    # Update the screen
    pygame.display.update()

    # Close the game if we QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

