import pygame
from Setting import *
import random  # 产生随机数


# 设置敌人类 (pygame.sprite.Sprite)表示Enemty类是Sprite()类的派生类
class Enemty(pygame.sprite.Sprite):
    def __init__(self):  # 初始化
        pygame.sprite.Sprite.__init__(self)
        self.settings = Settings()  # 设立一个Settings类
        self.image = pygame.image.load(self.settings.penemty).convert_alpha()  # 加载图片
        self.rect = self.image.get_rect()  # 获取外切矩形
        self.rect.centerx, self.rect.centery = random.randint(0, self.settings.screen_width) \
            , random.randint(-1000, 0)  # 飞机的位置在一定范围内随机出现
        self.p_speed = 2
        self.mask = pygame.mask.from_surface(self.image)
        # 爆炸图片
        self.boomimage_number = 6
        # 爆炸图片列表和每个图片对应的rect（外切矩形）属性列表
        self.booms = []
        self.booms_rects = []
        # 放入列表内
        for i in range(self.boomimage_number):
            self.boom = pygame.image.load(self.settings.booms[i])
            self.rect = self.boom.get_rect()
            self.booms.append(self.boom)
            self.booms_rects.append(self.rect)
        #     判断飞机是否存在
        self.active = True
        self.index = 0
        # 玩家杀死低级敌人得到的分数
        self.sorces = 2000
        self.life = 100

    def update(self, *args):  # 更新飞机位置
        self.rect.centery += self.p_speed
        if self.rect.midtop[1] > self.settings.screen_height:
            self.resent()

    def resent(self):
        self.rect.centerx, self.rect.centery = random.randint(0, self.settings.screen_width) \
            , random.randint(-100, 0)  # 飞机的位置在一定范围内随机出现

    def draw(self, screen):  # 绘制飞机
        screen.blit(self.image, self.rect)

    def placeboom(self):  # 放置爆炸图片的位置
        for index in range(self.boomimage_number):
            self.booms_rects[index].centerx, self.booms_rects[index].centery = self.rect.centerx, self.rect.centery

    def blit_boom(self, screen):  # 绘制爆炸图片
        if not self.settings.delay % 2:
            screen.blit(self.booms[self.index], self.booms_rects[self.index])
            self.index += 1
            self.index %= 6

    def blit(self, screen):
        self.lifex, self.lifey = self.rect.left + 50, self.rect.bottom - 80
        pygame.draw.rect(screen, (0, 0, 0), (self.lifex, self.lifey, 100, 2), 0)
        pygame.draw.rect(screen, (0, 255, 0), (self.lifex, self.lifey, self.life, 2), 0)


