import pygame
from settings import *
from player_car import PlayerCar
from sprites import Generic, Sidewalk
from pytmx.util_pygame import load_pygame

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = Camera()
        self.setup()

    def setup(self):
        tmx_data = load_pygame(TMX_PATH)

        # roads
        for  x,y, surf  in tmx_data.get_layer_by_name('road').tiles():
            Generic((x*TILE_SIZE*SCALE,y*TILE_SIZE*SCALE),
                    surf,self.all_sprites,LAYERS['road'],
                    scale = SCALE)
        #sidewalk
        for  x,y, surf  in tmx_data.get_layer_by_name('sidewalk').tiles():
            Sidewalk((x*TILE_SIZE*SCALE,y*TILE_SIZE*SCALE),
                    surf,self.all_sprites,LAYERS['sidewalk'],
                    scale = SCALE)

        #blocks
        for  x,y, surf  in tmx_data.get_layer_by_name('blocks').tiles():
            Generic((x*TILE_SIZE*SCALE,y*TILE_SIZE*SCALE),
                    surf,self.all_sprites,LAYERS['blocks'],
                    scale = SCALE)

        #buildings
        for  x,y, surf  in tmx_data.get_layer_by_name('buildings').tiles():
            Generic((x*TILE_SIZE*SCALE,y*TILE_SIZE*SCALE),
                    surf,self.all_sprites,LAYERS['buildings'],
                    scale = SCALE)

        #props
        for x, y, surf in tmx_data.get_layer_by_name('buildingprops').tiles():
            Generic((x * TILE_SIZE * SCALE, y * TILE_SIZE * SCALE),
                    surf, self.all_sprites, LAYERS['props'],
                    scale=SCALE)

        for x, y, surf in tmx_data.get_layer_by_name('props').tiles():
            Generic((x * TILE_SIZE * SCALE, y * TILE_SIZE * SCALE),
                    surf, self.all_sprites, LAYERS['props'],
                    scale=SCALE)

        #trees
        for x, y, surf in tmx_data.get_layer_by_name('trees').tiles():
            Generic((x * TILE_SIZE * SCALE, y * TILE_SIZE * SCALE),
                    surf, self.all_sprites, LAYERS['trees'],
                    scale=SCALE)

        #fences
        for x, y, surf in tmx_data.get_layer_by_name('fences').tiles():
            Generic((x * TILE_SIZE * SCALE, y * TILE_SIZE * SCALE),
                    surf, self.all_sprites, LAYERS['fences'],
                    scale=SCALE)

        # map
        Generic(pos = (0,0),
                surf = pygame.image.load(PNG_BASE_MAP_PATH).convert_alpha(),
                groups = self.all_sprites,
                z = LAYERS['ground'],
                scale =SCALE)
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