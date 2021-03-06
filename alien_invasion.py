import sys
import pygame
from pygame.display import set_caption
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # 初始化游戏,设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #设置背景色
    bg_color = (230, a30, 230)
    # 创建一艘飞船
    ship = Ship(ai_settings,screen)
    # 创建件一个用于存储子弹的编组
    bullet = Group()
    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()


