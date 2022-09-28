from pygame.math import Vector2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
TILE_SIZE = 16
SCALE = 3

LAYERS = {
    'ground' : 0,
    'blocks' : 1,
    'main' : 2
}

PLAYER_START_X = 105*SCALE*TILE_SIZE+TILE_SIZE*SCALE/2
PLAYER_START_Y = 180*SCALE*TILE_SIZE