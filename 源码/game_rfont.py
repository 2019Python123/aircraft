import pygame

'''
    导弹数量
    子弹数量
    冲击波数量
    生命值 
    飞机生命数量显示
    分数显示和最高分数显示
    等级数量
'''


class Rfont():
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.Font("font\\FZZJ-HaiTZKJW.TTF", 20)
        self.font_one = pygame.font.Font("font\\FZZJ-HaiTZKJW.TTF", 40)
        # 是否被读取一次文件
        self.readed = False

    # 生命条
    def rect_life(self, screen, settings):
        self.life_number = "生命值 :" + str(settings.life)
        self.font_life = self.font.render(self.life_number, 1, (255, 255, 255))
        self.life_rect = self.font_life.get_rect()
        self.life_rect.left = 0
        self.life_rect.top = 580
        screen.blit(self.font_life, self.life_rect)
        pygame.draw.rect(screen, (0, 0, 0), (0, 600, 100, 10), 0)
        pygame.draw.rect(screen, (0, 255, 0), (0, 600, settings.life // 4, 10), 0)

    # 子弹数量的显示
    def bullet_b(self, screen, settings, bulltes):
        self.b_number = "子弹数量: ∞"
        self.font_bullet = self.font.render(self.b_number, 1, (255, 255, 255))
        self.rect_billet = self.font_bullet.get_rect()
        self.rect_billet.left = 0
        self.rect_billet.top = 680
        screen.blit(self.font_bullet, self.rect_billet)
        pygame.draw.rect(screen, (0, 0, 0), (0, 700, 100, 10), 0)
        pygame.draw.rect(screen, (0, 255, 0), (0, 700, (settings.bullet_rect // 3 - len(bulltes) * 2), 10), 0)

    #     玩家分数的显示
    def show_grades(self, screen, settings):
        self.sorce = "分数 :" + str(settings.sofar_soreces)
        self.font_s = self.font.render(self.sorce, 1, (0, 255, 0))
        self.rect_s = self.font_s.get_rect()
        self.rect_s.left = 0
        self.rect_s.top = 10
        screen.blit(self.font_s, self.rect_s)

    # 敌人数量的显示
    def show_enemy(self, screen, armys):
        self.enemynumber = "敌军数量：" + str(len(armys))
        self.font_e = self.font.render(self.enemynumber, 1, (0, 255, 0))
        self.rect_e = self.font_e.get_rect()
        self.rect_e.left = 0
        self.rect_e.top = 50
        screen.blit(self.font_e, self.rect_e)

    # 读取文件
    def show_read(self, screen, settings):
        self.beast_str = "总分数:" + str(settings.soreces)
        self.beast_f = self.font_one.render(self.beast_str, 1, (0, 255, 0))
        self.beast_rect = self.beast_f.get_rect()
        self.beast_rect.left = 530
        self.beast_rect.top = 100
        screen.blit(self.beast_f, self.beast_rect)
        self.readed = True

    # 显示玩家分数
    def show_grades_one(self, screen, settings):
        self.sorce_one = "当局分数:" + str(settings.sofar_soreces)
        self.font_s_one = self.font_one.render(self.sorce_one, 1, (0, 255, 0))
        self.rect_s_one = self.font_s.get_rect()
        self.rect_s_one.left = 530
        self.rect_s_one.top = 150
        screen.blit(self.font_s_one, self.rect_s_one)

    # 显示玩家无敌时间
    def show_time(self, screen, settings):
        self.time = "无敌时间：" + str(60 - settings.clock_count)
        self.font_t = self.font.render(self.time, 1, (0, 255, 0))
        self.rect_t = self.font_t.get_rect()
        self.rect_t.left = 530
        self.rect_t.top = 180
        screen.blit(self.font_t, self.rect_t)

    # 显示玩家生命矩形图
    def show_lifeicon(self, screen, settings):
        self.life_icon = pygame.image.load(settings.life_icon)
        self.icon_rect = self.life_icon.get_rect()
        self.icon_rect.centerx = settings.screen_width - 120
        self.icon_rect.centery = settings.screen_height - 50
        screen.blit(self.life_icon, self.icon_rect)

        self.lnumber = "X" + str(settings.player)
        self.font_l = self.font_one.render(self.lnumber, 1, (255, 255, 255))
        self.rect_l = self.font_l.get_rect()
        self.rect_l.centerx = settings.screen_width - 40
        self.rect_l.centery = settings.screen_height - 50
        screen.blit(self.font_l, self.rect_l)

    # 显示冲击波的能量
    def wave_rect(self, screen, settings):
        self.txt_wave = "冲击波能量值: " + str(settings.wave_energy)
        self.font_w = self.font.render(self.txt_wave, 1, (255, 255, 255))
        self.rect_w = self.font_w.get_rect()
        self.rect_w.left = 0
        self.rect_w.top = 620
        screen.blit(self.font_w, self.rect_w)
        pygame.draw.rect(screen, (0, 0, 0), (0, 650, 100, 10), 0)
        pygame.draw.rect(screen, (0, 255, 0), (0, 650, settings.wave_energy - settings.use_energy, 10), 0)

    # 显示玩家火箭数量和图标
    def show_rocket(self, screen, settings):
        self.image = pygame.image.load(settings.daodan_icon)
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 500
        screen.blit(self.image, self.rect)
        self.txt_rocket = "X" + str(settings.daodan_number)
        self.font_r = self.font_one.render(self.txt_rocket, 1, (255, 255, 255))
        self.rect_r = self.font_r.get_rect()
        self.rect_r.left = 80
        self.rect_r.top = 500
        screen.blit(self.font_r, self.rect_r)

    # 显示段位
    def rank(self, settings, screen):
        self.ranks = []
        self.rects_rank = []
        number = settings.soreces // 5000000
        if number > 4:
            number = 4
        for index in range(5):
            image = pygame.image.load(settings.ranks_image[index])
            self.ranks.append(image)
        for index in range(5):
            rect = self.ranks[index].get_rect()
            self.rects_rank.append(rect)
        for index in range(5):
            self.rects_rank[index].left = 0
            self.rects_rank[index].top = 430
        screen.blit(self.ranks[number], self.rects_rank[number])

    # 胜利界面或失败界面上显示段位
    def rank_font(self, screen):
        self.font_rank = self.font_one.render("当前段位:", 1, (0, 255, 0))
        self.rect_rk = self.font_rank.get_rect()
        self.rect_rk.left = 530
        self.rect_rk.top = 40
        screen.blit(self.font_rank, self.rect_rk)

    # 显示段位图标
    def rank_copy(self, settings, screen):
        self.ranks = []
        self.rects_rank = []
        number = settings.soreces // 5000000
        if number > 4:
            number = 4
        for index in range(5):
            image = pygame.image.load(settings.ranks_image[index])
            self.ranks.append(image)
        for index in range(5):
            rect = self.ranks[index].get_rect()
            self.rects_rank.append(rect)
        for index in range(5):
            self.rects_rank[index].left = 720
            self.rects_rank[index].top = 34
        screen.blit(self.ranks[number], self.rects_rank[number])
