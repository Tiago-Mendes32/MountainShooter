import random
import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, WIN_HEIGHT, WIN_WIDTH, MENU_OPTION, EVENT_ENEMY, ENEMY_SPAWN_TIME, C_GREEN, C_CYAN, \
    EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player1 = EntityFactory.get_entity('Player1')
        player1.score = player_score[0]
        self.entity_list.append(player1)
        if game_mode == MENU_OPTION[1]:
            player2 = EntityFactory.get_entity('Player2')
            player2.score = player_score[1]
            self.entity_list.append(player2)

        if game_mode == MENU_OPTION[2]:
            self.entity_list.append(EntityFactory.get_entity('Player2', (WIN_WIDTH - 90, WIN_HEIGHT / 2)))
        pygame.time.set_timer(EVENT_ENEMY, ENEMY_SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):
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

                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if ent.name == 'Player1':
                                player_score[0] = ent.score
                            if ent.name == 'Player2':
                                player_score[1] = ent.score
                        return  True

            found_player = False
            for ent in self.entity_list:
              if isinstance(ent, Player):
                  found_player = True

            if not found_player:
                return False

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
