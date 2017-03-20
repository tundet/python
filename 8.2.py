# -*- coding: cp1252 -*-

filename = input("Give the file name: ")
try:
    filecontent = open(filename,"r")
    number = int(filecontent.read())
    filecontent.close()
    result = 1000 / number
    print("The result was",result)
except IOError:
    print("There seems to be no file with that name.")
except ValueError:
    print("The file contents were unsuitable.")
except Exception:
    print("There was a problem with the program.")



