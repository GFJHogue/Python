import sys
import pygame

pygame.init()
pygame.display.set_caption("The Legend of Zelda: A Link To The Python")
screen=pygame.display.set_mode((1138,640))


link=pygame.sprite.Sprite()
link.images=["",[],[],[],[],"",[],[],[],[]]#["",[DR],[D],[DR],[L],"",[R],[UL],[U],[UR]]
link.images[1].append(pygame.image.load("textures/entities/linkDL.png"))
link.images[1].append(pygame.image.load("textures/entities/linkDL1.png"))
link.images[1].append(pygame.image.load("textures/entities/linkDL.png"))
link.images[1].append(pygame.image.load("textures/entities/linkDL2.png"))
link.images[2].append(pygame.image.load("textures/entities/linkD.png"))
link.images[2].append(pygame.image.load("textures/entities/linkD1.png"))
link.images[2].append(pygame.image.load("textures/entities/linkD2.png"))
link.images[2].append(pygame.image.load("textures/entities/linkD3.png"))
link.images[2].append(pygame.image.load("textures/entities/linkD2.png"))
link.images[2].append(pygame.image.load("textures/entities/linkD1.png"))
link.images[2].append(pygame.image.load("textures/entities/linkD.png"))
link.images[2].append(pygame.image.load("textures/entities/linkD4.png"))
link.images[2].append(pygame.image.load("textures/entities/linkD5.png"))
link.images[2].append(pygame.image.load("textures/entities/linkD6.png"))
link.images[2].append(pygame.image.load("textures/entities/linkD5.png"))
link.images[2].append(pygame.image.load("textures/entities/linkD4.png"))
link.images[3].append(pygame.image.load("textures/entities/linkDR.png"))
link.images[3].append(pygame.image.load("textures/entities/linkDR1.png"))
link.images[3].append(pygame.image.load("textures/entities/linkDR.png"))
link.images[3].append(pygame.image.load("textures/entities/linkDR2.png"))
link.images[4].append(pygame.image.load("textures/entities/linkL.png"))
link.images[4].append(pygame.image.load("textures/entities/linkL1.png"))
link.images[4].append(pygame.image.load("textures/entities/linkL2.png"))
link.images[4].append(pygame.image.load("textures/entities/linkL3.png"))
link.images[4].append(pygame.image.load("textures/entities/linkL2.png"))
link.images[4].append(pygame.image.load("textures/entities/linkL1.png"))
link.images[4].append(pygame.image.load("textures/entities/linkL.png"))
link.images[4].append(pygame.image.load("textures/entities/linkL4.png"))
link.images[4].append(pygame.image.load("textures/entities/linkL5.png"))
link.images[4].append(pygame.image.load("textures/entities/linkL6.png"))
link.images[4].append(pygame.image.load("textures/entities/linkL5.png"))
link.images[4].append(pygame.image.load("textures/entities/linkL4.png"))
link.images[6].append(pygame.image.load("textures/entities/linkR.png"))
link.images[6].append(pygame.image.load("textures/entities/linkR1.png"))
link.images[6].append(pygame.image.load("textures/entities/linkR2.png"))
link.images[6].append(pygame.image.load("textures/entities/linkR3.png"))
link.images[6].append(pygame.image.load("textures/entities/linkR2.png"))
link.images[6].append(pygame.image.load("textures/entities/linkR1.png"))
link.images[6].append(pygame.image.load("textures/entities/linkR.png"))
link.images[6].append(pygame.image.load("textures/entities/linkR4.png"))
link.images[6].append(pygame.image.load("textures/entities/linkR5.png"))
link.images[6].append(pygame.image.load("textures/entities/linkR6.png"))
link.images[6].append(pygame.image.load("textures/entities/linkR5.png"))
link.images[6].append(pygame.image.load("textures/entities/linkR4.png"))
link.images[7].append(pygame.image.load("textures/entities/linkUL.png"))
link.images[7].append(pygame.image.load("textures/entities/linkUL1.png"))
link.images[7].append(pygame.image.load("textures/entities/linkUL.png"))
link.images[7].append(pygame.image.load("textures/entities/linkUL2.png"))
link.images[8].append(pygame.image.load("textures/entities/linkU.png"))
link.images[8].append(pygame.image.load("textures/entities/linkU1.png"))
link.images[8].append(pygame.image.load("textures/entities/linkU2.png"))
link.images[8].append(pygame.image.load("textures/entities/linkU3.png"))
link.images[8].append(pygame.image.load("textures/entities/linkU2.png"))
link.images[8].append(pygame.image.load("textures/entities/linkU1.png"))
link.images[8].append(pygame.image.load("textures/entities/linkU.png"))
link.images[8].append(pygame.image.load("textures/entities/linkU4.png"))
link.images[8].append(pygame.image.load("textures/entities/linkU5.png"))
link.images[8].append(pygame.image.load("textures/entities/linkU6.png"))
link.images[8].append(pygame.image.load("textures/entities/linkU5.png"))
link.images[8].append(pygame.image.load("textures/entities/linkU4.png"))
link.images[9].append(pygame.image.load("textures/entities/linkUR.png"))
link.images[9].append(pygame.image.load("textures/entities/linkUR1.png"))
link.images[9].append(pygame.image.load("textures/entities/linkUR.png"))
link.images[9].append(pygame.image.load("textures/entities/linkUR2.png"))
link.frame=0
link.image=link.images[2][0]#[facingDirection][frame]
link.rect=link.image.get_rect()
linkXY=[0,0,0,0,72,72,8,2]#[x,y,movex,movey,sizex,sizey,facingDirections,facing]

tree=pygame.sprite.Sprite()
tree.image=pygame.image.load("textures/entities/tree_1.png")
tree.rect=tree.image.get_rect()
treeXY=[400,300,0,0,128,160,1,2]


def coords(s):
    return((s[0],s[1]))#(x,y)

def moveme(c):
    c[0]=c[0]+c[2]
    c[1]=c[1]+c[3]
    if(c[0]<0)or(c[0]>1138-c[4]):
        c[0]=c[0]-c[2]
    if(c[1]<0)or(c[1]>640-c[5]):
        c[1]=c[1]-c[3]
    return

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
        s.image=s.images[c[7]][0]
    else:
        s.frame=s.frame+0.33
        if(s.frame>len(s.images[c[7]])-1):
            s.frame=0
        s.image=s.images[c[7]][int(s.frame)]
    return


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
    moveme(linkXY)
    sprites(link,linkXY)
    blit(link,linkXY)
    blit(tree,treeXY)
    pygame.display.update([link.rect,tree.rect])
    pygame.time.wait(23)
