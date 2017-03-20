# -*- coding: cp1252 -*-

class Player:
    """Player-class: stores data on team colors and points."""
    __points = 0
    teamcolor= ""
    def __init__(self):
        self.teamcolor = input("What color do I get?: ")
    def tellscore(self):
        print("I am ",self.teamcolor,", we have ",self.__points," points!", sep ="")
    def goal(self):
        self.__points = self.__points + 1

def main():
    first = Player()
    second = Player()

    first.goal()
    first.goal()
    second.goal()
    first.tellscore()
    second.tellscore()

if __name__ == "__main__":
    main()