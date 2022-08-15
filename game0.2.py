# Guess the world and set an alert if letter was already tried

import random
from time import sleep
import pygame

# initilize the game
pygame.init()
pygame.font.init()

# Create the screen
screen = pygame.display.set_mode((800,600))

# Set title
pygame.display.set_caption('Hangman')

# Set a word to guess
# https://www.thegamegal.com/word-generator/
word_list = [
'preach',
'encourage',
'cook',
'regret',
'sit',
'dive',
'wish',
'fall',
'maintain',
'haunt',
]
theWord = random.choice(word_list)
print(theWord)

# theWord = 'W e l c o m e'

# Set Lives
lives=2


# Letters guessed
guessed = []

# Formatting text
def format_my_text(myText, fontName: str = 'Century',fontSize: int = 25,fontColor = (19,61,87)):
    f = pygame.font.SysFont(fontName, fontSize)
    fsurf = f.render("{}".format(myText), True, fontColor)
    return fsurf

# Keyboard text
tried = False
wrongLetter = False
imageNo = 1
display_word = ""

# Set Labels
Heading_Label = format_my_text('HANGMAN',fontSize=50)
GameOver = format_my_text('Game Over',fontSize=50)
guessTheWord_Label = format_my_text('GUESS THE WORD')
tries_Label = format_my_text(f'Tries : {lives}')
triedAlready = format_my_text(f'You have alreay tried. Please choose another letter',fontColor='white')
enteredWrongLetter = format_my_text(f'Incorrect letter. Please any other letter',fontColor='red')

# Draw The Word
def DrawTheWord():
    global lives
    global display_word
    if lives > 0:
        for letter in theWord:
            if letter in guessed:
                display_word += letter+' '
            else:
                display_word += '_ '
            
    Word_Label = format_my_text(display_word,fontSize=100)
    screen.blit(Word_Label,(200,300))

# display Name,Tries, Title
def DrawStartScreen():
    global lives
    if lives > 0:
        global tried
        global wrongLetter
        global imageNo
        
        # Set image 
        hangmanImage = pygame.image.load(f'Images\hangman0{imageNo}.png')
        screen.blit(hangmanImage,(0,200))

        screen.blit(Heading_Label,(250,200))
        screen.blit(guessTheWord_Label,(560,50))
        screen.blit(format_my_text(f'Tries : {lives}'),(30,50))

        if tried is True:
            DrawTheWord()
            screen.blit(triedAlready,(100,100))
            # Update the screen
            pygame.display.update()
            sleep(1)

        if wrongLetter is True and lives > 0:
            lives -= 1
            imageNo += 1
            DrawTheWord()
            screen.blit(enteredWrongLetter,(100,100))
            # Update the screen
            pygame.display.update()
            sleep(1)

        tried = False
        wrongLetter = False

# Game loop
running = True
while running:
    # Hangman background
    screen.fill((245,180,26))

    DrawStartScreen()
    DrawTheWord()
    # Close the game if we QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print(text)
                text = ''
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text = event.unicode
                if text in theWord:
                    if text in guessed:
                        tried = True
                    else:
                        guessed.append(text)
                        tried = False
                else:
                    wrongLetter = True

    if lives == 0:
        screen.fill((245,180,26))
        screen.blit(GameOver,(250,200))
        pygame.display.update()
    else:
        # Update the screen
        pygame.display.update()
