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

block_color = (53,115,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Human Tetris')
clock = pygame.time.Clock()

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
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 15)
    textSurfStart, textRectStart = text_objects(msg, smallText)
    textRectStart.center = ((x+(w/2)), (y+(50/2)))
    gameDisplay.blit(textSurfStart, textRectStart)

def start_game():
    cap = cv2.VideoCapture(0)
    seconds = 3

    millis = seconds * 1000
    while (millis > 0):
       # Capture frame-by-frame
        ret, frame = cap.read()
        millis = millis - 10
      # Display the resulting frame
        cv2.imshow('video recording', frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
           #this method holds execution for 10 milliseconds, which is why we 
           #reduce millis by 10
            break

     #once the while loop breaks, write img
    img_name = "example.jpg"
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))

def game_intro():

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
        
        
        pygame.display.update()
        clock.tick(15)
        

game_intro()
pygame.quit()
quit()
