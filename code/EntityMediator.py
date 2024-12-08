from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShoot import EnemyShoot
from code.Entity import Entity
from code.PlayerShoot import PlayerShoot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(entity: Entity):
            if isinstance(entity, Enemy):
                if entity.rect.right < 0:
                    entity.health = 0

            if isinstance(entity,PlayerShoot):
                if entity.rect.left >= WIN_WIDTH:
                    entity.health = 0

            if isinstance(entity,EnemyShoot):
                if entity.rect.right <= 0:
                    entity.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity = entity_list[i]
            EntityMediator.__verify_collision_window(entity)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)


