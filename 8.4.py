# -*- coding: cp1252 -*-

import time
notefile = "notebook.txt"

while True:
    try:
        handle = open(notefile,"r")
        handle.close()
    except IOError:
        print("No default notebook was found, created one.")
        handle = open(notefile,"w")
        handle.close()

    print("Now using file",notefile)
    print("(1) Read the notebook\n(2) Add note\n\
(3) Empty the notebook\n(4) Change the notebook\n(5) Quit\n")
    selection = int(input("Please select one: "))
    if selection == 1:
        handle = open(notefile,"r")
        notelist = handle.read()
        print(notelist)
        handle.close()

    elif selection == 2:
        handle = open(notefile,"a")
        merkinta = input("Write a new note: ")
        timestamp = time.strftime("%X %x")
        handle.write(merkinta+":::"+timestamp+"\n")
        handle.close()

    elif selection == 3:
        handle = open(notefile,"w")
        handle.close()
        print("Notes deleted.")
    elif selection == 4:
        newfile = input("Give the name of the new file: ")
        try:
            handle = open(newfile,"r")
            handle.close()
            notefile = newfile
        except IOError:
            print("No notebook with that name detected, created one.")
            handle = open(newfile,"w")
            handle.close()
            notefile = newfile

    elif selection == 5:
        print("Notebook shutting down, thank you.")
        break
    else:
        print("Incorrect selection.")

