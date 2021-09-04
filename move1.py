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


class Pang(object):
    def __init__(self):
        self.speed = 5
        self.isUp = None
        self.isRight = None

    def stop(self):
        self.speed = 5
        self.isUp = None
        self.isRight = None


pang = Pang()


def panMove(rect, pang):
    # 如果isUp是True，向上；如果isUp是False，向下；如果isRight是True，向右；如果isRight是False，向左
    if pang.isUp is not None:
        if pang.isUp:
            if panrect.top < height:
                rect = rect.move([0, -pang.speed])
            else:
                print("已经到最下边了！")
        else:
            if panrect.top > 0:
                rect = rect.move([0, pang.speed])
        pang.speed -= 1
        if rect.top > 477:
            rect.move([0, 477 - rect.top])
            pang.stop()
    if pang.isRight is not None:
        if pang.isRight:
            if rect.right != width:
                rect = rect.move([pang.speed, 0])
            else:
                print("已经到最右边了！")
        else:
            if rect.left >= 0:
                rect = rect.move([-pang.speed, 0])
            else:
                print("已经到最左边了！")
        pang.speed -= 1
        if pang.speed == 0:
            pang.stop()
    return rect


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
            if event.key == pygame.K_LEFT:
                pang.speed = 5
                pang.isUp = None
                pang.isRight = False
            if event.key == pygame.K_RIGHT:
                pang.speed = 5
                pang.isUp = None
                pang.isRight = True
            if event.key == pygame.K_UP:
                pang.speed = 10
                pang.isUp = True
                pang.isRight = None
    panrect = panMove(panrect, pang)
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
    if panrect.left == 0 or panrect.right == width:
        # 图片掉头
        pan = pygame.transform.flip(pan, True, False)
        pan1 = pygame.transform.flip(pan1, True, False)

    if panrect.left == 0 or panrect.right == width:
        # 图片掉头
        pan = pygame.transform.flip(pan, True, False)
        pan1 = pygame.transform.flip(pan1, True, False)

