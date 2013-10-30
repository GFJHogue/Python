from math import sqrt
from sys import exit
from random import randint

import pygame


pygame.init()
pygame.mixer.init()
pygame.display.set_caption("The Legend of Zelda: A Link To The Python")
screen = pygame.display.set_mode((1138,640))
pygame.mixer.music.load("audio/music/title.ogg")
pygame.mixer.music.play()
screen.blit(pygame.image.load("textures/background/title.png"),(0,0))
pygame.display.update()
#pygame.time.wait(15000)
screen.blit(pygame.image.load("textures/background/horse.png"),(0,0))
pygame.display.update()
#pygame.time.wait(5000)


font = pygame.font.Font(None,32)
room = 0
rupees = 0
text_rupees = font.render(str(rupees),True,(0,255,0))
lives = 10
move = 0
sw = 0
text_guide0 = font.render("W",True,(255,255,255))
text_guide1 = font.render("A",True,(255,255,255))
text_guide2 = font.render("S",True,(255,255,255))
text_guide3 = font.render("D",True,(255,255,255))
text_guide4 = font.render("How to move:",True,(0,255,255))
text_guide5 = font.render("Use SPACE with:",True,(0,255,255))
text_guide6 = font.render("<- These are your lives",True,(255,200,200))
text_guide7 = font.render("This is your score ->",True,(200,255,200))
text_guide8 = font.render("Use E on:",True,(0,255,255))
text_guide9 = font.render('Use Z to get out of a "sticky situation"',True,(0,255,255))
text_prompt1 = font.render("What the heck are you doing in that bunny costume? Take it off (Q)!",True,(255,255,0))

#entities
link = pygame.sprite.Sprite()
link.images = [["",[],[],[],[],"",[],[],[],[]],["","",[],"",[],"",[],"",[],""],
    ["","",[],"",[],"",[],"",[],""],[],["","",[],"",[],"",[],"",[],""],
    ["","",[],"",[],"",[],"",[],""]]
    #["",[DR],[D],[DR],[L],"",[R],[UL],[U],[UR]]
