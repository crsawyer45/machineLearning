import random
import cubeConstants
import numpy as np
from piece import Piece


class Cube:
    def __init__(self, pieceList=None):
        if pieceList is None:
            self.solved = True
            self.pieces = []
            for x in range(-1, 2, 1):
                for y in range(-1, 2, 1):
                    for z in range(-1, 2, 1):
                        if x == 0 and y == 0 and z == 0:
                            continue
                        self.pieces.append(Piece([x, y, z]))
        else:
            self.solved = False
            self.pieces = pieceList
        self.moves = []
        self.leftColor = self.getColor(-1, 0, 0, 'x')
        self.frontColor = self.getColor(0, -1, 0, 'y')
        self.rightColor = self.getColor(1, 0, 0, 'x')
        self.backColor = self.getColor(0, 1, 0, 'y')
        self.upperColor = self.getColor(0, 0, 1, 'z')
        self.downerColor = self.getColor(0, 0, -1, 'z')
        return

    # randomly mixes the cube using 30 turns --- currently same mix every time
    def mix(self):
        seq = []
        for i in range(10):
            random.seed()
            seq.append(random.choice(cubeConstants.turnOptions))
        self.turnCube(seq)
        print(seq)
        # print(self.moves)
        self.moves = []
        return

    # turns the cube given a one-hot vector of the 12 turns
    def vectorTurn(self, turn):
        for i in range(len(turn)):
            if turn[i] == 1:
                self.turnCube([cubeConstants.turnOptions[i]])
                break
        return

    # turns the cube given a value between 0 and 11
    def integerTurn(self, turn):
        if 0 <= turn < 12:
            self.turnCube([cubeConstants.turnOptions[turn]])
        else:
            print("bad turn integer")
        return

    # pass character sequence for moves to be carried out in order on cube
    def turnCube(self, sequence):
        for i in sequence:
            if i == "R":
                self.__R()
            elif i == "L":
                self.__L()
            elif i == "B":
                self.__B()
            elif i == "F":
                self.__F()
            elif i == "U":
                self.__U()
            elif i == "D":
                self.__D()
            elif i == "R'":
                self.__Rp()
            elif i == "L'":
                self.__Lp()
            elif i == "B'":
                self.__Bp()
            elif i == "F'":
                self.__Fp()
            elif i == "U'":
                self.__Up()
            elif i == "D'":
                self.__Dp()
            elif i == "->":
                self.__rotateRight()
            elif i == "<-":
                self.__rotateLeft()
            else:
                print("bad sequence list command: ", i)
        return

    # turn the back face of the cube
    def __B(self):
        # rotate piece representation
        for piece in self.pieces:
            if piece.pos[1] == 1:
                piece.rotate(cubeConstants.rotYi, "y")
        self.moves.append("B")
        return

    # turn the back face of the cube ccw
    def __Bp(self):
        # rotate piece representation
        for piece in self.pieces:
            if piece.pos[1] == 1:
                piece.rotate(cubeConstants.rotY, "y")
        self.moves.append("B'")
        return

    # turn the front face of the cube
    def __F(self):
        # rotate piece representation
        for piece in self.pieces:
            if piece.pos[1] == -1:
                piece.rotate(cubeConstants.rotY, "y")
        self.moves.append("F")
        return

    # turn the front face of the cube ccw
    def __Fp(self):
        # rotate piece representation
        for piece in self.pieces:
            if piece.pos[1] == -1:
                piece.rotate(cubeConstants.rotYi, "y")
        self.moves.append("F'")
        return

    # turn the right face of the cube cw
    def __R(self):
        # rotate piece representation
        for piece in self.pieces:
            if piece.pos[0] == 1:
                piece.rotate(cubeConstants.rotXi, "x")
        self.moves.append("R")
        return

    # turn the right face of the cube ccw
    def __Rp(self):
        # rotate piece representation
        for piece in self.pieces:
            if piece.pos[0] == 1:
                piece.rotate(cubeConstants.rotX, "x")
        self.moves.append("R'")
        return

    # turn the left face of the cube
    def __L(self):
        # rotate piece representation
        for piece in self.pieces:
            if piece.pos[0] == -1:
                piece.rotate(cubeConstants.rotX, "x")
        self.moves.append("L")
        return

    # turn the left face of the cube ccw
    def __Lp(self):
        # rotate piece representation
        for piece in self.pieces:
            if piece.pos[0] == -1:
                piece.rotate(cubeConstants.rotXi, "x")
        self.moves.append("L'")
        return

    # turn the downer face of the cube
    def __D(self):
        # rotate piece representation
        for piece in self.pieces:
            if piece.pos[2] == -1:
                piece.rotate(cubeConstants.rotZ, "z")
        self.moves.append("D")
        return

    # turn the downer face of the cube ccw
    def __Dp(self):
        # rotate piece representation
        for piece in self.pieces:
            if piece.pos[2] == -1:
                piece.rotate(cubeConstants.rotZi, "z")
        self.moves.append("D'")
        return

    # turn the upper face of the cube
    def __U(self):
        # rotate piece representation
        for piece in self.pieces:
            if piece.pos[2] == 1:
                piece.rotate(cubeConstants.rotZi, "z")
        self.moves.append('U')
        return

    # turn the upper face of the cube ccw
    def __Up(self):
        # rotate piece representation
        for piece in self.pieces:
            if piece.pos[2] == 1:
                piece.rotate(cubeConstants.rotZ, "z")
        self.moves.append("U'")
        return

    # rotate side perspective of cube by 90 deg, way easier in just piece representation
    def __rotateRight(self):
        for piece in self.pieces:
            piece.rotate(cubeConstants.rotZ, "z")
        self.leftColor, self.frontColor, self.rightColor, self.backColor = \
            self.backColor, self.leftColor, self.frontColor, self.rightColor
        self.moves.append("->")
        return

    # rotate side perspective of cube by -90 deg, way easier in just piece representation
    def __rotateLeft(self):
        for piece in self.pieces:
            piece.rotate(cubeConstants.rotZi, "z")
        self.leftColor, self.frontColor, self.rightColor, self.backColor = \
            self.frontColor, self.rightColor, self.backColor, self.leftColor
        self.moves.append("<-")
        return

    # prints state of cube --- needs to be fixed for piece representation
    def printState(self):
        print(self.getFaceColors(z=1))
        print(self.getFaceColors(x=-1))
        print(self.getFaceColors(y=-1))
        print(self.getFaceColors(x=1))
        print(self.getFaceColors(y=1))
        print(self.getFaceColors(z=-1))
        return

    # returns the colors of a face in a string...not great but will do for now, maybe abandon getColor()
    def getFaceColors(self, x=None, y=None, z=None):
        face = ""
        if x == 1:
            for z in range(1, -2, -1):
                for y in range(-1, 2, 1):
                    face += self.getColor(x, y, z, 'x')
                face += '\n'

        elif x == -1:
            for z in range(1, -2, -1):
                for y in range(1, -2, -1):
                    face += self.getColor(x, y, z, 'x')
                face += '\n'

        elif y == 1:
            for z in range(1, -2, -1):
                for x in range(1, -2, -1):
                    face += self.getColor(x, y, z, 'y')
                face += '\n'

        elif y == -1:
            for z in range(1, -2, -1):
                for x in range(-1, 2, 1):
                    face += self.getColor(x, y, z, 'y')
                face += '\n'

        elif z == 1:
            for y in range(1, -2, -1):
                for x in range(-1, 2, 1):
                    face += self.getColor(x, y, z, 'z')
                face += '\n'

        elif z == -1:
            for y in range(-1, 2, 1):
                for x in range(-1, 2, 1):
                    face += self.getColor(x, y, z, 'z')
                face += '\n'

        return face

    # returns the color of a piece at a given position with a given face...maybe abandon this for getPiece() only
    def getColor(self, x, y, z, face):
        for piece in self.pieces:
            if piece.pos[0] == x and piece.pos[1] == y and piece.pos[2] == z:
                return piece.colors[face]

    # returns the state of the cube in a big one-hot vector
    def getVectorState(self):
        state = []  # back, downer, front, left, right, upper
        # back
        for z in range(1, -2, -1):
            for x in range(1, -2, -1):
                state.append(self.getColor(x, 1, z, 1))
        # downer
        for y in range(-1, 2, 1):
            for x in range(-1, 2, 1):
                state.append(self.getColor(x, y, -1, 2))
        # front
        for z in range(1, -2, -1):
            for x in range(-1, 2, 1):
                state.append(self.getColor(x, -1, z, 1))
        # left
        for z in range(1, -2, -1):
            for y in range(1, -2, -1):
                state.append(self.getColor(-1, y, z, 0))
        # right
        for z in range(1, -2, -1):
            for y in range(-1, 2, 1):
                state.append(self.getColor(1, y, z, 0))
        # upper
        for y in range(1, -2, -1):
            for x in range(-1, 2, 1):
                state.append(self.getColor(x, y, 1, 2))
        state = np.array(state).reshape(1, -1)
        state = cubeConstants.colorEncoder.fit_transform(state).toarray()
        return state[0]

    # returns the piece with the given position on the cube
    def getPiece(self, x, y, z):
        for piece in self.pieces:
            if piece.pos[0] == x and piece.pos[1] == y and piece.pos[2] == z:
                return piece

    # returns the state of the cross pieces in a one hot vector based on position
    def getVectorStateOfCrossPieces(self):
        left, front, right, back = [], [], [], []
        for piece in self.pieces:
            if piece.type != 'edge' or self.downerColor not in piece.colors.values():
                continue

            if self.leftColor in piece.colors.values():
                left = list(piece.pos)
                for i in piece.colors.values():
                    if i == self.downerColor:
                        left.append(1)
                    else:
                        left.append(0)

            elif self.frontColor in piece.colors.values():
                front = list(piece.pos)
                for i in piece.colors.values():
                    if i == self.downerColor:
                        front.append(1)
                    else:
                        front.append(0)

            elif self.rightColor in piece.colors.values():
                right = list(piece.pos)
                for i in piece.colors.values():
                    if i == self.downerColor:
                        right.append(1)
                    else:
                        right.append(0)

            elif self.backColor in piece.colors.values():
                back = list(piece.pos)
                for i in piece.colors.values():
                    if i == self.downerColor:
                        back.append(1)
                    else:
                        back.append(0)

        return left + front + right + back

    # returns the state of the corner pieces in a one hot vector
    def getVectorStateOfCornerPieces(self):
        state = []
        for x in range(-1, 2, 2):
            for y in range(-1, 2, 2):
                for z in range(-1, 2, 2):
                    for dim in range(3):
                        state.append(self.getColor(x, y, z, dim))
        state = np.array(state).reshape(1, -1)
        state = cubeConstants.colorEncoder.fit_transform(state).toarray()
        return state[0]

    # gets the state of the edges pieces in a one hot vector
    def getVectorStateOfEdgePieces(self):
        edges = []
        for z in range(-1, 2):
            for y in range(-1, 2):
                for x in range(-1, 2):
                    if (x+y+z == -2 or x+y+z == 2 or x+y+z == 0) and not (x == 0 and y == 0 and z == 0):
                        edges.append(self.getColor(x, y, z, 'x'))
                        edges.append(self.getColor(x, y, z, 'y'))
                        edges.append(self.getColor(x, y, z, 'z'))
        for i in range(12):
            edges.remove(None)
        # print(edges)
        edges = np.array(edges).reshape(1, -1)
        return cubeConstants.colorEncoder.fit_transform(edges).toarray()[0]

    # returns the number of cross pieces in the correct place (max 4)
    def getNumberOfCrossPiecesSolved(self):
        num = 0
        for piece in self.pieces:
            if list(piece.pos) == [-1, 0, -1] and \
                    piece.colors == {'x': self.leftColor, 'y': None, 'z': self.downerColor}:
                num += 1
            elif list(piece.pos) == [0, -1, -1] and \
                    piece.colors == {'x': None, 'y': self.frontColor, 'z': self.downerColor}:
                num += 1
            elif list(piece.pos) == [1, 0, -1] and \
                    piece.colors == {'x': self.rightColor, 'y': None, 'z': self.downerColor}:
                num += 1
            elif list(piece.pos) == [0, 1, -1] and \
                    piece.colors == {'x': None, 'y': self.backColor, 'z': self.downerColor}:
                num += 1
        return num

    # returns the number of first layer corner pieces in the correct place (max 4)
    def getNumberOfBottomCornerPiecesSolved(self):
        num = 0
        for x in range(-1, 2, 2):
            for y in range(-1, 2, 2):
                corner = self.getPiece(x, y, -1).colors
                centerx = self.getPiece(x, 0, 0).colors['x']
                centery = self.getPiece(0, y, 0).colors['y']
                if corner['x'] == centerx and corner['y'] == centery and corner['z'] == self.downerColor:
                    num += 1
        return num

    def getNumberOfMiddleEdgePiecesSolved(self):
        num = 0
        for x in range(-1, 2, 2):
            for y in range(-1, 2, 2):
                edge = self.getPiece(x, y, 0).colors
                centerx = self.getPiece(x, 0, 0).colors['x']
                centery = self.getPiece(0, y, 0).colors['y']
                if edge['x'] == centerx and edge['y'] == centery:
                    num += 1
        return num

    def getNumberOfLastLayerPiecesOriented(self):
        return
