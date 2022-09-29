from pygame.math import Vector2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
TILE_SIZE = 16
SCALE = 2
CAR_SCALE = 0.5;
LAYERS = {
    'ground' : 0,
    'road': 1,
    'sidewalk': 2,
    'fences': 3,
    'buildings': 4,
    'trees': 5,
    'props': 6,
    'blocks' : 7,
    'main' : 8
}

TMX_PATH = '../graphics/map/map.tmx';
PNG_BASE_MAP_PATH = '../graphics/map/map.png'
PLAYER_START_X = 105*SCALE*TILE_SIZE+TILE_SIZE*SCALE/2
PLAYER_START_Y = 190*SCALE*TILE_SIZE