# 中级敌人类继承sprig模块的Sprite类
class MEnemty(pygame.sprite.Sprite):
    def __init__(self):  # 初始化
        pygame.sprite.Sprite.__init__(self)
        self.settings = Settings()  # 设立一个Settings类
        self.image = pygame.image.load(self.settings.menemty).convert_alpha()  # 加载图片
        self.rect = self.image.get_rect()  # 获取外切矩形
        self.rect.centerx, self.rect.centery = random.randint(0, self.settings.screen_width) \
            , random.randint(-1000, 0)  # 飞机的位置在一定范围内随机出现
        self.p_speed = 1
        self.mask = pygame.mask.from_surface(self.image)
        # 爆炸图片
        self.boomimage_number = 6
        # 爆炸图片列表和每个图片对应的rect（外切矩形）属性列表
        self.booms = []
        self.booms_rects = []
        # 放入列表内
        for i in range(self.boomimage_number):
            self.boom = pygame.image.load(self.settings.booms[i])
            self.rect = self.boom.get_rect()
            self.booms.append(self.boom)
            self.booms_rects.append(self.rect)
        #     判断飞机是否存在
        self.active = True
        self.index = 0
        # 玩家杀死低级敌人得到的分数
        self.sorces = 8000
        self.life = 200

    def update(self, *args):  # 更新飞机位置
        self.rect.centery += self.p_speed
        if self.rect.midtop[1] > self.settings.screen_height:
            self.resent()

    def resent(self):  # 重新放置图片
        self.rect.centerx, self.rect.centery = random.randint(0, self.settings.screen_width) \
            , random.randint(-100, 0)  # 飞机的位置在一定范围内随机出现

    def draw(self, screen):  # 绘制图片
        screen.blit(self.image, self.rect)

    def placeboom(self):  # 放置爆炸图片
        for index in range(self.boomimage_number):
            self.booms_rects[index].centerx, self.booms_rects[index].centery = self.rect.centerx, self.rect.centery

    # 绘制敌人爆炸的过程图片
    def blit_boom(self, screen):  # 绘制爆炸图片
        if not self.settings.delay % 2:
            screen.blit(self.booms[self.index], self.booms_rects[self.index])
            self.index += 1
            self.index %= 6

    # 绘制敌人生命矩形图
    def blit(self, screen):
        self.lifex, self.lifey = self.rect.left + 50, self.rect.bottom - 110
        pygame.draw.rect(screen, (0, 0, 0), (self.lifex, self.lifey, 100, 5), 0)
        pygame.draw.rect(screen, (0, 255, 0), (self.lifex, self.lifey, self.life // 2, 5), 0)


# 高级敌人类继承sprig模块的Sprite类
class BEnemty(pygame.sprite.Sprite):
    def __init__(self):  # 初始化
        pygame.sprite.Sprite.__init__(self)
        self.settings = Settings()  # 设立一个Settings类
        self.image = pygame.image.load(self.settings.boos).convert_alpha()  # 加载图片
        self.rect = self.image.get_rect()  # 获取外切矩形
        self.rect.centerx, self.rect.centery = random.randint(0, self.settings.screen_width) \
            , random.randint(-1000, 0)  # 飞机的位置在一定范围内随机出现
        self.p_speed = 1
        self.mask = pygame.mask.from_surface(self.image)
        # 爆炸图片
        self.boomimage_number = 6
        # 爆炸图片列表和每个图片对应的rect（外切矩形）属性列表
        self.booms = []
        self.booms_rects = []
        # 放入列表内
        for i in range(self.boomimage_number):
            self.boom = pygame.image.load(self.settings.booms[i])
            self.rect = self.boom.get_rect()
            self.booms.append(self.boom)
            self.booms_rects.append(self.rect)
        #     判断飞机是否存在
        self.active = True
        self.index = 0
        # 玩家杀死低级敌人得到的分数
        self.sorces = 30000
        # 敌人生命
        self.life = 5000

    def update(self, *args):  # 更新飞机位置
        self.rect.centery += self.p_speed
        if self.rect.midtop[1] > self.settings.screen_height:
            self.resent()

    def resent(self):
        self.rect.centerx, self.rect.centery = random.randint(0, self.settings.screen_width) \
            , random.randint(-100, 0)  # 飞机的位置在一定范围内随机出现

    def draw(self, screen):  # 绘制敌人
        screen.blit(self.image, self.rect)

    def placeboom(self):  # 放置爆炸图片的位置
        for index in range(self.boomimage_number):
            self.booms_rects[index].center = self.rect.center

    def blit_boom(self, screen):  # 绘制敌人爆炸过程图片
        if not self.settings.delay % 2:
            screen.blit(self.booms[self.index], self.booms_rects[self.index])
            self.index += 1
            self.index %= 6

    def blit(self, screen):
        self.lifex, self.lifey = self.rect.left + 170, self.rect.bottom + 50
        pygame.draw.rect(screen, (0, 0, 0), (self.lifex, self.lifey, 200, 20), 0)
        pygame.draw.rect(screen, (255, 0, 0), (self.lifex, self.lifey, self.life // 25, 20), 0)
