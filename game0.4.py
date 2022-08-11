# Set hangman art and lives

import pygame
import hangman_art

# initilize the game
pygame.init()
pygame.font.init()

# Create the screen
screen = pygame.display.set_mode((800,600))

# Set title
pygame.display.set_caption('Hangman')

# Set a word to guess
theWord = 'Welcome'

# Get length of word
Word_Label = '_ '*len(theWord)

# Set Lives
lives=6

# Set image
hangmanImage = pygame.image.load('LivesLeft_6_br.png')

# Formatting text
def format_my_text(myText, fontName: str = 'Century',fontSize: int = 25,fontColor = (19,61,87)):
    f = pygame.font.SysFont(fontName, fontSize)
    fsurf = f.render("{}".format(myText), True, fontColor)
    return fsurf

# Set Labels
Heading_Label = format_my_text('HANGMAN',fontSize=50)
guessTheWord_Label = format_my_text('GUESS THE WORD')
tries_Label = format_my_text('Tries : ')
Word_Label = format_my_text(Word_Label,fontSize=100)
# always just center the text rectangle when you grab it
Word_Label_rect = Word_Label.get_rect(center=(500,300))


# Game loop
running = True
while running:

    # Hangman background
    screen.fill((245,180,26))

    # font color
    screen.blit(hangmanImage,(0,200))
    screen.blit(Heading_Label,(250,200))
    screen.blit(guessTheWord_Label,(560,50))
    screen.blit(tries_Label,(30,50))
    # always just center the text rectangle when you grab it
    screen.blit(Word_Label,Word_Label_rect)

    # Update the screen
    pygame.display.update()

    # Close the game if we QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
