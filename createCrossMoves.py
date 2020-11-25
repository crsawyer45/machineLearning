from cube import Cube
import json
import copy

optimalMoves = {}

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
            optimalMoves[state] = (moveCount, prev)
        elif(state in optimalMoves and optimalMoves[state][0] > moveCount):
            optimalMoves[state] = (moveCount, prev)
        recursiveGeneration(newCube, i, moveCount + 1)
    if(moveCount == 4):
        print("Branch at level 3 complete: ", prev)

cube = Cube()
recursiveGeneration(cube, -1, 1)
output = open("optimalMovesCross7.json", "w", encoding='utf8')
for i in optimalMoves:
    string = ""
    string = i + "\n" + str(optimalMoves[i]) + "\n"
    output.write(string)
