'''
储存所有的游戏属性
'''

import random


class Settings():
    # 初始化函数（构造函数）
    def __init__(self):
        # 设置屏幕属性宽度，高度，游戏图标，背景图片,游戏名称,背景颜色
        self.screen_width = 1300
        self.screen_height = 750
        self.size = self.screen_width, self.screen_height
        self.game_icon = "GAME_IMAGE\\PaperPlane.png"
        self.screen_image_start = "GAME_IMAGE\\bgb.jpg"
        self.screen_set = "GAME_IMAGE\\bg6.jpg"
        self.screen_play = "GAME_IMAGE\\bg8.jpg"
        self.game_name = "Star_Wars"
        self.bg_color = (255, 255, 255)

        # 设置游戏开始界面属性，进入游戏的图像（普通和被点击的图像），退出游戏的图像（普通和被点击的图像）
        self.enter_image = "GAME_IMAGE\\enter_game_one.tga"
        self.enter_image_click = "GAME_IMAGE\\enter_game_two.tga"
        self.exit_image = "GAME_IMAGE\\exit_game_one.tga"
        self.exit_image_click = "GAME_IMAGE\\exit_game_two.tga"

        # 设置失败和胜利时的图片
        self.lose = "GAME_IMAGE\\shibai.png"
        self.victory = "GAME_IMAGE\\victory.png"

        # 设置玩家飞机的图片
        self.aircraft_image = "GAME_IMAGE\\LXPlane.png"
        # 爆炸的图片
        self.booms = ["GAME_IMAGE\\one.png", "GAME_IMAGE\\two.png", "GAME_IMAGE\\three.png", "GAME_IMAGE\\four.png", \
                      "GAME_IMAGE\\five.png", "GAME_IMAGE\\six.png"]
        # 飞机移动的距离
        self.airplane_movex = 0
        self.airplane_movey = 0
        # 飞机移动方向的状态
        self.airplane_left_move = False
        self.airplane_right_move = False
        self.airplane_down_move = False
        self.airplane_up_move = False

        self.life_icon = "GAME_IMAGE\\PaperPlane_01.png"  # 加载玩家生命图标
        self.daodan_icon = "GAME_IMAGE\\daodan.jpg"  # 导弹的图标
        self.bullet = "GAME_IMAGE\\bullet1.png"  # 玩家普通子弹子弹
        self.wave = "GAME_IMAGE\\impact.png"  # 冲击波
        self.rocket = "GAME_IMAGE\\daod.png"  # 导弹
        self.ranks_image = ["GAME_IMAGE\\qt.png", "GAME_IMAGE\\by.png", "GAME_IMAGE\\hj.png", "GAME_IMAGE\\xy.png" \
            , "GAME_IMAGE\\zs.png"]  # 段位图标
        self.uplevel = "GAME_IMAGE\\uplevel.tga"  # 玩家升级标志
        self.life = 400  # 玩家生命值
        self.player = 4  # 玩家命的输量
        self.player_copy = 4
        self.com_attack = 100  # 攻击值
        self.wave_attack = 60
        self.rocket_attack = 1000

        # 设置游戏中背景音乐
        self.music = "Py_game_music\\bgm3.wav"
        self.boom_music = "Py_game_music\\boom.wav"  # 爆炸音效
        self.shot_rocket_music = "Py_game_music\\rocket.wav"  # 发射导弹音效
        self.victory_music = "Py_game_music\\victory.wav"  # 胜利时的音乐
        self.play_music = "Py_game_music\\bgm.wav"  # 背景音乐
        self.laugh_music = "Py_game_music\\laugh.wav"  # 失败时的音乐
        self.clcik_music = "Py_game_music\\click.wav"  # 点击声音
        self.b_shoot = "Py_game_music\\rshoot.wav"  # 子弹连射的声音

        # 游戏设置图标
        self.set_game = "GAME_IMAGE\\set2.png"
        self.set_game_click = "GAME_IMAGE\\set3.png"  # 游戏设置被点击的图标
        self.music_control = "GAME_IMAGE\\music1.png"  # 游戏音乐设置
        self.music_off = "GAME_IMAGE\\offmusic.png"  # 音乐的开启按钮
        self.music_on = "GAME_IMAGE\\openmusic.png"  # 音乐的关闭按钮

        self.back = "GAME_IMAGE\\close1.tga"  # 返回按钮普通
        self.back_one = "GAME_IMAGE\\close2.tga"  # 返回按钮高亮

        # 设置重玩图标
        self.renew = "GAME_IMAGE\\returng1.png"
        self.renew_click = "GAME_IMAGE\\returng2.png"  # 被按下的重玩图标
        self.back_menu = "GAME_IMAGE\\menu1.png"  # 返回菜单按钮
        self.back_menu_click = "GAME_IMAGE\\menu2.png"  # 被点击的返回菜单按钮
        self.cont = "GAME_IMAGE\\continue1.png"  # 继续游戏按钮
        self.cont_click = "GAME_IMAGE\\continue2.png"  # 被点击的继续游戏按钮

        # 敌人飞机图片,(初级敌人)生命值，攻击值
        self.penemty = "GAME_IMAGE\\penemty.png"
        self.p_enemtyNumber = 0  # 随机敌军数量

        # 敌人飞机图片,（中级）生命值，攻击值
        self.menemty = "GAME_IMAGE\\menemty.png"
        self.m_enemtyNumber = 0

        # 敌人飞机图片,(高级)生命值，攻击值
        self.boos = "GAME_IMAGE\\BOSS.png"
        self.boos_number = 0

        # 供给图片
        self.supply = "GAME_IMAGE\\rock.png"
        self.supply_life = "GAME_IMAGE\\blood.png"
        # 随机补给
        self.random_supply = 0

        # 子弹数量
        self.bullet_number = 149
        # 子弹矩形图的长度
        self.bullet_rect = 300
        # 导弹数量
        self.daodan_number = 3
        # 冲击波能量和使用的能量 一次冲击波花费25能量值
        self.wave_energy = 100
        self.use_energy = 0
        '''
        
        游戏事件和其它属性
        '''
        # 判断是不是退出游戏  False为是:
        self.running = True
        # 判断是不是持续移动飞机
        self.moving = False
        # 判断要不要结束某一界面的循环
        self.over = False
        # 进入游戏设置界面   False表示不进入
        self.enter_set = False
        # 是否切换音乐开关图标  True为是
        self.change_fp = False
        # 储存 游戏事件
        self.even = ""
        # 判断是不是进入游戏 False 不进
        self.enter_play = False
        # 是不是回到游戏界面 True 是
        self.interface = True
        # 游戏帧数
        self.FPS = 60
        # 是否进入esc界面  False 不进入
        self.esc = False
        # 如果玩家死亡点击重新游戏 False 不重新游戏
        self.click_replay = False
        # 玩家是否点击重玩(这个是判断要不要所有敌人和玩家变成初始化状态)
        self.re = False
        # 判断玩家飞机是否撞机 False 没有
        self.air_collide = False
        # 判断敌机是否被子弹攻击 False 没有
        self.enemy_collide = False
        # 是否播放失败和胜利音效
        self.play_l = False
        self.play_v = False
        # 是否从游戏中回到菜单 False 不回
        self.game_t_start = False
        # 是否按继续游戏进入游戏  False 没有按’继续游戏‘按钮
        self.an_regame = False
        # 是否按到继续游戏按钮
        self.continue_click = False
        # 是否因为失败重开游戏（控制飞机是否复原）
        self.regame = False
        # 是否失败
        self.losed = False
        # 是否从开始界面进入游戏(控制游戏界面是否正确)
        self.an_start = False
        # 胜利界面 False 表示不进入该界面
        self.cont_v = False
        # 失败界面  False 表示不进入该界面
        self.lose_l = False
        # 每次胜利后进入下一关敌人就会增加1个
        self.add_army = 1
        # 设置延迟
        self.delay = 60
        # 玩家总分数,当前分数
        self.soreces = 0
        self.sofar_soreces = 0
        # 玩家是否无敌 False 不无敌
        self.invincible = False
        # 玩家死亡的次数
        self.die_count = 0
        self.die_count_copy = 0
        # 时钟的计算
        self.clock_count = 0
        # 玩家生命的复制
        self.life_copy = 4
        # 是不是刚进入游戏
        self.just_play = True
        # 记录敌人数量
        self.total_enemy = 0
        # 投放一个空投
        self.drop = False
        # 是否胜利
        self.vic = False
        # 玩家是否关闭音乐 False 表示不关闭
        self.close_music = False
