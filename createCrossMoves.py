from cube import Cube
import json
import copy
import fileUtils

optimalMoves = {}

def createMoves(cube):
    for i in range(12):
        newCube = copy.deepcopy(cube)
        newCube.integerTurn(i)
        state = str(newCube.getVectorStateOfCrossPieces())
        if(state not in optimalMoves):
            optimalMoves[state] = (moveCount, newCube.turnOptions[i])
        elif(state in optimalMoves and optimalMoves[state][0] > moveCount):
            optimalMoves[state] = (moveCount, newCube.turnOptions[i])


def recursiveGeneration(cube, prev, moveCount):
    if(moveCount > 3):
        return
    for i in range(12):
        if(i % 2 == 0 and prev == i + 1):
            continue
        if(i % 2 == 1 and prev == i - 1):
            continue
        newCube = copy.deepcopy(cube)
        newCube.integerTurn(i)
        state = str(newCube.getVectorStateOfCrossPieces())
        if(state not in optimalMoves):
            optimalMoves[state] = (moveCount, newCube.turnOptions[i])
        elif(state in optimalMoves and optimalMoves[state][0] > moveCount):
            optimalMoves[state] = (moveCount, newCube.turnOptions[i])
        recursiveGeneration(newCube, i, moveCount + 1)
    if(moveCount == 4):
        print("Branch at level 3 complete: ", i)

def createFirstSevenMoves():
    cube = Cube()
    recursiveGeneration(cube, -1, 1)
    output = open("optimalMovesCross7.json", "w", encoding='utf8')
    for i in optimalMoves:
        string = ""
        string = i + "\n" + str(optimalMoves[i]) + "\n"
        output.write(string)

def createFirstEightMoves():
    lines = readListsFromFile("optimalMovesCross7.json")
    list = []
    tuples = []
    for i in range(0, len(lines), 2):
        state = convertStringToList(lines[i])
        properties = convertStringToTuple(lines[i+1])
        list.append(state)
        tuples.append(properties)
        optimalMoves[str(state)] = properties


    for i in range(len(tuples)):
        if tuples[i][0] == 7:
            createMoves(list[i])
    print(list)
    print(tuple)
    i = 0
