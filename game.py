import pygame
from pygame.locals import *
import numpy
import random

pygame.init()
 
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("batana bro")
 
gameOn = True
playing = False

b = pygame.Surface((40,40))
b.fill((219,140,61))
c = pygame.Surface((36,36))
c.fill((0,0,0))
p = pygame.Surface((30,30))
p.fill((255,255,255))
e = pygame.Surface((30,30))
e.fill((0,0,0))
fog = pygame.Surface((30,30))
fog.fill((70,77,89))
s = pygame.Surface((30,30))
s.fill((212,175,55))

board_data = numpy.zeros((20,20))
hail_data = numpy.zeros((20,20))

def reckon_board(board_data):
    for i in range(20):
        for j in range(20):
            board_data[i][j] = 0
    count = 0
    while count!= 50:
        x = random.choice(range(20))
        y = random.choice(range(20))
        if board_data[x][y] == 0 and x + y != 0:
            count+=1
            board_data[x][y] = 9
    for i in range(20):
        for j in range(20):
            if board_data[i][j]!=9:
                mcount = 0
                for x in [-1,0,1]:
                    for y in [-1,0,1]:
                        if i+x >= 0 and i+x < 20 and j+y >= 0 and j+y < 20 and board_data[i+x][j+y] == 9:
                            mcount+=1
                board_data[i][j] = mcount

    for i in range(20):
        for j in range(20):
            board_data[i][j]+=10
    
    for [x,y] in [[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[2,0],[2,1],[3,0]]:
        board_data[x][y]-=10

def reset_board(board_data):
    for i in range(20):
        for j in range(20):
            board_data[i][j] = 0

def print_board(vx,vy,board_data,mfont):
    x = 55
    y = 55
    for i in range(10):
        for j in range(10):
            screen.blit(b,(x,y))
            screen.blit(c,(x+2,y+2))
            text = mfont.render("%d" % (board_data[vx+i][vy+j]%10),True,(255,0,0))
            if board_data[vx+i][vy+j] == 9:
                screen.fill((255,0,0),(x+5,y+5,30,30))
            elif board_data[vx+i][vy+j] >= 10:
                screen.blit(fog,(x+5,y+5))
            y+=50
        x+=50
        y = 55

clock = pygame.time.Clock()

font = pygame.font.Font("BASKVILL.ttf", 48)
fonter = pygame.font.Font("BASKVILL.ttf", 36)
mfont = pygame.font.Font("BASKVILL.ttf",18)
text = font.render("PLAY", True, (255, 0, 0))
gtext = fonter.render("GIVE UP",True,(255,0,0))
name = mfont.render("HP",True,(0,0,0))
button_rect = pygame.Rect(770-text.get_width()/2, 300-text.get_height()/2, text.get_width(), text.get_height())
buttoner_rect = pygame.Rect(770-gtext.get_width()/2, 400-gtext.get_height()/2, gtext.get_width(), gtext.get_height())
p.blit(name,(15-name.get_width()/2,15-name.get_height()/2))

px = 0
py = 0
vx = 0
vy = 0
sx = 19
sy = 19

t = 0

screen.blit(text,(770-text.get_width()/2,300-text.get_height()/2)) 
print_board(0,0,board_data=board_data,mfont=mfont)

TIMEREVENT = pygame.USEREVENT + 1
SNITCHMOVE = pygame.USEREVENT + 2

while gameOn:

    if playing:
        screen.blit(p,(60+px*50,60+py*50))
        if sx-vx >= 0 and sx-vx <= 9 and sy-vy >= 0 and sy-vy <= 9:
            screen.blit(s,(60+(sx-vx)*50,60+(sy-vy)*50))
        surf = pygame.Surface((44,44))
        surf.fill((219,140,61))
        surf2 = pygame.Surface((40,40))
        surf2.fill((0,0,0))
        surf3 = pygame.Surface((20,20))
        surf3.fill((219,140,61))
        screen.blit(surf,(748,478))
        screen.blit(surf2,(750,480))
        screen.blit(surf3,(750+vx*2,480+vy*2))
    
    for event in pygame.event.get():
         
        if event.type == KEYDOWN:
            if event.key == K_UP and playing and py != 0 and board_data[vx+px][vy+py-1] != 9:
                screen.blit(e,(60+px*50,60+py*50))
                py-=1
            elif event.key == K_DOWN and playing and py != 9 and board_data[vx+px][vy+py+1] != 9:
                screen.blit(e,(60+px*50,60+py*50))
                py+=1
            elif event.key == K_RIGHT and playing and px != 9 and board_data[vx+px+1][vy+py] != 9:
                screen.blit(e,(60+px*50,60+py*50))
                px+=1
            elif event.key == K_LEFT and playing and px != 0 and board_data[vx+px-1][vy+py] != 9:
                screen.blit(e,(60+px*50,60+py*50))
                px-=1
            elif event.key == K_w and playing and vy != 0 and py!=9:
                vy-=1
                py+=1
            elif event.key == K_s and playing and vy != 10 and py!=0:
                vy+=1
                py-=1
            elif event.key == K_a and playing and vx != 0 and px!=9:
                vx-=1
                px+=1
            elif event.key == K_d and playing and vx != 10 and px!=0:
                vx+=1
                px-=1
            elif event.key == K_LSHIFT or event.key == K_RSHIFT and playing:
                t+=5
                for i in range(3):
                    for j in range(3):
                        if i-1+vx+px >= 0 and i-1+vx+px < 20 and j-1+vy+py >= 0 and j-1+vy+py < 20:
                            board_data[i-1+vx+px][j-1+vy+py] = 0    
            for i in range(7):
                for j in range(7):
                    if abs(i-3)+abs(j-3) <= 3 and vx+px+i-3 >= 0 and vx+px+i-3 < 20 and vy+py+j-3 >= 0 and vy+py+j-3 < 20:
                        board_data[vx+px+i-3][vy+py+j-3]%=10
            print_board(vx,vy,board_data=board_data,mfont=mfont)

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos) and playing == False:
                playing = True
                screen.fill((0,0,0),button_rect)
                ttext = font.render("0",True,(255,0,0))
                screen.blit(gtext,(770-gtext.get_width()/2,400-gtext.get_height()/2))
                screen.blit(ttext,(770-ttext.get_width()/2,300-ttext.get_height()/2))
                reckon_board(board_data=board_data) 
                print_board(vx,vy,board_data=board_data,mfont=mfont)
                pygame.time.set_timer(TIMEREVENT,1000)  
                pygame.time.set_timer(SNITCHMOVE,333)
            elif buttoner_rect.collidepoint(event.pos) and playing:
                t = 0
                reset_board(board_data=board_data)
                vx = 0
                vy = 0
                px = 0
                py = 0
                print_board(vx,vy,board_data=board_data,mfont=mfont)
                screen.fill((0,0,0),button_rect)
                screen.fill((0,0,0),buttoner_rect)
                screen.fill((0,0,0),(748,478,44,44))
                playing = False
                screen.blit(text,(770-text.get_width()/2,300-text.get_height()/2)) 
            
        elif event.type == TIMEREVENT and playing:
            t+=1
            x = random.choice(range(20))
            y = random.choice(range(20))
            if not(px==x and py == y):
                board_data[x][y] = 9
            ttext = font.render("%d" % t,True,(255,0,0))
            screen.fill((0,0,0),button_rect)
            screen.blit(ttext,(770-ttext.get_width()/2,300-ttext.get_height()/2))

        elif event.type == SNITCHMOVE and playing:
            sx+=(random.choice(range(3))-1)
            sy+=(random.choice(range(3))-1)
            if sx > 19:
                sx = 19
            elif sx < 0:
                sx = 0
            if sy > 19:
                sy = 19
            elif sy < 0:
                sy = 0

        elif event.type == QUIT:
            gameOn = False

    pygame.display.flip()
