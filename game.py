import pygame
from pygame.locals import *
import random

pygame.init()
 
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Bully-Sweeper")
 
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

x = 55
y = 55

for i in range(10):
    for j in range(10):
        screen.blit(b,(x,y))
        screen.blit(c,(x+2,y+2))
        y+=50
    x+=50
    y = 55

clock = pygame.time.Clock()

font = pygame.font.Font("BASKVILL.ttf", 48)
fonter = pygame.font.Font("BASKVILL.ttf", 36)
text = font.render("PLAY", True, (255, 0, 0))
gtext = fonter.render("GIVE UP",True,(255,0,0))
button_rect = pygame.Rect(770-text.get_width()/2, 300-text.get_height()/2, text.get_width(), text.get_height())
buttoner_rect = pygame.Rect(770-gtext.get_width()/2, 400-gtext.get_height()/2, gtext.get_width(), gtext.get_height())

px = random.choice(range(10))
py = random.choice(range(10))

t = 0

screen.blit(text,(770-text.get_width()/2,300-text.get_height()/2)) 

TIMEREVENT = pygame.USEREVENT + 1

while gameOn:

    if playing:
        screen.blit(p,(60+px*50,60+py*50)) 
    
    for event in pygame.event.get():
         
        if event.type == KEYDOWN:
            if event.key == K_UP and playing and py != 0:
                screen.blit(e,(60+px*50,60+py*50))
                py-=1
            elif event.key == K_DOWN and playing and py != 9:
                screen.blit(e,(60+px*50,60+py*50))
                py+=1
            elif event.key == K_RIGHT and playing and px != 9:
                screen.blit(e,(60+px*50,60+py*50))
                px+=1
            elif event.key == K_LEFT and playing and px != 0:
                screen.blit(e,(60+px*50,60+py*50))
                px-=1

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                playing = True
                screen.fill((0,0,0),button_rect)
                ttext = font.render("0:00",True,(255,0,0))
                screen.blit(gtext,(770-gtext.get_width()/2,400-gtext.get_height()/2))
                screen.blit(ttext,(770-ttext.get_width()/2,300-ttext.get_height()/2)) 
                pygame.time.set_timer(TIMEREVENT,1000)  
            elif buttoner_rect.collidepoint(event.pos) and playing:
                t = 0
                x = 55
                y = 55
                for i in range(10):
                    for j in range(10):
                        screen.blit(b,(x,y))
                        screen.blit(c,(x+2,y+2))
                        y+=50
                    x+=50
                    y = 55
                screen.fill((0,0,0),button_rect)
                screen.fill((0,0,0),buttoner_rect)
                playing = False
                screen.blit(text,(770-text.get_width()/2,300-text.get_height()/2)) 
            
        elif event.type == TIMEREVENT and playing:
            t+=1
            if t%60 < 10:
                ttext = font.render("%d:0%d" % (t/60,t%60),True,(255,0,0))
                screen.fill((0,0,0),button_rect)
                screen.blit(ttext,(770-ttext.get_width()/2,300-ttext.get_height()/2)) 
            else:
                ttext = font.render("%d:%d" % (t/60,t%60),True,(255,0,0))
                screen.fill((0,0,0),button_rect)
                screen.blit(ttext,(770-ttext.get_width()/2,300-ttext.get_height()/2)) 

        elif event.type == QUIT:
            gameOn = False

    pygame.display.flip()