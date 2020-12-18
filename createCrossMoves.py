from cube import Cube
import json
import copy
# import fileUtils
import numpy as np

optimalMoves = {}

# def createMoves(cube, moveCount):
#     for i in range(12):
#         newCube = copy.deepcopy(cube)
#         newCube.integerTurn(i)
#         state = str(newCube.getVectorStateOfCrossPieces())
#         if(state not in optimalMoves):
#             optimalMoves[state] = (moveCount, newCube.encoder.fit_transform(turnOptions[i]).toarray()[0])
#         elif(state in optimalMoves and optimalMoves[state][0] > moveCount):
#             optimalMoves[state] = (moveCount, newCube.encoder.fit_transform(turnOptions[i]).toarray()[0])
#     return

def recursiveGeneration(cube, prev, moveCount, max):
    if(moveCount > max):
        return
    for i in range(12):
        if(i % 2 == 0 and prev == i + 1):
            continue
        if(i % 2 == 1 and prev == i - 1):
            continue

        newCube = copy.deepcopy(cube)
        newCube.integerTurn(i)
        state = str(newCube.getVectorStateOfCrossPieces())
        moveToEncode = np.array(newCube.turnOptions[i]).reshape(1,-1)

        if(state not in optimalMoves):
            optimalMoves[state] = (
                moveCount, list(newCube.encoder.fit_transform(moveToEncode).toarray()[0]))
        elif(state in optimalMoves and optimalMoves[state][0] > moveCount):
            optimalMoves[state] = (
                moveCount, list(newCube.encoder.fit_transform(moveToEncode).toarray()[0]))

        recursiveGeneration(newCube, i, moveCount + 1, max)

    if(moveCount == 4):
        print("Branch at level 3 complete: ", i)

# create the all first seven possible moves and determine their optimal move back to solved
def createFirstSevenMoves():
    cube = Cube()
    recursiveGeneration(cube, -1, 1, 7)
    output = open("optimalMovesCross7.json", "w", encoding='utf8')
    str = json.dumps(optimalMoves, indent=4)
    output.write(str)
    return

createFirstSevenMoves()
# def createFirstEightMoves():
#     lines = readListsFromFile("optimalMovesCross7.json")
#     list = []
#     tuples = []
#     for i in range(0, len(lines), 2):
#         state = convertStringToList(lines[i])
#         properties = convertStringToTuple(lines[i+1])
#         list.append(state)
#         tuples.append(properties)
#
#     for i in range(len(tuples)):
#         if tuples[i][0] == 7:
#             createMoves(list[i])
#     print(list)
#     print(tuple)
#     i = 0
