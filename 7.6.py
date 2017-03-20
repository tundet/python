# -*- coding: cp1252 -*-

import time

while True:
    print("(1) Read the notebook\n(2) Add note\n\
(3) Empty the notebook\n(4) Quit\n")
    selection = int(input("Please select one: "))
    if selection == 1:
        handle = open("notebook.txt","r")
        lista = handle.read()
        print(lista)
        handle.close()

    elif selection == 2:
        handle = open("notebook.txt","a")
        note = input("Write a new note: ")
        timestamp = time.strftime("%X %x")
        handle.write(note+":::"+timestamp+"\n")
        handle.close()

    elif selection == 3:
        handle = open("notebook.txt","w")
        handle.close()
        print("Notes deleted.")

    elif selection == 4:
        print("Notebook shutting down, thank you.")
        break
    else:
        print("Incorrect selection.")

