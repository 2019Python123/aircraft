# 引入模块
import sys
import pygame
from pygame.locals import *
import Bullet
import math
import random
import Enemy


# 引入自定义模块,并且可以直接用其里面定义的类和方法,比如：实例化一个对象OB=class_name(),\
# 而不这样引用则需：OB=Modul_name.class_name()


# 绘制游戏开始界面
def blit_screen_star(settings, interface):
    interface.blit_enter()
    interface.blit_exit()
    interface.blit_game_set()

    # 如果玩家点击’退出游戏按钮‘则退出游戏
    if not settings.running:
        pygame.quit()
        sys.exit()
    #  刷新屏幕将绘制的图像一直显示
    pygame.display.update()


#     绘制屏幕
def blit_screen(screen, settings, bg_game):
    # 使屏幕变成银白色（255,255,255）是rgb颜色用元祖表示
    screen.fill(settings.bg_color)
    # 绘制游戏背景图,进入游戏图像，退出游戏图像
    screen.blit(bg_game, (0, 0))


# 移动飞机
def move(airplane):
    # 如果飞机的下移状态为True则飞机的中心y坐标值增加3
    if airplane.air_settings.airplane_down_move:
        airplane.air_settings.airplane_movey += airplane.speed

    #  如果飞机的上移状态为True则飞机的中心y坐标值减小3
    if airplane.air_settings.airplane_up_move:
        airplane.air_settings.airplane_movey -= airplane.speed

    #  如果飞机的左移状态为True则飞机的中心x坐标值增加3
    if airplane.air_settings.airplane_left_move:
        airplane.air_settings.airplane_movex -= airplane.speed

    # 如果飞机的右移状态为True则飞机的中心x坐标值减小3
    if airplane.air_settings.airplane_right_move:
        airplane.air_settings.airplane_movex += airplane.speed


# 处理飞机的键盘事件
def key_check_air(airplane, settings, bullet1, wave, rockets, game_music):
    # 如果是按下键盘
    if settings.even.type == KEYDOWN:
        # 飞机是运动的状态
        settings.moving = True
        # 如果是向下建
        if settings.even.key == K_DOWN or settings.even.key == K_s:
            # 飞机向下移动状态为真
            airplane.air_settings.airplane_down_move = True
            game_music.click.play()
        elif settings.even.key == K_UP or settings.even.key == K_w:
            # 飞机向上移动状态为真
            airplane.air_settings.airplane_up_move = True
            game_music.click.play()
        elif settings.even.key == K_LEFT or settings.even.key == K_a:
            # 飞机向左移动状态为真
            airplane.air_settings.airplane_left_move = True
            game_music.click.play()
        elif settings.even.key == K_RIGHT or settings.even.key == K_d:
            # 飞机向右移动状态为真
            airplane.air_settings.airplane_right_move = True
            game_music.click.play()
        #     如果玩家按下ESC建就进入ESC界面
        elif settings.even.key == K_ESCAPE:
            settings.enter_play = False
            game_music.click.play()
            settings.esc = True
        #   按下空格键，q，e，玩家发射子弹
        elif settings.even.key == K_SPACE:
            game_music.click.play()
            bullet1.add(Bullet.bullet(airplane.rect.midtop))
        elif settings.even.key == K_q and settings.use_energy < 100:
            wave.add(Bullet.Wave(airplane.rect.midtop))
            settings.use_energy += 25
            game_music.click.play()
        elif settings.even.key == K_e and settings.daodan_number > 0:
            game_music.click.play()
            rockets.add(Bullet.Rbullet(airplane.rect.midtop))
            settings.daodan_number -= 1
    # 如果是松开键盘
    elif settings.even.type == KEYUP:
        # 飞机处于停滞状态
        settings.moving = False
        if settings.even.key == K_DOWN or settings.even.key == K_s:
            # 飞机向下移动状态为假
            airplane.air_settings.airplane_down_move = False
        if settings.even.key == K_UP or settings.even.key == K_w:
            # 飞机向上移动状态为假
            airplane.air_settings.airplane_up_move = False
        if settings.even.key == K_LEFT or settings.even.key == K_a:
            # 飞机向左移动状态为假
            airplane.air_settings.airplane_left_move = False
        if settings.even.key == K_RIGHT or settings.even.key == K_d:
            # 飞机向右移动状态为假
            airplane.air_settings.airplane_right_move = False
            # 停止发射子弹
        if settings.even.key == K_SPACE:
            settings.rounds = False


