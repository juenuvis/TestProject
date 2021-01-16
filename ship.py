import pygame
class Ship():
    def __init__(self, screen):
        # """初始化飞船，并设置起初试位置"""
        self.screen = screen

        # """加载飞船图像，并获取其外接矩形“”“
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect() 
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        # 在飞船的属性center 中存储小数值
        self.center = float(self.rect.centerx)
    def update(self):
        # 根据移动标记调整飞船位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factot
        self.rect.centerx = self.center
        # 限制飞船移动范围
    def blitme(self):
        # in new position draw boat
        self.screen.blit(self.image, self.rect)
