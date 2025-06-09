import pygame
from constants import *
player=pygame.Rect(784,200,10,60)
opponent=pygame.Rect(6,200,10,60)
FONT=pygame.font.Font("C:\\Users\\Lenovo-Pc\\Downloads\\Stagera.otf",30)
ball=pygame.Rect(400-10,200-10,20,20)
ball_xd=ball_speed
ball_yd=ball_speed
player2=pygame.Rect(6,200,10,60)
ANSWER_LIST=[['1','opponent'],['2','another player','second player','player2']]