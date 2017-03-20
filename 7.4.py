# -*- coding: cp1252 -*-

def testme(parameter):
    if len(parameter) < 6:
        return False
    elif parameter.isalpha() == True:
        return False
    elif parameter.isdigit() == True:
        return False
    else:
        return True