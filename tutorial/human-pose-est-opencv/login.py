import pygame as pg
import csv
import platform

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

playerName = ""


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
                    print("Playername = " + playerName + " playerscore = ")
                    print(counter())
                    write_to_file(playerName, counter)
                    self.text = ''
                    read_the_file()
                    game_over()
                    
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
        
def read_the_file():
    with open("PlayerNames.csv") as f_obj:
        content = f_obj.readlines() 

    for line in content[:-1]:
        print(line.strip().split(','))

        
def write_to_file(playerName, counter):
    
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None        
    
    with open('PlayerNames.csv', 'a', newline=newline) as output_file:
        output_writer = csv.writer(output_file)
    
        output_writer.writerow([playerName, counter()])

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
