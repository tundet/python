# -*- coding: cp1252 -*-

userinput = input("Give a number: ")
try:
    userinput = int(userinput)
except Exception:
    print("The input was malformed.")
else:
    print("The input was suitable!")