import random
import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, WIN_HEIGHT, WIN_WIDTH, MENU_OPTION, EVENT_ENEMY, ENEMY_SPAWN_TIME, C_GREEN, C_CYAN
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000  # 20 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg', (0, 0)))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if game_mode == MENU_OPTION[1]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        if game_mode == MENU_OPTION[2]:
            self.entity_list.append(EntityFactory.get_entity('Player2', (WIN_WIDTH - 90, WIN_HEIGHT / 2)))
        pygame.time.set_timer(EVENT_ENEMY, ENEMY_SPAWN_TIME)

    def run(self, ):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

                if isinstance(ent, Player):
                    shoot = ent.shoot()
                    if shoot:
                        self.entity_list.append(shoot)

                if isinstance(ent, Enemy):
                    shoot = ent.shoot()
                    if shoot:
                        self.entity_list.append(shoot)

                if ent.name == 'Player1':
                    self.level_text(18, f'Player1 - Health: {ent.health} | Score: {ent.score}', C_GREEN, (10, 30))

                if ent.name == 'Player2':
                    self.level_text(18, f'Player2 - Health: {ent.health} | Score: {ent.score}', C_CYAN, (10, 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            # printed text level
            self.level_text(25, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_WHITE, (10, 5))
            self.level_text(25, f'FPS: {clock.get_fps() :.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(25, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

            # call collision manager
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
