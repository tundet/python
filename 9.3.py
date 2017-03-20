# -*- coding: cp1252 -*-

filehandle = open("words.txt","r")
words = filehandle.readlines()
filehandle.close()
words.sort()
print("Words in an alphabetical order:")
for i in words:
    print(i[:-1])
