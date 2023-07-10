import pygame, os, button
pygame.font.init()
pygame.mixer.init()



WIDTH=1280
HEIGHT=720
BORDER = pygame.Rect(WIDTH//2 - 5,0,10, HEIGHT) #To make this smack dab in the middle you have to make the x half of the width because it will be off
C_LAYER = 2 #all characters in this layer
GROUND_LAYER = 1
TILESIZE = 32
COLOR = (255, 0 , 0)
WHITE_COLOR = (255, 255, 255)
FPS=60
BACKGROUND_COLOR = (0,0,255)
SPACEBACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('All Code/Pygame_projects/TestGame/assets','b2.png')), (WIDTH, HEIGHT))
MIDDLECOLOR = (0, 0, 0)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
#PAUSE NEEDS TRANSPARENT SURFACE


#Button configs 
play_b = pygame.image.load(os.path.join('All Code/Pygame_projects/TestGame/assets','play_button.png'))
setting_b = pygame.image.load(os.path.join('All Code/Pygame_projects/TestGame/assets','settings_button.png'))
exit_b = pygame.image.load(os.path.join('All Code/Pygame_projects/TestGame/assets','exit_button.png'))

play_b_button = button.Button(100,200,play_b,2)
setting_button = button.Button(100,200,setting_b,2)
exit_button = button.Button(100,200,exit_b,2)
#spaceship configs
D_HEALTH = 3
D_HEALTHFONT = pygame.font.SysFont('comicsans', 40)
SPEED = 8
MAX_BULLETS = 8
BULLET_HIT = pygame.mixer.Sound(os.path.join('All Code/Pygame_projects/TestGame/assets', 'hit.wav'))
BULLET_FIRE = pygame.mixer.Sound(os.path.join('All Code/Pygame_projects/TestGame/assets', 'shot.wav'))
BULLET_COLOR = (255, 255, 0)
BULLET_SPEED = 12
SPACESHIPSIZE = (108,80)#(WIDTH,HEIGHT) I can also have each as a seperate variable and repalce SPACESHIP SIZE WITH (WIDTH, HEIGHT)
SPACESHIPWIDTH= SPACESHIPSIZE[0]
SPACESHIPHEIGHT= SPACESHIPSIZE[1]

#Player 1 configs 
P1_HEALTH = 10
SPACESHIP1IMG = pygame.image.load(os.path.join('All Code/Pygame_projects/TestGame/assets','spaceShip1.png'))
SPACESHIP1 = pygame.transform.rotate(pygame.transform.scale(
    SPACESHIP1IMG,SPACESHIPSIZE),90)
player1 = pygame.Rect(WIDTH/4,HEIGHT/2,SPACESHIPWIDTH,SPACESHIPHEIGHT)
p1Bullets =[]

#Player 2 configs
P2_HEALTH = 10
player2 = pygame.Rect(WIDTH *.75,HEIGHT/2,SPACESHIPWIDTH,SPACESHIPHEIGHT)
p2Bullets =[]
SPACESHIP2IMG = pygame.image.load(os.path.join('All Code/Pygame_projects/TestGame/assets','spaceShip2.png'))
SPACESHIP2 = pygame.transform.rotate(pygame.transform.scale(
    SPACESHIP2IMG,SPACESHIPSIZE),270)


#EVENT CONFIGS

P1_HIT = pygame.USEREVENT + 1
P2_HIT = pygame.USEREVENT + 2
PAUSE_EVENT = pygame.USEREVENT + 3