import pygame
from Setting import *


class setting():
    # 初始化游戏设置界面的属性
    def __init__(self, screen):
        self.settings = Settings()  # 实例化Setting模块的Setings类
        self.screen = screen        # 游戏屏幕的赋值
        self.music_control = pygame.image.load(self.settings.music_control)  # 加载音乐控制图片
        self.music_control_rect = self.music_control.get_rect()              # 获取该图片的外切矩形的属性
        self.off_musci = pygame.image.load(self.settings.music_off)          # 加载关闭音乐的图片
        self.off_musci_rect = self.off_musci.get_rect()                      # 获取该图片的外切矩形的属性
        self.oppen_music = pygame.image.load(self.settings.music_on)         # 加载开启音乐的图片
        self.oppen_music_rect = self.oppen_music.get_rect()                  # 获取该图片的外切矩形的属性
        self.back_one = pygame.image.load(self.settings.back)                # 加载’关闭‘未点击的图片
        self.back_one_rect = self.back_one.get_rect()                        # 获取该图片的外切矩形的属性
        self.back_two = pygame.image.load(self.settings.back_one)            # 加载‘关闭’被鼠标点击的图片
        self.back_two_rect = self.back_two.get_rect()                        # 获取该图片的外切矩形的属性

    def replace_music(self):
        # 放置上面加载的所有图标
        self.music_control_rect.centerx, self.music_control_rect.centery = 500, 400
        self.off_musci_rect.centerx, self.off_musci_rect.centery = 660, 400
        self.oppen_music_rect.centerx, self.oppen_music_rect.centery = 660, 400
        self.back_one_rect.centerx, self.back_one_rect.centery = 660, 500
        self.back_two_rect.centerx, self.back_two_rect.centery = 660, 500

    # 绘制游戏设置界面
    def blit_settings(self):  # 绘制音乐控制的图标
        self.screen.blit(self.music_control, self.music_control_rect)

    def blit_off(self):       # 绘制关闭音乐的图标
        self.screen.blit(self.off_musci, self.off_musci_rect)

    def blit_oppen(self):       # 绘制开启音乐的图标
        self.screen.blit(self.oppen_music, self.oppen_music_rect)

    def blit_back_one(self):    # 绘制’关闭‘未被点击的图标
        self.screen.blit(self.back_one, self.back_one_rect)

    def blit_back_two(self):    # 绘制‘关闭’被鼠标点击的图标
        self.screen.blit(self.back_two, self.back_one_rect)
