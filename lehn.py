#School Assignment that deals with number validation using the Lehn Algorithm.

from os import system
from sys import exit

import pygame

h = []

def sin():
    global a,c,n
    c = 0
    a = list(n[len(n) - 1::-1])
    
    for l in range(1, len(a),2):
        a[l] = str(int(a[l]) * 2)
        
        if int(a[l]) > 9:
            a[l] = str(int(a[l][0]) + int(a[l][1]))
    
    valid()

def ccn():
    global a,c,n
    c = int(n[len(n) - 1])
    a = list(n[len(n) - 2::-1])
    
    for l in range(1, len(a),2):
        a[l] = str(int(a[l]) * 2)
        
        if int(a[l]) > 9:
            a[l] = str(int(a[l]) - 9)
    
    
    valid()

def valid():
    global a,c,n
    t = 0
    
    for l in range(0, len(a)):
        t = t + int(a[l])
    
    if t % 10 == c:
        print 'The Number, "' + n + '" is Valid.'
        h.append(n + ", Valid")
    else:
        print 'The Number, "' + n + '" is NOT Valid.'
        h.append(n + ", Invalid")

while True:
    while True:
        n = raw_input("Enter a 9 or 16 Digit Number: ")
        
        if(n.isdigit() and (9 <= len(n) <= 16)):
            system("cls")
            break
        
        system("cls")
        print "[ERROR] Please Try Again.\n"
    
    if len(n) == 9:
        sin()
    else:
        ccn()
    
    while True:
        print "\n1. Enter Another Number\n2. View History\n3. Exit\n"
        menu = raw_input(">")
        system("cls")
        
        if menu == "1":
            break
        elif menu == "2":
            print "[HISTORY]"
            for l in range(0, len(h)):
                print str(l+1) + ". " + h[l] + "\n"
        elif menu == "3":
            exit()