#   开始界面的事件处理
def start_event_check(interface, settings, screen, bg_game, bullets, armys, airplane, wave, rockets, SL, game_music):
    for even in pygame.event.get():
        # 如果事件是QUIT，游戏退出
        if even.type == QUIT:
            sys.exit()
        # 处理游戏开始界面的鼠标处理
        if even.type == MOUSEBUTTONDOWN:
            # 如果是鼠标右键
            if even.button == 1:
                # 判断鼠标所在的位置是不是在 ”进入游戏“ 外切矩形坐标内
                if (even.pos[0] > interface.enter_rect.left and even.pos[
                    0] < interface.enter_rect.right) and \
                        (even.pos[1] > interface.enter_rect.top and even.pos[
                            1] < interface.enter_rect.bottom):
                    game_music.click.play()
                    # 在屏幕绘制”进入游戏“的图像
                    interface.blit_enter_click()
                    # 使更新的图片刷新在屏幕上
                    pygame.display.flip()
                    # 延迟时间进行下一个图像绘制
                    settings.interface = False
                    settings.enter_play = True
                    pygame.time.delay(100)
                    # 切换到游戏场景
                    settings.over = True
                    # 如果是从游戏中返回到菜单
                    if settings.game_t_start:
                        # 删除子弹，敌人，将玩家重新放到屏幕下方中心
                        SL.empty()
                        bullets.empty()
                        armys.empty()
                        wave.empty()
                        rockets.empty()
                        airplane.replace()
                        create_army(settings, armys)
                        # if settings.losed and settings.game_t_start:
                        # 玩家复活
                        airplane.active = True
                        # 一些属性改变
                        settings.losed = False
                        settings.an_start = True
                        settings.game_t_start = False
                        settings.air_collide = False
                        # 玩家属性初始化
                        settings.player = 4
                        settings.player_copy = 4
                        settings.life = 400
                        settings.bullet_rect = 300
                        settings.die_count = 0
                        settings.die_count_copy = 0
                        settings.invincible = False
                        settings.use_energy = 0
                        settings.sofar_soreces = 0
                        settings.daodan_number = 3
                # 判断鼠标所在的位置是不是在 ”退出游戏“ 外切矩形坐标内
                if (even.pos[0] > interface.exit_rect.left and even.pos[
                    0] < interface.exit_rect.right) and \
                        (even.pos[1] > interface.exit_rect.top and even.pos[
                            1] < interface.exit_rect.bottom):
                    game_music.click.play()
                    # 在屏幕上绘制”退出游戏“的图像
                    interface.blit_exit_click()
                    #  使更新的图片刷新在屏幕上
                    pygame.display.update()
                    # 延迟时间进行下一个图像绘制
                    pygame.time.delay(100)
                    settings.running = False
                #    如果点击的是游戏设置图标的外切矩形范围则生效点击游戏设置事件
                if (even.pos[0] > interface.game_set_rect.left and even.pos[
                    0] < interface.game_set_rect.right) and \
                        (even.pos[1] > interface.game_set_rect.top and even.pos[
                            1] < interface.game_set_rect.bottom):
                    game_music.click.play()
                    # 绘制游戏设置被点击的图标
                    interface.blit_game_set_click()
                    # 将游戏设置被点击的图标显示到屏幕上
                    pygame.display.update()
                    # 延迟时间进行下一个图像的绘制
                    pygame.time.delay(100)
                    # 进入游戏设置界面
                    settings.enter_set = True
    blit_screen(screen, settings, bg_game)
    blit_screen_star(settings, interface)


