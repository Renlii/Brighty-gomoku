#import packages
import pygame 
from pygame.locals import *
import sys

    
#about screen
Screen= width, height = 1440,960


#init the game
pygame.mixer.init(44100,-16,1,512)
pygame.init()

#insert music & sounds
move_sound = pygame.mixer.Sound("move.wav")
celebrate = pygame.mixer.Sound("Celebration.wav")
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

#Timer

clock = pygame.time.Clock()

frame_count = 0
frame_rate = 60
start_time = 90

#font setting
font = pygame.font.Font(None, 40)
text_black = font.render('Black win!',True, GREEN, BLUE)
text_white = font.render('White win!',True, GREEN, BLUE)
textRect_black = text_black.get_rect()
textRect_white = text_white.get_rect()
textRect_black.center = (1440 // 2, 960 // 2)
textRect_white.center = (1440 // 2, 960 // 2)




game_over = False
n=1 #n 用于判断谁改下了 当n为单数时 后手下子  n为偶数时 先手下子
all_black=[]
all_white=[]
time_black_win=0
time_white_win=0

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

def RestartButton():
    pygame.draw.line(Screen, BLACK, [1300,300], [1300,350], 2)
    pygame.draw.line(Screen, BLACK, [1350,300], [1350,350], 2)
    pygame.draw.line(Screen, BLACK, [1300,300], [1350,300], 2)
    pygame.draw.line(Screen, BLACK, [1300,350], [1350,350], 2)
    font_re = pygame.font.SysFont(None, 21)
    text = font_re.render("Restart", True, RED)
    Screen.blit(text, (1300, 360))
    pygame.display.update()

def ScreenSetUp():
    global Screen
    global boardImage
    global restart_button

    Screen.fill(WHITE)
    boardImage = pygame.image.load('boardphoto.jpg') #Background Image
    timerImg = pygame.image.load("Timer.jpg") #Timer Image
    timerImg = pygame.transform.scale(timerImg, (75,75))
    Screen.blit(timerImg,(1226,70))
    Screen.blit(boardImage, (0,0))


    #pygame.draw.line(Screen, Color, Start_position, End_position, Width)
    #Draw the board
    for i in range (50):
        pygame.draw.line(Screen, BLACK, [25*i, 0], [25*i,950], 1)
        pygame.draw.line(Screen, BLACK, [0,25*i], [1225, 25*i], 1)
    RestartButton()
    pygame.display.update()

def reset():
    global n
    global all_black
    global all_white
    global time_black_win
    global time_white_win
    global game_over
    global empty_intersection
    global frame_count
    global frame_rate
    global start_time
    
    pygame.init()
    empty_intersection = Empty_intersection()
    n=1 #n 用于判断谁改下了 当n为单数时 后手下子  n为偶数时 先手下子
    all_black=[]
    all_white=[]
    time_black_win=0
    time_white_win=0
    game_over = False
    frame_count = 0
    frame_rate = 60
    start_time = 90

    pygame.mixer.music.play(-1)
    ScreenSetUp()

#所有的空的交点
def Empty_intersection():
    empty_int=[]
    for i in range(50):
        for a in range(39):
            empty_int.append([25*i,25*a])
    return empty_int

empty_intersection = Empty_intersection()
#print(empty_intersection)

ScreenSetUp()
while True:
    
    #Timer
    
    total_seconds = frame_count // frame_rate
    minutes = total_seconds // 60 # Divide by 60 to get minutes
    seconds = total_seconds % 60 # Remainder is seconds
    output_string = "Time:{0:02}:{1:02}".format(minutes, seconds)
    

    #Blit it to the screen
    text = font.render(output_string, True, BLACK,WHITE)
    Screen.blit(text, [1280,100],)
    
    #Calculate total seconds
    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0
    frame_count += 1
    
    clock.tick(frame_rate)

    pygame.display.flip() #update
    
    for new_event in pygame.event.get(): #Exit
        
        if new_event.type == pygame.QUIT:
            
            
            pygame.quit()
            sys.exit()
        

        
        if new_event.type == pygame.MOUSEBUTTONUP:
            
            pos = pygame.mouse.get_pos()
            #print(pos)
            pos_position = [round(x / 25) for x in pos]
            #print(pos_position)
            intersection_position = [pos_position[i] * 25 for i in range(len(pos_position))]
            #print(intersection_position)
            button_set = [[1300,300],[1300,325],[1300,350],[1325,300],[1325,325],[1325,350],[1350,300],[1350,325],[1350,350]]

            if intersection_position in button_set:
                reset()
            if intersection_position in empty_intersection:

                pygame.mixer.Sound.play(move_sound)
                
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
                        font_GO = pygame.font.SysFont(None, 80)
                        text_GO = "GAME OVER within {0:02}:{1:02}!!".format(minutes, seconds)
                        reminder = font_GO.render(text_GO, True, BLACK)

#"Ti                      
                        pygame.mixer.music.stop()
                        pygame.mixer.Sound.play(celebrate)
                        #pygame.time.delay(20000)
                        Screen.blit(reminder, reminder.get_rect())
                        pygame.display.update()
                        game_over = True
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
                        font_GO = pygame.font.SysFont(None, 80)
                        text_GO = "GAME OVER within {0:02}:{1:02}!!".format(minutes, seconds)
                        reminder = font_GO.render(text_GO, True, BLACK)

                        
                        pygame.mixer.music.stop()
                        pygame.mixer.Sound.play(celebrate)
                        #pygame.time.delay(20000)
                        Screen.blit(reminder, reminder.get_rect())
                        pygame.display.update()
                        game_over = True
                
                pygame.display.update()
              
    x, y = pygame.mouse.get_pos()
    #print(x,y)

pygame.quit()


