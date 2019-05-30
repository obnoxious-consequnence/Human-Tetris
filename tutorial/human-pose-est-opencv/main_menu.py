import pygame
import time
import random
import numpy as np
import cv2

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0, 200, 0)
blue = (0,0,200)
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue = (0,0,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Human Tetris')
clock = pygame.time.Clock()

stickfigImg = pygame.image.load('backgroundmain.png')
posesImg = pygame.image.load('poses.png')
camera = cv2.VideoCapture(0)
recording = False

def stickFig(x,y):
    gameDisplay.blit(stickfigImg, (x,y))

def poses(x,y):
    gameDisplay.blit(posesImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    

    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "play":
                start_game()
            elif action == "score":
                print("Scoreboard clicked!")
            elif action == "quit":
                pygame.quit()
                quit()
            elif action == "go":
                cap_screen()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 15)
    textSurfStart, textRectStart = text_objects(msg, smallText)
    textRectStart.center = ((x+(w/2)), (y+(50/2)))
    gameDisplay.blit(textSurfStart, textRectStart)
    

def cap_screen():
    seconds = 3
    millis = seconds * 1000
    recording = True
    while recording and (millis > 0):
        gameDisplay.fill(white)
        ret, frame = camera.read()
        millis = millis - 10
        frame2 = cv2.cvtColor(np.rot90(frame), cv2.COLOR_BGR2RGB)
        frame2 = pygame.surfarray.make_surface(frame2)
        gameDisplay.blit(frame2, (0,0))
        pygame.display.update()
    img_name = "example.jpg"
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))
    

def game_menu():
    x = 100
    y = 0
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
               
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_objects("Human Tetris: Main Menu", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("Start Game",150, 450, 100, 50,green,bright_green, "play")
        button("Scoreboard",350, 450, 100, 50,blue,bright_blue, "score")
        button("Exit Game",550, 450, 100, 50,red,bright_red, "quit")
        stickFig(x,y)  
        
        pygame.display.update()
        clock.tick(15)
        
def start_game():

    x = 100
    y = 300
    
    gameExit = False
 
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        headerText = pygame.font.Font('freesansbold.ttf',35)
        TextSurf, TextRect = text_objects("Objective: ", headerText)
        TextRect.center = ((display_width/2),(50))
        gameDisplay.blit(TextSurf, TextRect)
        subText = pygame.font.Font('freesansbold.ttf',20)
        TextSurf, TextRect2 = text_objects("Try to pose best possible way according to", subText)
        TextRect2.center = ((display_width/2),(150))
        gameDisplay.blit(TextSurf, TextRect2)
        subText2 = pygame.font.Font('freesansbold.ttf',20)
        TextSurf, TextRect3 = text_objects("the picture shown. Below are examples of poses:", subText2)
        TextRect3.center = ((display_width/2),(200))
        gameDisplay.blit(TextSurf, TextRect3)
        poses(x,y)
        button("Ready?",350, 500, 100, 50,green,bright_green, "go")
        pygame.display.update()
        clock.tick(15)

game_menu()
start_game()


