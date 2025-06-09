import pygame
import sys
from gamepy_colors import *
import numpy as np
from tools import *
import random

TILE_SIZE=130
ch=0
pygame.init()
t_dis=pygame.display.set_mode((400,400))
pygame.display.set_caption('TIC_TAC_TOE')


t_dis.fill(white)
shape()

pygame.display.update()

pygame.display.update()
turn=True
while True :

    for event in pygame.event.get() :
 
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            pygame.mixer.music.stop()
    
        if event.type==pygame.MOUSEBUTTONUP:
           
            pos=pygame.mouse.get_pos()
            for sq in range(len(sq_list)):
                
                if sq_list[sq].collidepoint(pos):
                    row,col=sq//3,sq%3
                    if game_board[row][col]==0:
                        
                        if turn:
                            kerm()
                            cross(sq)
                            turn=not turn
                            
                            game_board[row][col]=int(turn)+1
                        


                        else:  
                            turn=not turn  
                            circle(sq)
                            
                            kerm()
                            game_board[row][col]=int(turn)+1
                           
    pygame.display.update()
    state=check(game_board)  
    if state!='continue':
        
        if state!='Tie':
            print(f' player {state} won !!!')
            
            winner()
           
        else:
            print('Tie,no one scores')
            tie()
    
        while True:
        
                    again=str(input('Would you rather to play again (y/n): '))

                    match again:
                         case 'y':
                            print(f'....... \n running ..')
                            game_board=restart()
                            shape()
                    
                            break
                    
                         case 'n':
                            pygame.quit()
                            sys.exit()
                            pygame.mixer.music.stop()
                            break 
                        

                         case _:
                            print('invalid input.please enter y or n ')
                    
                        
                    
                


            
            































