link.images[0][1].append(pygame.image.load("textures/entities/linkDL.png"))
link.images[0][1].append(pygame.image.load("textures/entities/linkDL1.png"))
link.images[0][1].append(pygame.image.load("textures/entities/linkDL.png"))
link.images[0][1].append(pygame.image.load("textures/entities/linkDL2.png"))
link.images[0][2].append(pygame.image.load("textures/entities/linkD.png"))
link.images[0][2].append(pygame.image.load("textures/entities/linkD1.png"))
link.images[0][2].append(pygame.image.load("textures/entities/linkD2.png"))
link.images[0][2].append(pygame.image.load("textures/entities/linkD3.png"))
link.images[0][2].append(pygame.image.load("textures/entities/linkD2.png"))
link.images[0][2].append(pygame.image.load("textures/entities/linkD1.png"))
link.images[0][2].append(pygame.image.load("textures/entities/linkD.png"))
link.images[0][2].append(pygame.image.load("textures/entities/linkD4.png"))
link.images[0][2].append(pygame.image.load("textures/entities/linkD5.png"))
link.images[0][2].append(pygame.image.load("textures/entities/linkD6.png"))
link.images[0][2].append(pygame.image.load("textures/entities/linkD5.png"))
link.images[0][2].append(pygame.image.load("textures/entities/linkD4.png"))
link.images[0][3].append(pygame.image.load("textures/entities/linkDR.png"))
link.images[0][3].append(pygame.image.load("textures/entities/linkDR1.png"))
link.images[0][3].append(pygame.image.load("textures/entities/linkDR.png"))
link.images[0][3].append(pygame.image.load("textures/entities/linkDR2.png"))
link.images[0][4].append(pygame.image.load("textures/entities/linkL.png"))
link.images[0][4].append(pygame.image.load("textures/entities/linkL1.png"))
link.images[0][4].append(pygame.image.load("textures/entities/linkL2.png"))
link.images[0][4].append(pygame.image.load("textures/entities/linkL3.png"))
link.images[0][4].append(pygame.image.load("textures/entities/linkL2.png"))
link.images[0][4].append(pygame.image.load("textures/entities/linkL1.png"))
link.images[0][4].append(pygame.image.load("textures/entities/linkL.png"))
link.images[0][4].append(pygame.image.load("textures/entities/linkL4.png"))
link.images[0][4].append(pygame.image.load("textures/entities/linkL5.png"))
link.images[0][4].append(pygame.image.load("textures/entities/linkL6.png"))
link.images[0][4].append(pygame.image.load("textures/entities/linkL5.png"))
link.images[0][4].append(pygame.image.load("textures/entities/linkL4.png"))
link.images[0][6].append(pygame.image.load("textures/entities/linkR.png"))
link.images[0][6].append(pygame.image.load("textures/entities/linkR1.png"))
link.images[0][6].append(pygame.image.load("textures/entities/linkR2.png"))
link.images[0][6].append(pygame.image.load("textures/entities/linkR3.png"))
link.images[0][6].append(pygame.image.load("textures/entities/linkR2.png"))
link.images[0][6].append(pygame.image.load("textures/entities/linkR1.png"))
link.images[0][6].append(pygame.image.load("textures/entities/linkR.png"))
link.images[0][6].append(pygame.image.load("textures/entities/linkR4.png"))
link.images[0][6].append(pygame.image.load("textures/entities/linkR5.png"))
link.images[0][6].append(pygame.image.load("textures/entities/linkR6.png"))
link.images[0][6].append(pygame.image.load("textures/entities/linkR5.png"))
link.images[0][6].append(pygame.image.load("textures/entities/linkR4.png"))
link.images[0][7].append(pygame.image.load("textures/entities/linkUL.png"))
link.images[0][7].append(pygame.image.load("textures/entities/linkUL1.png"))
link.images[0][7].append(pygame.image.load("textures/entities/linkUL.png"))
link.images[0][7].append(pygame.image.load("textures/entities/linkUL2.png"))
link.images[0][8].append(pygame.image.load("textures/entities/linkU.png"))
link.images[0][8].append(pygame.image.load("textures/entities/linkU1.png"))
link.images[0][8].append(pygame.image.load("textures/entities/linkU2.png"))
link.images[0][8].append(pygame.image.load("textures/entities/linkU3.png"))
link.images[0][8].append(pygame.image.load("textures/entities/linkU2.png"))
link.images[0][8].append(pygame.image.load("textures/entities/linkU1.png"))
link.images[0][8].append(pygame.image.load("textures/entities/linkU.png"))
link.images[0][8].append(pygame.image.load("textures/entities/linkU4.png"))
link.images[0][8].append(pygame.image.load("textures/entities/linkU5.png"))
link.images[0][8].append(pygame.image.load("textures/entities/linkU6.png"))
link.images[0][8].append(pygame.image.load("textures/entities/linkU5.png"))
link.images[0][8].append(pygame.image.load("textures/entities/linkU4.png"))
link.images[0][9].append(pygame.image.load("textures/entities/linkUR.png"))
link.images[0][9].append(pygame.image.load("textures/entities/linkUR1.png"))
link.images[0][9].append(pygame.image.load("textures/entities/linkUR.png"))
link.images[0][9].append(pygame.image.load("textures/entities/linkUR2.png"))
link.images[1][2].append(pygame.image.load("textures/entities/link_1D.png"))
link.images[1][2].append(pygame.image.load("textures/entities/link_1D1.png"))
link.images[1][2].append(pygame.image.load("textures/entities/link_1D2.png"))
link.images[1][2].append(pygame.image.load("textures/entities/link_1D3.png"))
link.images[1][2].append(pygame.image.load("textures/entities/link_1D2.png"))
link.images[1][2].append(pygame.image.load("textures/entities/link_1D1.png"))
link.images[1][2].append(pygame.image.load("textures/entities/link_1D.png"))
link.images[1][2].append(pygame.image.load("textures/entities/link_1D1.png"))
link.images[1][2].append(pygame.image.load("textures/entities/link_1D4.png"))
link.images[1][2].append(pygame.image.load("textures/entities/link_1D5.png"))
link.images[1][2].append(pygame.image.load("textures/entities/link_1D4.png"))
link.images[1][2].append(pygame.image.load("textures/entities/link_1D1.png"))
link.images[1][4].append(pygame.image.load("textures/entities/link_1L.png"))
link.images[1][4].append(pygame.image.load("textures/entities/link_1L1.png"))
link.images[1][4].append(pygame.image.load("textures/entities/link_1L2.png"))
link.images[1][4].append(pygame.image.load("textures/entities/link_1L3.png"))
link.images[1][4].append(pygame.image.load("textures/entities/link_1L2.png"))
link.images[1][4].append(pygame.image.load("textures/entities/link_1L1.png"))
link.images[1][4].append(pygame.image.load("textures/entities/link_1L.png"))
link.images[1][4].append(pygame.image.load("textures/entities/link_1L4.png"))
link.images[1][4].append(pygame.image.load("textures/entities/link_1L5.png"))
link.images[1][4].append(pygame.image.load("textures/entities/link_1L6.png"))
link.images[1][4].append(pygame.image.load("textures/entities/link_1L5.png"))
link.images[1][4].append(pygame.image.load("textures/entities/link_1L4.png"))
link.images[1][6].append(pygame.image.load("textures/entities/link_1R.png"))
link.images[1][6].append(pygame.image.load("textures/entities/link_1R1.png"))
link.images[1][6].append(pygame.image.load("textures/entities/link_1R2.png"))
link.images[1][6].append(pygame.image.load("textures/entities/link_1R3.png"))
link.images[1][6].append(pygame.image.load("textures/entities/link_1R2.png"))
link.images[1][6].append(pygame.image.load("textures/entities/link_1R1.png"))
link.images[1][6].append(pygame.image.load("textures/entities/link_1R.png"))
link.images[1][6].append(pygame.image.load("textures/entities/link_1R4.png"))
link.images[1][6].append(pygame.image.load("textures/entities/link_1R5.png"))
link.images[1][6].append(pygame.image.load("textures/entities/link_1R6.png"))
link.images[1][6].append(pygame.image.load("textures/entities/link_1R5.png"))
link.images[1][6].append(pygame.image.load("textures/entities/link_1R4.png"))
link.images[1][8].append(pygame.image.load("textures/entities/link_1U.png"))
link.images[1][8].append(pygame.image.load("textures/entities/link_1U1.png"))
link.images[1][8].append(pygame.image.load("textures/entities/link_1U2.png"))
link.images[1][8].append(pygame.image.load("textures/entities/link_1U3.png"))
link.images[1][8].append(pygame.image.load("textures/entities/link_1U2.png"))
link.images[1][8].append(pygame.image.load("textures/entities/link_1U1.png"))
link.images[1][8].append(pygame.image.load("textures/entities/link_1U.png"))
link.images[1][8].append(pygame.image.load("textures/entities/link_1U4.png"))
link.images[1][8].append(pygame.image.load("textures/entities/link_1U5.png"))
link.images[1][8].append(pygame.image.load("textures/entities/link_1U6.png"))
link.images[1][8].append(pygame.image.load("textures/entities/link_1U5.png"))
link.images[1][8].append(pygame.image.load("textures/entities/link_1U4.png"))
link.images[2][2].append(pygame.image.load("textures/entities/link_2D.png"))
link.images[2][4].append(pygame.image.load("textures/entities/link_2L.png"))
link.images[2][6].append(pygame.image.load("textures/entities/link_2R.png"))
link.images[2][8].append(pygame.image.load("textures/entities/link_2U.png"))
link.images[3].append(pygame.image.load("textures/entities/link_3.png"))
link.images[4][2].append(pygame.image.load("textures/entities/link_4D.png"))
link.images[4][2].append(pygame.image.load("textures/entities/link_4D1.png"))
link.images[4][2].append(pygame.image.load("textures/entities/link_4D2.png"))
link.images[4][2].append(pygame.image.load("textures/entities/link_4D3.png"))
link.images[4][2].append(pygame.image.load("textures/entities/link_4D4.png"))
link.images[4][2].append(pygame.image.load("textures/entities/link_4D5.png"))
link.images[4][4].append(pygame.image.load("textures/entities/link_4L.png"))
link.images[4][4].append(pygame.image.load("textures/entities/link_4L1.png"))
link.images[4][4].append(pygame.image.load("textures/entities/link_4L2.png"))
link.images[4][4].append(pygame.image.load("textures/entities/link_4L3.png"))
link.images[4][4].append(pygame.image.load("textures/entities/link_4L4.png"))
link.images[4][4].append(pygame.image.load("textures/entities/link_4L5.png"))
link.images[4][4].append(pygame.image.load("textures/entities/link_4L6.png"))
link.images[4][4].append(pygame.image.load("textures/entities/link_4L7.png"))
link.images[4][4].append(pygame.image.load("textures/entities/link_4L8.png"))
link.images[4][6].append(pygame.image.load("textures/entities/link_4R.png"))
link.images[4][6].append(pygame.image.load("textures/entities/link_4R1.png"))
link.images[4][6].append(pygame.image.load("textures/entities/link_4R2.png"))
link.images[4][6].append(pygame.image.load("textures/entities/link_4R3.png"))
link.images[4][6].append(pygame.image.load("textures/entities/link_4R4.png"))
link.images[4][6].append(pygame.image.load("textures/entities/link_4R5.png"))
link.images[4][6].append(pygame.image.load("textures/entities/link_4R6.png"))
link.images[4][6].append(pygame.image.load("textures/entities/link_4R7.png"))
link.images[4][6].append(pygame.image.load("textures/entities/link_4R8.png"))
link.images[4][8].append(pygame.image.load("textures/entities/link_4U.png"))
link.images[4][8].append(pygame.image.load("textures/entities/link_4U1.png"))
link.images[4][8].append(pygame.image.load("textures/entities/link_4U2.png"))
link.images[4][8].append(pygame.image.load("textures/entities/link_4U3.png"))
link.images[4][8].append(pygame.image.load("textures/entities/link_4U4.png"))
link.images[4][8].append(pygame.image.load("textures/entities/link_4U5.png"))
link.images[4][8].append(pygame.image.load("textures/entities/link_4U6.png"))
link.images[4][8].append(pygame.image.load("textures/entities/link_4U7.png"))
link.images[4][8].append(pygame.image.load("textures/entities/link_4U8.png"))
link.images[5][2].append(pygame.image.load("textures/entities/link_5D.png"))
link.images[5][2].append(pygame.image.load("textures/entities/link_5D1.png"))
link.images[5][2].append(pygame.image.load("textures/entities/link_5D.png"))
link.images[5][2].append(pygame.image.load("textures/entities/link_5D2.png"))
link.images[5][4].append(pygame.image.load("textures/entities/link_5L.png"))
link.images[5][4].append(pygame.image.load("textures/entities/link_5L1.png"))
link.images[5][6].append(pygame.image.load("textures/entities/link_5R.png"))
link.images[5][6].append(pygame.image.load("textures/entities/link_5R1.png"))
link.images[5][8].append(pygame.image.load("textures/entities/link_5U.png"))
link.images[5][8].append(pygame.image.load("textures/entities/link_5U1.png"))
link.images[5][8].append(pygame.image.load("textures/entities/link_5U.png"))
link.images[5][8].append(pygame.image.load("textures/entities/link_5U2.png"))
link.frame = 0
link.image = link.images[1][2][0]#[facingDirection][frame]
link.rect = link.image.get_rect()
linkXY = [532,284,0,0,72,72,4,2,5]
#[x,y,movex,movey,sizex,sizey,facingDirections,facing,type]

