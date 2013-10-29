from os import system
from sys import exit


f = [[],[],[]]

while True:
    while len(f[1]) <= len(f[0]):
        f[1].append("")
    
    while len(f[2]) <= len(f[0]):
        f[2].append("")
    
    if len(f[0]) == 0:
        print "[iHaveNoFriends]"
    else:
        print "[Friends]"
    
    w = "[FRIENDS]\n"
    
    for c in range(0,len(f[0])):
        print(str(c + 1) + ". " + f[0][c] +
            (" | Phone #: " + f[1][c]) * (len(f[1][c]) > 0) +
            (" | Email: " + f[2][c]) * (len(f[2][c]) > 0))
        w = w + "\n\n" + f[0][c] + "\n\t" + f[1][c] + "\n\t" + f[2][c]
    
    file = open("friends.txt","w")
    file.write(w)
    file.close()
    
    menu = raw_input("\n[MENU]\n1. Add a new friend\n2. Delete a Friend (by " +
        "index)\n3. Delete a Friend (by name)\n4. Add a new friend (specific" +
        "location)\n5. Sort Friends Alphabetically\n6. Add a Friend's Phone " +
        "#\n7. Add a Friend's Email\n8. Exit\n\n>")
    
    if menu == "1":
        f[0].append(raw_input("\nEnter Name: "))
    elif menu == "2":
        while True:
            i = raw_input("\nEnter Index of Friend to Delete: ")
            
            if i.isdigit():
                i = int(i) - 1
                break
        
        f[0].pop(i)
    elif menu == "3":
        while True:
            n = raw_input("\nEnter Name of Friend to Delete: ")
            
            if f[0].count(n) > 0:
                break
        
        f[0].remove(n)
        f[1].remove(n)
        f[2].remove(n)
    elif menu == "4":
        while True:
            i = raw_input("\nEnter Index to Add Friend To: ")
            
            if i.isdigit():
                i = int(i) - 1
                break
        
        f[0].insert(i,raw_input("\nEnter Name: "))
        f[1].insert(i,"")
        f[2].insert(i,"")
    elif menu == "5":
        s = []
        
        for c in range(0,len(f[0])):
            s.append([f[0][c],f[1][c],f[2][c]])
        
        s.sort()
        
        for c in range(0,len(s)):
            f[0][c] = s[c][0]
            f[1][c] = s[c][1]
            f[2][c] = s[c][2]
        
    elif menu == "6":
        while True:
            n = raw_input("\nEnter Name of Friend: ")
            
            if f[0].count(n) > 0:
                break
        
        while True:
            f[1][f[0].index(n)] = raw_input("\nEnter Phone #:")
            
            if f[1][f[0].index(n)].isdigit():
                break
    elif menu == "7":
        while True:
            n = raw_input("\nEnter Name of Friend: ")
            
            if f[0].count(n) > 0:
                break
        
        f[2][f[0].index(n)] = raw_input("\nEnter Email: ") 
    elif menu == "8":
        exit()
    
    system("cls")
