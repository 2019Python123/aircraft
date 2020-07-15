import pygame
from Setting import *

'''
玩家的飞机
'''


class H_airplane(pygame.sprite.Sprite):
    def __init__(self, screen):
        # 初始化基类
        pygame.sprite.Sprite.__init__(self)
        # 获取屏幕
        self.screen = screen
        # 获取飞机属性
        self.air_settings = Settings()
        # 获取屏幕尺寸
        self.screen_rect = self.screen.get_rect()
        # 加载玩家飞机图片
        self.image = pygame.image.load(self.air_settings.aircraft_image).convert_alpha()
        # 加载玩家爆炸的图片,booms表示装爆炸图片的列表，rects表示对应booms每张图片的外切矩形的集合
        self.boomimage_number = 6
        self.booms = []
        self.booms_rects = []
        for i in range(self.boomimage_number):
            self.boom = pygame.image.load(self.air_settings.booms[i])
            self.rect = self.boom.get_rect()
            self.booms.append(self.boom)
            self.booms_rects.append(self.rect)
        # 获取飞机外切矩形
        self.rect = self.image.get_rect()
        # mask属性用来碰撞的完美检测
        self.mask = pygame.mask.from_surface(self.image)
        # 玩家是否活着
        self.active = True
        self.index = 0
        # 等级
        self.leavel = 1
        # 控制移动速度
        self.speed = 3

    #  将飞机放在屏幕底部中心
    def place_aircraft(self):
        self.rect.centerx = self.screen_rect.centerx + self.air_settings.airplane_movex
        self.rect.centery = self.screen_rect.bottom - self.rect.height // 2 + self.air_settings.airplane_movey

    # 绘制飞机
    def blit_aircraft(self, settings):
        self.screen.blit(self.image, self.rect)
        if settings.soreces // 50000 > self.leavel:
            self.leavel += settings.soreces // 50000
            self.uplevel()

    # 重新放置飞机
    def replace(self):
        self.rect.centerx -= self.air_settings.airplane_movex
        self.rect.centery -= self.air_settings.airplane_movey
        self.air_settings.airplane_movex = 0
        self.air_settings.airplane_movey = 0

    # 将爆炸图片的位置跟随着玩家的飞机
    def placeboom(self):
        for index in range(self.boomimage_number):
            self.booms_rects[index].centerx, self.booms_rects[index].centery = self.rect.centerx, self.rect.centery

    # 绘制爆炸图片
    def blit_boom(self):
        if not self.air_settings.delay % 2:
            self.screen.blit(self.booms[self.index], self.booms_rects[self.index])
            self.index += 1
            self.index %= 6

    # 绘制玩家飞机升级的图片
    def uplevel(self):
        self.up_image = pygame.image.load(self.air_settings.uplevel)
        self.rect_up = self.up_image.get_rect()
        self.rect_up.left = self.rect.left + 25
        self.rect_up.top = self.rect.top
        self.screen.blit(self.up_image, self.rect_up)

    # 在屏幕上显示玩家的等级
    def show_level(self):
        self.font = pygame.font.Font("font\\FZZJ-HaiTZKJW.TTF", 20)
        self.txt = "等级：" + str(self.leavel)
        self.font_txt = self.font.render(self.txt, 1, (0, 255, 0))
        self.rect_txt = self.font_txt.get_rect()
        self.rect_txt.left = 0
        self.rect_txt.top = 300
        self.screen.blit(self.font_txt, self.rect_txt)
