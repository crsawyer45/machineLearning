import json
import numpy as np
import re

def readListsFromFile(file):
    file = open(file, "r", encoding='utf8')
    data = file.readlines()
    return data

def convertStringToList(string):
    string = re.sub(',', '', string)
    string = re.sub('\[', '', string)
    string = re.sub('\]', '', string)
    stringList = string.split()
    list = []
    for i in stringList:
        list.append(float(i))
    return list

def convertStringToTuple(string):
    string = re.sub(',', '', string)
    string = re.sub('\(', '', string)
    string = re.sub('\)', '', string)
    values = string.split()
    for i in range(len(values)):
        values[i] = int(values[i])
    return tuple(values)


# lines = readListsFromFile("optimalMovesCross3.json")
# list = convertStringToList(lines[0])
# tuple = convertStringToTuple(lines[1])
# print(list)
# print(tuple)
