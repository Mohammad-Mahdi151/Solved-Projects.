import pygame
import sys
pygame.init()
from ping_colors import *
from ping_functions import *
from constants import *
from object import *
import time
player_score=0
opponent_score=0
player2_score=0
collision=False

while True:

    try:
        choice=input(f'Do you want to play with the opponent or another player \n (or "quit" to exit)?')
    except ValueError:
        print(f'There is no mode called "{choice}",try again !!')

    GAME_SCREEN=pygame.display.set_mode((800,400))
    pygame.display.set_caption('ping pong')
    pygame.display.update()

    clock=pygame.time.Clock()
    first=time.time()

    if choice in  ANSWER_LIST[0]:
        while True:
            
            GAME_SCREEN.fill(blue)
            khotot()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    pygame.mixer.music.stop()


            keys=pygame.key.get_pressed()
            change_sit(player,keys)
            
            if ball.bottom>=400 or ball.top<=0:
                ball_yd*=-1
            if (ball.colliderect(player) and not collision) or (ball.colliderect(opponent) and collision):
                shoot_ball()
                collision=not collision
                ball_xd*=-1
            ball.x+=ball_xd
            ball.y+=ball_yd
            
        # ball.right>player.center[0]
            if ball.x>800:
                get_score()
                opponent_score+=1
                ball.x,ball.y=400-10,200-10
        # ball.left<opponent.center[0]
            if ball.x<0:
                get_score()
                player_score+=1
                ball.x,ball.y=400-10,200-10
            if opponent.center[1]>ball.center[1] and opponent.top>=12:
                opponent.y-=paddle_speed
            if opponent.center[1]<ball.center[1] and opponent.bottom<=390:
                opponent.y+=paddle_speed
            show_score(GAME_SCREEN,str(opponent_score),white,True)
            show_score(GAME_SCREEN,str(player_score),white,False)
            pygame.draw.ellipse(GAME_SCREEN,yellow,ball)
            pygame.draw.rect(GAME_SCREEN,red,player)
            pygame.draw.rect(GAME_SCREEN,red,opponent)
            show_time()
        
            

            if opponent_score==10: 

                wining_sound()
                show_score(GAME_SCREEN,f'Opponent won!!!',purple,True)
                pygame.display.update()
                while True:
                    try:
                        again=input('Do you want t play again(y/n):')
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
            
            elif player_score==10:
                wining_sound()
                show_score(GAME_SCREEN,f'player won1!!',purple,False)
                pygame.display.update()
                while True:
                    try:
                            again=input('Do you want t play again(y/n):')
                            break
                    except ValueError as e:
                            print(e)
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
            
            pygame.display.update()
            
            clock.tick(60)
    if choice in ANSWER_LIST[1]:
        
        while True:
            
            GAME_SCREEN.fill(blue)
            khotot()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    pygame.mixer.music.stop()


            keys=pygame.key.get_pressed()

            change_sit(player,keys)
            change_sit2(player2,keys)
            if ball.bottom>=400 or ball.top<=0:
                ball_yd*=-1
            if (ball.colliderect(player) and not collision) or (ball.colliderect(player2) and collision):
                shoot_ball()
                collision=not collision
                ball_xd*=-1
            ball.x+=ball_xd
            ball.y+=ball_yd
            
        # ball.right>player.center[0]
            if ball.x>800:
                get_score()
                player2_score+=1
                ball.x,ball.y=400-10,200-10
        # ball.left<opponent.center[0]
            if ball.x<0:
                get_score()
                player_score+=1
                ball.x,ball.y=400-10,200-10
            show_score(GAME_SCREEN,str(player2_score),white,True)
            show_score(GAME_SCREEN,str(player_score),white,False)
            pygame.draw.ellipse(GAME_SCREEN,yellow,ball)
            pygame.draw.rect(GAME_SCREEN,red,player)
            pygame.draw.rect(GAME_SCREEN,red,player2)
            show_time()

        

            if player2_score==10: 

                wining_sound()
                show_score(GAME_SCREEN,f'player2 won!!!',purple,True)
                pygame.display.update()
                while True:
                    try:
                        again=input('Do you want t play again(y/n):')
                        break
                    except ValueError as f:
                        print(f)
                match (again):
                    case 'y':
                        player_score,player2_score=0,0
                        show_time()
                        player.x,player.y=784,200
                        player2.x,player2.y=6,200
                        ball.x,ball.y=400-10,200-10
                        pygame.display.update()
                        print(f'Ok.....\n running...')
                    case 'n':
                        print(f'Thank you for playing')
                        exit()
            
            elif player_score==10:
                wining_sound()
                show_score(GAME_SCREEN,f'player won1!!',purple,False)
                pygame.display.update()
                while True:
                    try:
                        again=input('Do you want t play again(y/n):')
                        break
                    except ValueError as e:
                        print(e)
                match (again):
                    case 'y':
                        player_score,player2_score=0,0
                        show_time()
                        player.x,player.y=784,200
                        player2.x,player2.y=6,200
                        ball.x,ball.y=400-10,200-10
                        pygame.display.update()
                        print(f'Ok.....\n running...')
                    case 'n':
                        print(f'Thank you for playing')
                        exit()
            
            pygame.display.update()
            
            clock.tick(60)
    if choice=='quit':
        pygame.quit()
        sys.exit()
        pygame.mixer.music.stop()

    else:
        print(f'There is no mode called "{choice}",try again !!')





















































    
        


























































