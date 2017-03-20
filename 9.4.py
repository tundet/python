# -*- coding: cp1252 -*-

import time
import pickle

notefile = "notebook.dat"
notelist = []
try:
    handle = open(notefile,"rb")
    notelist = pickle.load(handle)
    handle.close()
except Exception:
    print("No default notebook was found, created one.")
    handle = open(notefile,"w")
    handle.close()

while True:
    print("(1) Read the notebook\n(2) Add note\n\
(3) Edit a note\n(4) Delete a note\n(5) Save and quit\n")
    selection = int(input("Please select one: "))
    if selection == 1:
        for i in notelist:
            print(i)
    elif selection == 2:
        newnote = input("Write a new note: ")
        timestamp = time.strftime("%X %x")
        notelist.append(newnote+":::"+timestamp)
    elif selection == 3:
        print("The list has",len(notelist),"notes.")
        changenote = int(input("Which of them will be changed?: "))-1
        print(notelist[changenote])
        uusi = input("Give the new note: ")
        timestamp = time.strftime("%X %x")
        notelist[changenote] = uusi+":::"+timestamp
    elif selection == 4:
        print("The list has",len(notelist),"notes.")
        deleteme = int(input("Which of them will be deleted?: "))-1
        deletednote = notelist.pop(deleteme)
        print("Deleted note",deletednote)
    elif selection == 5:
        savedata = open(notefile,"wb")
        pickle.dump(notelist,savedata)
        savedata.close()
        print("Notebook shutting down, thank you.")
        break
    else:
        print("Incorrect selection.")

