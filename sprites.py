import pygame, math, random
  
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = self.height = TILESIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(COLOR)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