lsoldier = pygame.sprite.Sprite()
lsoldier.images = [["","",[],"",[],"",[],"",[],""],
    ["","",[],"",[],"",[],"",[],""]]
lsoldier.images[0][2].append(pygame.image.load("textures/entities/lSoldierD.png"))
lsoldier.images[0][2].append(pygame.image.load("textures/entities/lSoldierD1.png"))
lsoldier.images[0][4].append(pygame.image.load("textures/entities/lSoldierL.png"))
lsoldier.images[0][4].append(pygame.image.load("textures/entities/lSoldierL1.png"))
lsoldier.images[0][6].append(pygame.image.load("textures/entities/lSoldierR.png"))
lsoldier.images[0][6].append(pygame.image.load("textures/entities/lSoldierR1.png"))
lsoldier.images[0][8].append(pygame.image.load("textures/entities/lSoldierU.png"))
lsoldier.images[0][8].append(pygame.image.load("textures/entities/lSoldierU1.png"))
lsoldier.frame = 0
lsoldier.health = 3
lsoldier.prev = (0,0)
lsoldier.agro = False
lsoldier.image = lsoldier.images[0][4][0]
lsoldier.rect = link.image.get_rect()
lsoldierXY = [1000,400,0,0,72,72,4,4,0]
lsoldier1 = pygame.sprite.Sprite()
lsoldier1.images = lsoldier.images
lsoldier1.frame = 0
lsoldier1.health = 3
lsoldier1.prev = (0,0)
lsoldier1.agro = True
lsoldier1.image = lsoldier1.images[0][4][0]
lsoldier1.rect = lsoldier1.image.get_rect()
lsoldier1XY = [1000,0,0,0,72,72,4,4,0]
lsoldier2 = pygame.sprite.Sprite()
lsoldier2.images = lsoldier.images
lsoldier2.frame = 0
lsoldier2.health = 3
lsoldier2.prev = (0,0)
lsoldier2.agro = True
lsoldier2.image = lsoldier2.images[0][4][0]
lsoldier2.rect = lsoldier2.image.get_rect()
lsoldier2XY = [1000,72,0,0,72,72,4,4,0]
lsoldier3 = pygame.sprite.Sprite()
lsoldier3.images = lsoldier.images
lsoldier3.frame = 0
lsoldier3.health = 3
lsoldier3.prev = (0,0)
lsoldier3.agro = True
lsoldier3.image = lsoldier3.images[0][4][0]
lsoldier3.rect = lsoldier3.image.get_rect()
lsoldier3XY = [1000,144,0,0,72,72,4,4,0]
lsoldier4 = pygame.sprite.Sprite()
lsoldier4.images = lsoldier.images
lsoldier4.frame = 0
lsoldier4.health = 3
lsoldier4.prev = (0,0)
lsoldier4.agro = True
lsoldier4.image = lsoldier4.images[0][4][0]
lsoldier4.rect = lsoldier4.image.get_rect()
lsoldier4XY = [1000,300,0,0,72,72,4,4,0]

