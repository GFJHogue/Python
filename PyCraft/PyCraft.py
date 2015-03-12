import math  # Used in charater movement.
import os  # Used in file and directory manipulation.
from random import randint  # Used for random generation.
from sys import exit  # For closing the game.
from urllib import urlopen  # Used for importing player skins.

import pygame


def CHECK():  # Checks the status of mouse, keys, and all events.
    global EVENT, KEYS, MOUSE, BUTTON
    EVENT = pygame.event.poll()
    KEYS = pygame.key.get_pressed()
    MOUSE = pygame.mouse.get_pos()
    BUTTON = pygame.mouse.get_pressed()

def ID(obj):  # Dictates the correspondace of block/tile IDs.
    if obj == " 1":
        return stone
    elif obj == " 2":
        return grass_plains
    elif obj == " 3":
        return dirt
    elif obj == " 4":
        return cobblestone
    elif obj == " 5":
        return plank_oak
    elif obj == " 6" or obj == "17":
        return log_oak
    elif obj == "18":
        return leaves_oak
    else:
        return None

def DURABILITY(obj):  # Returns block durability value.
    global MODIFY
    
    if obj == " 1" or obj == " 4":
        if MODIFY[0] == 1:
            return(115.0)
        else:
            return(750.0)
    elif obj == " 2" or obj == " 3":
        return(90.0)
    elif obj == " 5" or obj == " 6" or obj == "17":
        return(300.0)

def BLOCKDROP(block):  # Returns the item value of a item dropped from a block.
    global MODIFY
    
    if block == " 1" or block == " 4":
        if MODIFY[0] >= 1:
            return " 4"
        else:
            return None
    elif block == " 2" or block == " 3":
        return " 3"
    elif block == " 5":
        return " 5"
    elif block == " 6" or block == "17":
        return "17"

def ITEMID(item):  # Dictates the correspondace of item IDs.
    if item == " 3":
        return dirtItem
    if item == " 4":
        return cobblestoneItem
    if item == " 5":
        return plank_oakItem
    if item == "17":
        return log_oakItem
    if item == "270":
        return woodpick
    if item == "280":
        return stick

def generate(file):  # Generates a random chunk and writes it to a new file.
    f = open(file,"w+")
    
    for c in range(256):
        r = randint(0,19)
        
        if r == 0:
            r = randint(0,4)
            
            if r == 0:
                r = randint(0,1)
                if r == 0:
                    f.write(" 2 1\n")
                elif r == 1:
                    f.write(" 2 2\n")
            elif r == 1:
                f.write(" 2 6\n")
            else:
                f.write(" 2  \n")
        else:
            f.write(" 2  \n")
    
    f.close()
    return

def loadChunk(coords):  # Reads a chunk file returning a rendered chunk.
    global WORLD
    file = ("saves/" + WORLD + "/" + str(coords[0]) +
            "." + str(coords[1]) + ".dat")
    
    if not os.path.exists(file):  # Generates file if it doesn't exist.
        generate(file)
    
    rawData = open(file)
    data = [coords,[]]
    
    for c in range(256):
        line = rawData.readline().rstrip()
        data[1].append(line)
    
    rawData.close()
    return renderChunk(data)

def overwriteBlock(block):  # Edits the chunk file if a block is broken.
    file = ("saves/" + WORLD + "/" + str(block[1][0] / 768) +
        "." + str(block[1][1] / 768) + ".dat")
    oldData = open(file)
    data = []
    
    for c in range(256):
        line = oldData.readline()
        
        if c == ((block[1][0] % 768) / 48) + (((block[1][1] % 768) / 48) * 16):
            data.append(line[:2] + "  \n")
            item = line[2:4]  # Records block value of item to be dropped.
        else:
            data.append(line)
    
    oldData.close()
    newData = open(file,"w")
    
    for c in range(256):
        newData.write(data[c])
    
    newData.close()
    placeChunk(True)
    dropItem(BLOCKDROP(item),block[1])  # Drops item from block (optional).
    return

