#School Assignment that deals with number validation using the Luhn Algorithm.

from os import system
from random import randint
from sys import exit


def num(d):
    global n
    
    while True:
        n = raw_input("Enter a " + str(d) + " Digit Number: ")
        
        if n.isdigit() and len(n) == d:
            system("cls")
            return True
        
        system("cls")
        print "[ERROR] Please Try Again.\n"

def ccn():
    validate(list(n[len(n) - 2::-1]),0, int(n[len(n) - 1]))

def sin():
    validate(list(n),1,0)

def validate(a,m,c):
    global h,n
    t = 0
    
    for l in range(m, len(a),2):
        a[l] = str(int(a[l]) * 2)
        
        if int(a[l]) > 9:
            a[l] = str(int(a[l]) - 9)
    
    for l in range(0, len(a)):
        t = t + int(a[l])
    
    if (10 - (t % 10) == c and m == 0) or t % 10 == c:
        print 'The Number, "' + n + '", is Valid.'
        h.append(n + ", Valid")
    else:
        print 'The Number, "' + n + '", is NOT Valid.'
        h.append(n + ", Invalid")

def generateCCN():
    global h
    r = str(randint(0,999999999999999))
    a = list(r[::-1])
    t = 0
    
    for l in range(0,15,2):
        a[l] = str(int(a[l]) * 2)
        
        if int(a[l]) > 9:
            a[l] = str(int(a[l]) - 9)
    
    for l in range(0,15):
        t = t + int(a[l])
    
    r = r + str(10 - (t % 10))
    print 'New Credit Card Number: "' + r + '"'
    h.append(r + ", Generated")


h = []

while True:
    print ("\n1. Check A Credit Card Number\n2. Check A Social Insurance Num" +
        "ber\n3. Generate A Credit Card Number\n5. View History\n6. Exit\n")
    menu = raw_input(">")
    system("cls")
    
    if menu == "1":
        num(16)
        ccn()
    elif menu == "2":
        num(9)
        sin()
    elif menu == "3":
        generateCCN()
    elif menu == "5":
        print "[HISTORY]"
        
        for l in range(0, len(h)):
            print str(l+1) + ". " + h[l] + "\n"
        
    elif menu == "6":
        exit()


