#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.EnemyShoot import EnemyShoot
from code.Entity import Entity
from code.Const import ENTITY_SPEED, WIN_WIDTH, ENTITY_SHOOT_DELAY


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shoot_delay = ENTITY_SHOOT_DELAY[self.name + 'Shoot']

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shoot_delay -= 1
        if self.shoot_delay == 0:
            self.shoot_delay = ENTITY_SHOOT_DELAY[self.name + 'Shoot']
            return EnemyShoot(name=self.name + 'Shoot', position=(self.rect.centerx - 40, self.rect.centery))