def placeChunk(force = False):  # Loads chunks when needed or forced.
    global BLOCKS, CHUNKS, TREES, X, Y
    
    if CHUNKS[0][1] != (X / 768, Y / 768) or force:
        BLOCKS = []
        TREES = []
        CHUNKS = []
        CHUNKS.append(loadChunk((X / 768, Y / 768)))  # Loads 6 current chunks.
        CHUNKS.append(loadChunk((X / 768 + 1, Y / 768)))
        CHUNKS.append(loadChunk((X / 768 + 2, Y / 768)))
        CHUNKS.append(loadChunk((X / 768, Y / 768 + 1)))
        CHUNKS.append(loadChunk((X / 768 + 1, Y / 768 + 1)))
        CHUNKS.append(loadChunk((X / 768 + 2, Y / 768 + 1)))
    
    return

def renderChunk(data):  # Returns 16x16tiles as a chunk from chunk data.
    chunk = [pygame.Surface((768,768)),data[0]] 
    blocks = [pygame.Surface((768,768),pygame.SRCALPHA,32).convert_alpha(),[]]
    
    for c in range(256):  # Renders chunk tiles.
        chunk[0].blit(ID(data[1][c][:2]),((c % 16) * 48,(c / 16) * 48))
        
        if data[1][c][2:] != "":  # Renders block shadows.
            blocks[0].blit(SHADOW,((c % 16) * 48 - 48,(c / 16) * 48 - 48))
            blocks[1].append((data[1][c][2:],((c % 16) * 48,(c / 16) * 48)))
    
    for c in range(len(blocks[1])):  # Renders blocks over shadows.
        blocks[0].blit(ID(blocks[1][c][0]),blocks[1][c][1])
    
    chunk[0].blit(blocks[0],(0,0))  # Renders blocks/shadows on tiles.
    loadBlocks(blocks[1],data[0])  # Collects block data for blocks in chunck.
    return chunk

def blitChunk():  # Blits a set of 6 chunks on the screen.
    global CHUNKS, X, Y
    
    for c in range(len(CHUNKS)):
        screen.blit(CHUNKS[c][0],((768 * CHUNKS[c][1][0]) - X,
            (768 * CHUNKS[c][1][1]) - Y))

def rotate(image, angle):  # Returns a square image rotated on its centre.
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

def blitPlayer():  # Blits the rotated player sprite based on mouse location.
    global MOUSE, PLAYER, SKIN
    PLAYER.image = rotate(SKIN, -math.degrees(
        math.atan2(360 - MOUSE[1],512 - MOUSE[0])) -90)
    return(screen.blit(PLAYER.image,PLAYER.rect))

def loadBlocks(blocks,loc):  # Extracts block-specific data from chunk data.
    global BLOCKS, TREES

    for c in range(len(blocks)):
        BLOCKS.append((blocks[c][0],(blocks[c][1][0] + loc[0] * 768,
            blocks[c][1][1] + loc[1] * 768)))
        
        if blocks[c][0] == " 6":  # Collects locations of tree blocks.
            TREES.append((blocks[c][1][0] + loc[0] * 768,
                blocks[c][1][1] + loc[1] * 768))
    
    return

