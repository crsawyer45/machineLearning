import cubeConstants
import json


class Solver:
    def __init__(self, cube):
        self.cube = cube
        self.crossMoves = json.loads(open("crossMoves.json").read())
        return

    def solveCube(self):
        self.solveCross()
        self.solveFirstLayer()
        self.solveSecondLayer()
        self.__orientLastLayer()
        self.__permuteLastLayer()
        return self.optimizedMoves()

    def solveCross(self):
        while self.cube.getNumberOfCrossPiecesSolved() != 4:
            state = str(self.cube.getVectorStateOfCrossPieces())
            self.cube.vectorTurn(self.crossMoves[state])
        return

    def solveFirstLayer(self):
        while self.cube.getNumberOfBottomCornerPiecesSolved() != 4:
            for i in range(4):
                rightCorner = self.cube.getPiece(1, -1, 1).colors

                if rightCorner['y'] == self.cube.downerColor and rightCorner['x'] == self.cube.rightColor and \
                        rightCorner['z'] == self.cube.frontColor:
                    self.cube.turnCube(cubeConstants.firstLayerAlgorithms[0])
                    self.cube.turnCube(cubeConstants.firstLayerAlgorithms[4])
                    break

                elif rightCorner['x'] == self.cube.downerColor and rightCorner['y'] == self.cube.frontColor and \
                        rightCorner['z'] == self.cube.rightColor:
                    self.cube.turnCube(cubeConstants.firstLayerAlgorithms[1])
                    self.cube.turnCube(cubeConstants.firstLayerAlgorithms[4])
                    break

                elif rightCorner['z'] == self.cube.downerColor and rightCorner['x'] == self.cube.frontColor and \
                        rightCorner['y'] == self.cube.rightColor:
                    self.cube.turnCube(cubeConstants.firstLayerAlgorithms[2])
                    self.cube.turnCube(cubeConstants.firstLayerAlgorithms[4])
                    break

                else:
                    self.cube.turnCube(cubeConstants.firstLayerAlgorithms[3])

                bottomCorner = self.cube.getPiece(1, -1, -1).colors
                if self.cube.downerColor in bottomCorner.values() and \
                        (bottomCorner['x'] != self.cube.rightColor or bottomCorner['y'] != self.cube.frontColor or
                         bottomCorner['z'] != self.cube.downerColor):
                    self.cube.turnCube(cubeConstants.firstLayerAlgorithms[0])
                    break

            self.cube.turnCube(cubeConstants.firstLayerAlgorithms[4])
        return

    def solveSecondLayer(self):
        while self.cube.getNumberOfMiddleEdgePiecesSolved() != 4:
            for i in range(4):
                frontEdge = self.cube.getPiece(0, -1, 1).colors
                rightEdge = self.cube.getPiece(1, 0, 1).colors

                if frontEdge['y'] == self.cube.frontColor and frontEdge['z'] == self.cube.rightColor:
                    self.cube.turnCube(cubeConstants.secondLayerAlgorithms[0])

                elif rightEdge['x'] == self.cube.rightColor and rightEdge['z'] == self.cube.frontColor:
                    self.cube.turnCube(cubeConstants.secondLayerAlgorithms[1])

                else:
                    self.cube.turnCube(cubeConstants.secondLayerAlgorithms[2])

                middleEdge = self.cube.getPiece(1, -1, 0).colors
                if self.cube.upperColor not in middleEdge.values() and \
                        (middleEdge['y'] != self.cube.frontColor or middleEdge['x'] != self.cube.rightColor):
                    self.cube.turnCube(cubeConstants.secondLayerAlgorithms[0])

            self.cube.turnCube(cubeConstants.secondLayerAlgorithms[3])
        return

    def __orientLastLayer(self):
        while self.cube.getNumberOfLastLayerPiecesOriented() != 9:
            break
        return

    def __permuteLastLayer(self):
        return

    def optimizedMoves(self):
        moveList = self.cube.moves
        return moveList
