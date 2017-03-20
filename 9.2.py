# -*- coding: cp1252 -*-

mylist = []
while True:
    selection = int(input("Would you like to\n(1)Add or\n(2)\
Remove items or\n(3)Quit?: "))
    if selection == 1:
        lisays = input("What will be added?: ")
        mylist.append(lisays)
    elif selection == 2:
        print("There are",len(mylist),"items in the list.")
        deleteme = input("Which item is deleted?: ")
        try:
            mylist.pop(int(deleteme))
        except Exception:
            print("Incorrect selection.")
    elif selection == 3:
        print("The following items remain in the list:")
        for i in mylist:
            print(i)
        break
    else:
        print("Incorrect selection.")