def breakBlock():  # Breaks a block if clicked by a player.
    global BLOCKS, break_block, BUTTON, MOUSE
    brake = 1
    
    if pygame.Rect(320,168,384,384).collidepoint(MOUSE):
        for c in range(len(BLOCKS)):  # Checks if any blocks are under cursor.
            if (pygame.Rect(BLOCKS[c][1],(48,48))
                    .collidepoint(MOUSE[0]+X,MOUSE[1]+Y)):
                for d in range(int(DURABILITY(BLOCKS[c][0]))):
                    CHECK()  # Loops for breaking time based on DURABILITY.
                    
                    if not BUTTON[0]:  # Stops if player stops holding button.
                        return
                    
                    if brake == 6:
                        r = randint(1,4)
                        
                        if BLOCKS[c][0] == " 1" or BLOCKS[c][0] == " 4":
                            if r == 1:
                                b_stone1.play()
                            elif r == 2:
                                b_stone2.play()
                            elif r == 3:
                                b_stone3.play()
                            elif r == 4:
                                b_stone4.play()
                        elif BLOCKS[c][0] == " 2" or BLOCKS[c][0] == " 3":
                            if r == 1:
                                b_grass1.play()
                            elif r == 2:
                                b_grass2.play()
                            elif r == 3:
                                b_grass3.play()
                            elif r == 4:
                                b_grass4.play()
                        elif BLOCKS[c][0] == " 5" or BLOCKS[c][0] == " 6" or BLOCKS[c][0] == "17":
                            if r == 1:
                                b_wood1.play()
                            elif r == 2:
                                b_wood2.play()
                            elif r == 3:
                                b_wood3.play()
                            elif r == 4:
                                b_wood4.play()
                    else:
                        brake = brake + 1
                    
                    screen.blit(break_block[int(d / DURABILITY(BLOCKS[c][0])
                            * 10)],(BLOCKS[c][1][0] - X,BLOCKS[c][1][1] - Y))
                    pygame.display.update(pygame.Rect(
                            BLOCKS[c][1][0] - X,BLOCKS[c][1][1] - Y,48,48))
                    pygame.time.wait(10)
                
                overwriteBlock(BLOCKS[c])
                break
    
    return

def movePlayer():  # Player movement control.
    global KEYS, STEP, X, x, Y, y
    
    if KEYS[pygame.K_LSHIFT]:  # Run.
        speed = 2.5
    else:
        speed = 1
    # Calculating change in x,y to 1 pixel towards MOUSE using slope.
    dX = -speed * (512 - MOUSE[0]) / math.sqrt((512 - MOUSE[0]) ** 2 +
        (360 - MOUSE[1]) ** 2)
    dY = -speed * (360 - MOUSE[1]) / math.sqrt((512 - MOUSE[0]) ** 2 +
        (360 - MOUSE[1]) ** 2)
    
    if KEYS[pygame.K_w]:
        x,y = x + dX, y + dY
    
    if KEYS[pygame.K_a]:
        x,y = x + dY, y - dX
    
    if KEYS[pygame.K_s]:
        x,y = x - dX, y - dY
    
    if KEYS[pygame.K_d]:
        x,y = x - dY, y + dX
    
    solidBlock()
    X,Y = int(x),int(y)  # Rounds location to nearest pixel for blitting.
    
    if STEP >= 72:
        STEP = 1
        r = randint(1,6)
        
        if r == 1:
            step1.play()
        elif r == 2:
            step2.play()
        elif r == 3:
            step3.play()
        elif r == 4:
            step4.play()
        elif r == 5:
            step5.play()
        elif r == 6:
            step6.play()
    else:
        STEP = STEP + speed

    return

def solidBlock():  # Checks if player is walking into any block obstructions.
    global X, x, Y, y
    player_rect = pygame.Rect(int(x)+488,int(y)+336,48,48).inflate(-16,-16)
    
    for c in range(len(BLOCKS)):
        if player_rect.colliderect(pygame.Rect(BLOCKS[c][1],(48,48))):
            x,y = X,Y  # Corrects movement.
            break
    
    return

def dropItem(item,loc):  # Records data and location of a dropped item.
    global ITEMS
    
    if item == None:
        return
    
    ITEMS.append((item,loc))
    return

def blitItems():  # Renders dropped items on the screen.
    global ITEMS
    
    if ITEMS == []:
        return
    
    for c in range(len(ITEMS)):  # Renders only if visible on screen.
        if screen.get_rect().colliderect(pygame.Rect(
                ITEMS[c][1][0] - X,ITEMS[c][1][1] - Y,32,32)):
            screen.blit(ITEMID(ITEMS[c][0]),(
                ITEMS[c][1][0] - X,ITEMS[c][1][1] - Y))
            if pickupItems(c):
                break
    
    return

