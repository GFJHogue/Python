#School Assignment that deals with number validation using the Luhn Algorithm.

from random import randint
from sys import exit

import pygame


def num(d):
    global event,n,keys
    n = ""
    text_prompt = font.render("Enter a " + str(d) + "-Digit Number:", True,
                              (0,0,0))
    text_n = font.render(">" + n + ("_" * (d - len(n))) + "<", True, (0,0,0))
    
    while True:
        while len(n) < d:
            if(event.type == pygame.QUIT)or(keys[pygame.K_ESCAPE]):
                exit()
            
            if (event.type==pygame.KEYDOWN):
                if len(pygame.key.name(event.key)) == 1 and pygame.key.name(event.key).isdigit():
                    n = n + pygame.key.name(event.key)
                elif pygame.key.name(event.key) == "backspace":
                    n = n[:len(n) - 1]
                text_n = font.render(">" + n + ("_" * (d - len(n))) + "<",
                                     True, (0,0,0))
            
            screen.fill((255,255,255))
            screen.blit(text_prompt,(0,0))
            screen.blit(text_n,(0,40))
            event = pygame.event.poll()
            keys = pygame.key.get_pressed()
            pygame.display.update()
        
        if len(n) == d:
            return
        
        n = ""

def ccn():
    validate(list(n[len(n) - 2::-1]),0, int(n[len(n) - 1]))

def sin():
    validate(list(n),1,0)

def validate(a,m,c):
    global event,h,n,keys,menu_4,menu_6,pos,prs
    t = 0
    text_prompt = font.render("Click to Continue...", True, (0,0,0))
    
    for l in range(m, len(a),2):
        a[l] = str(int(a[l]) * 2)
        
        if int(a[l]) > 9:
            a[l] = str(int(a[l]) - 9)
    
    for l in range(0, len(a)):
        t = t + int(a[l])
    
    if (10 - (t % 10) == c and m == 0) or t % 10 == c:
        text_valid = font.render('This Number is Valid.', True, (0,0,0))
        pygame.draw.rect(screen,(0,255,0),menu_4)
    else:
        text_valid = font.render('This Number is NOT Valid.', True, (0,0,0))
        pygame.draw.rect(screen,(255,0,0),menu_4)
    
    screen.blit(text_valid,(0,120))
    pygame.draw.rect(screen,(255,200,200),menu_6)
    screen.blit(text_prompt,(0,200))
    pygame.display.update()
    
    while True:
        event = pygame.event.poll()
        keys = pygame.key.get_pressed()
        prs = pygame.mouse.get_pressed()[0]
        pos = pygame.mouse.get_pos()
        
        if(event.type == pygame.QUIT)or(keys[pygame.K_ESCAPE]):
            exit()
        
        if prs and menu_6.collidepoint(pos):
            pygame.time.wait(1000)
            return

def generateCCN():
    global event,h,keys,menu_4,menu_6,pos,prs
    text_generate = font.render("Generating... Click to stop", True, (0,0,0))
    text_info = font.render("New Credit Card Number:", True, (0,0,0))
    text_prompt = font.render("Click to Continue...", True, (0,0,0))
    pygame.time.wait(1000)
    
    while True:
        event = pygame.event.poll()
        keys = pygame.key.get_pressed()
        prs = pygame.mouse.get_pressed()[0]
        pos = pygame.mouse.get_pos()
        r = str(randint(100000000000000,999999999999999))
        text_r = font.render(r, True, (0,0,0))
        screen.fill((255,255,255))
        screen.blit(text_generate,(0,0))
        screen.blit(text_r,(0,40))
        pygame.display.update()
        
        if(event.type == pygame.QUIT)or(keys[pygame.K_ESCAPE]):
            exit()
        
        if prs:
            pygame.time.wait(1000)
            break
    
    a = list(r[::-1])
    t = 0
    
    for l in range(0,15,2):
        a[l] = str(int(a[l]) * 2)
        
        if int(a[l]) > 9:
            a[l] = str(int(a[l]) - 9)
    
    for l in range(0,15):
        t = t + int(a[l])
    
    if t % 10 == 0:
        r = r + "0"
    else:
        r = r + str(10 - (t % 10))
    
    text_r = font.render(r, True, (0,0,0))
    screen.blit(text_info,(0,80))
    pygame.draw.rect(screen,(0,255,0),menu_4)
    screen.blit(text_r,(0,120))
    pygame.draw.rect(screen,(255,200,200),menu_6)
    screen.blit(text_prompt,(0,200))
    pygame.display.update()
    
    while True:
        event = pygame.event.poll()
        keys = pygame.key.get_pressed()
        prs = pygame.mouse.get_pressed()[0]
        pos = pygame.mouse.get_pos()
        
        if(event.type == pygame.QUIT)or(keys[pygame.K_ESCAPE]):
            exit()

        if prs and menu_6.collidepoint(pos):
            pygame.time.wait(1000)
            break