# 游戏设置界面
def set_even_check(screen, bg_game, settings, game_setting, game_music):
    for even in pygame.event.get():
        # 如果是QUIT事件则退出游戏
        if even.type == QUIT:
            pygame.quit()
            sys.exit()
        #     鼠标事件
        elif even.type == MOUSEBUTTONDOWN:
            # 按下右键
            if even.button == 1:
                # 控制音乐开关
                if (even.pos[0] > game_setting.oppen_music_rect.left \
                    and even.pos[0] < game_setting.oppen_music_rect.right) \
                        and (even.pos[1] > game_setting.oppen_music_rect.top and even.pos[1] \
                             < game_setting.oppen_music_rect.bottom):
                    game_music.click.play()
                    if settings.change_fp == False:
                        settings.change_fp = True
                        pygame.mixer.music.pause()
                        settings.close_music = True
                    else:
                        settings.change_fp = False
                        pygame.mixer.music.unpause()
                        settings.close_music = False
                # 退出设置界面
                if (game_setting.back_one_rect.left < even.pos[0] < game_setting.back_one_rect.right) \
                        and (even.pos[1] > game_setting.back_two_rect.top and even.pos[
                    1] < game_setting.back_two_rect.bottom):
                    game_music.click.play()
                    game_setting.blit_back_two()
                    settings.interface = True
                    settings.enter_set = False
                    pygame.display.update()
                    pygame.time.delay(100)
    #                 绘制图片和屏幕背景
    game_setting.replace_music()
    screen.fill(settings.bg_color)
    screen.blit(bg_game, (0, 0))
    game_setting.blit_settings()
    if settings.change_fp:
        game_setting.blit_oppen()
    else:
        game_setting.blit_off()
    game_setting.blit_back_one()

    pygame.display.update()


# 设置游戏场景的事件处理
def running_even_check(settings, airplane, bullet1, Invincible, TIMESUPPLY, SL, supply_list, wave, roakets, game_music):
    for even in pygame.event.get():
        # 对settings类里的储存事件赋值（事件）
        settings.even = even
        # 退出游戏
        if even.type == QUIT:
            pygame.quit()
            sys.exit()
        #     如果是无敌事件
        elif even.type == Invincible:
            if (settings.die_count <= settings.life_copy) and (settings.die_count > 0) \
                    and settings.die_count - settings.die_count_copy == 1:
                settings.invincible = True
                settings.die_count_copy += 1
                settings.clock_count += 1
            else:
                settings.clock_count += 1
                if settings.clock_count / 60 > 1:
                    settings.clock_count = 0
                if settings.clock_count // 60:
                    settings.invincible = False
        elif even.type == TIMESUPPLY:
            # 随机在精灵组里添加一个空投精灵
            settings.random_supply = random.randint(0, 1)
            SL.add(supply_list[settings.random_supply])
            for each in SL:
                each.rect.centerx, each.rect.centery = random.randint(0, each.settings.screen_width) \
                    , random.randint(-500, 0)  # 飞机的位置在一定范围内随机出现
            settings.drop = True
        #     如果玩家关闭游戏音乐则音乐停止,负责继续开启
        if settings.close_music:
            pygame.mixer.music.pause()
        elif not settings.close_music:
            pygame.mixer.music.unpause()
        key_check_air(airplane, settings, bullet1, wave, roakets, game_music)


