# -*- coding: cp1252 -*-

FILE_NAME = "notebook.txt"

while True:

    print("(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Quit\n")
    choice = int(input("Please select one: "))

    if(choice == 1):
        handle = open(FILE_NAME, "r")
        content = handle.read()
        print(content)
    elif(choice == 2):
        handle = open(FILE_NAME, "a")
        note = input("Write a new note: ")
        handle.write(note + "\n")
        handle.close()
    elif(choice == 3):
        handle = open(FILE_NAME, "w")
        handle.close()
        print("Notes deleted.")
    elif(choice == 4):
        print("Notebook shutting down, thank you.")
        break
    else:
        print("Incorrect selection")
