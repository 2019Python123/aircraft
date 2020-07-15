import pygame
import sys
from Setting import *


# 设置游戏开始界面
class InterFace():
    def __init__(self, screen):
        # 获取屏幕
        self.screen = screen
        #
        self.settings = Settings()
        # 获取屏幕的矩形
        self.screen_rect = screen.get_rect()

        # 导入 ”进入游戏“ 的图片
        self.enter_game = pygame.image.load(self.settings.enter_image).convert_alpha()
        # 获取该图片的外切矩形
        self.enter_rect = self.enter_game.get_rect()

        # 导入点击 “进入游戏” 的图片
        self.enter_click = pygame.image.load(self.settings.enter_image_click).convert_alpha()
        # 获取该图片的外切矩形
        self.enter_rect_click = self.enter_click.get_rect()

        # 导入 “退出游戏” 的图片
        self.exit_game = pygame.image.load(self.settings.exit_image).convert_alpha()
        # 获取该图片的外切矩形
        self.exit_rect = self.exit_game.get_rect()

        # 导入 “退出游戏” 被点击的图片
        self.exit_click = pygame.image.load(self.settings.exit_image_click).convert_alpha()
        # 获取该图片的外切矩形
        self.exit_rect_click = self.exit_click.get_rect()

        # 导入游戏设置图标
        self.game_set = pygame.image.load(self.settings.set_game).convert_alpha()
        # 获取该图标的外切矩形
        self.game_set_rect = self.game_set.get_rect()

        # 导入游戏设置被点击的图标
        self.game_set_click = pygame.image.load(self.settings.set_game_click).convert_alpha()
        # 获取该图标的外切矩形
        self.game_set_click_rect = self.game_set.get_rect()

        # 将 “进入游戏” 图标放置在屏幕中间
        self.enter_rect.centerx = self.screen_rect.centerx
        self.enter_rect.centery = self.screen_rect.centery
        # 将 “进入游戏” 被点击图标放置在屏幕中间
        self.enter_rect_click.centerx = self.screen_rect.centerx
        self.enter_rect_click.centery = self.screen_rect.centery

        # 将 “退出游戏” 图标放置在 ”进入游戏“ 下面
        self.exit_rect.centerx = self.enter_rect.centerx
        self.exit_rect.centery = self.enter_rect.centery + 100
        # 将 “退出游戏” 被点击图标放置在 “进入游戏” 下面
        self.exit_rect_click.centerx = self.enter_rect.centerx
        self.exit_rect_click.centery = self.enter_rect.centery + 100

        # 将“游戏设置“按钮放在界面右下角
        self.game_set_rect.centerx, self.game_set_rect.centery = 1200, 700
        # 将”游戏设置“被点击按钮放在同样的位置
        self.game_set_click_rect.centerx, self.game_set_click_rect.centery = 1200, 700

    # 绘制进入游戏过程的图片
    def blit_enter(self):
        self.screen.blit(self.enter_game, self.enter_rect)

    def blit_enter_click(self):
        self.screen.blit(self.enter_click, self.enter_rect_click)

    # 绘制退出游戏过程的图片
    def blit_exit(self):
        self.screen.blit(self.exit_game, self.exit_rect)

    def blit_exit_click(self):
        self.screen.blit(self.exit_click, self.exit_rect_click)

    # 绘制游戏设置的过程
    def blit_game_set(self):
        self.screen.blit(self.game_set, self.game_set_rect)

    def blit_game_set_click(self):
        self.screen.blit(self.game_set_click, self.game_set_click_rect)
