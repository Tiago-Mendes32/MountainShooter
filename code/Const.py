import pygame

# C
COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (253, 208, 23)

# E
ENEMY_SPAWN_TIME = 3000

ENTITY_SHOOT_DELAY = {
    'Player1Shoot':20,
    'Player2Shoot': 40,
    'Enemy1Shoot': 80,
    'Enemy2Shoot': 120
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Player1': 300,
    'Player2': 300,
    'Enemy1': 300,
    'Enemy2': 300,
    'Player1Shoot': 999,
    'Player2Shoot': 999,
    'Enemy1Shoot': 999,
    'Enemy2Shoot': 999,
}

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 6,
    'Level1Bg6': 8,
    'Player1': 4,
    'Player1Shoot': 1,
    'Player2': 4,
    'Player2Shoot': 1,
    'Enemy1': 2,
    'Enemy1Shoot': 3,
    'Enemy2': 1,
    'Enemy2Shoot': 2,
}

EVENT_ENEMY = pygame.USEREVENT + 1

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP, 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN, 'Player2': pygame.K_s}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT, 'Player2': pygame.K_d}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT, 'Player2': pygame.K_a}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL, 'Player2': pygame.K_LCTRL}

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
