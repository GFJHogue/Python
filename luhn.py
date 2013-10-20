#School Assignment that deals with number validation using the Luhn Algorithm.

from os import system
from random import randint
from sys import exit

import pygame


def num(d):
    global n
    
    while True:
        n = raw_input("Enter a " + str(d) + " Digit Number: ")
        
        if n.isdigit() and len(n) == d:
            system("cls")
            return True
        
        system("cls")
        print "[ERROR] Please Try Again.\n"

def ccn():
    validate(list(n[len(n) - 2::-1]),0, int(n[len(n) - 1]))

def sin():
    validate(list(n),1,0)

def validate(a,m,c):
    global h,n
    t = 0
    
    for l in range(m, len(a),2):
        a[l] = str(int(a[l]) * 2)
        
        if int(a[l]) > 9:
            a[l] = str(int(a[l]) - 9)
    
    for l in range(0, len(a)):
        t = t + int(a[l])
    
    if (10 - (t % 10) == c and m == 0) or t % 10 == c:
        print 'The Number, "' + n + '", is Valid.'
        h.append(n + ", Valid")
    else:
        print 'The Number, "' + n + '", is NOT Valid.'
        h.append(n + ", Invalid")

def generateCCN():
    global h
    r = str(randint(100000000000000,999999999999999))
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
    
    print 'New Credit Card Number: "' + r + '"'
    h.append(r + ", Generated")

def generateSIN():
    global h
    
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
    
    print 'New Social Insurance Number: "' + r + '"'
    h.append(r + ", Generated")

h = []
pygame.init()
pygame.display.set_caption("Credit Card Number & SIN Validation")
screen = pygame.display.set_mode((600,240))
font = pygame.font.Font(None,40)
text_menu1 = font.render("1. Check A Credit Card Number", True, (0,0,0))
text_menu2 = font.render("2. Check A Social Insurance Number", True, (0,0,0))
text_menu3 = font.render("3. Generate A Credit Card Number", True, (0,0,0))
text_menu4 = font.render("4. Generate A Social Insurance Number", True, (0,0,0))
text_menu5 = font.render("5. View History", True, (0,0,0))
text_menu6 = font.render("6. Exit", True, (0,0,0))

while True:
    event = pygame.event.poll()
    keys = pygame.key.get_pressed()
    pos = pygame.mouse.get_pos()
    prs = pygame.mouse.get_pressed()[0]
    menu_1 = pygame.Rect(0,0,600,40)
    menu_2 = pygame.Rect(0,40,600,40)
    menu_3 = pygame.Rect(0,80,600,40)
    menu_4 = pygame.Rect(0,120,600,40)
    menu_5 = pygame.Rect(0,160,600,40)
    menu_6 = pygame.Rect(0,200,600,40)
    pygame.draw.rect(screen,(255,0,0),menu_1)
    pygame.draw.rect(screen,(255,200,200),menu_2)
    pygame.draw.rect(screen,(255,0,0),menu_3)
    pygame.draw.rect(screen,(255,200,200),menu_4)
    pygame.draw.rect(screen,(255,0,0),menu_5)
    pygame.draw.rect(screen,(255,200,200),menu_6)
    screen.blit(text_menu1,(0,0))
    screen.blit(text_menu2,(0,40))
    screen.blit(text_menu3,(0,80))
    screen.blit(text_menu4,(0,120))
    screen.blit(text_menu5,(0,160))
    screen.blit(text_menu6,(0,200))
    pygame.draw.circle(screen,(0,255,0),pos,3)
    pygame.display.update()
    
    if(event.type == pygame.QUIT)or(keys[pygame.K_ESCAPE]):
        exit()
    
    print ("\n1. Check A Credit Card Number\n2. Check A Social Insurance Num" +
        "ber\n3. Generate A Credit Card Number\n4. Generate A Social Insuran" +
        "ce Number\n5. View History\n6. Exit\n")
    print pos
    menu = ""
    system("cls")
    
    if prs:
        if menu_1.collidepoint(pos):
            num(16)
            ccn()
        elif menu_2.collidepoint(pos):
            num(9)
            sin()
        elif menu_3.collidepoint(pos):
            generateCCN()
        elif menu_4.collidepoint(pos):
            generateSIN()
        elif menu_5.collidepoint(pos):
            print "[HISTORY]"
            
            for l in range(0, len(h)):
                print str(l+1) + ". " + h[l] + "\n"
            
        elif menu_6.collidepoint(pos):
            exit()
