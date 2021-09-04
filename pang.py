# -*- coding:utf-8 -*-
import sys        # 导入sys模块
import pygame     # 导入pygame模块

# 初始化pygame
pygame.init()
# 设置窗口并显示
size = screenWidth, screenHeight = 800, 600
screen = pygame.display.set_mode(size)
# 设置背景色
color = (255, 255, 255)
screen.fill(color)
# 地平线偏移
landlineOffset = 37
# 默认的速度
speed = 10
# 加载并填入背景
background = pygame.image.load('assets/background.jpg')


class Pang(object):
    def __init__(self):
        self.downSpeed = speed
        self.rightSpeed = speed
        self.isUp = None
        self.isRight = None
        # 初始化图片
        self.images = [
            [pygame.image.load('assets/pan-right-walk.png'), pygame.image.load('assets/pan-right-stand.png')],
            [pygame.image.load('assets/pan-left-walk.png'), pygame.image.load('assets/pan-left-stand.png')]
        ]
        self.panDirectIndex = 0
        self.panActIndex = 0
        self.pan = None
        self.rect = None
        self.imageRight = True
        # 初始化图片尺寸
        self.panWidth = 65
        self.panHeight = 85
        # 初始化图片位置
        for self.pan in self.images[self.panDirectIndex]:
            self.rect = self.pan.get_rect()
            self.rect = self.rect.move((0, screenHeight - self.panHeight - landlineOffset))

    def draw(self):
        if self.isRight is not None:
            if self.panActIndex == 0:
                self.panActIndex = 1
            else:
                self.panActIndex = 0
            if self.isRight:
                self.panDirectIndex = 0
            else:
                self.panDirectIndex = 1
        # 重新画企鹅
        screen.blit(self.images[self.panDirectIndex][self.panActIndex], self.rect)

    def stop(self):
        self.downSpeed = speed
        self.rightSpeed = speed
        self.isUp = None
        self.isRight = None

    def changeSize(self, factor):
        width = self.images[0][0].get_width()
        height = self.images[0][0].get_height()
        for index0 in range(len(self.images)):
            for index1 in range(len(self.images[index0])):
                self.images[index0][index1] = pygame.transform.scale(self.images[index0][index1],
                                                           (int(width * factor), int(height * factor)))


    def move(self):
        # 处理垂直位置
        if self.isUp:
            if self.rect.top < 0:
                # print('升到顶了，准备往下落', self.rect.top)
                if self.downSpeed > 0:
                    self.downSpeed = -1
            # 上升和下降都是这块，取决于self.speed是否大于0
            self.rect = self.rect.move([0, -self.downSpeed])
            # 越升越慢，越落越快
            self.downSpeed -= 1
            # 落到底了，停止下落，修正位置
            if self.rect.bottom > screenHeight - landlineOffset:
                # print('一脚踩进了土里', self.rect.bottom)
                self.rect = self.rect.move([0, -(landlineOffset - (screenHeight - self.rect.bottom))])
                # print('把脚从土里拔出来了', self.rect.bottom)
                # 停止下落
                self.isUp = None

        # 处理水平位置
        if self.isRight is not None:
            if self.isRight:
                if self.rect.right <= screenWidth:
                    self.rect = self.rect.move([self.rightSpeed, 0])
                else:
                    pass
                    # print("已经到最右边了！")
            else:
                if self.rect.left >= 0:
                    self.rect = self.rect.move([-self.rightSpeed, 0])
                else:
                    pass
                    # print("已经到最左边了！")
            self.rightSpeed -= 1
            if self.rightSpeed <= 0:
                self.isRight = None


class Brick(object):
    def __init__(self, left, top, width, height):
        self.rect = pygame.draw.rect(screen, pygame.color.Color('#000000'), [left, top, width, height])
        self.image = pygame.image.load('assets/brick.png')
        screen.blit(self.image, self.rect, (0, 0, width, height))


pang = Pang()
# 设置时钟
clock = pygame.time.Clock()
# 执行死循环，确保窗口一直显示
while True:
    clock.tick(30)
    # 检查事件
    for event in pygame.event.get():
        # 如果单击关闭窗口，则退出
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or pygame.K_a == event.key:
                pang.rightSpeed = speed
                pang.isRight = False
            if event.key == pygame.K_RIGHT or pygame.K_d == event.key:
                pang.rightSpeed = speed
                pang.isRight = True
            if event.key == pygame.K_UP or pygame.K_w == event.key:
                pang.downSpeed = speed
                pang.isUp = True
            # if pygame.K_z == event.key:
            #    pang.changeSize(0.9)
            # if pygame.K_x == event.key:
            #    pang.changeSize(1.1)
    pang.move()
    # 重新画背景，避免原来的图片遗留
    screen.blit(background, (0, 0))
    # 重新画企鹅
    pang.draw()
    Brick(200, screenHeight - landlineOffset - 100, 50, 100)
    Brick(600, screenHeight - landlineOffset - 300, 80, 300)
    Brick(200, 0, 60, 100)
    # Brick(500, 100, 60, 100)
    # 更新全部显示
    pygame.display.flip()
