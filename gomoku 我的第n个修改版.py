''' UI & deep learning & rules '''



#import packages
import pygame 
from pygame.locals import *


#about screen
Screen= width, height = 1440,960


#init the game
pygame.init()

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


font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('White win!', True, GREEN, BLUE)
textRect = text.get_rect()
textRect.center = (1440 // 2, 960 // 2)


def who_wins(color_of_list, new_position):
    """color_of_list 代表了谁在下子（那个颜色） new_position 代表了新下的那个子的位置 我们需要对比新\
    下的子的位置和所有原来在list中的位置 看看有没有五个连续的 如果有五个连续的则判定胜利"""
    global red_1
    global black_1
    global display_1
    a=0
    red_1=False
    black_1=False
    display_1=a
    # 横向判断
    for i in range(1,5):
        if [int(new_position[0])+25*i,int(new_position[1])] in color_of_list:
            a+=1
            print("a+=1",a)
        else:
            break
        print([int(new_position[0])+25*i,int(new_position[1])] in color_of_list)
        print([int(new_position[0])+25*i,int(new_position[1])])
        print("value i:",i)
    for i in range(1,5):
        if [int(new_position[0]) -25*i,int(new_position[1])] in color_of_list:
            a+=1
        else:
            break
    if a >= 4:
        if (n-1)%2 == 0:
            red_1=True
            return(a)
        if (n-1)%2 ==1:
            black_1=True
            return(a)



    # 纵向判断
    #a=0
    for i in range(1,5):
        if [int(new_position[0]), int(new_position[1])+25*i] in color_of_list:
            a+=1
        else:
            break
    for i in range(1,5):
        if [int(new_position[0]), int(new_position[1])-25*i] in color_of_list:
            a+=1
        else:
            break
    if a>= 4:
        if (n-1)%2 == 0:
            red_1=True
            return (a)
        if (n-1)%2 == 1:
            black_1=True
            return (a)
    # 左上右下
    #a=0
    for i in range(1,5):
        if [int(new_position[0])+25*i, int(new_position[1])-25*i] in color_of_list:
            a+=1
        else:
            break
    for i in range(1,5):
        if [int(new_position[0])-25*i, int(new_position[1])+25*i] in color_of_list:
            a+=1
        else:
            break
    if a>= 4:
        if (n-1)%2 == 0:
            red_1=True
            return (a)
        if (n-1)%2 == 1:
            black_1=True
            return (a)
    # 左下右上
    #a=0
    for i in range(1,5):
        if [int(new_position[0])+25*i, int(new_position[1])+25*i] in color_of_list:
            a+=1
        else:
            break
    for i in range(1,5):
        if [int(new_position[0])-25*i, int(new_position[1])+25*i] in color_of_list:
            a+=1
        else:
            break
    if a>= 4:
        if (n-1)%2 == 0:
            red_1=True
            return (a)
        if (n-1)%2 == 1:
            black_1=True
            return (a)
    print(a)


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

n=0 #n 用于判断谁改下了 当n为单数时 后手下子  n为偶数时 先手下子
all_black=[]
all_white=[]

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
                if n%2 == 0:
                    n+=1
                    pygame.draw.circle(Screen, BLACK, intersection_position, 10, 0)
                    all_black.append(intersection_position)
                    empty_intersection.remove(intersection_position)
                    who_wins(all_black,intersection_position)
                    #print('black_1 is',black_1)
                    #print("n is",n)
                    #print("a is",display_1)
                    if black_1 == True:
                        display_surface.blit(text, textRect)
                        pygame.display.update()
                elif n%2 == 1:
                    n+=1
                    pygame.draw.circle(Screen, WHITE, intersection_position,10, 0)
                    all_white.append(intersection_position)
                    empty_intersection.remove(intersection_position)
                    who_wins(all_white,intersection_position)
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
#rule
#text display
# AI (deep learning? or simple AI branch