tree = pygame.sprite.Sprite()
tree.image = pygame.image.load("textures/entities/tree_1.png")
tree.rect = tree.image.get_rect()
treeXY = [400,300,0,0,128,160,1,2,0]
tree.rect.topleft = (400,300)

chest = pygame.sprite.Sprite()
chest.images = []
chest.images.append(pygame.image.load("textures/entities/chest_1.png"))
chest.images.append(pygame.image.load("textures/entities/chest_1O.png"))
chest.image = chest.images[0]
chest.rect = chest.image.get_rect()
chestXY = [1000,500,0,0,32,32,1,2,0]

bush = pygame.sprite.Sprite()
bush.images = []
bush.images.append(pygame.image.load("textures/entities/bush_1.png"))
bush.images.append(pygame.image.load("textures/entities/bush_1B.png"))
bush.image = bush.images[0]
bush.rect = bush.image.get_rect()
bush.r = True
bush.damage = 0
bushXY = [800,100,0,0,32,32,1,2,0]
bush1 = pygame.sprite.Sprite()
bush1.images = bush.images
bush1.image = bush1.images[0]
bush1.rect = bush1.image.get_rect()
bush1.r = True
bush1.damage = 0
bush1XY = [randint(100,1000),randint(100,500),0,0,32,32,1,2,0]
bush2 = pygame.sprite.Sprite()
bush2.images = bush.images
bush2.image = bush2.images[0]
bush2.rect = bush2.image.get_rect()
bush2.r = True
bush2.damage = 0
bush2XY = [randint(100,1000),randint(100,500),0,0,32,32,1,2,0]
bush3 = pygame.sprite.Sprite()
bush3.images = bush.images
bush3.image = bush3.images[0]
bush3.rect = bush3.image.get_rect()
bush3.r = True
bush3.damage = 0
bush3XY = [randint(100,1000),randint(100,500),0,0,32,32,1,2,0]
bush4 = pygame.sprite.Sprite()
bush4.images = bush.images
bush4.image = bush4.images[0]
bush4.rect = bush4.image.get_rect()
bush4.r = True
bush4.damage = 0
bush4XY = [randint(100,1000),randint(100,500),0,0,32,32,1,2,0]

#items
sword = pygame.sprite.Sprite()
sword.image = pygame.image.load("textures/items/sword.png")
sword.rect = sword.image.get_rect()
swordXY = [0,0,0,0,72,72,1,2,0]

fftyrupees = pygame.sprite.Sprite()
fftyrupees.image = pygame.image.load("textures/items/50rupees.png")
fftyrupees.rect = fftyrupees.image.get_rect()
fftyrupeesXY = [0,0,0,0,72,72,1,2,0]
fftyrupees.value = 50

#HUD
heart = pygame.sprite.Sprite()
heart.images = []
heart.images.append(pygame.image.load("textures/items/heart.png"))
heart.images.append(pygame.image.load("textures/items/heart1.png"))
heart.images.append(pygame.image.load("textures/items/heart2.png"))
heart.image = heart.images[0]
heart.rect = heart.image.get_rect()
heartXY = [0,0,0,0,14,14,1,2,0]

