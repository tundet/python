# -*- coding: cp1252 -*-

def main():
    number = int(input("Give a number: "))
    poweroftwo(number)

def poweroftwo(n):
    res = 2**n
    print("The result is", res)

if __name__ == "__main__":
    main()