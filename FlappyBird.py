# -*- coding:utf-8 -*-
import sys
import pygame
import random


class Bird(object):
    """定义一个鸟类"""
    def __init__(self):
        """定义初始化方法"""
        self.birdRect = pygame.Rect(65, 50, 50, 50)    # 鸟的矩形
        self.birdStatus = [pygame.image.load('assets/bird.png'),
                           pygame.image.load('assets/bird_up.png'),
                           pygame.image.load('assets/bird_down.png')]
        self.status = 0         # 默认飞行状态
        self.birdX = 120        # 鸟所在的X轴坐标
        self.birdY = 350        # 鸟所在的Y轴坐标，即上下飞行的高度
        self.jump = False       # 默认小鸟会自动降落
        self.jumpSpeed = 10     # 跳跃高度
        self.gravity = 5        # 重力
        self.dead = False       # 默认小鸟生命状态为活着

    def birdUpdate(self):
        if self.jump:
            # 小鸟跳跃
            print(self.jumpSpeed)
            self.jumpSpeed -= 1                   # 速度递减，上升越来越慢
            self.birdY -= self.jumpSpeed          # 小鸟的Y坐标减小，小鸟上升
        else:
            # 小鸟坠落
            self.gravity += 0.2                   # 重力递增，下降越来越快
            self.birdY += self.gravity            # 小鸟的Y坐标增加，小鸟下降
        self.birdRect[1] = self.birdY             # 更改Y轴位置


class Pipeline(object):
    """定义一个管道类"""
    def __init__(self):
        """定义初始化方法"""
        pass

    def updatePipeline(self):
        """水平移动"""
        pass


def createMap():
    """定义创建地图的方法"""
    screen.fill((255, 255, 255))          # 填充颜色
    screen.blit(background, (0, 0))       # 填入到背景
    # 显示小鸟
    if bird.dead:                         # 撞管道状态
        bird.status = 2
    elif bird.jump:                       # 起飞状态
        bird.status = 1
    screen.blit(bird.birdStatus[bird.status], (bird.birdX, bird.birdY))    # 设置小鸟的坐标
    bird.birdUpdate()                     # 小鸟异动

    pygame.display.update()               # 更新显示


if __name__ == '__main__':
    """主程序"""
    pygame.init()                              # 初始化pygame
    size = width, height = 400, 600            # 设置窗口
    screen = pygame.display.set_mode(size)     # 显示窗口
    clock = pygame.time.Clock()                # 设置时钟
    pipeline = Pipeline()                      # 实例化管道类
    bird = Bird()                              # 实例化鸟类
    while True:
        clock.tick(60)                         # 每秒执行60次
        # 轮询事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                  # 退出
                sys.exit()
            if(event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not bird.dead:
                bird.jump = True        # 跳跃
                bird.gravity = 5        # 重力
                bird.jumpSpeed = 10     # 跳跃速度
        background = pygame.image.load('assets/background.jpg')  # 加载背景图片
        createMap()                           # 创建地图
