import pygame
import sys
from pygame.locals import *
from Setting import *


class music():
    def __init__(self):
        self.settings = Settings()
        # 设置开始游戏界面的音乐
        self.star_music = pygame.mixer.music.load(self.settings.music)
        # 设置玩游戏的音乐
        self.play_game_music = pygame.mixer.music.load(self.settings.play_music)
        # 设置飞机爆炸的音乐
        self.boom_music = pygame.mixer.Sound(self.settings.boom_music)
        # 设置胜利时的音乐
        self.vectory_music = pygame.mixer.Sound(self.settings.victory_music)
        # 设置发射导弹的声音
        self.rocket_music = pygame.mixer.Sound(self.settings.shot_rocket_music)
        # 游戏失败时的音效
        self.lose_music = pygame.mixer.Sound(self.settings.laugh_music)
        # 鼠标点击声音
        self.click = pygame.mixer.Sound(self.settings.clcik_music)
        # 子弹连射的声音
        self.shoot_dada = pygame.mixer.Sound(self.settings.b_shoot)