def pickupItems(i):  # Player picks up items that come in contact.
    global ITEMS, PLAYER
    
    if PLAYER.rect.colliderect(pygame.Rect(
            ITEMS[i][1][0] - X,ITEMS[i][1][1] - Y,32,32)):
        insertInventory(ITEMS[i][0],1)
        ITEMS.pop(i)
        return(True)
    
    return(False)

def blitTrees():  # Renders treetops(leaves) above trees if visible on screen.
    global TREES
    
    if TREES == []:
        return
    
    for c in range(len(TREES)):
        if screen.get_rect().colliderect(pygame.Rect(
                TREES[c][0] - 48 - X,TREES[c][1] - 48 - Y,144,144)):
            screen.blit(tree_oak,(TREES[c][0] - 48 - X,TREES[c][1] - 48 - Y))
    
    return

def blitHUD():  # Shows the HUD (INVENTORY).
    global INVENTORY
    switchItem()
    
    for c in range(len(INVENTORY[0])):
        if INVENTORY[0][c][1] > 0:
            screen.blit(ITEMID(INVENTORY[0][c][0]),(c * 32,688))
            screen.blit(minecraft_txt.render(
                str(INVENTORY[0][c][1]),1,(255,255,255)),(c * 32,688))
    
    return

def CRAFTING():  # Shows the Crafting Menu.
    global BUTTON, EVENT, FADE, INVENTORY, MOUSE
    item = None
    screen.blit(FADE,(0,0))
    
    while True:
        CHECK()
        
        if EVENT.type == pygame.QUIT or KEYS[pygame.K_ESCAPE]:
            pygame.mixer.music.fadeout(1000)
            pygame.time.wait(1000)
            exit()
        
        if EVENT.type == pygame.KEYDOWN and EVENT.key == pygame.K_c:
            break
        
        if(EVENT.type == pygame.MOUSEBUTTONUP and EVENT.button == 1
                and pygame.Rect(0,688,1024,32).collidepoint(MOUSE)):
            for c in range(len(INVENTORY[0])):
                if MOUSE[0] / 32 == c and INVENTORY[0][c][0] != "  ":
                    item = INVENTORY[0][c]
                    break
        
        pygame.draw.rect(screen,(128,128,128),(0,688,1024,32))
        blitHUD()
        
        if item != None:
            RECIPES(item)
        
        pygame.display.update()
        pygame.time.wait(100)

def RECIPES(item):  # Shows recipes for crafting menu based on Inventory.
    global INVENTORY
    p = False
    
    if item[0] == " 5":
        for c in range(len(INVENTORY[0])):
            if INVENTORY[0][c][0] == "280" and INVENTORY[0][c][1] >= 2:
                p = True
        
        if item[1] >= 2:
            if BUTTON[0] and pygame.Rect(0,656,256,32).collidepoint(MOUSE):
                insertInventory("280",4)
                insertInventory(" 5",-2)
            
            pygame.draw.rect(screen,(128,128,128),(0,656,256,32))
            screen.blit(plank_oakItem,(0,656))
            screen.blit(minecraft_txt.render("2",1,(255,255,255)),(0,656))
            screen.blit(ARROW,(32,656))
            screen.blit(stick,(64,656))
            screen.blit(minecraft_txt.render("4",1,(255,255,255)),(64,656))
        
        if item[1] >= 3 and p:
            if BUTTON[0] and pygame.Rect(0,624,256,32).collidepoint(MOUSE):
                insertInventory("270",1)
                insertInventory(" 5",-3)
                insertInventory("280",-2)
            
            pygame.draw.rect(screen,(128,128,128),(0,624,256,32))
            screen.blit(plank_oakItem,(0,624))
            screen.blit(minecraft_txt.render("3",1,(255,255,255)),(0,624))
            screen.blit(stick,(32,624))
            screen.blit(minecraft_txt.render("2",1,(255,255,255)),(32,624))
            screen.blit(ARROW,(64,624))
            screen.blit(woodpick,(96,624))
            screen.blit(minecraft_txt.render("1",1,(255,255,255)),(96,624))
        
    elif item[0] == "17":
        if item[1] >= 1:
            if BUTTON[0] and pygame.Rect(0,656,256,32).collidepoint(MOUSE):
                insertInventory(" 5",4)
                insertInventory("17",-1)
            
            pygame.draw.rect(screen,(128,128,128),(0,656,256,32))
            screen.blit(log_oakItem,(0,656))
            screen.blit(minecraft_txt.render("1",1,(255,255,255)),(0,656))
            screen.blit(ARROW,(32,656))
            screen.blit(plank_oakItem,(64,656))
            screen.blit(minecraft_txt.render("4",1,(255,255,255)),(64,656))
    
    elif item[0] == "280":
        for c in range(len(INVENTORY[0])):
            if INVENTORY[0][c][0][1] == "5" and INVENTORY[0][c][1] >= 3:
                p = True
        
        if item[1] >= 2 and p:
            if BUTTON[0] and pygame.Rect(0,624,256,32).collidepoint(MOUSE):
                insertInventory("270",1)
                insertInventory(" 5",-3)
                insertInventory("280",-2)
            
            pygame.draw.rect(screen,(128,128,128),(0,624,256,32))
            screen.blit(plank_oakItem,(32,624))
            screen.blit(minecraft_txt.render("3",1,(255,255,255)),(32,624))
            screen.blit(stick,(0,624))
            screen.blit(minecraft_txt.render("2",1,(255,255,255)),(0,624))
            screen.blit(ARROW,(64,624))
            screen.blit(woodpick,(96,624))
            screen.blit(minecraft_txt.render("1",1,(255,255,255)),(96,624))
    
    return

