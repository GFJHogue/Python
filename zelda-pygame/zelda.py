import sys
import pygame


pygame.display.set_caption("The Legend of Zelda: A Link To The Python")
screen=pygame.display.set_mode((1138,640))


link=pygame.sprite.Sprite()
link.images=[""]
link.images.append(pygame.image.load("textures/entities/linkDL1.png"))
link.images.append(pygame.image.load("textures/entities/linkD1.png"))
link.images.append(pygame.image.load("textures/entities/linkDR1.png"))
link.images.append(pygame.image.load("textures/entities/linkL1.png"))
link.images.append("")
link.images.append(pygame.image.load("textures/entities/linkR1.png"))
link.images.append(pygame.image.load("textures/entities/linkUL1.png"))
link.images.append(pygame.image.load("textures/entities/linkU1.png"))
link.images.append(pygame.image.load("textures/entities/linkUR1.png"))
link.image=link.images[2]
link.rect=link.image.get_rect()
linkXY=[0,0,0,0,72,72]

tree=pygame.sprite.Sprite()
tree.image=pygame.image.load("textures/entities/tree1.png")
tree.rect=tree.image.get_rect()
treeXY=[100,300,0,0,128,160]


def coords(s):
    return((s[0],s[1]))

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
    if(c[2]==-1)and(c[3]==1):
        s.image=s.images[1]
    elif(c[2]==1)and(c[3]==1):
        s.image=s.images[3]
    elif(c[2]==-1)and(c[3]==-1):
        s.image=s.images[7]
    elif(c[2]==1)and(c[3]==-1):
        s.image=s.images[9]
    elif(c[3]==1):
        s.image=s.images[2]
    elif(c[2]==-1):
        s.image=s.images[4]
    elif(c[2]==1):
        s.image=s.images[6]
    elif(c[3]==-1):
        s.image=s.images[8]
    return


screen.fill((74,156,74))
pygame.display.update()

while(True):
    event=pygame.event.poll()
    if(event.type==pygame.QUIT):
        sys.exit()
    keys=pygame.key.get_pressed()
    if(keys[pygame.K_w]):
        linkXY[3]=-1
    if(keys[pygame.K_a]):
        linkXY[2]=-1
    if(keys[pygame.K_s]):
        linkXY[3]=1
    if(keys[pygame.K_d]):
        linkXY[2]=1
    if((keys[pygame.K_w])and(keys[pygame.K_s]))or((keys[pygame.K_w]==False)and(keys[pygame.K_s]==False)):
        linkXY[3]=0
    if((keys[pygame.K_a])and(keys[pygame.K_d]))or((keys[pygame.K_a]==False)and(keys[pygame.K_d]==False)):
        linkXY[2]=0

    screen.fill((74,156,74))
    moveme(linkXY)
    sprites(link,linkXY)
    blit(tree,treeXY)
    blit(link,linkXY)
    pygame.display.update([link.rect,tree.rect])
    pygame.time.wait(3)
