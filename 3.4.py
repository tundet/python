# -*- coding: cp1252 -*-

n1 = int(input("Give a number: "))
n2 = int(input("Give another number: "))

if(n1 % 2 == 0 and n2 % 2 == 0):
    print("Both numbers are even.")
elif(n1 % 2 == 0 or n2 % 2 == 0):
    print("One of the numbers is even.")
else:
    print("Both numbers are odd.")
