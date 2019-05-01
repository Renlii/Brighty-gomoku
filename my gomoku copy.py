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
    print(a)



#background photo
def ScreenSetUp():
    global Screen
    global boardImage
    Screen.fill(WHITE)
    boardImage = pygame.image.load('boardphoto.jpg')
    Screen.blit(boardImage, (0,0))
    #pygame.draw.line(Screen, Color, Start_position, End_position, Width)
    #Draw the board
    for i in range (50):
        pygame.draw.line(Screen, BLACK, [25*i, 0], [25*i,950], 1)
        pygame.draw.line(Screen, BLACK, [0,25*i], [1225, 25*i], 1)
    pygame.display.update()

ScreenSetUp()

def RestartButton():
    #red to quit
    pygame.draw.line(Screen, RED, [1000,100], [1000,150], 2)
    pygame.draw.line(Screen, RED, [1050,100], [1050,150], 2)
    pygame.draw.line(Screen, RED, [1000,100], [1050,100], 2)
    pygame.draw.line(Screen, RED, [1000,150], [1050,150], 2)
    #blue to continue
    pygame.draw.line(Screen, BLUE, [200,100], [200,150], 2)
    pygame.draw.line(Screen, BLUE, [250,100], [250,150], 2)
    pygame.draw.line(Screen, BLUE, [200,100], [250,100], 2)
    pygame.draw.line(Screen, BLUE, [200,150], [250,150], 2)
    pygame.display.update()

#所有的空的交点
def Empty_intersection():
    empty_int=[]
    for i in range(50):
        for a in range(39):
            empty_int.append([25*i,25*a])
    return empty_int

empty_intersection = Empty_intersection()
#print(empty_intersection)

n=1 #n 用于判断谁改下了 当n为单数时 后手下子  n为偶数时 先手下子
all_black=[]
all_white=[]
time_black_win=0
time_white_win=0

def game_loop(f):
    global quit_button
    global continue_button
    #global time_to_quit
    if f == False:
        pygame.init()
        quit_button = [[1000,100],[1000,125],[1000,150],[1025,100],[1025,125],[1025,150],[1050,100],[1050,125],[1050,150]]
        continue_button = [[200,100],[200,125],[200,150],[225,100],[225,125],[225,150],[250,100],[250,125],[250,150]]
        intersection_position = go_step()
        if intersection_position in continue_button:
            pygame.init()
            ScreenSetUp()
            game_main()
            game_loop(game_main())
        elif intersection_position in quit_button:
            #time_to_quit = True
            pygame.quit()
            sys.exit()
            pygame.display.update()
        else:
            print("Can you follow instructions???!!!")
    else:
            print("follow instructions dude!!!")

def go_step():
    for new_event in pygame.event.get():
        if new_event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            pygame.display.update()
        if new_event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            #print(pos)
            pos_position = [round(x / 25) for x in pos]
            #print(pos_position)
            intersection_position = [pos_position[i] * 25 for i in range(len(pos_position))]
            return intersection_position

#while not time_to_quit:
def game_main():
    global n
    global time_black_win
    global time_white_win
    #time_to_quit = False
    while True:   
        intersection_position = go_step()
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
                    Screen.fill(WHITE)
                    reminder = font.render("Press the RED button to quit or BLUE to continue!", True, GREEN, BLUE)
                    Screen.blit(reminder, reminder.get_rect())
                    pygame.display.update()
                    RestartButton()
                    return False   
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
                    Screen.fill(WHITE)
                    reminder = font.render("Press the button to quit or anywhere else to continue!", True, GREEN, BLUE)
                    Screen.blit(reminder, reminder.get_rect())
                    pygame.display.update()
                    RestartButton()
                    return False
                    #RestartButton()
                    #game_loop()
            pygame.display.update()
#获取鼠标位置 get mouse position          
x, y = pygame.mouse.get_pos()
#print(x,y)

game_main()
game_loop(game_main())

pygame.quit()

"""
def loop_board():
    time_to_quit = False
    while not time_to_quit:
        game_main()
        game_loop(game_main())

#loop_board()
pygame.quit()


for evento in pygame.event.get():
    if evento.type == pygame.MOUSEBUTTONDOWN:
        pos_e = pygame.mouse.get_pos()
        print(pos_e)
        type(pos_e)
        type(pos_e[0])
"""
