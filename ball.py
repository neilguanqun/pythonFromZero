# -*- coding:utf-8 -*-
import sys        # 导入sys模块
import pygame     # 导入pygame模块

pygame.init()                           # 初始化pygame
size = width, height = 640, 480         # 设置窗口
screen = pygame.display.set_mode(size)  # 显示窗口
color = (255, 255, 255)                 # 设置颜色

ball = pygame.image.load('assets/ball.jpg')    # 加载图片
ballrect = ball.get_rect()              # 获取矩形区域

speed = [5, 5]                          # 设置异动的X轴、Y轴距离
clock = pygame.time.Clock()             # 设置时钟
# 执行死循环，确保窗口一直显示
while True:
    clock.tick(60)                      # 每秒执行60次
    # 检查事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('我要退出啦~~')
            pygame.quit()               # 如果单击关闭窗口，则退出
            sys.exit()                  # 退出pygame
        if event.type == pygame.KEYDOWN:
            print('我要退出啦啦啦~~')
            pygame.quit()               # 如果单击关闭窗口，则退出
            sys.exit()                  # 退出pygame

    ballrect = ballrect.move(speed)     # 移动小球
    # 碰到左右边缘
    if ballrect.left < 0 or ballrect.right > width:
        print('ballrect.left=', ballrect.left)
        print('ballrect.right=', ballrect.right)
        print('左右边缘：', speed)
        speed[0] = -speed[0]
        print('左右边缘调向：', speed)
    # 碰到上下边缘
    if ballrect.top < 0 or ballrect.bottom > height:
        print('ballrect.top=', ballrect.top)
        print('ballrect.bottom=', ballrect.bottom)
        print('上下边缘：', speed)
        speed[1] = -speed[1]
        print('上下边缘调向：', speed)

    screen.fill(color)            # 填充颜色
    screen.blit(ball, ballrect)   # 将图片画到窗口上
    pygame.display.flip()         # 更新全部显示
