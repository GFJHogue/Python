import sys, random
import pygame

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("The Legend of Zelda: A Link To The Python")
screen=pygame.display.set_mode((1138,640))
font=pygame.font.Font(None,100)
text_intro0=font.render("The Legend of Zelda:",True,(255,0,0),(74,156,74))
text_intro1=font.render("A Link To The Python",True,(255,255,128),(74,156,74))
screen.fill((74,156,74))
screen.blit(text_intro0,(100,200))
screen.blit(text_intro1,(400,340))
pygame.display.flip()
pygame.time.wait(3000)

rupees=0
lives=0

#entities
link=pygame.sprite.Sprite()
link.images=[["",[],[],[],[],"",[],[],[],[]],["","",[],"",[],"",[],"",[],""],["","",[],"",[],"",[],"",[],""],[],["","",[],"",[],"",[],"",[],""]]#["",[DR],[D],[DR],[L],"",[R],[UL],[U],[UR]]
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
link.frame=0
link.image=link.images[1][2][0]#[facingDirection][frame]
link.rect=link.image.get_rect()
linkXY=[0,0,0,0,72,72,4,2,1]#[x,y,movex,movey,sizex,sizey,facingDirections,facing,type]

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

bush=pygame.sprite.Sprite()
bush.images=[]
bush.images.append(pygame.image.load("textures/entities/bush_1.png"))
bush.images.append(pygame.image.load("textures/entities/bush_1B.png"))
bush.image=bush.images[0]
bush.rect=bush.image.get_rect()
bush.damage=0
bushXY=[800,100,0,0,32,32,1,2,0]

#items
sword=pygame.sprite.Sprite()
sword.image=pygame.image.load("textures/items/sword.png")
sword.rect=sword.image.get_rect()
swordXY=[0,0,0,0,72,72,1,2,0]

fftyrupees=pygame.sprite.Sprite()
fftyrupees.image=pygame.image.load("textures/items/50rupees.png")
fftyrupees.rect=fftyrupees.image.get_rect()
fftyrupeesXY=[0,0,0,0,72,72,1,2,0]
fftyrupees.value=50

#music
pygame.mixer.music.load("audio/music/overworld.ogg")

#sounds
sound_sword=[]
sound_sword.append(pygame.mixer.Sound("audio/sounds/sword1.ogg"))
sound_sword.append(pygame.mixer.Sound("audio/sounds/sword2.ogg"))
sound_sword.append(pygame.mixer.Sound("audio/sounds/sword3.ogg"))
sound_sword.append(pygame.mixer.Sound("audio/sounds/sword4.ogg"))

sound_itemfanfare=pygame.mixer.Sound("audio/sounds/itemfanfare.ogg")

sound_grasscut=pygame.mixer.Sound("audio/sounds/grasscut.ogg")


def coords(s):
    return((s[0],s[1]))#(x,y)

def rectlist(l):
    rl=[]
    for c in range(0,len(l)):
        rl.append(l[c].rect)
    return(rl)

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

def swing(e=[],exy=[]):
    if(keys[pygame.K_SPACE])and(linkXY[8]==1):
        sound_sword[random.randint(0,3)].play()
        div=1
        if(linkXY[7]==2):
            linkXY[0]=linkXY[0]+6
            linkXY[1]=linkXY[1]+10
            div=2
        elif(linkXY[7]==4):
            linkXY[0]=linkXY[0]-12
            linkXY[1]=linkXY[1]+6
        elif(linkXY[7]==6):
            linkXY[0]=linkXY[0]+12
            linkXY[1]=linkXY[1]+6
        elif(linkXY[7]==8):
            linkXY[0]=linkXY[0]-4
            linkXY[1]=linkXY[1]-14
        
        for frame in range(0,9):
            link.image=link.images[4][linkXY[7]][int(frame/div)]
            screen.fill((74,156,74))
            blit(bush,bushXY)
            blit(link,linkXY)
            blit(tree,treeXY)
            blit(chest,chestXY)
            layer(link,linkXY,tree,treeXY)
            layer(link,linkXY,chest,chestXY)
            layer(link,linkXY,bush,bushXY,bush.r)
            pygame.display.update([link.rect])
            pygame.time.wait(23)
        
        if(linkXY[7]==2):
            linkXY[0]=linkXY[0]-6
            linkXY[1]=linkXY[1]-10
        elif(linkXY[7]==4):
            linkXY[0]=linkXY[0]+12
            linkXY[1]=linkXY[1]-6
        elif(linkXY[7]==6):
            linkXY[0]=linkXY[0]-12
            linkXY[1]=linkXY[1]-6
        elif(linkXY[7]==8):
            linkXY[0]=linkXY[0]+4
            linkXY[1]=linkXY[1]+14
        
        if(link.rect.collidelistall(rectlist(e))):
            en=link.rect.collidelistall(rectlist(e))[0]
            if((linkXY[7]==2)and(linkXY[1]<exy[en][1]))or((linkXY[7]==4)and(linkXY[0]>exy[en][0]))or((linkXY[7]==6)and(linkXY[0]<exy[en][0]))or((linkXY[7]==8)and(linkXY[1]>exy[en][1])):
                e[en].damage=1
        
        sprites(link,linkXY)
        screen.fill((74,156,74))
        blit(bush,bushXY)
        blit(link,linkXY)
        blit(tree,treeXY)
        blit(chest,chestXY)
        layer(link,linkXY,tree,treeXY)
        layer(link,linkXY,chest,chestXY)
        layer(link,linkXY,bush,bushXY,bush.r)
        pygame.display.update()
        return

