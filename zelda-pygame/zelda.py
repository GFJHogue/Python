import sys
import pygame

pygame.init()
pygame.display.set_caption("The Legend of Zelda: A Link To The Python")
screen=pygame.display.set_mode((1138,640))
font=pygame.font.Font(None,100)
text_intro0=font.render("The Legend of Zelda:",True,(255,0,0),(74,156,74))
text_intro1=font.render("A Link To The Python",True,(255,255,128),(74,156,74))
screen.fill((74,156,74))
screen.blit(text_intro0,(100,200))
screen.blit(text_intro1,(400,340))
pygame.display.flip()
pygame.time.wait(2000)

#entities
link=pygame.sprite.Sprite()
link.images=[["",[],[],[],[],"",[],[],[],[]],["","",[],"",[],"",[],"",[],""],["","",[],"",[],"",[],"",[],""],[]]#["",[DR],[D],[DR],[L],"",[R],[UL],[U],[UR]]
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
link.frame=0
link.image=link.images[1][2][0]#[facingDirection][frame]
link.rect=link.image.get_rect()
linkXY=[0,0,0,0,72,72,8,2,0]#[x,y,movex,movey,sizex,sizey,facingDirections,facing,type]

tree=pygame.sprite.Sprite()
tree.image=pygame.image.load("textures/entities/tree_1.png")
tree.rect=tree.image.get_rect()
treeXY=[400,300,0,0,128,160,1,2,0]
tree.rect.topleft=(400,300)

chest=pygame.sprite.Sprite()
chest.images=[]
chest.images.append(pygame.image.load("textures/entities/chest_1.png"))
chest.images.append(pygame.image.load("textures/entities/chest_1O.png"))
chest.image=chest.images[0]
chest.rect=chest.image.get_rect()
chestXY=[1000,500,0,0,32,32,1,2,0]

#items
sword=pygame.sprite.Sprite()
sword.image=pygame.image.load("textures/items/sword.png")
sword.rect=sword.image.get_rect()
swordXY=[0,0,0,0,72,72,1,2,0]


def coords(s):
    return((s[0],s[1]))#(x,y)

def moveme(c):
    c[0]=c[0]+c[2]
    c[1]=c[1]+c[3]
    if(c[0]<0)or(c[0]>1138-c[4]):
        c[0]=c[0]-c[2]
    if(c[1]<0)or(c[1]>640-c[5]):
        c[1]=c[1]-c[3]
    return(c)

def blit(s,c):
    s.rect.topleft=coords(c)
    return(screen.blit(s.image,s.rect))

def sprites(s,c):
    if(c[6]==8):
        if(c[2]<0)and(c[3]>0):
            c[7]=1
        elif(c[2]>0)and(c[3]>0):
            c[7]=3
        elif(c[2]<0)and(c[3]<0):
            c[7]=7
        elif(c[2]>0)and(c[3]<0):
            c[7]=9
        elif(c[3]>0):
            c[7]=2
        elif(c[2]<0):
            c[7]=4
        elif(c[2]>0):
            c[7]=6
        elif(c[3]<0):
            c[7]=8
    elif(c[6]==4):
        if(c[3]>0):
            c[7]=2
        elif(c[3]<0):
            c[7]=8
        elif(c[2]<0):
            c[7]=4
        elif(c[2]>0):
            c[7]=6
    if(c[2]==0)and(c[3]==0):
        s.frame=0
        s.image=s.images[c[8]][c[7]][0]
    else:
        s.frame=s.frame+0.33
        if(s.frame>len(s.images[c[8]][c[7]])-1):
            s.frame=0
        s.image=s.images[c[8]][c[7]][int(s.frame)]
    return

def solidobject(c,o,h,v):
    if(c[0]+c[4]-h>o[0])and(c[0]+h<o[0]+o[4])and(c[1]+c[5]-v>o[1])and(c[1]+v<o[1]+o[5]):
        c[0]=c[0]-c[2]
        c[1]=c[1]-c[3]
    return

def layer(a,axy,b,bxy):
    if(pygame.sprite.collide_rect(a,b)):
        if(axy[1]+axy[5]/2>bxy[1]+bxy[5]/2):
            blit(b,bxy)
            blit(a,axy)
        else:
            blit(a,axy)
            blit(b,bxy)
    return

def chests(c,cxy,i,ixy,s,sxy):
    if(keys[pygame.K_SPACE])and(pygame.sprite.collide_rect(s,c)):
        c.image=c.images[1]
        s.image=s.images[3][0]
        ixy[0]=sxy[0]
        ixy[1]=sxy[1]-35
        blit(c,cxy)
        blit(s,sxy)
        blit(i,ixy)
        pygame.display.update([link.rect,chest.rect,sword.rect])
        if(i==sword):
            sxy[8]=1
            sxy[6]=4
        pygame.time.wait(5000)
        screen.fill((74,156,74))

screen.fill((74,156,74))
pygame.display.update()

while(True):
    event=pygame.event.poll()
    keys=pygame.key.get_pressed()
    if(event.type==pygame.QUIT)or(keys[pygame.K_ESCAPE]):
        sys.exit()
    if(keys[pygame.K_w]):
        linkXY[3]=-4
    if(keys[pygame.K_a]):
        linkXY[2]=-4
    if(keys[pygame.K_s]):
        linkXY[3]=4
    if(keys[pygame.K_d]):
        linkXY[2]=4
    if((keys[pygame.K_w])and(keys[pygame.K_s]))or((keys[pygame.K_w]==False)and(keys[pygame.K_s]==False)):
        linkXY[3]=0
    if((keys[pygame.K_a])and(keys[pygame.K_d]))or((keys[pygame.K_a]==False)and(keys[pygame.K_d]==False)):
        linkXY[2]=0

    screen.fill((74,156,74))

    sprites(link,moveme(linkXY))
    solidobject(linkXY,treeXY,33,45)
    solidobject(linkXY,chestXY,24,24)
    
    chests(chest,chestXY,sword,swordXY,link,linkXY)

    blit(link,linkXY)
    blit(chest,chestXY)
    blit(tree,treeXY)
    layer(link,linkXY,tree,treeXY)
    layer(link,linkXY,chest,chestXY)

    pygame.display.update([link.rect,tree.rect,chest.rect,sword.rect])
    pygame.time.wait(23)
