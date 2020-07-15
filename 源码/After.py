import Setting
import pygame

'''
用来显示成功或失败时的图片
'''


class g_image():
    def __init__(self, screen):                                        # 传入screen（是一个Surface对象，俗称屏幕）参数
        self.screen = screen
        self.rect_s = self.screen.get_rect()                           # 获取屏幕的属性
        self.settings = Setting.Settings()                             # 实例化Setting模块里的Settings类
        self.lose = pygame.image.load(self.settings.lose)              # 加载失败图片
        self.rect_l = self.lose.get_rect()                             # 获取该图片外切矩形属性
        self.victory = pygame.image.load(self.settings.victory)        # 加载胜利图片
        self.rect_v = self.victory.get_rect()                          # 获取该图片外切矩形属性
        # 加载继续游戏按钮和被点击的那妞
        self.cont = pygame.image.load(self.settings.cont)
        self.cont_click = pygame.image.load(self.settings.cont_click)
        # 获取俩个图标的外切矩形
        self.cont_rect = self.cont.get_rect()
        self.cont_click_rect = self.cont_click.get_rect()
        self.reg = pygame.image.load(self.settings.renew)               # 加载重新游戏按钮
        self.reg_click = pygame.image.load(self.settings.renew_click)   # 加载重新游戏被鼠标点击的游戏按钮
        self.reg_rect = self.reg.get_rect()                             # 获取该图标的外切矩形的属性
        self.reg_click_rect = self.reg_click.get_rect()                 # 获取该图标（被点击）的外切矩形的属性

    # 放置失败的图标
    def update_l(self):
        self.rect_l.center = self.rect_s.center

    # 放置胜利的图标
    def update_v(self):
        self.rect_v.center = self.rect_s.center

    # 放置“继续游戏”按钮
    def update_cont(self):
        self.cont_rect.centerx, self.cont_rect.centery = self.rect_s.centerx - 20, self.rect_s.centery + 220
        self.cont_click_rect.centerx, self.cont_click_rect.centery = self.rect_s.centerx - 20, self.rect_s.centery + 220

    # 放置“重新游戏”按钮
    def update_reg(self):
        self.reg_rect.centerx, self.reg_rect.centery = self.rect_s.centerx - 50, self.rect_s.centery + 150
        self.reg_click_rect.centerx, self.reg_click_rect.centery = self.rect_s.centerx - 50, self.rect_s.centery + 150

    # 绘制失败图像
    def draw_l(self):
        self.screen.blit(self.lose, self.rect_l)

    # 绘制胜利图像
    def draw_v(self):
        self.screen.blit(self.victory, self.rect_v)

    # 绘制继续游戏按钮
    def draw_cont(self):
        self.screen.blit(self.cont, self.cont_rect)

    # 绘制继续游戏背点击后的按钮
    def draw_cont_c(self):
        self.screen.blit(self.cont_click, self.cont_click_rect)

    # 绘制重新游戏按钮
    def draw_reg(self):
        self.screen.blit(self.reg, self.reg_rect)

    # 绘制重新游戏背点击后的按钮
    def draw_reg_click(self):
        self.screen.blit(self.reg_click, self.reg_click_rect)
