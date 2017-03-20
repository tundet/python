# -*- coding: cp1252 -*-

class Player:
    teamcolor = "Blue"
    points = "300"

    def printout(self):
        print("The", self.teamcolor,"contender has", self.points,"points!")

def main():
    bigman = Player()
    bigman.teamcolor = "Blue"
    bigman.points = 300
    bigman.printout()

if __name__=="__main__":
    main()