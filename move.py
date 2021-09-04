# -*- coding:utf-8 -*-
import sys        # 导入sys模块
import pygame     # 导入pygame模块

# 初始化pygame
pygame.init()
# 设置窗口并显示
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
# 设置背景色
color = (255, 255, 255)
screen.fill(color)
# 加载图片
panNum = 0
pan = pygame.image.load('assets/pan-right-walk.png')
pan1 = pygame.image.load('assets/pan-right-stand.png')
# 初始化图片位置
panrect = pan.get_rect()
panrect = panrect.move((0, 477))
# 加载并填入背景
background = pygame.image.load('assets/background.jpg')

# 设置移动的距离
speed = 5
# 设置时钟
clock = pygame.time.Clock()
# 执行死循环，确保窗口一直显示
while True:
    # 检查事件
    for event in pygame.event.get():
        # 如果单击关闭窗口，则退出
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('K_LEFT')
                panrect = panrect.move([-speed, 0])
            if event.key == pygame.K_RIGHT:
                print('K_RIGHT')
                panrect = panrect.move([speed, 0])
            if event.key == pygame.K_UP:
                print('K_UP')
                panrect = panrect.move([0, -100])
                pygame.time.delay(1000)
                panrect = panrect.move([0, 20])
    # 重新画背景，避免原来的图片遗留
    screen.blit(background, (0, 0))
    # 将图片重新画到窗口上
    if panNum == 0:
        screen.blit(pan, panrect)
        panNum = 1
    else:
        screen.blit(pan1, panrect)
        panNum = 0
    # 更新全部显示
    pygame.display.flip()

    # 计算下一步的移动方向：碰到左右边缘，则掉头
    if panrect.left < 0 or panrect.right > width:
        print('不撞南墙不回头！')
        # 图片掉头
        pan = pygame.transform.flip(pan, True, False)
        pan1 = pygame.transform.flip(pan1, True, False)

