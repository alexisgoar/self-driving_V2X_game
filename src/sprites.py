import pygame
from settings import *


class Generic(pygame.sprite.Sprite):
    def __init__(self,pos,surf,groups,z=LAYERS['main'],scale=1):
        super().__init__(groups)
        self.image = surf
        h = self.image.get_height()
        w = self.image.get_width()
        self.image = pygame.transform.scale(self.image,((w*scale,h*scale)))
        self.rect = self.image.get_rect(topleft = pos)
        self.z = z

class Sidewalk(Generic):
    def __init__(self,pos,surf,groups,z,scale):
        super().__init__(pos,surf,groups,z,scale)
        self.hitbox = self.rect.copy().inflate(self.rect.width,self.rect.width)
