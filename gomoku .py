''' UI & deep learning & rules '''



#import packages
import pygame 
from pygame.locals import *


#about screen
Screen= width, height = 1440,960


#init the game
pygame.mixer.init(44100,-16,1,512)
pygame.init()

#insert sound and music
move_sound = pygame.mixer.Sound("move.wav")
pygame.mixer.music.load("Away.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

#setup screen
Screen = pygame.display.set_mode(Screen)
pygame.display.set_caption("Gomoku")

#define colors
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
Screen.fill(WHITE)

#background photo
boardImage = pygame.image.load('boardphoto.jpg')
Screen.blit(boardImage, (0,0))





font = pygame.font.Font(None, 40)
text_black = font.render('Black win!', True, GREEN, BLUE)
text_white = font.render('White win!', True, GREEN, BLUE)
textRect_black = text_black.get_rect()
textRect_white = text_white.get_rect()
textRect_black.center = (1440 // 2, 960 // 2)
textRect_white.center = (1440 // 2, 960 // 2)


def who_wins(color_of_list, new_position):
    """color_of_list 代表了谁在下子（那个颜色） new_position 代表了新下的那个子的位置 我们需要对比新\
    下的子的位置和所有原来在list中的位置 看看有没有五个连续的 如果有五个连续的则判定胜利"""
    global black_1
    global white_1
    global display_1
    a=0
    black_1=False
    white_1=False
    display_1=a
    
    for i in range(1,5):
        # horizontal
        if [int(new_position[0])+25*i,int(new_position[1])] in color_of_list:
            a+=1
        elif [int(new_position[0]) -25*i,int(new_position[1])] in color_of_list:
            a+=1
        # vertical
        elif [int(new_position[0]), int(new_position[1])+25*i] in color_of_list:
            a+=1
        elif [int(new_position[0]), int(new_position[1])-25*i] in color_of_list:
            a+=1
        # up left, down right
        elif [int(new_position[0])+25*i, int(new_position[1])-25*i] in color_of_list:
            a+=1
        elif [int(new_position[0])-25*i, int(new_position[1])+25*i] in color_of_list:
            a+=1
        # up right, down left
        elif [int(new_position[0])+25*i, int(new_position[1])+25*i] in color_of_list:
            a+=1
        elif [int(new_position[0])-25*i, int(new_position[1])-25*i] in color_of_list:
            a+=1
        else:
            print("value i:",i)
            break
    if a >= 4:
        if (n-1)%2 == 1:
            black_1=True
            return(a)
        if (n-1)%2 == 0:
            white_1=True
            return(a)
    print('asjgfaosiuhf',a)


#pygame.draw.line(Screen, Color, Start_position, End_position, Width)
#Draw the board
for i in range (50):
    pygame.draw.line(Screen, BLACK, [25*i, 0], [25*i,950], 1)
    pygame.draw.line(Screen, BLACK, [0,25*i], [1225, 25*i], 1)
pygame.display.update()


#计算线的交点 compute the line intersection
#def line_intersection(line_1, line_2):


#所有的空的交点
empty_intersection=[]
for i in range(50):
    for a in range(39):
        empty_intersection.append([25*i,25*a])

#print(empty_intersection)

n=1 #n 用于判断谁改下了 当n为单数时 后手下子  n为偶数时 先手下子
all_black=[]
all_white=[]
time_black_win=0
time_white_win=0


time_to_quit = False
while not time_to_quit:
    for new_event in pygame.event.get():
        if new_event.type == pygame.QUIT:
            time_to_quit = True
        if new_event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            #print(pos)
            pos_position = [round(x / 25) for x in pos]
            #print(pos_position)
            intersection_position = [pos_position[i] * 25 for i in range(len(pos_position))]
            #print(intersection_position)
            if intersection_position in empty_intersection:
                if n%2 == 1:
                    n+=1
                    pygame.draw.circle(Screen, BLACK, intersection_position, 12, 0)
                    all_black.append(intersection_position)
                    empty_intersection.remove(intersection_position)
                    who_wins(all_black,intersection_position)
                    #print('black_1 is',black_1)
                    #print("n is",n)
                    #print("a is",display_1)
                    if black_1 == True:
                        Screen.blit(text_black, textRect_black)
                        pygame.display.update()
                        time_black_win+=1
                        time_to_quit = True
                elif n%2 == 0:
                    n+=1
                    pygame.draw.circle(Screen, WHITE, intersection_position,12, 0)
                    all_white.append(intersection_position)
                    empty_intersection.remove(intersection_position)
                    who_wins(all_white,intersection_position)
                    if white_1 == True:
                        Screen.blit(text_white, textRect_white)
                        pygame.display.update()
                        time_white_win+=1
                        time_to_quit = True
                pygame.display.update()
    
    #获取鼠标位置 get mouse position          
    x, y = pygame.mouse.get_pos()
    #print(x,y)
    

pygame.quit()

"""
p1 = sorted(empty__intersection.append(pos))
p2 = sorted(empty__intersection.append(pos), key=lambda x: x[1])
px = p1.index(pos)
py = p2.index(pos)
first_x = p1[px-1]
second_x = p1[px+1]
first_y = p2[py-1]
second-y = p2[py+1]
"""
#time

#text display
# AI (deep learning? or simple AI branch




#谁先走
#https://docs.python.org/2/library/random.html
#https://www.researchgate.net/publication/312325842_Move_prediction_in_Gomoku_using_deep_learning

#def ResetBoard(board)
#def NewBoard()
#def OnBoard(x, y)
#def ValidMoves(board, tile)  tile是已经存在的自己的棋子  othertile对方的棋子

import random

def WhoGoesFirst():
    if random.randint('player', 'computer') == 'player':
        player = 'black'
        computer = 'white'
    else:
        player = 'white'
        computer = 'black'

