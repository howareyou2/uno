import pygame
from pygame.locals import *
import math

class Card(pygame.sprite.Sprite):
    def __init__(self, name, position):
        pygame.sprite.Sprite.__init__(self)
        self.name = name 
        self.image = pygame.image.load('./img/'+name+'.png') # 카드 이미지 불러오기
        self.image = pygame.transform.scale(self.image, (80, 100)) # 카드 크기 조절
        self.orig_pos = position
        self.position = position
        self.user_rotation = 0
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    # 게임 구현에서 사용된 기능 카드 이동
    def update(self, dest_loc): 
        x, y = self.position
        vx, vy = (dest_loc[0] - x, dest_loc[1] - y)
        vx, vy = (x/(x**2+y**2)**0.5, y/(x**2+y**2)**0.5)

        speed = 5

        x = x+speed*vx
        y = y+speed*vy

        if x>=dest_loc[0]:
            x = dest_loc[0]
        if y>=dest_loc[1]:
            y = dest_loc[1]

        self.position = (x, y)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
    
    def rotation(self, rotate): # 카드 회전
        self.image = pygame.transform.rotate(self.image, rotate)

    def getposition(self):
        return self.position

    def setposition(self, x, y): # 카드 위치 변경
        i_x = x
        i_y = y
        self.position = (i_x, i_y)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    # 게임 실행에 사용됨, 카드 이동
    def move(self, compare_pos):
        x, y = self.position
        i_x = compare_pos[0]
        i_y = compare_pos[1]

        if x > i_x+60 and y == i_y:
            x -= 70

        elif y > i_y:
            if x <= 200:
                x = 620
                y = y - 80
            else:
                x -=70
        self.position = (x, y)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def get_rect(self):
        return self.rect

    def get_name(self):
        return self.name

    def transform(self,x,y):
        self.image=pygame.transform.scale(self.image,(x,y))