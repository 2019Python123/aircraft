import pygame
from Setting import *


# 补给类
class surply(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.settings = Settings()
        self.image = pygame.image.load(self.settings.supply)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx, self.rect.centery = random.randint(0, self.settings.screen_width) \
            , random.randint(-500, 0)  # 飞机的位置在一定范围内随机出现
        self.speed = 1
        self.name = 'R'

    def update(self, *args):
        self.rect.y += self.speed
        self.rect.x = self.rect.x

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Lsurply(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.settings = Settings()
        self.image = pygame.image.load(self.settings.supply_life)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx, self.rect.centery = random.randint(0, self.settings.screen_width) \
            , random.randint(-500, 0)  # 飞机的位置在一定范围内随机出现
        self.speed = 1
        self.name = 'L'

    def update(self, *args):
        self.rect.y += self.speed
        self.rect.x = self.rect.x

    def draw(self, screen):
        screen.blit(self.image, self.rect)