def insertInventory(item,amount):  # Inserts amount of item into INVENTORY.
    global INVENTORY
    
    for c in range(len(INVENTORY[0])):
        if INVENTORY[0][c][0] == item and INVENTORY[0][c][1] + amount >= 0:
            INVENTORY[0][c][1] = INVENTORY[0][c][1] + amount
            return
        elif INVENTORY[0][c][1] == 0:
            INVENTORY[0][c][0] = item
            INVENTORY[0][c][1] = amount
            return

def switchItem():  # Changes selected item in INVENTORY.
    global EVENT, USE
    
    if EVENT.type == pygame.MOUSEBUTTONDOWN:  # Using Scroll Wheel.
        if EVENT.button == 5:
            if USE >= 8:
                USE = 0
            else:
                USE = USE + 1
        elif EVENT.button == 4:
            if USE <= 0:
                USE = 8
            else:
                USE = USE - 1
    
    if EVENT.type == pygame.KEYDOWN:  # Using number keys.
        if EVENT.key == pygame.K_1:
            USE = 0
        elif EVENT.key == pygame.K_2:
            USE = 1
        elif EVENT.key == pygame.K_3:
            USE = 2
        elif EVENT.key == pygame.K_4:
            USE = 3
        elif EVENT.key == pygame.K_5:
            USE = 4
        elif EVENT.key == pygame.K_6:
            USE = 5
        elif EVENT.key == pygame.K_7:
            USE = 6
        elif EVENT.key == pygame.K_8:
            USE = 7
        elif EVENT.key == pygame.K_9:
            USE = 8
    
    tool()
    pygame.draw.rect(screen,(0,255,0),(USE * 32,688,32,32))
    
    return

def tool():  # Changes block breaking behavior based on selected tool item.
    global MODIFY, USE
    
    if INVENTORY[0][USE][0] == "270":
        MODIFY[0] = 1
    else:
        MODIFY[0] = 0
    
    return

def placeBlock():  # Places a block from player's inventory where the mouse is located.
    global INVENTORY, MOUSE, USE
    
    if(pygame.Rect(320,168,384,384).collidepoint(MOUSE)
            and INVENTORY[0][USE][1] >= 1):
        if ID(INVENTORY[0][USE][0]) != None:
            insertInventory(INVENTORY[0][USE][0],-1)
        
        writeBlock(INVENTORY[0][USE][0],((MOUSE[0] + X) / 48
                                        ,(MOUSE[1] + Y) / 48))

