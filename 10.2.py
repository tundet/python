# -*- coding: cp1252 -*-

class Player:
    teamcolor = "Blue"
    __points = 0

    def tellscore(self):
        print("I am", self.teamcolor+", we have", self.__points, "points!")
    def goal(self):
        self.__points += 1
    def printout(self):
        print("The", self.teamcolor,"contender has", self.__points,"points!")

def main():
    bigman = Player()
    bigman.goal()
    bigman.tellscore()

if __name__=="__main__":
    main()