#music
pygame.mixer.music.load("audio/music/rabbit.ogg")

#sounds
sound_sword = []
sound_sword.append(pygame.mixer.Sound("audio/sounds/sword1.ogg"))
sound_sword.append(pygame.mixer.Sound("audio/sounds/sword2.ogg"))
sound_sword.append(pygame.mixer.Sound("audio/sounds/sword3.ogg"))
sound_sword.append(pygame.mixer.Sound("audio/sounds/sword4.ogg"))

sound_damage = pygame.mixer.Sound("audio/sounds/damage.ogg")
sound_death = pygame.mixer.Sound("audio/sounds/death.ogg")

sound_itemfanfare = pygame.mixer.Sound("audio/sounds/itemfanfare.ogg")

sound_grasscut = pygame.mixer.Sound("audio/sounds/grasscut.ogg")

sound_rupee = []
sound_rupee.append(pygame.mixer.Sound("audio/sounds/rupee1.ogg"))
sound_rupee.append(pygame.mixer.Sound("audio/sounds/rupee2.ogg"))

sound_enemychase = pygame.mixer.Sound("audio/sounds/enemychase.ogg")
sound_enemyhit = pygame.mixer.Sound("audio/sounds/enemyhit.ogg")
sound_enemykill = pygame.mixer.Sound("audio/sounds/enemykill.ogg")


def room00():
    global move,room
    sprites(link,moveme(linkXY))
    screen.fill((156,74,74))
    swing("00")
    room00F()
    
    if move != 0:
        if move == 2:
            linkXY[1] = 0
        elif move == 4:
            linkXY[0] = 1136 - 72
        elif move == 6:
            linkXY[0] = 0
        elif move == 8:
            linkXY[1] = 640 - 72
        room = 1
        move = 0

def room00F():
    global rects
    screen.blit(text_guide0,(557,270))
    screen.blit(text_guide1,(525,310))
    screen.blit(text_guide2,(560,350))
    screen.blit(text_guide3,(595,310))
    screen.blit(text_guide4,(500,240))
    screen.blit(text_guide5,(100,100))
    screen.blit(text_guide6,(100,0))
    screen.blit(text_guide7,(880,0))
    screen.blit(text_guide8,(880,100))
    screen.blit(text_guide9,(400,500))
    screen.blit(sword.image,(270,75))
    screen.blit(chest.images[0],(990,95))
    sblit(link,linkXY)
    rects = [pygame.Rect(0,0,1138,640)]

def room01():
    global move,room
    if lsoldier.health > 0:
        npc(lsoldier,lsoldierXY,True,"01")
        sprites(lsoldier,moveme(lsoldierXY))
    
    sprites(link,moveme(linkXY))
    swing("01",[bush,lsoldier],[bushXY,lsoldierXY])
    chests(chest,chestXY,sword,swordXY,link,linkXY)
    bushes(bush,bushXY,linkXY)
    room01F()
    
    if move != 0 and linkXY[8] == 1 and lsoldier.health <= 0:
        if move == 2:
            linkXY[1] = 0
        elif move == 4:
            linkXY[0] = 1136 - 72
        elif move == 6:
            linkXY[0] = 0
        elif move == 8:
            linkXY[1] = 640 - 72
        room = 2

def room01F():
    global rects
    solidobject(linkXY,treeXY,33,45)
    solidobject(linkXY,chestXY,24,24)
    solidobject(lsoldierXY,treeXY,33,45)
    solidobject(lsoldierXY,chestXY,24,24)
    screen.blit(text_prompt1,(100,0))
    sblit(bush,bushXY)
    sblit(link,linkXY)
    
    if lsoldier.health > 0:
        sblit(lsoldier,lsoldierXY)
    
    sblit(tree,treeXY)
    sblit(chest,chestXY)
    layer(link,linkXY,tree,treeXY)
    layer(link,linkXY,chest,chestXY)
    layer(link,linkXY,bush,bushXY,bush.r)
    pickup(fftyrupees,fftyrupeesXY)
    rects = [link.rect, tree.rect, chest.rect, sword.rect, bush.rect,
        fftyrupees.rect, lsoldier.rect, pygame.Rect(0,0,1138,32)]

def room02():
    global sw
    if lsoldier1.health > 0:
        npc(lsoldier1,lsoldier1XY,True,"02")
        sprites(lsoldier1,moveme(lsoldier1XY))
    if lsoldier2.health > 0:
        npc(lsoldier2,lsoldier2XY,True,"02")
        sprites(lsoldier2,moveme(lsoldier2XY))
    if lsoldier3.health > 0:
        npc(lsoldier3,lsoldier3XY,True,"02")
        sprites(lsoldier3,moveme(lsoldier3XY))
    if lsoldier4.health > 0:
        npc(lsoldier4,lsoldier4XY,True,"02")
        sprites(lsoldier4,moveme(lsoldier4XY))
    
    if(lsoldier1.health <= 0 and lsoldier2.health <= 0 and
            lsoldier3.health <= 0 and lsoldier4.health <= 0):
        if sw == 0:
            pygame.mixer.music.load("audio/music/overworld.ogg")
            pygame.mixer.music.play()
            sw = 1
        
        screen.blit(text_prompt1,(100,0))
    
    sprites(link,moveme(linkXY))
    swing("02",[lsoldier1,lsoldier2,lsoldier3,lsoldier4,bush1,bush2,bush3,bush4],
        [lsoldier1XY,lsoldier2XY,lsoldier3XY,lsoldier4XY,bush1XY,bush2XY,bush3XY,bush4XY])
    bushes(bush1,bush1XY,linkXY)
    bushes(bush2,bush2XY,linkXY)
    bushes(bush3,bush3XY,linkXY)
    bushes(bush4,bush4XY,linkXY)
    room02F()