def writeBlock(item,loc):  # Edits the chunk file of a placed block.
    global WORLD
    
    if ID(item) != None:
        file = ("saves/" + WORLD + "/" + str(loc[0] / 16) +
            "." + str(loc[1] / 16) + ".dat")
        oldData = open(file)
        data = []
        
        for c in range(256):
            line = oldData.readline()
            
            if c == loc[0] % 16 + (loc[1] % 16) * 16:
                data.append(line[:2] + item + " \n")
            else:
                data.append(line)
        
        oldData.close()
        newData = open(file,"w")
        
        for c in range(256):
            newData.write(data[c])
        
        newData.close()
        placeChunk(True)
    
    return


pygame.init()
screen = pygame.display.set_mode((1024,720))#,pygame.FULLSCREEN)


"""TITLE SCREEN"""
background = pygame.image.load("textures/background.jpg")
logo = pygame.image.load("textures/PY-CRAFT.png")

"""TILES"""
stone = pygame.image.load("textures/tiles/stone.png")
grass_plains = pygame.image.load("textures/tiles/grass/plains.png")
dirt = pygame.image.load("textures/tiles/dirt.png")
cobblestone = pygame.image.load("textures/tiles/cobblestone.png")
plank_oak = pygame.image.load("textures/tiles/plank/oak.png")
log_oak = pygame.image.load("textures/tiles/log/oak.png")
leaves_oak = pygame.image.load("textures/tiles/leaves/oak.png")

"""ITEMS"""
ARROW = pygame.image.load("textures/items/ARROW.png")
dirtItem = pygame.image.load("textures/items/dirt.png")
cobblestoneItem = pygame.image.load("textures/items/cobblestone.png")
plank_oakItem = pygame.image.load("textures/items/plank/oak.png")
log_oakItem = pygame.image.load("textures/items/log/oak.png")
woodpick = pygame.image.load("textures/items/woodpick.png")
stick = pygame.image.load("textures/items/stick.png")

"""SHADING"""
FADE = pygame.image.load("textures/FADE.png")
SHADOW = pygame.image.load("textures/tiles/SHADOW.png")

"""ANIMATIONS"""
break_block = []
break_block.append(pygame.image.load("textures/animations/breaking/0.png"))
break_block.append(pygame.image.load("textures/animations/breaking/1.png"))
break_block.append(pygame.image.load("textures/animations/breaking/2.png"))
break_block.append(pygame.image.load("textures/animations/breaking/3.png"))
break_block.append(pygame.image.load("textures/animations/breaking/4.png"))
break_block.append(pygame.image.load("textures/animations/breaking/5.png"))
break_block.append(pygame.image.load("textures/animations/breaking/6.png"))
break_block.append(pygame.image.load("textures/animations/breaking/7.png"))
break_block.append(pygame.image.load("textures/animations/breaking/8.png"))
break_block.append(pygame.image.load("textures/animations/breaking/9.png"))

"""FLOATING STRUCTURES"""
tree_oak = pygame.image.load("textures/tiles/tree/oak.png")

"""FONTS"""
minecraft_txt = pygame.font.Font("textures/fonts/Minecraft.ttf",12)
minecraftBIG_txt = pygame.font.Font("textures/fonts/Minecraft.ttf",40)
control_0 = minecraft_txt.render("[W] Forward; [S] Backward; [A] Strafe Left; [D] Strafe Right; [LEFT MOUSE] Break Block; [Right MOUSE] Place Block",1,(255,255,255))
control_1 = minecraft_txt.render("Use the Mouse wheel to select an item.",1,(255,255,255))

