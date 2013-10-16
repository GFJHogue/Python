from os import system

import pygame

h = []

while True:
    t = 0
    
    while True:
        n = raw_input("Enter a 9 or 16 Digit Number: ")
        
        if(n.isdigit() and (len(n) == 9 or len(n) == 16)):
            system("cls")
            break
        
        system("cls")
        print "[ERROR] Please Try Again.\n"
    
    c = int(n[len(n)-1])
    a = list(n[len(n)-2::-1])
    
    for l in range(0, len(a),2):
        a[l] = str(int(a[l]) * 2)
        if int(a[l]) > 9:
            a[l] = str(int(a[l]) - 9)

    for l in range(0, len(a)):
        t = t + int(a[l])
    
    if t % 10 == c:
        print 'The Number, "' + n + '" is Valid.'
        h.append(n + ", Valid")
    else:
        print 'The Number, "' + n + '" is NOT Valid.'
        h.append(n + ", Invalid")
    
    while True:
        print "\n1. Enter Another Number\n2. View History\n3. Exit\n"
        menu = raw_input(">")
        system("cls")
        
        if menu == "1" or menu == "3":
            break
        elif menu == "2":
            print "[HISTORY]"
            for l in range(0, len(h)):
                print str(l+1) + ". " + h[l] + "\n"
    
    if menu == "3":
        break