# 处理游戏esc界面
def esc_even_check(screen, bg_image, Esc, settings, bullets, airplane, armys, wave, rockets, SL, game_music):
    for even in pygame.event.get():
        if even.type == QUIT:
            pygame.quit()
            sys.exit()
        #     如果用户点击鼠标左键
        if even.type == MOUSEBUTTONDOWN:
            if even.button == 1:
                # 如果鼠标点击的范围是重新游戏按钮上
                if (Esc.renewG_rect.left < even.pos[0] < Esc.renewG_rect.right) and \
                        (Esc.renewG_rect.top < even.pos[1] < Esc.renewG_rect.bottom):
                    # 播放点击音效
                    game_music.click.play()
                    # 绘制背景
                    screen.blit(Esc.renewG_click, Esc.renewG_click_rect)
                    # 显示图片
                    pygame.display.flip()
                    # 进入游戏，管比该界面
                    settings.enter_play = True
                    settings.esc = False
                    # 删除子弹等玩家属性，敌人，空投将玩家重新放到屏幕下方中心
                    bullets.empty()
                    armys.empty()
                    wave.empty()
                    rockets.empty()
                    airplane.replace()
                    SL.empty()
                    create_army(settings, armys)
                    # 玩家复活
                    airplane.active = True
                    settings.re = True
                    settings.an_regame = True
                    if settings.an_regame:
                        settings.regame = False
                        settings.losed = False
                        settings.air_collide = False
                    #     初始化玩家属性
                    settings.player = 4
                    settings.player_copy = 4
                    settings.life = 400
                    settings.bullet_rect = 300
                    settings.die_count = 0
                    settings.die_count_copy = 0
                    settings.invincible = False
                    settings.soreces = 0
                    settings.daodan_number = 3
                    settings.use_energy = 0
                    settings.sofar_soreces = 0
                    pygame.time.delay(200)
                #     如果是点击菜单按钮上
                if (Esc.remenu_rect.left < even.pos[0] < Esc.remenu_rect.right) and \
                        (Esc.remenu_rect.top < even.pos[1] < Esc.remenu_rect.bottom):
                    # 播放点击音效
                    game_music.click.play()
                    # 绘制屏幕背景
                    screen.blit(Esc.remenu_click, Esc.remenu_click_rect)
                    # 显示图片
                    pygame.display.flip()
                    # 改变条件
                    settings.esc = False
                    settings.interface = True
                    settings.enter_set = False
                    settings.game_t_start = True
                    pygame.time.delay(200)
                #    如果是按下继续游戏按钮
                if (Esc.cont_rect.left < even.pos[0] < Esc.cont_rect.right) and \
                        (Esc.cont_rect.top < even.pos[1] < Esc.cont_rect.bottom) and not settings.losed:  # 是否失败
                    # 播放点击音效
                    game_music.click.play()
                    # 绘制背景
                    screen.blit(Esc.cont_click, Esc.cont_click_rect)
                    # 显示背景
                    pygame.display.flip()
                    settings.enter_play = True
                    settings.esc = False
                    pygame.time.delay(100)
    # 绘制重新游戏按钮和菜单按钮
    screen.blit(bg_image, (0, 0))
    screen.blit(Esc.remenu, Esc.remenu_rect)
    screen.blit(Esc.renewG, Esc.renewG_rect)
    screen.blit(Esc.cont, Esc.cont_rect)
    pygame.display.update()


# 绘制子弹
def bilt_bullet(screen, bullet1, settings, wave, rockets, game_music):
    # 玩家子弹移动
    bullet1.update()
    wave.update()
    rockets.update()
    # 检测玩家子弹是否出界出界就移除该子弹
    for each in bullet1:
        if each.rect.top <= 0 or settings.enemy_collide:
            bullet1.remove(each)
            settings.enemy_collide = False
    for each in wave:
        if each.rect.top <= 0 or settings.enemy_collide:
            bullet1.remove(each)
            settings.enemy_collide = False
    for each in rockets:
        if each.rect.top <= 0 or settings.enemy_collide:
            bullet1.remove(each)
            settings.enemy_collide = False
    #         绘制子弹在屏幕上
    bullet1.draw(screen)
    wave.draw(screen)
    rockets.draw(screen)
    # 如果敌人大于22个就开启无限冲击波模式
    if settings.use_energy == 100 and settings.total_enemy > 20:
        for i in range(4):
            settings.use_energy -= 25


# 绘制敌人
def blit_midenemty(armys, screen, settings, bullets, game_music, wave, rockets,airplane):
    for each in armys:
        # 如果是重玩
        if settings.re or settings.just_play:
            each.rect.centerx, each.rect.centery = random.randint(0, each.settings.screen_width) \
                , random.randint(-1000, 0)  # 飞机的位置在一定范围内随机出现
            settings.just_play = False
        # 检测敌人碰撞
        armys_hit(each, bullets, settings, wave, rockets, armys,airplane)
        # 如果敌人还活着，敌人正常行动
        if each.active:
            each.update()
            each.draw(screen)
            each.blit(screen)
            pygame.mixer.music.unpause()
        #     负责绘制敌人爆炸场景
        else:
            each.placeboom()
            each.blit_boom(screen)
            armys.remove(each)
            game_music.boom_music.play()
    #         所有敌人没了进入游戏胜利界面
    if len(armys) == 0:
        settings.play_v = True
        settings.cont_v = True
        settings.enter_play = False
        pygame.mixer.music.pause()
    #     播放胜利音效
    if settings.play_v:
        game_music.vectory_music.play()
        settings.play_v = False
    settings.re = False