"""SOUNDS"""
step1 = pygame.mixer.Sound("sounds/step/grass1.ogg")
step2 = pygame.mixer.Sound("sounds/step/grass2.ogg")
step3 = pygame.mixer.Sound("sounds/step/grass3.ogg")
step4 = pygame.mixer.Sound("sounds/step/grass4.ogg")
step5 = pygame.mixer.Sound("sounds/step/grass5.ogg")
step6 = pygame.mixer.Sound("sounds/step/grass6.ogg")
step1.set_volume(0.5)
step2.set_volume(0.5)
step3.set_volume(0.5)
step4.set_volume(0.5)
step5.set_volume(0.5)
step6.set_volume(0.5)
b_grass1 = pygame.mixer.Sound("sounds/break/grass1.ogg")
b_grass2 = pygame.mixer.Sound("sounds/break/grass2.ogg")
b_grass3 = pygame.mixer.Sound("sounds/break/grass3.ogg")
b_grass4 = pygame.mixer.Sound("sounds/break/grass4.ogg")
b_stone1 = pygame.mixer.Sound("sounds/break/stone1.ogg")
b_stone2 = pygame.mixer.Sound("sounds/break/stone2.ogg")
b_stone3 = pygame.mixer.Sound("sounds/break/stone3.ogg")
b_stone4 = pygame.mixer.Sound("sounds/break/stone4.ogg")
b_wood1 = pygame.mixer.Sound("sounds/break/wood1.ogg")
b_wood2 = pygame.mixer.Sound("sounds/break/wood2.ogg")
b_wood3 = pygame.mixer.Sound("sounds/break/wood3.ogg")
b_wood4 = pygame.mixer.Sound("sounds/break/wood4.ogg")
b_grass1.set_volume(0.2)
b_grass2.set_volume(0.2)
b_grass3.set_volume(0.2)
b_grass4.set_volume(0.2)
b_stone1.set_volume(0.2)
b_stone2.set_volume(0.2)
b_stone3.set_volume(0.2)
b_stone4.set_volume(0.2)
b_wood1.set_volume(0.2)
b_wood2.set_volume(0.2)
b_wood3.set_volume(0.2)
b_wood4.set_volume(0.2)


while True:  # Title Screen.
    CHECK()
    
    if EVENT.type == pygame.QUIT or KEYS[pygame.K_ESCAPE]:
        pygame.mixer.music.fadeout(1000)
        pygame.time.wait(1000)
        exit()
    
    if EVENT.type == pygame.KEYDOWN and EVENT.key == pygame.K_RETURN:
        break
    
    screen.blit(background,(0,0))
    screen.blit(logo,(217,277))
    screen.blit(minecraftBIG_txt.render("Press ENTER",1,(0,0,0),(0,255,255)),(0,0))
    screen.blit(minecraftBIG_txt.render("Movement: W,A,S,D    Run: LSHIFT    Crafting: C",1,(255,255,255),(0,0,0)),(0,680))
    pygame.display.update()

NAME = ""

while True:  # User enters a valid Minecraft Username.
    CHECK()
    
    if EVENT.type == pygame.QUIT or KEYS[pygame.K_ESCAPE]:
        pygame.mixer.music.fadeout(1000)
        pygame.time.wait(1000)
        exit()
    
    if EVENT.type == pygame.KEYDOWN:
        if len(pygame.key.name(EVENT.key)) == 1:
            if KEYS[pygame.K_LSHIFT] or KEYS[pygame.K_RSHIFT]:
                if pygame.key.name(EVENT.key) == "-":
                    NAME = NAME + "_"
                else:
                    NAME = NAME + pygame.key.name(EVENT.key).upper()
            else:
                NAME = NAME + pygame.key.name(EVENT.key)
        elif pygame.key.name(EVENT.key) == "backspace":
            NAME = NAME[:len(NAME) - 1]
        elif EVENT.key == pygame.K_RETURN:
            break
    
    screen.fill((0,0,0))
    screen.blit(minecraftBIG_txt.render("Minecraft Username: " + NAME,1,(255,255,255)),(0,0))
    pygame.display.update()

WORLD = ""

