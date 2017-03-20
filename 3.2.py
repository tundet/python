# -*- coding: cp1252 -*-

user = input("Give name: ")

if(user == "John"):
    user = input("Give password: ")
    if(user == "ABC123"):
        print("Both inputs are correct!")
    else:
        print("The password is incorrect.")
else:
    print("The given name is wrong.")