def room02F():
    global rects
    sblit(bush1,bush1XY)
    sblit(bush2,bush2XY)
    sblit(bush3,bush3XY)
    sblit(bush4,bush4XY)
    sblit(link,linkXY)
    
    if lsoldier1.health > 0:
        sblit(lsoldier1,lsoldier1XY)
    if lsoldier2.health > 0:
        sblit(lsoldier2,lsoldier2XY)
    if lsoldier3.health > 0:
        sblit(lsoldier3,lsoldier3XY)
    if lsoldier4.health > 0:
        sblit(lsoldier4,lsoldier4XY)
    
    layer(link,linkXY,bush1,bush1XY,bush1.r)
    layer(link,linkXY,bush2,bush2XY,bush2.r)
    layer(link,linkXY,bush3,bush3XY,bush3.r)
    layer(link,linkXY,bush4,bush4XY,bush4.r)
    pickup(fftyrupees,fftyrupeesXY)
    rects = [link.rect,lsoldier1.rect,lsoldier2.rect,lsoldier3.rect,
        lsoldier4.rect,bush1.rect,bush2.rect,bush3.rect,bush4.rect,pygame.Rect(0,0,1138,32)]

def rooms(r):
    if r == "00":
        room00F()
    elif r == "01":
        room01F()
    elif r == "02":
        room02F()

def coords(s):#len(s) >= 2
    return((s[0],s[1]))#(x,y)

def rectlist(l):
    rl = []
    for c in range(0,len(l)):
        rl.append(l[c].rect)
    return(rl)

def moveme(c):#len(c) >= 6
    global move,linkXY
    c[0] = c[0] + c[2]
    c[1] = c[1] + c[3]
    if(c[0] < 0):
        c[0] = c[0] - c[2]
        if c == linkXY:
            move = 4
    elif(c[0] > 1138 - c[4]):
        c[0] = c[0] - c[2]
        if c == linkXY:
            move = 6
    if(c[1] < 0):
        c[1] = c[1] - c[3]
        if c == linkXY:
            move = 8
    elif(c[1] > 640 - c[5]):
        c[1] = c[1] - c[3]
        if c == linkXY:
            move = 2
    return(c)

def sblit(s,c):#len(c) >= 2
    s.rect.topleft = coords(c)
    return(screen.blit(s.image,s.rect))

def sprites(s,c):#len(c) >= 9
    if(c[6] == 8):
        if(c[2] < 0) and (c[3] > 0):
            c[7] = 1
        elif(c[2] > 0) and (c[3] > 0):
            c[7] = 3
        elif(c[2] < 0) and (c[3] < 0):
            c[7] = 7
        elif(c[2] > 0) and (c[3] < 0):
            c[7] = 9
        elif(c[3] > 0):
            c[7] = 2
        elif(c[2] < 0):
            c[7] = 4
        elif(c[2] > 0):
            c[7] = 6
        elif(c[3] < 0):
            c[7] = 8
    elif(c[6] == 4):
        if(c[2] < 0):
            c[7] = 4
        elif(c[2] > 0):
            c[7] = 6
        elif(c[3] > 0):
            c[7] = 2
        elif(c[3] < 0):
            c[7] = 8
    if(c[2] == 0) and (c[3] == 0):
        s.frame = 0
        s.image = s.images[c[8]][c[7]][0]
    else:
        s.frame = s.frame + 0.33
        if(s.frame > len(s.images[c[8]][c[7]])):
            s.frame = 0
        s.image = s.images[c[8]][c[7]][int(s.frame)]

def swing(r,e = [],exy = []):#len(e) == len(exy)
    if(keys[pygame.K_SPACE]) and (linkXY[8] == 1):
        sound_sword[randint(0,3)].play()
        div = 1
        if(linkXY[7] == 2):
            linkXY[0] = linkXY[0] + 6
            linkXY[1] = linkXY[1] + 10
            div = 2
        elif(linkXY[7] == 4):
            linkXY[0] = linkXY[0] - 12
            linkXY[1] = linkXY[1] + 6
        elif(linkXY[7] == 6):
            linkXY[0] = linkXY[0] + 12
            linkXY[1] = linkXY[1] + 6
        elif(linkXY[7] == 8):
            linkXY[0] = linkXY[0] - 4
            linkXY[1] = linkXY[1] - 14
        
        for frame in range(0,9):
            link.image = link.images[4][linkXY[7]][int(frame / div)]
            screen.fill((74,156,74))
            rooms(r)
            pygame.display.update([link.rect])
            pygame.time.wait(20)
        
        if(linkXY[7] == 2):
            linkXY[0] = linkXY[0] - 6
            linkXY[1] = linkXY[1] - 10
        elif(linkXY[7] == 4):
            linkXY[0] = linkXY[0] + 12
            linkXY[1] = linkXY[1] - 6
        elif(linkXY[7] == 6):
            linkXY[0] = linkXY[0] - 12
            linkXY[1] = linkXY[1] - 6
        elif(linkXY[7] == 8):
            linkXY[0] = linkXY[0] + 4
            linkXY[1] = linkXY[1] + 14
        
        if(link.rect.collidelistall(rectlist(e))):
            en = link.rect.inflate(20,20).collidelistall(rectlist(e))[0]
            if(((linkXY[7] == 2) and (linkXY[1] < exy[en][1])) or 
                    ((linkXY[7] == 4) and (linkXY[0] > exy[en][0])) or 
                    ((linkXY[7] == 6) and (linkXY[0] < exy[en][0])) or 
                    ((linkXY[7] == 8) and (linkXY[1] > exy[en][1]))):
                e[en].damage = 1
                
                if(e[en] == link or e[en] == lsoldier or e[en] == lsoldier1
                        or e[en] == lsoldier2 or e[en] == lsoldier3
                        or e[en] == lsoldier4):
                    damaged(1,e[en],exy[en],linkXY,r)
        
        sprites(link,linkXY)
        screen.fill((74,156,74))
        rooms(r)
        pygame.display.update()

