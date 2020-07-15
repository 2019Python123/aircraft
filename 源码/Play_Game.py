from Human_airplane import *
import Setting
from Interface import *
import Game_Funtion as gf
from music_set import *
from game_setting import *
from ESC import *
import Supply
import After
import game_rfont


def run_game():
    # 初始化界面
    pygame.init()
    # 初始化mixer模块
    pygame.mixer.init()
    # 初始化font模块
    pygame.font.init()
    game_music = music()
    # settings的对象
    settings = Setting.Settings()
    pygame.mixer.music.load(settings.music)
    pygame.mixer.music.play(-1, 0.0)
    #
    rfont = game_rfont.Rfont()
    # 自定义玩家复活时无敌事件
    Invincible = pygame.USEREVENT + 1
    pygame.time.set_timer(Invincible, 1000 // 60 * 2)
    # 设置屏幕大小
    screen = pygame.display.set_mode(settings.size)
    # settings的对象
    game_setting = setting(screen)
    # Interface的对象
    interface = InterFace(screen)
    # H_airplane的对象
    airplane = H_airplane(screen)
    # esc对象
    esc = Esc(screen)
    # 设置游戏名称
    pygame.display.set_caption(settings.game_name)
    # 设置游戏开始界面的背景
    bg_game = pygame.image.load(settings.screen_image_start).convert_alpha()
    # 设置游戏设置界面
    bg_set = pygame.image.load(settings.screen_set).convert_alpha()
    # 设置游戏时的背景
    bg_play = pygame.image.load(settings.screen_play).convert_alpha()
    # 设置游戏图标
    game_icon = pygame.image.load(settings.game_icon).convert_alpha()
    pygame.display.set_icon(game_icon)
    # 设置游戏帧数
    clock = pygame.time.Clock()
    # g_image对象
    gimage = After.g_image(screen)
    # 玩家子普通弹精灵组
    bullet1 = pygame.sprite.Group()
    # 玩家冲击波精灵组
    wave = pygame.sprite.Group()
    # 玩家导弹精灵组
    rockets = pygame.sprite.Group()
    # 补给总数
    SL = pygame.sprite.Group()
    # 敌人总数
    armys = pygame.sprite.Group()
    # 定时发送补给
    TIMESUPPLY = pygame.USEREVENT
    pygame.time.set_timer(TIMESUPPLY, 1000 * 10)
    # 补给列表
    supply_list = [Supply.surply(), Supply.Lsurply()]
    # 创造敌人
    gf.create_army(settings, armys)
    # 游戏事件
    while True:
        active = pygame.display.get_active()
        # 游戏开始界面
        if settings.interface and not settings.enter_set:
            gf.start_event_check(interface, settings, screen, bg_game, bullet1, armys, airplane, wave, rockets, SL,
                                 game_music)
        # 进入游戏设置界面
        if settings.enter_set and settings.enter_set:
            gf.set_even_check(screen, bg_set, settings, game_setting, game_music)

        # 游戏场景
        if settings.enter_play:
            # 事件处理
            gf.running_even_check(settings, airplane, bullet1, Invincible, TIMESUPPLY, SL, supply_list, wave, rockets,
                                  game_music)
            if active:
                # 绘制屏幕背景
                gf.blit_screen(screen, settings, bg_play)
                # 游戏内玩家属性的显示
                gf.show(rfont, settings, screen, bullet1, armys)
                # 如果玩家无敌就显示玩家无敌的时间
                if settings.invincible:
                    rfont.show_time(screen, settings)
                #     如果空投精灵组里的精灵的数量为0则不发放空投
                if len(SL) == 0:
                    settings.drop = False
                else:
                    settings.drop = True
                # 绘制玩家飞机
                gf.air_blit(airplane, settings, armys, bullet1, game_music, SL, wave, rockets)
                # 绘制子弹
                gf.bilt_bullet(screen, bullet1, settings, wave, rockets, game_music)
                # 绘制敌人
                gf.blit_midenemty(armys, screen, settings, bullet1, game_music, wave, rockets,airplane)
                if settings.drop:
                    gf.tou(screen, SL)
                # 延迟每帧减一
                settings.delay -= 1
                if settings.delay == 0:
                    settings.delay = 60
                # 使屏幕一直显示图片
                pygame.display.update()
        # 玩家按下esc按键
        if settings.esc:
            # 绘制游戏返回界面
            gf.esc_even_check(screen, bg_play, esc, settings, bullet1, airplane, armys, wave, rockets, SL, game_music)
        # 游戏胜利界面
        if settings.cont_v:
            gf.cont(armys, airplane, settings, gimage, bullet1, screen, bg_game, rfont,
                    wave, rockets, SL, game_music)
        # 游戏失败界面
        if settings.lose_l:
            gf.regame(armys, airplane, settings, gimage, bullet1, screen, bg_game, rfont,
                      wave, rockets, SL, game_music)
        #     游戏帧数
        clock.tick(settings.FPS)


# 运行程序
if __name__ == "__main__":
    run_game()