def armys_hit(each, bullets, settings, wave, rockets, armys,airplane):
    # 检测普通子弹
    distance = pygame.sprite.spritecollide(each, bullets, False, pygame.sprite.collide_mask)
    # 检测冲击波
    distance_w = pygame.sprite.spritecollide(each, wave, False, pygame.sprite.collide_mask)
    # 检测导弹
    distance_r = pygame.sprite.spritecollide(each, rockets, False, pygame.sprite.collide_mask)
    if distance:
        # 敌人扣血
        each.life -= settings.com_attack
        if each.life < 0:
            each.life = 0
        # 玩家加分
        if each.life <= 0:
            each.active = False
            settings.soreces += each.sorces*airplane.leavel//4
            settings.sofar_soreces += each.sorces*airplane.leavel//4
        settings.enemy_collide = True
    if distance_w:
        # 敌人扣血
        each.life -= settings.wave_attack
        if each.life < 0:
            each.life = 0
        # 玩家加分
        if each.life <= 0:
            each.active = False
            settings.soreces += each.sorces*(airplane.leavel//100+1)
            settings.sofar_soreces += each.sorces*(airplane.leavel*0.3+1)
        settings.enemy_collide = True
    if distance_r:
        # 敌人扣血
        each.life -= settings.rocket_attack
        if each.life < 0:
            each.life = 0
        # 玩家加分
        if each.life <= 0:
            each.active = False
            settings.soreces += each.sorces*airplane.leavel//4
            settings.sofar_soreces += each.sorces*airplane.leavel//4
        settings.enemy_collide = True
        for each1 in bullets:
            # 检测普通子弹是否击中敌人
            distance_bu = pygame.sprite.collide_mask(each1, each)
            if distance_bu:
                bullets.remove(each)
    for each in wave:
        if each.rect.top <= 0:
            wave.remove(each)
    for each in rockets:
        if each.rect.top <= 0:
            wave.remove(each)


# 检测飞机是否出了屏幕，如果出了屏幕就不能向出屏幕的那个方向移动
def judge_air(airplane, settings):
    if airplane.rect.centerx < 0:
        airplane.air_settings.airplane_left_move = False
    elif airplane.rect.centerx > settings.screen_width:
        airplane.air_settings.airplane_right_move = False
    if airplane.rect.centery <= 0:
        airplane.air_settings.airplane_up_move = False
    elif airplane.rect.centery >= settings.screen_height:
        airplane.air_settings.airplane_down_move = False


# 创建敌人精灵组
def create_army(settings, armys):
    # 随机敌人数量
    settings.p_enemtyNumber = random.randint(5, 10)
    settings.m_enemtyNumber = random.randint(5, 10)
    settings.boos_number = random.randint(3, 5)
    # 如果是胜利了准备进入下一次游戏
    if settings.vic:
        # 敌人数量随机增加
        settings.p_enemtyNumber += settings.add_army
        settings.m_enemtyNumber += settings.add_army
        settings.boos_number += settings.add_army
        settings.vc = False
    # 敌人总数
    settings.total_enemy = settings.p_enemtyNumber + settings.m_enemtyNumber + settings.boos_number
    # 将每个敌人类添加到敌人精灵组里
    for index in range(settings.p_enemtyNumber):
        armys.add(Enemy.Enemty())
    for index in range(settings.m_enemtyNumber):
        armys.add(Enemy.MEnemty())
    for index in range(settings.boos_number):
        armys.add(Enemy.BEnemty())


# 检测玩家的碰撞
def hit(airplane, armys, bullets, settings, game_music, SL):
    # 玩家与敌人碰撞
    distance = pygame.sprite.spritecollide(airplane, armys, False, pygame.sprite.collide_mask)
    if distance and not settings.air_collide:
        if not settings.delay % 2:
            airplane.placeboom()
            airplane.blit_boom()
        airplane.active = False
        settings.air_collide = True
        settings.play_l = True
        bullets.empty()
        settings.player -= 1
        settings.losed = True
        settings.life -= 100
        settings.die_count += 1
        game_music.boom_music.play()
    #     玩家与空投碰撞
    for each in SL:
        distance_one = pygame.sprite.collide_mask(airplane, each)
        if distance_one:
            if each.name == 'R' and settings.daodan_number <= 6:
                settings.daodan_number += 1

            else:
                if settings.player < 6:
                    settings.player += 1
                    settings.player_copy += 1
            SL.remove(each)


# 绘制飞机
def air_blit(airplane, settings, armys, bullets, game_music, SL, wave, rockets):
    # 显示玩家等级
    airplane.show_level()
    # 如果玩家还活着
    if airplane.active:
        # 检测飞机是否出了屏幕，如果出了屏幕就不能向出屏幕的那个方向移动
        judge_air(airplane, settings)
        # 移动飞机
        move(airplane)
        # 放置飞机
        airplane.place_aircraft()
        airplane.blit_aircraft(settings)
        # 如果玩家没有从设置中关闭了音乐
        if not settings.close_music:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
    #         如果玩家不处于无敌状态
    if not settings.invincible:
        # 检测玩家碰撞
        hit(airplane, armys, bullets, settings, game_music, SL)
    # 如果玩家命玩完了
    if settings.player == 0:
        if not airplane.active:
            # 删除所有的精灵组敌人等等
            bullets.empty()
            wave.empty()
            rockets.empty()
            # 恢复初始化
            settings.use_energy = 0
            settings.daodan_number = 3
            # 关闭音乐
            pygame.mixer.music.pause()
            # 控制进入失败界面的条改变
            settings.lose_l = True
            settings.enter_play = False
        #     如果玩家按重新游戏的按钮或者玩家失败了，并且玩家死了（嘿嘿！，我也懵了”狗头“）
        if (settings.regame or settings.losed) and not airplane.active:
            if settings.an_regame or settings.an_start:
                settings.regame = False
        # 如果玩家失败了
        if settings.play_l:
            # 播放失败音效
            game_music.lose_music.play()
            settings.play_l = False
    #         如果玩家的copy生命值和生命值不相等
    if settings.player_copy != settings.player:
        # 重新放置玩家飞机
        airplane.replace()
        # 玩家复活
        airplane.active = True
        # 玩家没有碰撞
        settings.air_collide = False
        # copy生命值+1
        settings.player_copy -= 1


# 成果界面事件处理
def cont(armys, airplane, settings, gimage, bullets, screen, bg_game, rfont, wave, rockets, SL, game_music):
    # 放置图片位置，绘制屏幕背景
    gimage.update_cont()
    screen.blit(bg_game, (0, 0))
    gimage.update_v()
    # 绘制图片
    gimage.draw_v()
    # 显示玩家属性
    rfont.show_grades_one(screen, settings)
    rfont.show_read(screen, settings)
    rfont.rank_copy(settings, screen)
    rfont.rank_font(screen)
    # 表示存储玩家分数的文件读了一次
    settings.readed = True
    settings.vc = True
    for even in pygame.event.get():
        # 如果事件=QUIT事件就退出游戏
        if even.type == QUIT:
            pygame.quit()
            sys.exit()
        #     如果是用右键鼠标建点击重新游戏的按钮
        if even.type == MOUSEBUTTONDOWN:
            if even.button == 1:
                if (gimage.cont_rect.left < even.pos[0] < gimage.cont_rect.right) and \
                        (gimage.cont_rect.top < even.pos[1] < gimage.cont_rect.bottom):
                    game_music.click.play()
                    gimage.draw_cont_c()
                    pygame.display.flip()
                    settings.cont_v = False
                    # 删除子弹等玩家属性，敌人，空投。将玩家重新放到屏幕下方中心
                    bullets.empty()
                    armys.empty()
                    wave.empty()
                    rockets.empty()
                    SL.empty()
                    airplane.replace()
                    # 创造敌人
                    create_army(settings, armys)
                    # 玩家复活
                    airplane.active = True
                    # 控制游戏的一些条件改变
                    settings.re = True
                    settings.an_regame = True
                    alert_move(airplane)
                    # 如果按下了重新游戏的按钮
                    if settings.an_regame:
                        settings.regame = False
                        settings.losed = False
                        settings.air_collide = False
                    # 进入游戏的条件改变
                    settings.enter_play = True
                    # 玩家属性初始化
                    settings.life = 400
                    settings.bullet_rect = 300
                    settings.die_count = 0
                    settings.die_count_copy = 0
                    settings.invincible = False
                    settings.use_energy = 0
                    settings.sofar_soreces = 0
                    pygame.time.delay(200)
    # 绘制游戏背景图,进入游戏图像，退出游戏图像

    gimage.draw_cont()
    pygame.display.update()


# 失败游戏界面的事件处理
def regame(armys, airplane, settings, gimage, bullets, screen, bg_game, rfont, wave, rockets, SL, game_music):
    # 放置图片位置和背景
    gimage.update_reg()
    screen.blit(bg_game, (0, 0))
    gimage.update_l()
    # 绘制背景
    gimage.draw_l()
    # 绘制玩家的分数情况和段位情况
    rfont.show_grades_one(screen, settings)
    rfont.show_read(screen, settings)
    rfont.rank_copy(settings, screen)
    rfont.rank_font(screen)
    # 表示存储分数文件被读过一次
    settings.readed = True
    # 音乐暂停
    pygame.mixer.music.pause()
    # 事件循环处理
    for even in pygame.event.get():
        # 如果事件=QUIT事件就退出游戏
        if even.type == QUIT:
            pygame.quit()
            sys.exit()
        #     如果是用右键鼠标建点击重新游戏的按钮
        elif even.type == MOUSEBUTTONDOWN:
            if even.button == 1:
                if (gimage.reg_rect.left < even.pos[0] < gimage.reg_rect.right) and \
                        (gimage.reg_rect.top < even.pos[1] < gimage.reg_rect.bottom):
                    # 播放点击音效
                    game_music.click.play()
                    # 绘制点击后的图片
                    gimage.draw_reg_click()
                    # 将图片显示在屏幕
                    pygame.display.flip()
                    # 进入失败界面的条件改变
                    settings.lose_l = False
                    # 删除玩家子弹等属性，敌人，空投，清零，将玩家重新放到屏幕下方中心
                    bullets.empty()
                    armys.empty()
                    wave.empty()
                    SL.empty()
                    rockets.empty()
                    airplane.replace()
                    create_army(settings, armys)
                    # 玩家复活
                    airplane.active = True
                    # 绘制玩家飞机
                    airplane.blit_aircraft(settings)
                    # 一些控制游戏的条件改变
                    settings.re = True
                    settings.an_regame = True
                    alert_move(airplane)
                    settings.losed = False
                    settings.air_collide = False
                    settings.enter_play = True
                    # 玩家属性初始化
                    settings.player = 4
                    settings.player_copy = 4
                    settings.life = 400
                    settings.bullet_rect = 300
                    settings.die_count = 0
                    settings.die_count_copy = 0
                    settings.invincible = False
                    settings.use_energy = 0
                    settings.daodan_number = 3
                    settings.sofar_soreces = 0
                    pygame.time.delay(200)
    # 绘制游戏背景图,进入游戏图像，退出游戏图像

    gimage.draw_reg()
    pygame.display.update()


# 改变飞机移动方向状态
def alert_move(airplane):
    airplane.air_settings.airplane_down_move = False  # 向下移动状态
    airplane.air_settings.airplane_up_move = False  # 向上移动状态
    airplane.air_settings.airplane_left_move = False  # 向左移动状态
    airplane.air_settings.airplane_right_move = False  # 向右移动状态


# 投放空投
def tou(screen, SL):
    for each in SL:
        if each.rect.midtop[1] > each.settings.screen_height:
            SL.remove(each)
        else:
            each.update()
            each.draw(screen)


# 玩家属性的显示
def show(rfont, settings, screen, bullet1, armys):
    # 显示玩家生命值的矩形图
    rfont.rect_life(screen, settings)
    # 玩家子弹数量的矩形图
    rfont.bullet_b(screen, settings, bullet1)
    # 玩家当局分数的显示
    rfont.show_grades(screen, settings)
    # 敌人数量的显示
    rfont.show_enemy(screen, armys)
    # 玩家生命图标的显示
    rfont.show_lifeicon(screen, settings)
    # 玩家冲击波的能量值的显示
    rfont.wave_rect(screen, settings)
    # 玩家火箭数量和图标的显示
    rfont.show_rocket(screen, settings)
    # 玩家段位的显示
    rfont.rank(settings, screen)