def solidobject(c,o,h,v):#len(c) >= 6,len(o) >= 6
    if((c[0] + c[4] - h > o[0]) and (c[0] + h < o[0] + o[4]) and 
            (c[1] + c[5] - v > o[1]) and (c[1] + v < o[1] + o[5])):
        c[0] = c[0] - c[2]
        c[1] = c[1] - c[3]

def layer(a,axy,b,bxy,r = True):#len(axy) >= 6, len(bxy) >= 6
    if(pygame.sprite.collide_rect(a,b)) and (r == True):
        if(axy[1] + axy[5] / 2 > bxy[1] + bxy[5] / 2):
            sblit(b,bxy)
            sblit(a,axy)
        else:
            sblit(a,axy)
            sblit(b,bxy)

def chests(c,cxy,i,ixy,s,sxy):
    global rects
    if((keys[pygame.K_e]) and (pygame.sprite.collide_rect(s,c)) and 
            (c.image == c.images[0])):
        c.image = c.images[1]
        s.image = s.images[3][0]
        ixy[0] = sxy[0]
        ixy[1] = sxy[1] - 35
        rooms("01")
        sblit(i,ixy)
        pygame.display.update(rects)
        if(i == sword):
            sxy[8] = 1
            sxy[6] = 4
            sxy[7] = 2
        pygame.mixer.music.pause()
        sound_itemfanfare.play()
        pygame.time.wait(1020)
        pygame.mixer.music.unpause()
        screen.fill((74,156,74))

def bushes(b,bxy,sxy):
    if(b.damage == 1) and (b.image == b.images[0]):
        sound_grasscut.play()
        b.damage = 3
        b.image = b.images[1]
        b.r = False
        drop(bxy,0)
    if(b.image == b.images[0]):
        solidobject(sxy,bxy,24,20)
        b.r = True

def drop(lxy,t):
    if(t == 0):
        fftyrupeesXY[0] = lxy[0]
        fftyrupeesXY[1] = lxy[1]
        fftyrupeesXY[8] = 1

def pickup(i,ixy):#len(ixy) >= 9
    global rupees,text_rupees
    if(ixy[8] == 1):
        sblit(i,ixy)
        if(i.rect.colliderect(link.rect.inflate(-24,-24))):
            sound_rupee[randint(0,1)].play()
            ixy[8] = 0
            rupees = rupees + i.value
            text_rupees = font.render(str(rupees),True,(0,255,0))

def npc(s,c,e,r):
    if coords(c) == s.prev or randint(0,49) == 0:
        c[7] = randint(1,4) * 2
    
    if(e == True and ((c[7] == 2 and c[0] - c[4] <= linkXY[0] <= c[0] + c[4]
            and c[1] < linkXY[1] < c[1] + (5 * c[5])) or
            (c[7] == 4 and c[1] - c[5] <= linkXY[1] <= c[1] + c[5]
            and c[0] > linkXY[0] > c[0] - (5 * c[4])) or
            (c[7] == 6 and c[1] - c[5] <= linkXY[1] <= c[1] + c[5]
            and c[0] < linkXY[0] < c[0] + (5 * c[4])) or
            (c[7] == 8 and c[0] - c[4] <= linkXY[0] <= c[0] + c[4]
            and c[1] > linkXY[1] > c[1] - (5 * c[5]))) and s.agro == False):
        sound_enemychase.play()
        s.agro = True
    else:
        if c[7] == 2:
            c[2] = 0
            c[3] = 2
        elif c[7] == 4:
            c[3] = 0
            c[2] = -2
        elif c[7] == 6:
            c[3] = 0
            c[2] = 2
        elif c[7] == 8:
            c[2] = 0
            c[3] = -2
    
    if s.agro == True:
        if c[0] < linkXY[0]:
            c[2] =(2 * (linkXY[0] - c[0]) /
                sqrt((linkXY[0] - c[0]) ** 2 + (linkXY[1] - c[1]) ** 2))
            c[3] =(2 * (linkXY[1] - c[1]) /
                sqrt((linkXY[0] - c[0]) ** 2 + (linkXY[1] - c[1]) ** 2))
        elif c[0] > linkXY[0]:
            c[2] =(2 * (linkXY[0] - c[0]) /
                sqrt((linkXY[0] - c[0]) ** 2 + (linkXY[1] - c[1]) ** 2))
            c[3] =(2 * (linkXY[1] - c[1]) /
                sqrt((linkXY[0] - c[0]) ** 2 + (linkXY[1] - c[1]) ** 2))
        else:
            c[2] = 0
        
        if(s.rect.inflate(-72,-72).colliderect(link.rect) and
                (((c[7] == 2) and (c[1] < linkXY[1])) or 
                ((c[7] == 4) and (c[0] > linkXY[0])) or 
                ((c[7] == 6) and (c[0] < linkXY[0])) or 
                ((c[7] == 8) and (c[1] > linkXY[1])))):
            damaged(1,link,linkXY,c,r)
    s.prev = (c[0],c[1])