def generateSIN():
    global event,h,keys,menu_4,menu_6,pos,prs
    text_generate = font.render("Generating... Click to stop", True, (0,0,0))
    text_info = font.render("New Social Insurance Number:", True, (0,0,0))
    text_prompt = font.render("Click to Continue...", True, (0,0,0))
    pygame.time.wait(1000)
    
    while True:
        event = pygame.event.poll()
        keys = pygame.key.get_pressed()
        prs = pygame.mouse.get_pressed()[0]
        pos = pygame.mouse.get_pos()
        
        while True:
            r = str(randint(100000000,999999999))
            a = list(r)
            t = 0
            
            for l in range(1,9,2):
                a[l] = str(int(a[l]) * 2)
                
                if int(a[l]) > 9:
                    a[l] = str(int(a[l]) - 9)
            
            for l in range(0,9):
                t = t + int(a[l])
            
            if t % 10 == 0:
                break
        
        text_r = font.render(r, True, (0,0,0))
        screen.fill((255,255,255))
        screen.blit(text_generate,(0,0))
        screen.blit(text_r,(0,40))
        pygame.display.update()
        
        if(event.type == pygame.QUIT)or(keys[pygame.K_ESCAPE]):
            exit()
        
        if prs:
            pygame.time.wait(1000)
            break
    
    screen.blit(text_info,(0,80))
    pygame.draw.rect(screen,(0,255,0),menu_4)
    screen.blit(text_r,(0,120))
    pygame.draw.rect(screen,(255,200,200),menu_6)
    screen.blit(text_prompt,(0,200))
    pygame.display.update()
    
    while True:
        event = pygame.event.poll()
        keys = pygame.key.get_pressed()
        prs = pygame.mouse.get_pressed()[0]
        pos = pygame.mouse.get_pos()
        
        if(event.type == pygame.QUIT)or(keys[pygame.K_ESCAPE]):
            exit()

        if prs and menu_6.collidepoint(pos):
            pygame.time.wait(1000)
            break

pygame.init()
pygame.display.set_caption("Credit Card Number & SIN Validation")
screen = pygame.display.set_mode((480,240))
font = pygame.font.SysFont("microsoftyahei", 30)
text_menu1 = font.render("Check A Credit Card Number", True, (0,0,0))
text_menu2 = font.render("Generate A Credit Card Number", True, (0,0,0))
text_menu3 = font.render("Check A SIN", True, (0,0,0))
text_menu4 = font.render("Generate A SIN", True, (0,0,0))
text_menu6 = font.render("Exit", True, (0,0,0))

while True:
    event = pygame.event.poll()
    keys = pygame.key.get_pressed()
    pos = pygame.mouse.get_pos()
    prs = pygame.mouse.get_pressed()[0]
    menu_1 = pygame.Rect(0,0,480,40)
    menu_2 = pygame.Rect(0,40,480,40)
    menu_3 = pygame.Rect(0,80,480,40)
    menu_4 = pygame.Rect(0,120,480,40)
    menu_5 = pygame.Rect(0,160,480,40)
    menu_6 = pygame.Rect(0,200,480,40)
    pygame.draw.rect(screen,(225,225,225),menu_1)
    pygame.draw.rect(screen,(200,200,200),menu_2)
    pygame.draw.rect(screen,(225,225,225),menu_3)
    pygame.draw.rect(screen,(200,200,200),menu_4)
    pygame.draw.rect(screen,(255,255,255),menu_5)
    pygame.draw.rect(screen,(255,100,100),menu_6)
    screen.blit(text_menu1,(0,0))
    screen.blit(text_menu2,(0,40))
    screen.blit(text_menu3,(0,80))
    screen.blit(text_menu4,(0,120))
    screen.blit(text_menu6,(0,200))
    pygame.display.update()
    
    if(event.type == pygame.QUIT)or(keys[pygame.K_ESCAPE]):
        exit()
    
    if prs:
        if menu_1.collidepoint(pos):
            num(16)
            ccn()
        elif menu_2.collidepoint(pos):
            generateCCN()
        elif menu_3.collidepoint(pos):
            num(9)
            sin()
        elif menu_4.collidepoint(pos):
            generateSIN()
        elif menu_6.collidepoint(pos):
            exit()
