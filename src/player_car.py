import pygame
from settings import *
import numpy as np
class PlayerCar(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.import_assests();

        self.image = pygame.image.load(self.graphics['normal']).convert_alpha()
        h = self.image.get_height()
        w = self.image.get_width()
        self.image = pygame.transform.scale(self.image, ((round(w * CAR_SCALE), round(h * CAR_SCALE))))
        self.blit_image = self.image

        self.rect = self.image.get_rect(center = pos)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.z = LAYERS['main']
        self.hitbox = self.rect.copy().inflate(self.rect.width,self.rect.height);

        self.orientation = pygame.math.Vector2(self.rect.center)
        self.rotation = 90
        self.rotationSpeed = 100
        self.rotationSpeedFactor = 0;
        self.speedFactor = 0
        self.speed = 200

    def import_assests(self):
        self.graphics = {'normal' : '../graphics/car.png'};

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.speedFactor = 1
        elif keys[pygame.K_DOWN]:
            self.speedFactor = -1
        else:
            self.speedFactor = 0

        if keys[pygame.K_RIGHT]:
            self.rotationSpeedFactor = -1
        elif keys[pygame.K_LEFT]:
            self.rotationSpeedFactor = 1
        else:
            self.rotationSpeedFactor = 0

    def move(self,dt):
        self.pos.x += self.orientation.x*self.speed*self.speedFactor*dt
        self.pos.y += self.orientation.y*self.speed*self.speedFactor*dt
        self.hitbox.centerx = round(self.pos.x);
        self.rect.centerx = self.hitbox.centerx;

        self.hitbox.centery = round(self.pos.y);
        self.rect.centery = self.hitbox.centery;


    def rotate(self,dt):
        self.rotation += self.rotationSpeed*self.rotationSpeedFactor*dt
        self.image = pygame.transform.rotate(self.blit_image,self.rotation)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.orientation.x = np.cos(self.rotation*np.pi/180);
        self.orientation.y = -1*np.sin(self.rotation*np.pi/180)

    def update(self,dt):
        self.input()
        self.move(dt)
        self.rotate(dt)