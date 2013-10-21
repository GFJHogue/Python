from os import system
from sys import exit


f = []

while True:
    menu = raw_input("1. Add a new friend\n2. Delete a Friend (by index)\n3." +
        " Delete a Friend (by name)\n4. Add a new friend (specific location)" +
        "\n5. Sort Friends Alphabetically\n6. Exit\n\n>")
    
    if menu == "1":
        f.append(raw_input())
    elif menu == "2":
    elif menu == "3":
    elif menu == "4":
    elif menu == "5":
    elif menu == "6":
        system("cls")
