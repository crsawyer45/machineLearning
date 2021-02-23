from cube import Cube
import json
import copy
import utils
import numpy as np

optimalMoves = {}
newMoves = {}

def generateMoves(cube, moves, moveCount):
    for i in range(12):
        newCube = copy.deepcopy(cube)
        newCube.integerTurn(i)
        state = str(newCube.getVectorStateOfCrossPieces().tolist())
        moveToEncode = np.array(newCube.turnOptions[i]).reshape(1,-1)
        if(state not in moves and state not in newMoves):
            newMoves[state] = (moveCount, list(newCube.encoder.fit_transform(moveToEncode).toarray()[0]))
        elif(state in moves and moves[state][0] > moveCount):
            print("hit error")
            moves[state] = (moveCount, list(newCube.encoder.fit_transform(moveToEncode).toarray()[0]))
    return

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

# create the first eight possible moves using known first seven moves
def createOneAdditionalMove(startingMoveCount, input, output):
    dict = json.loads(open(input).read())
    print(len(dict))
    count = 0
    for i in dict:
        if dict[i][0] == startingMoveCount:
            count += 1
            cube = Cube(utils.makePiecesFromCrossStateString(i))
            generateMoves(cube, dict, startingMoveCount + 1)
    file = open(output, "w", encoding="utf8")
    str = json.dumps(newMoves, indent=4)
    file.write(str)
    return

# createOneAdditionalMove(8, "allMoves.json", "ninthMove.json")
#
# dict1 = json.loads(open("allMoves.json").read())
# dict2 = json.loads(open("ninthMove.json").read())
#
# dict3 = {**dict1, **dict2}
# file = open("allMovesFinal.json", "w", encoding="utf8")
# str = json.dumps(dict3, indent=4)
# file.write(str)

dict = json.loads(open("allCrossMoves.json").read())
print(len(dict))
