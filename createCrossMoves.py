import cubeConstants
from cube import Cube
import json
import copy
import numpy as np


def run():
    cubeDict = {}
    cube = Cube()
    cubeDict[0] = [cube]
    masterMoveDict = generateMoves(cubeDict, {}, 9, 1)
    file = open('crossMoves.json', "w", encoding="utf8")
    string = json.dumps(masterMoveDict, indent=4)
    file.write(string)
    return


def generateMoves(cubeDict, moveDict, movesToGenerate, moveCount):
    if moveCount > movesToGenerate:
        return moveDict
    else:
        cubeDict[moveCount] = []
        for cube in cubeDict[moveCount - 1]:
            for i in range(12):
                newCube = copy.deepcopy(cube)
                newCube.integerTurn(i)
                state = str(newCube.getVectorStateOfCrossPieces())

                # determine the move needed to undo the rotation that was just made
                if i % 2 == 0:
                    moveToEncode = np.array(cubeConstants.turnOptions[i+1]).reshape(1, -1)
                else:
                    moveToEncode = np.array(cubeConstants.turnOptions[i-1]).reshape(1, -1)

                # if the new state of the cube is not in the dict, add it and the turn needed to undo it
                if state not in moveDict:
                    moveDict[state] = list(cubeConstants.turnEncoder.fit_transform(moveToEncode).toarray()[0])
                    cubeDict[moveCount].append(newCube)
        print('Move Completed: ', moveCount)
        return generateMoves(cubeDict, moveDict, movesToGenerate, moveCount+1)


if __name__ == "__main__":
    run()
