import pygame
import time
import random
import numpy as np
import cv2
import logic
import scoreSys
import os
import login

# Init pygame
pygame.init()

# Setting up the display
display_width = 800
display_height = 600

# Setting up colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)

# Setting up variables
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Human Tetris')
clock = pygame.time.Clock()

stickfigImg = pygame.image.load('backgroundmain.png')
posesImg = pygame.image.load('poses.png')
camera = cv2.VideoCapture(0)

# Setting up the cam to fill out gameDisplay
camera.set(cv2.CAP_PROP_FRAME_WIDTH, display_width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, display_height)


def stickFig(x, y):
    gameDisplay.blit(stickfigImg, (x, y))


def poses(x, y):
    gameDisplay.blit(posesImg, (x, y))


def text_objects(text, font, color=black):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    # Mouse controll
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Statement block that controlls the game screens
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
                # cap_screen()
                select_pose()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 15)
    textSurfStart, textRectStart = text_objects(msg, smallText)
    textRectStart.center = ((x+(w/2)), (y+(50/2)))
    gameDisplay.blit(textSurfStart, textRectStart)


def cap_screen(pose_nr, req_pose, len_poses):

    t_start = time.time()
    t_end = t_start + 5

    while time.time() < t_end:
        gameDisplay.fill(white)

        # Capture frame-by-frame
        ret, frame = camera.read()

        # Turns the diplay 90 degrees and changes color
        frame2 = cv2.cvtColor(np.rot90(frame), cv2.COLOR_BGR2RGB)
        frame2 = pygame.surfarray.make_surface(frame2)

        gameDisplay.blit(frame2, (0, 0))

        font = cv2.FONT_HERSHEY_SIMPLEX
        largeText = pygame.font.Font('freesansbold.ttf', 28)
        fontColor = (255, 0, 0)

        # Displays the time remaing, before picture is taken, and evaluaed
        t_now = time.time()

        TextSurf, TextRect = text_objects(
            str(int((t_end + 1) - t_now)), largeText, fontColor)
        TextRect.center = (int(display_width/2), 20)
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()

    # Once the while loop breaks, write img
    if not os.path.exists('imgs'):
        os.makedirs('imgs')

    img_name = "imgs/0{}_{}.jpg".format(pose_nr + 1, req_pose)
    cv2.imwrite(img_name, frame)

    return img_name


def score_screen(counter, res):
    t_start = time.time()
    t_end = t_start + 5

    while time.time() < t_end:
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         quit()
        gameDisplay.fill(white)

        largeText = pygame.font.Font('freesansbold.ttf', 50)
        smallText = pygame.font.Font('freesansbold.ttf', 28)

        TextSurf, TextRect = text_objects("Score Screen", largeText)
        TextRect.center = ((display_width/2), (50))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf1, TextRect1 = text_objects(str('Response: ' + res), smallText)
        TextRect1.center = ((display_width/2), (90))
        gameDisplay.blit(TextSurf1, TextRect1)

        TextSurf2, TextRect2 = text_objects(
            ('Score: ' + str(counter())), smallText)
        TextRect2.center = ((display_width/2), (110))
        gameDisplay.blit(TextSurf2, TextRect2)

        pygame.display.update()
        clock.tick(15)


def game_menu():
    x = 100
    y = 0
    intro = True

    # Init gameloop
    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Displaying text
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_objects("Human Tetris: Main Menu", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        # Setting up buttons
        button("Start Game", 150, 450, 100, 50, green, bright_green, "play")
        button("Scoreboard", 350, 450, 100, 50, blue, bright_blue, "score")
        button("Exit Game", 550, 450, 100, 50, red, bright_red, "quit")
        stickFig(x, y)

        # Makes sure to update the gameDisplay
        pygame.display.update()
        clock.tick(15)


def assignment_menu(reg_pose):

    # Setting up time variabels
    t_start = time.time()
    t_end = t_start + 5

    while time.time() < t_end:
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 28)
        fontColor = (255, 0, 0)

        # Displays the time remaing, before picture is taken
        t_now = time.time()

        # Displays some text
        TextSurf, TextRect = text_objects(
            str(int((t_end + 1) - t_now)), largeText, fontColor)
        TextRect.center = (int(display_width/2), 20)
        gameDisplay.blit(TextSurf, TextRect)

        # Displays an img, showing the req_pose
        assignment_img = pygame.image.load(
            './stick_poses/' + reg_pose + '.bmp')
        gameDisplay.blit(assignment_img, (100, 50))

        clock.tick(15)
        pygame.display.update()


def start_game():

    x = 100
    y = 300

    gameExit = False

    # Init gameloop
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        headerText = pygame.font.Font('freesansbold.ttf', 35)
        TextSurf, TextRect = text_objects("Objective: ", headerText)
        TextRect.center = ((display_width/2), (50))
        gameDisplay.blit(TextSurf, TextRect)

        subText = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect2 = text_objects(
            "Try to pose best possible way according to", subText)
        TextRect2.center = ((display_width/2), (150))
        gameDisplay.blit(TextSurf, TextRect2)

        TextSurf, TextRect3 = text_objects(
            "the picture shown. Below are examples of poses:", subText)
        TextRect3.center = ((display_width/2), (200))
        gameDisplay.blit(TextSurf, TextRect3)

        # Setting up image and button
        poses(x, y)
        button("Ready?", 350, 500, 100, 50, green, bright_green, "go")
        pygame.display.update()
        clock.tick(15)


def get_pose(pose):
    switcher = {
        0: 'T_Pose',
        1: 'Y_Pose',
        2: 'I_Pose',
        # 3: 'X_Pose',
    }
    return switcher.get(pose, "Nothing")


def select_pose():
    poses = [0, 1, 2]
    len_poses = len(poses)
    for x in range(0, len_poses):

        # Sets up the scoresystem for `this` game
        counter = scoreSys.counter

        # Picks a random number from poses, removes it
        # and selects a pose in the switch
        pose = random.choice(poses)
        poses.remove(pose)
        req_pose = get_pose(pose)

        # Starts assignment_menu
        assignment_menu(req_pose)

        # Starts cap_screen
        pose_img = cap_screen(x, req_pose, len_poses)

        # Starts openpose (evalute the pose)
        res = logic.openpose(pose_img, req_pose, counter)

        # Starts score_screen
        score_screen(counter, res)

    # Starts login.main
    login.main(counter)

    # Ends the game
    game_over(x, req_pose, len_poses)


# Starts the game
game_menu()
