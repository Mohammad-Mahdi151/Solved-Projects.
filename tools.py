import pygame
from gamepy_colors import *
import winsound
import numpy as np
import time
sq1=pygame.Rect(CORD[0],CORD[0],TILE_SIZE,TILE_SIZE)
sq2=pygame.Rect(CORD[1],CORD[0],TILE_SIZE,TILE_SIZE)
sq3=pygame.Rect(CORD[2],CORD[0],TILE_SIZE,TILE_SIZE)
sq4=pygame.Rect(CORD[0],CORD[1],TILE_SIZE,TILE_SIZE)
sq5=pygame.Rect(CORD[1],CORD[1],TILE_SIZE,TILE_SIZE)
sq6=pygame.Rect(CORD[2],CORD[1],TILE_SIZE,TILE_SIZE)
sq7=pygame.Rect(CORD[0],CORD[2],TILE_SIZE,TILE_SIZE)
sq8=pygame.Rect(CORD[1],CORD[2],TILE_SIZE,TILE_SIZE)
sq9=pygame.Rect(CORD[2],CORD[2],TILE_SIZE,TILE_SIZE)

sq_list=[sq1,sq2,sq3,sq4,sq5,sq6,sq7,sq8,sq9]

def shape():
    for g in sq_list:
        pygame.draw.rect(t_dis,black,(g))

def circle(i):
    row,col=i%3,i//3
    pygame.draw.circle(t_dis,
                       (blue),
                       (CORD[row]+HALF_TILE,CORD[col]+HALF_TILE),
                       40,7)
def cross(i):
    row,col=i//3,i%3
    pygame.draw.line(t_dis,(255,0,0),
                     (CORD[col]+20,CORD[row]+20),
                     (CORD[col]+TILE_SIZE-20,CORD[row]+TILE_SIZE-20),9)
    pygame.draw.line(t_dis,(255,0,0),
                     (CORD[col]+20,CORD[row]+TILE_SIZE-20),
                     (CORD[col]+TILE_SIZE-20,CORD[row]+20),9)
            
def check(gb):
    for i in range(3):
        row=np.unique(gb[:,i])
        col=np.unique(gb[i,:])

        if len(row)==1 and row!=0 :
            return row
          
        if len(col)==1 and col!=0 :
            return col
        
    if gb[0][0]==gb[1][1] and gb[1][1]==gb[2][2] and gb[0][0]!=0:
        return gb[1][1]
    
    
    elif gb[2][0]==gb[1][1] and gb[1][1]==gb[0][2] and gb[2][0]!=0:
        return gb[1][1]
    if 0 not in np.unique(gb):
    
        return 'Tie'
    
    return 'continue'


def restart():
    

    return np.array([[0,0,0],[0,0,0],[0,0,0]])


def winner():
    winsound.Beep(300,900)
def tie():
    winsound.Beep(100,100)


def kerm():
    # winsound.Beep(200,200)
    pygame.mixer.music.load('PING PONG.mp3')
    pygame.mixer.music.play()
    # game_sound="C:\\Users\\Lenovo-Pc\\Desktop\\doz.wav.wav"
    # winsound.PlaySound(game_sound,winsound.SND_FILENAME)


    





