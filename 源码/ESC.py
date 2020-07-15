import pygame
from Setting import *


# esc类:按下esc屏幕显示选择界面
class Esc():
    def __init__(self, screen):
        self.settings = Settings()
        self.screen = screen
        # 加载返回菜单按钮,被鼠标点击的按钮
        self.remenu = pygame.image.load(self.settings.back_menu)
        self.remenu_click = pygame.image.load(self.settings.back_menu_click)
        # 获取俩个图标的外切矩形
        self.remenu_rect = self.remenu.get_rect()
        self.remenu_click_rect = self.remenu_click.get_rect()
        # 加载重玩按钮,被点击的按钮
        self.renewG = pygame.image.load(self.settings.renew)
        self.renewG_click = pygame.image.load(self.settings.renew_click)
        # 获取俩个图标的外切矩形
        self.renewG_click_rect = self.renewG_click.get_rect()
        self.renewG_rect = self.renewG.get_rect()
        # 加载继续游戏按钮和被点击的那妞
        self.cont = pygame.image.load(self.settings.cont)
        self.cont_click = pygame.image.load(self.settings.cont_click)
        # 获取俩个图标的外切矩形
        self.cont_rect = self.cont.get_rect()
        self.cont_click_rect = self.cont_click.get_rect()

        # 放置图标
        self.renewG_rect.centerx, self.renewG_rect.centery = (650, 375)
        self.renewG_click_rect.centerx, self.renewG_click_rect.centery = (650, 375)
        self.remenu_rect.centerx, self.remenu_rect.centery = (650, 500)
        self.remenu_click_rect.centerx, self.remenu_click_rect.centery = (650, 500)
        self.cont_rect.centerx, self.cont_rect.centery = (650, 600)
        self.cont_click_rect.centerx, self.cont_click_rect.centery = (650, 600)
