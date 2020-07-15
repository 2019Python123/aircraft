import pygame
from Setting import *


# 设置子弹精灵继承pygame中sprite模块里的Sprite类
class bullet(pygame.sprite.Sprite):
    def __init__(self, airplane_position):                      # 传入飞机坐标（airplane_position）
        pygame.sprite.Sprite.__init__(self)                     # 初始化基类
        self.settings = Settings()                              # 实例化Setting模块里的Settings类
        self.image = pygame.image.load(self.settings.bullet)    # 加载子弹图片
        self.rect = self.image.get_rect()                       # 获取该图片的外切矩形属性
        self.speed = 4                                          # 子弹速度
        # self.bullet_tick = False
        self.rect.midbottom = airplane_position                 # 子弹最开始出现的位置是飞机的驾驶舱中间的位置
        self.mask = pygame.mask.from_surface(self.image)        # mask值用于完美检测子弹与敌人的碰撞

    def update(self, *args):                                    # 移动子弹
        self.rect.y -= self.speed

    def draw(self, screen):                                     # 重构基类draw函数，绘制子弹
        screen.blit(self.image, self.rect)


class Rbullet(pygame.sprite.Sprite):
    def __init__(self, airplane_position):                      # 传入飞机坐标（airplane_position）
        pygame.sprite.Sprite.__init__(self)                     # 初始化基类
        self.settings = Settings()                              # 实例化Setting模块里的Settings类
        self.image = pygame.image.load(self.settings.rocket)    # 加载导弹的图片
        self.rect = self.image.get_rect()                       # 获取该图片的外切矩形属性
        self.speed = 4                                          # 导弹速度
        # self.bullet_tick = False
        self.rect.midbottom = airplane_position                 # 子弹最开始出现的位置是飞机的驾驶舱中间的位置
        self.mask = pygame.mask.from_surface(self.image)        # mask值用于完美检测子弹与敌人的碰撞

    def update(self, *args):                                    # 移动导弹
        self.rect.y -= self.speed

    def draw(self, screen):                                     # 重构基类draw函数，绘制子弹
        screen.blit(self.image, self.rect)


class Wave(pygame.sprite.Sprite):
    def __init__(self, airplane_position):                      # 传入飞机坐标（airplane_position）
        pygame.sprite.Sprite.__init__(self)                     # 初始化基类
        self.settings = Settings()                              # 实例化Setting模块里的Settings类
        self.image = pygame.image.load(self.settings.wave)      # 加载导弹的图片
        self.rect = self.image.get_rect()                       # 获取该图片的外切矩形属性
        self.speed = 4                                          # 导弹速度
        # self.bullet_tick = False
        self.rect.midbottom = airplane_position                 # 子弹最开始出现的位置是飞机的驾驶舱中间的位置
        self.mask = pygame.mask.from_surface(self.image)        # mask值用于完美检测子弹与敌人的碰撞

    def update(self, *args):                                    # 移动导弹
        self.rect.y -= self.speed

    def draw(self, screen):                                     # 重构基类draw函数，绘制子弹
        screen.blit(self.image, self.rect)
