import pygame
from config import *
from button import *
from main import *

play_b = pygame.image.load(os.path.join('All Code/Pygame_projects/TestGame/assets','play_button.png'))
setting_b = pygame.image.load(os.path.join('All Code/Pygame_projects/TestGame/assets','setting_button.png'))
exit_b = pygame.image.load(os.path.join('All Code/Pygame_projects/TestGame/assets','exit_button.png'))

play_button = button.Button(100,200,play_b,2)
setting_button = button.Button(100,200,setting_b,2)
exit_button = button.Button(100,200,exit_b,2)


PAUSE = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('PAUSED')




game_paused = True
while game_paused:

    PAUSE.fill((202, 228, 241))



    #event handler
    for event in pygame.event.get():
        

        if event.type == pygame.QUIT:
            game_paused = False

    pygame.display.update()