def damaged(a,s,c,g,r):
    global lives
    prev = c[8]
    
    if s == link:
        sound_damage.play()
        lives = lives - a
        c[8] = 2
        c[6] = 4
        
        if 1 <= c[7] <= 3:
            c[7] = 2
        elif 7 <= c[7] <= 9:
            c[7] = 8
    else:
        sound_enemyhit.play()
        s.health = s.health - a
        s.agro = True
    
    for d in range(0,9):
        s.frame = 0
        sprites(s,c)
        
        if c[1] < g[1]:
            c[1] = c[1] - 6
        elif c[1] > g[1]:
            c[1] = c[1] + 6
        elif c[0] > g[0]:
            c[0] = c[0] + 6
        elif c[0] < g[0]:
            c[0] = c[0] - 6
        
        moveme(c)
        screen.fill((74,156,74))
        sblit(s,c)
        rooms(r)
        pygame.display.update([s.rect])
        pygame.time.wait(20)
    
    if lives <= 0:
        sound_death.play()
        pygame.mixer.music.load("audio/music/fortune.ogg")
        pygame.mixer.music.play()
        screen.blit(pygame.image.load("textures/background/lose.png"),(0,0))
        pygame.display.update()
        while True:
            event = pygame.event.poll()
            keys = pygame.key.get_pressed()
            
            if(event.type == pygame.QUIT) or (keys[pygame.K_ESCAPE]):
                exit()
            if keys[pygame.K_m]:
                screen.blit(pygame.image.load("textures/background/mikitz.png"),(0,0))
                pygame.display.update()
    elif s != link and s.health <= 0:
        sound_enemykill.play()
    
    if s == link:
        c[8] = prev

def hearts(l,t):
    for c in range(1,t+2):
        if c < l + 1:
            if c % 2 == 1:
                screen.blit(heart.images[1],((c + 1) * 8,5))
            elif c % 2 == 0:
                screen.blit(heart.images[0],(c * 8,5))
        elif c != l + 1 and c % 2 == 0:
            screen.blit(heart.images[2],(c * 8,5))


screen.fill((74,156,74))
pygame.display.update()

pygame.mixer.music.play()
intro = 1


while True:
    pos = pygame.mixer.music.get_pos()
    if(7055 > pos > 7005) and (intro == 1):
        pygame.mixer.music.play(-1,7.03)
        intro = 0
    if(pos > 34965) and room != 0:
        pygame.mixer.music.play(-1,7.03)
    event = pygame.event.poll()
    keys = pygame.key.get_pressed()
    if(event.type == pygame.QUIT) or (keys[pygame.K_ESCAPE]):
        exit()
    if(keys[pygame.K_w]):
        linkXY[3] = -4
    if(keys[pygame.K_a]):
        linkXY[2] = -4
    if(keys[pygame.K_s]):
        linkXY[3] = 4
    if(keys[pygame.K_d]):
        linkXY[2] = 4
    if(((keys[pygame.K_w]) and (keys[pygame.K_s])) or 
            ((keys[pygame.K_w] == False) and (keys[pygame.K_s] == False))):
        linkXY[3] = 0
    if(((keys[pygame.K_a]) and (keys[pygame.K_d])) or 
            ((keys[pygame.K_a] == False) and (keys[pygame.K_d] == False))):
        linkXY[2] = 0
    if keys[pygame.K_z]:
        linkXY[0] = 532
        linkXY[1] = 284
        screen.fill((74,156,74))
        pygame.display.update()
    if keys[pygame.K_q]:
        linkXY[8] = 0
        linkXY[6] = 8
        text_prompt1 = font.render("Find a weapon",True,(255,255,0))
    if keys[pygame.K_b]:
        linkXY[8] = 5
        linkXY[6] = 4
    
    screen.fill((74,156,74))
    
    if room == 0:
        room00()
        
        if room != 0:
            pygame.mixer.music.load("audio/music/overworld.ogg")
            pygame.mixer.music.play()
            screen.fill((74,156,74))
    elif room == 1:
        move = 0
        room01()
        
        if room != 1:
            pygame.mixer.music.load("audio/music/kakarikovillagesoldiers.ogg")
            pygame.mixer.music.play()
            screen.fill((74,156,74))
            text_prompt1 = font.render("Now get 200 Points to buy that thing" +
                " you really want.",True,(255,255,0))
    elif room == 2:
        room02()
        if rupees >= 200:
            pygame.time.wait(3000)
            pygame.mixer.music.load("audio/music/ending.ogg")
            pygame.mixer.music.play()
            screen.blit(pygame.image.load("textures/background/win.png"),(0,0))
            screen.blit(text_rupees,(1099,0))
            pygame.display.update()
            while True:
                event = pygame.event.poll()
                keys = pygame.key.get_pressed()
                
                if(event.type == pygame.QUIT) or (keys[pygame.K_ESCAPE]):
                    exit()
                if keys[pygame.K_m]:
                    screen.blit(pygame.image.load("textures/background/mikitz.png"),(0,0))
                    screen.blit(pygame.image.load("textures/background/horse.png"),(0,0))
                    pygame.display.update()

    screen.blit(text_rupees,(1099,0))
    
    hearts(lives,10)
    pygame.display.update(rects)
    pygame.time.wait(20)