while True:  # User enters the name of their world.
    CHECK()
    
    if EVENT.type == pygame.QUIT or KEYS[pygame.K_ESCAPE]:
        pygame.mixer.music.fadeout(1000)
        pygame.time.wait(1000)
        exit()
    
    if EVENT.type == pygame.KEYDOWN:
        if len(pygame.key.name(EVENT.key)) == 1:
            if KEYS[pygame.K_LSHIFT] or KEYS[pygame.K_RSHIFT]:
                if pygame.key.name(EVENT.key) == "-":
                    WORLD = WORLD + "_"
                else:
                    WORLD = WORLD + pygame.key.name(EVENT.key).upper()
            else:
                WORLD = WORLD + pygame.key.name(EVENT.key)
        elif pygame.key.name(EVENT.key) == "space":
            WORLD = WORLD + " "
        elif pygame.key.name(EVENT.key) == "backspace":
            WORLD = WORLD[:len(WORLD) - 1]
        elif EVENT.key == pygame.K_RETURN:
            break
    
    screen.fill((0,0,0))
    screen.blit(minecraftBIG_txt.render("World Name: " + WORLD,1,(255,255,255)),(0,0))
    pygame.display.update()

if not os.path.exists("players"):  # Creates player directory if it does not exist.
    os.makedirs("players")

PLAYER = pygame.sprite.Sprite()

if NAME == "":
    PLAYER.image = char
else:  # Imports Minecraft player skin and transforms it into PyCraft player format.
    f = open("players/" + NAME + ".png","wb")
    f.write(urlopen("http://s3.amazonaws.com/MinecraftSkins/" +
            NAME + ".png").read())
    f.close()
    rawskin = pygame.image.load("players/" + NAME + ".png")
    SKIN = pygame.Surface((16,16),pygame.SRCALPHA,32).convert_alpha()
    SKIN.blit(rawskin,(4,6),pygame.Rect(20,16,12,4))
    SKIN.blit(rawskin,(0,6),pygame.Rect(32,16,4,4))
    SKIN.blit(rawskin,(4,4),pygame.Rect(8,0,8,8))
    SKIN = pygame.transform.scale(SKIN,(48,48))
    face = pygame.Surface((8,8),pygame.SRCALPHA,32).convert_alpha()
    face.blit(rawskin,(0,0),pygame.Rect(8,8,8,8))
    SKIN.blit(pygame.transform.scale(face,(24,8)),(12,28))
    PLAYER.image = SKIN

PLAYER.rect = PLAYER.image.get_rect()
PLAYER.rect.topleft = (488,336)

if not os.path.exists("saves/" + WORLD): # Creates world directory if it does not exist.
    os.makedirs("saves/" + WORLD)

pygame.display.update()
X,Y = 0,0  # X,Y are coordinates rounded to ints.
x,y = 0.0,0.0
speed = 1
ITEMS = []
BLOCKS = []
CHUNKS = [["",(X / 768 + 1,Y / 768 + 1)]]
INVENTORY = [[["  ",0],["  ",0],["  ",0],
            ["  ",0],["  ",0],["  ",0],
            ["  ",0],["  ",0],["  ",0]]]
MODIFY = [0]
USE = 0
STEP = 1

while True:
    CHECK()
    
    if not pygame.mixer.music.get_busy():  # Plays random music if nothing is playing.
        r = randint(1,10)
        
        if r <= 6:
            r = randint(1,6)
            pygame.mixer.music.load("sounds/music/creative" + str(r) + ".ogg")
        elif r >= 7:
            r = randint(1,4)
            pygame.mixer.music.load("sounds/music/menu" + str(r) + ".ogg")
        
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(1.0)
    if EVENT.type == pygame.QUIT or KEYS[pygame.K_ESCAPE]:
        pygame.mixer.music.fadeout(1000)
        pygame.time.wait(1000)
        exit()
    
    if EVENT.type == pygame.KEYDOWN and EVENT.key == pygame.K_c:
        CRAFTING()
    
    if BUTTON[0]:
        breakBlock()
    
    if BUTTON[2]:
        placeBlock()
    
    placeChunk()
    blitChunk()
    blitItems()
    
    if(KEYS[pygame.K_w] or KEYS[pygame.K_a] or
            KEYS[pygame.K_s] or KEYS[pygame.K_d]):
        movePlayer()
    
    blitPlayer()
    blitTrees()
    blitHUD()
    screen.blit(control_1,(288,708))
    pygame.display.update()
    pygame.time.wait(5)