def solidobject(c,o,h,v):
    if(c[0]+c[4]-h>o[0])and(c[0]+h<o[0]+o[4])and(c[1]+c[5]-v>o[1])and(c[1]+v<o[1]+o[5]):
        c[0]=c[0]-c[2]
        c[1]=c[1]-c[3]
    return

def layer(a,axy,b,bxy,r=True):
    if(pygame.sprite.collide_rect(a,b))and(r==True):
        if(axy[1]+axy[5]/2>bxy[1]+bxy[5]/2):
            blit(b,bxy)
            blit(a,axy)
        else:
            blit(a,axy)
            blit(b,bxy)
    return

def chests(c,cxy,i,ixy,s,sxy):
    if(keys[pygame.K_e])and(pygame.sprite.collide_rect(s,c))and(c.image==c.images[0]):
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
            sxy[7]=2
        pygame.mixer.music.pause()
        sound_itemfanfare.play()
        pygame.time.wait(1020)
        pygame.mixer.music.unpause()
        screen.fill((74,156,74))
    return

def bushes(b,bxy,sxy):
    if(b.damage==1):
        sound_grasscut.play()
        b.damage=3
        b.image=b.images[1]
        b.r=False
        drop(bxy,0)
    if(b.image==b.images[0]):
        solidobject(sxy,bxy,24,20)
        b.r=True
    return

def drop(lxy,t):
    if(t==0):
        fftyrupeesXY[0]=lxy[0]
        fftyrupeesXY[1]=lxy[1]
        fftyrupeesXY[8]=1
    return

def pickup(i,ixy):
    global rupees
    if(ixy[8]==1):
        blit(i,ixy)
        if(i.rect.colliderect(link.rect.inflate(-24,-24))):
            ixy[8]=0
            rupees=rupees+i.value
    return

screen.fill((74,156,74))
pygame.display.update()

pygame.mixer.music.play()
intro=1

while(True):
    if(7055>pygame.mixer.music.get_pos()>7005)and(intro==1):
        pygame.mixer.music.play(-1,7.03)
        intro=0
    if(35125>pygame.mixer.music.get_pos()>34965):
        pygame.mixer.music.play(-1,7.03)
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

    sprites(link,moveme(linkXY))
    swing([bush],[bushXY])

    screen.fill((74,156,74))

    solidobject(linkXY,treeXY,33,45)
    solidobject(linkXY,chestXY,24,24)

    chests(chest,chestXY,sword,swordXY,link,linkXY)
    bushes(bush,bushXY,linkXY)

    blit(bush,bushXY)
    blit(link,linkXY)
    blit(tree,treeXY)
    blit(chest,chestXY)
    layer(link,linkXY,tree,treeXY)
    layer(link,linkXY,chest,chestXY)
    layer(link,linkXY,bush,bushXY,bush.r)
    pickup(fftyrupees,fftyrupeesXY)

    pygame.display.update([link.rect,tree.rect,chest.rect,sword.rect,bush.rect,fftyrupees.rect])
    pygame.time.wait(20)

