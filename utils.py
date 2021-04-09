import json
import numpy as np
import re
from piece import Piece

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
        list.append(int(float(i)))
    return list


def convertStringToTuple(string):
    string = re.sub(',', '', string)
    string = re.sub('\(', '', string)
    string = re.sub('\)', '', string)
    values = string.split()
    for i in range(len(values)):
        values[i] = int(values[i])
    return tuple(values)


def makePiecesFromCrossStateString(string):
    state = convertStringToList(string)
    pieces = []
    for i in range(4):
        position = [state[6 * i + 0], state[6 * i + 1], state[6 * i + 2]]
        temp = [state[6 * i + 3], state[6 * i + 4], state[6 * i + 5]]
        colors = []
        for c in range(len(temp)):
            if temp[c] == 1:
                colors.append("W")
            else:
                colors.append("X")
        pieces.append(Piece(position, i, colors))
    return pieces

# lines = readListsFromFile("optimalMovesCross3.json")
# list = convertStringToList(lines[0])
# tuple = convertStringToTuple(lines[1])
# print(list)
# print(tuple)
