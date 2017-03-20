# -*- coding: cp1252 -*-

import math

print("Calculator")
number1 = int(input("Give the first number: "))
number2 = int(input("Give the second number: "))

while True:
    print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2)\n\
(6)cos(number1/number2)\n(7)Change numbers\n(8)Quit")
    print("Current numbers:",number1,number2)
    selection = int(input("Please select something (1-6): "))
    if selection == 1:
        print("The result is:", number1+number2)
    elif selection == 2:
        print("The result is:", number1-number2)
    elif selection == 3:
        print("The result is:", number1*number2)
    elif selection == 4:
        print("The result is:", number1/number2)
    elif selection == 5:
        print("The result is:", math.sin(number1/number2))
    elif selection == 6:
        print("The result is:", math.cos(number1/number2))
    elif selection == 7:
        number1 = int(input("Give the first number: "))
        number2 = int(input("Give the second number: "))
    elif selection == 8:
        print("Thank you!")
        break
    else:
        print("Selection was not correct.")
