import pygame as pg
import csv
import platform
import pandas as pd

pg.init()

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

screen = pg.display.set_mode((display_width, display_height))
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 32)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event,counter):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    
                    playerName = self.text
                    print("Playername = " + playerName + " playerscore = " ,counter())                    
                    df = pd.read_csv("scoreboard.csv")
                    df.loc[-1] = [playerName, counter()]  # adding a row
                    df.index = df.index + 1  # shifting index
                    df.sort_index(inplace=True) 
                    df.to_csv("scoreboard.csv", index=False)
                    print(df.head())
                    self.text = ''
                    game_over(df)
                    
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)

        
def game_over(df):

    gameExit = False
    while not gameExit:
 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        screen.fill(white)
        largeText = pg.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_objects("Game Over", largeText)        
        TextRect.center = ((display_width/2),(50))
        screen.blit(TextSurf, TextRect)
        
        TextSurf2, TextRect2 = text_objects("Highscores:", largeText)
        TextRect2.center = ((display_width/2),(display_height/3))
        screen.blit(TextSurf2, TextRect2)
        
        TextSurf3, TextRect3 = text_objects("Highscores:", largeText)
        TextRect3.center = ((display_width/2),(display_height/3))
        screen.blit(TextSurf3, TextRect3)
        
        pg.display.update()
        
def main(counter):
    
    clock = pg.time.Clock()
    input_box1 = InputBox(display_width/2-70, display_height/2, 140, 32)
    """
    For flere textbokse: 
    input_box2 = InputBox(100, 300, 140, 32)
    input_boxes = [input_box1, input_box2]
    """
    input_boxes = [input_box1]
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event,counter)

        for box in input_boxes:
            box.update()

        screen.fill((white))
        for box in input_boxes:
            box.draw(screen)
        
        largeText = pg.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_objects("Write your username", largeText)
        TextRect.center = ((display_width/2),(display_height/3))
        screen.blit(TextSurf, TextRect)
        
        
        pg.display.flip()
        clock.tick(30)
        
def game_over():

    gameExit = False
    while not gameExit:
 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        screen.fill(white)
        largeText = pg.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_objects("Game Over", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect) 
        pg.display.update()
            
"""if __name__ == '__main__':
    main()
    read_the_file()
    pg.quit()"""
