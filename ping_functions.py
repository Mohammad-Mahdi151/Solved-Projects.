from constants import *
import pygame
from ping_colors import *
import time
from object import *
GAME_SCREEN=pygame.display.set_mode((800,400))
def khotot():
    NUMBER=[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400]

    pygame.draw.rect(GAME_SCREEN,white,(0,0,800,12))
    pygame.draw.rect(GAME_SCREEN,white,(0,390,800,12))
    pygame.draw.rect(GAME_SCREEN,white,(794,0,50,400))
    pygame.draw.rect(GAME_SCREEN,white,(0,0,6,400))
    for i in NUMBER:
        pygame.draw.rect(GAME_SCREEN,white,(400,i,2,5))
    pygame.draw.line(GAME_SCREEN,white,
                 (0,200),(800,200),3)

def shoot_ball():
    pygame.mixer.music.load('ping pong_sound.mp3')
    pygame.mixer.music.play()
def get_score():
    pygame.mixer.music.load('SCORE_SOUND.mp3')
    pygame.mixer.music.play()
def show_score(surface,_str,color,which):
    str_obj=FONT.render(_str,True,color)
    position=list(str_obj.get_size())
    if which:
        position[0]=400-position[0]-20
        position[1]=10
    else:
        position[0]=400+20
        position[1]=10
    surface.blit(str_obj,position)
first=time.time()
def show_time():
    
    second=(time.time()-first)/60
    font=pygame.font.Font("C:\\Users\\Lenovo-Pc\\Downloads\\Stagera.otf",25)
    str_ogg=font.render(f'{second:1.2f}',True,white)
    GAME_SCREEN.blit(str_ogg,(9,30))

    
def wining_sound():
    pygame.mixer.music.load('Victory-SOUND2_1.mp3')
    pygame.mixer.music.play()

def change_sit(player,keys):
    if keys[pygame.K_UP] and player.top>=12:
            player.y-=paddle_speed
    if keys[pygame.K_RIGHT] and player.right<=790:
            player.x+=paddle_speed
    if keys[pygame.K_LEFT] and player.left>=420:
            player.x-=paddle_speed
    if keys[pygame.K_DOWN] and player.bottom<=400-8:
            player.y+=paddle_speed
    return player
keys=pygame.key.get_pressed()

def speed_up(a,b):
    if a in [5,6,7,9] or b in [5,6,7,9]:
        global paddle_speed
        global ball_speed
        ball_speed+=1
        paddle_speed+=2
        change_sit(player,keys)
def restart(again):
        wining_sound()
        show_score(GAME_SCREEN,f'Opponent won!!!',purple,True)
        pygame.display.update()
        while True:
            try:
                again
                break
            except ValueError as f:
                print(f)
        match (again):
            case 'y':
                player_score,opponent_score=0,0
                show_time()
                player.x,player.y=784,200
                opponent.x,opponent.y=6,200
                ball.x,ball.y=400-10,200-10
                pygame.display.update()
                print(f'Ok.....\n running...')
            case 'n':
                print(f'Thank you for playing')
                exit()
     
def change_sit2(player2,keys):
     
    if keys[pygame.K_f] and player2.top>=12:
            player2.y-=paddle_speed
    if keys[pygame.K_g] and player2.right<=380:
            player2.x+=paddle_speed
    if keys[pygame.K_d] and player2.left>=10:
            player2.x-=paddle_speed
    if keys[pygame.K_c] and player2.bottom<=400-8:
            player2.y+=paddle_speed
    return player2
def increase_speed_if_needed(score1, score2):
    global ball_xd, ball_yd, paddle_speed 
    if score1 in [5, 7, 9] or score2 in [5, 7, 9]:
        ball_xd = abs(ball_xd) + ball_speed_increment if ball_xd > 0 else -(abs(ball_xd) + ball_speed_increment)
        ball_yd = abs(ball_yd) + ball_speed_increment if ball_yd > 0 else -(abs(ball_yd) + ball_speed_increment)
        paddle_speed += paddle_speed_increment
        