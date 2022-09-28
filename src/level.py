import pygame
from settings import *
from player_car import PlayerCar
from sprites import Generic

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = Camera()
        self.setup()

    def setup(self):
        Generic(pos = (0,0),
                surf = pygame.image.load('../graphics/map/map.png').convert_alpha(),
                groups = self.all_sprites,
                z = LAYERS['ground'],
                scale =3)
        self.player_car = PlayerCar((PLAYER_START_X,PLAYER_START_Y), self.all_sprites)

    def run(self,dt):
        self.display_surface.fill('green')
        self.all_sprites.custom_draw(self.player_car)
        self.all_sprites.update(dt)

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def custom_draw(self,player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH/2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT/2
        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -=self.offset
                    self.display_surface.blit(sprite.image,offset_rect)