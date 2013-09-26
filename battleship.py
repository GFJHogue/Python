#2013/09/08

import random,sys#ship spawning, closing
grid=["O ","O ","O ","O ","O ","O ","O ","O ","O ","O\n","O ","O ","O ","O ","O ","O ","O ","O ","O ","O\n","O ","O ","O ","O ","O ","O ","O ","O ","O ","O\n","O ","O ","O ","O ","O ","O ","O ","O ","O ","O\n","O ","O ","O ","O ","O ","O ","O ","O ","O ","O\n","O ","O ","O ","O ","O ","O ","O ","O ","O ","O\n","O ","O ","O ","O ","O ","O ","O ","O ","O ","O\n","O ","O ","O ","O ","O ","O ","O ","O ","O ","O\n","O ","O ","O ","O ","O ","O ","O ","O ","O ","O\n","O ","O ","O ","O ","O ","O ","O ","O ","O ","O\n"]#hits/misses
maps=["O ","O ","O ","O ","O ","O ","O ","O ","O ","O\n","O ","O ","O ","O ","O ","O ","O ","O ","O ","O\n","O ","O ","O ","O ","O ","O ","O ","O ","O ","O\n","O ","O ","O ","O ","O ","O ","O ","O ","O ","O\n","O ","O ","O ","O ","O ","O ","O ","O ","O ","O\n","O ","O ","O ","O ","O ","O ","O ","O ","O ","O\n","O ","O ","O ","O ","O ","O ","O ","O ","O ","O\n","O ","O ","O ","O ","O ","O ","O ","O ","O ","O\n","O ","O ","O ","O ","O ","O ","O ","O ","O ","O\n","O ","O ","O ","O ","O ","O ","O ","O ","O ","O"]#ships/misses
def ship(s):#ship spawning (s=length of ship)
	o=random.randint(0,1)#o=orientation of the ship
	if(o==0):#horizontal
		shipx=random.randint(0,10-s)
		shipy=random.randint(0,9)
		for c in range(shipx,shipx+s):
			if(maps[c+shipy*10][0]!="X"):
				maps[c+shipy*10]=maps[c+shipy*10].replace("O","X")
	elif(o==1):#vertical
		shipx=random.randint(0,9)
		shipy=random.randint(0,10-s)
		for c in range(shipy*10,shipy*10+s*10,10):
				if(maps[shipx+c][1]!="X"):
					maps[shipx+c]=maps[shipx+c].replace("O","X")
	return
def blit(g):#format grid for display
	blit="  0 1 2 3 4 5 6 7 8 9\nA "
	blit=blit+"".join(g[0:10])+"B "+"".join(g[10:20])+"C "+"".join(g[20:30])+"D "+"".join(g[30:40])+"E "+"".join(g[40:50])+"F "+"".join(g[50:60])+"G "+"".join(g[60:70])+"H "+"".join(g[70:80])+"I "+"".join(g[80:90])+"J "+"".join(g[90:100])
	return(blit)
def hits(c):#calculates user input
	if(c=="map"):#cheatcode to see ship-map
		print(blit(maps))
	elif(c=="win"):#cheatcode to win game
		win(True)
	elif(c=="exit"):#exit game command
		sys.exit()
	elif((ord(c[0])<=74)and(ord(c[0])>=65)and(ord(c[1])<=57)and(ord(c[1])>=48)):#uppercase letters
		if(maps[int(c[1])+(ord(c[0])-65)*10][0]=="X"):
			grid[int(c[1])+(ord(c[0])-65)*10]=grid[int(c[1])+(ord(c[0])-65)*10].replace("O","X")
			print("|  | .   |   |\n|--| |  -|-  |\n|  | |   |   .\n\n\n\n\n\n\n\n")
		else:
			grid[int(c[1])+(ord(c[0])-65)*10]=grid[int(c[1])+(ord(c[0])-65)*10].replace("O","0")
			maps[int(c[1])+(ord(c[0])-65)*10]=maps[int(c[1])+(ord(c[0])-65)*10].replace("O","0")
			print("  /\  /\   .  ___  ___\n /  \/  \  | |__  |__\n/        \ | ___| ___|\n\n\n\n\n\n\n\n")
	elif((ord(c[0])<=106)and(ord(c[0])>=97)and(ord(c[1])<=57)and(ord(c[1])>=48)):#lowercase letters
		if(maps[int(c[1])+(ord(c[0])-97)*10][0]=="X"):
			grid[int(c[1])+(ord(c[0])-97)*10]=grid[int(c[1])+(ord(c[0])-97)*10].replace("O","X")
			print("|  | .  |  |\n|--| | -|- |\n|  | |  |  .\n\n\n\n\n\n\n\n")
		else:
			grid[int(c[1])+(ord(c[0])-97)*10]=grid[int(c[1])+(ord(c[0])-97)*10].replace("O","0")
			maps[int(c[1])+(ord(c[0])-97)*10]=maps[int(c[1])+(ord(c[0])-97)*10].replace("O","0")
			print("  /\  /\   .  ___  ___\n /  \/  \  | |__  |__\n/        \ | ___| ___|\n\n\n\n\n\n\n\n")
	else:#bad input
		print("Example: A1 or a1")
	return
def win(v=False):#check if all ships have been sunk, restarting/closing game
	e=True
	for c in range(0,100):
		if(maps[c]!=grid[c]):#checks if all ships have been sunk
			e=False
	if((e==True)or(v==True)):
		r=raw_input("\ /  _        \        / .  __  |\n |  / \ |  |   \  /\  /  | |  | |\n |  \_/ |__|    \/  \/   | |  | .\n\nTry again? (y/n) ")
		if(r=="y"):#restarts game and randomizes boats
			for c in range(0,100):
				if((grid[c][0]=="0")or(grid[c][0]=="X")):
					grid[c]="O "
				if((maps[c][0]=="0")or(maps[c][0]=="X")):
					maps[c]="O "
			ship(5)
			ship(4)
			ship(3)
			ship(3)
			ship(2)
			print(" _       |   |  |  _   ___ |   .  _     _\n|_\  _  -|- -|- | |_| |__  |_  | |_|   |_| \/\n|_/ |_\  |   |  | |__ ___| | | | |   . |   /\n\n\n\n\n\n\n\n")
		else:#ends game
			sys.exit()
	return
ship(5)#standard set of Battleship ships
ship(4)
ship(3)
ship(3)
ship(2)
print(" _       |   |  |  _   ___ |   .  _     _\n|_\  _  -|- -|- | |_| |__  |_  | |_|   |_| \/\n|_/ |_\  |   |  | |__ ___| | | | |   . |   /\n\n\n\n\n\n\n\n")
while(True):#main game sequence
	print("\n"+blit(grid))#print grid
	hits(raw_input("->"))#shoot
	win()#check if won
