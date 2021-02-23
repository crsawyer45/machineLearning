from sklearn.preprocessing import OneHotEncoder
import random
import constants
import numpy as np
from piece import Piece

class Cube:
    def __init__(self, pieceList = None):
        if pieceList == None:
            self.solved = True
            self.pieces = []
            i = 0
            for x in range(-1,2,1):
                for y in range(-1,2,1):
                    for z in range(-1,2,1):
                        if(x == 0 and y == 0 and z == 0):
                            i += 1
                            continue
                        self.pieces.append(Piece([x,y,z], i))
                        i += 1
        else:
            self.solved = False
            self.pieces = pieceList
        self.moves = []
        self.turnOptions = ["B","B'","D","D'","F","F'","L","L'","R","R'","U","U'"]
        self.encoder = OneHotEncoder(categories= [self.turnOptions])
        self.categories = [['B','G','O','R','W','Y'] for i in range(24)]
        self.colorEncoder = OneHotEncoder(categories= self.categories)
        self.firstLayerAlgorithms = [
            ["B", "U", "B'"],
            ["B'", "U'", "B"],
            ["F", "U", "F'"],
            ["F'", "U'", "F"],
            ["L", "U", "L'"],
            ["L'", "U'", "L"],
            ["R", "U", "R'"],
            ["R'", "U'", "R"],
            ["U"],
            ["U'"]
        ]
        self.secondLayerAlgorithms = [
            ["U"],
            ["U", "B", "U'", "B'", "U'", "R'", "U", "R"],
            ["U", "F", "U'", "F'", "U'", "L'", "U", "L"],
            ["U", "L", "U'", "L'", "U'", "B'", "U", "B"],
            ["U", "R", "U'", "R'", "U'", "F'", "U", "F"],
            ["U'"],
            ["U'", "B'", "U", "B", "U", "L", "U'", "L'"],
            ["U'", "F'", "U", "F", "U", "R", "U'", "R'"],
            ["U'", "L'", "U", "L", "U", "F", "U'", "F'"],
            ["U'", "R'", "U", "R", "U", "B", "U'", "B'"]
        ]

    #turn the back face of the cube
    def __B(self):
        #rotate piece representation
        for piece in self.pieces:
            if(piece.pos[1] == 1):
                piece.rotate(constants.rotYi, "y")
        self.moves.append("B")
        return

    #turn the back face of the cube ccw
    def __Bp(self):
        #rotate piece representation
        for piece in self.pieces:
            if(piece.pos[1] == 1):
                piece.rotate(constants.rotY, "y")
        self.moves.append("B'")
        return

    #turn the front face of the cube
    def __F(self):
        #rotate piece representation
        for piece in self.pieces:
            if(piece.pos[1] == -1):
                piece.rotate(constants.rotY, "y")
        self.moves.append("F")
        return

    #turn the front face of the cube ccw
    def __Fp(self):
        #rotate piece representation
        for piece in self.pieces:
            if(piece.pos[1] == -1):
                piece.rotate(constants.rotYi, "y")
        self.moves.append("F'")
        return

    #turn the right face of the cube cw
    def __R(self):
        #rotate piece representation
        for piece in self.pieces:
            if(piece.pos[0] == 1):
                piece.rotate(constants.rotXi, "x")
        self.moves.append("R")
        return

    #turn the right face of the cube ccw
    def __Rp(self):
        #rotate piece representation
        for piece in self.pieces:
            if(piece.pos[0] == 1):
                piece.rotate(constants.rotX, "x")
        self.moves.append("R'")
        return

    #turn the left face of the cube
    def __L(self):
        #rotate piece representation
        for piece in self.pieces:
            if(piece.pos[0] == -1):
                piece.rotate(constants.rotX, "x")
        self.moves.append("L")
        return

    #turn the left face of the cube ccw
    def __Lp(self):
        #rotate piece representation
        for piece in self.pieces:
            if(piece.pos[0] == -1):
                piece.rotate(constants.rotXi, "x")
        self.moves.append("L'")
        return

    #turn the downer face of the cube
    def __D(self):
        #rotate piece representation
        for piece in self.pieces:
            if(piece.pos[2] == -1):
                piece.rotate(constants.rotZ, "z")
        self.moves.append("D")
        return

    #turn the downer face of the cube ccw
    def __Dp(self):
        #rotate piece representation
        for piece in self.pieces:
            if(piece.pos[2] == -1):
                piece.rotate(constants.rotZi, "z")
        self.moves.append("D'")
        return

    #turn the upper face of the cube
    def __U(self):
        #rotate piece representation
        for piece in self.pieces:
            if(piece.pos[2] == 1):
                piece.rotate(constants.rotZi, "z")
        self.moves.append('U')
        return

    #turn the upper face of the cube ccw
    def __Up(self):
        #rotate piece representation
        for piece in self.pieces:
            if(piece.pos[2] == 1):
                piece.rotate(constants.rotZ, "z")
        self.moves.append("U'")
        return

    #rotate side perspective of cube by 90 deg, way easier in just piece representation
    def rotateRight(self):
        for piece in self.pieces:
            piece.rotate(constants.rotZ, "z")
        return

    #rotate side perspective of cube by -90 deg, way easier in just piece representation
    def rotateLeft(self):
        for piece in self.pieces:
            piece.rotate(constants.rotZi, "z")
        return

    #pass character sequence for moves to be carried out in order on cube
    def turnCube(self, list):
        for i in list:
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
            else:
                print("bad sequence list command: ", i)
        return

    # gets the state of the edges pieces in a one hot vector
    def getVectorStateOfEdgePieces(self):
        edges = []
        for z in range(-1, 2):
            for y in range(-1, 2):
                for x in range(-1, 2):
                    if x+y+z == -2 or x+y+z == 2 or x+y+z == 0:
                        if not (x == 0 and y == 0 and z == 0):
                            edges.append(self.getColor(x, y, z, 0))
                            edges.append(self.getColor(x, y, z, 1))
                            edges.append(self.getColor(x, y, z, 2))
        for i in range(12):
            edges.remove(None)
        # print(edges)
        edges = np.array(edges).reshape(1,-1)
        return self.colorEncoder.fit_transform(edges).toarray()[0]

    #turns the cube given a one-hot vector of the 12 turns
    def vectorTurn(self, turn):
        for i in range(len(turn)):
            if turn[0,i] == 1:
                self.turnCube(self.turnOptions[i])
                break
        return

    #turns the cube given a value between 0 and 12
    def integerTurn(self, turn):
        if turn < 12 and turn >= 0:
            self.turnCube([self.turnOptions[turn]])
        else:
            print("bad turn integer")
        return

    #returns the number of cross pieces in the correct place (max 4)
    def getNumberOfCrossPiecesSolved(self):
        num = 0
        for piece in self.pieces:
            if piece.pos.tolist() == [-1,0,-1] and piece.colors == ["R", None, "W"]:
                num += 1
            elif piece.pos.tolist() == [0,-1,-1] and piece.colors == [None, "G", "W"]:
                num += 1
            elif piece.pos.tolist() == [1,0,-1] and piece.colors == ["O", None, "W"]:
                num += 1
            elif piece.pos.tolist() == [0,1,-1] and piece.colors == [None, "B", "W"]:
                num += 1
        return num

    #returns the number of first layer corner pieces in the correct place (max 4)
    def getNumberOfCornerPiecesSolved(self):
        num = 0
        for piece in self.pieces:
            if piece.pos.tolist() == [-1,-1,-1] and piece.colors == ["R", "G", "W"]:
                num += 1
            elif piece.pos.tolist() == [-1,1,-1] and piece.colors == ["R", "B", "W"]:
                num += 1
            elif piece.pos.tolist() == [1,-1,-1] and piece.colors == ["O", "G", "W"]:
                num += 1
            elif piece.pos.tolist() == [1,1,-1] and piece.colors == ["O", "B", "W"]:
                num += 1
        return num

    # randomly mixes the cube using 30 turns --- currently same mix every time
    def mix(self):
        seq = []
        for i in range(30):
            random.seed(i)
            seq.append(random.choice(self.turnOptions))
        self.turnCube(seq)
        self.moves = []
        return

    # returns the color of a piece at a given position with a given face
    def getColor(self, x, y, z, face):
        for piece in self.pieces:
            if piece.pos[0] == x and piece.pos[1] == y and piece.pos[2] == z:
                return piece.colors[face]

    #returns the state of the cube in a big one-hot vector
    def getVectorState(self):
        state = [] #back, downer, front, left, right, upper
        #back
        for z in range(1, -2, -1):
            for x in range(1, -2, -1):
                state.append(self.getColor(x, 1, z, 1))
        #downer
        for y in range(-1, 2, 1):
            for x in range(-1, 2, 1):
                state.append(self.getColor(x, y, -1, 2))
        #front
        for z in range(1, -2, -1):
            for x in range(-1, 2, 1):
                state.append(self.getColor(x, -1, z, 1))
        #left
        for z in range(1, -2, -1):
            for y in range(1, -2, -1):
                state.append(self.getColor(-1, y, z, 0))
        #right
        for z in range(1, -2, -1):
            for y in range(-1, 2, 1):
                state.append(self.getColor(1, y, z, 0))
        #upper
        for y in range(1, -2, -1):
            for x in range(-1, 2, 1):
                state.append(self.getColor(x, y, 1, 2))
        state = np.array(state).reshape(1,-1)
        state = self.colorEncoder.fit_transform(state).toarray()
        return state[0]

    def getVectorStateOfCornerPieces(self):
        state = []
        for x in range(-1, 2, 2):
            for y in range(-1, 2, 2):
                for z in range(-1, 2, 2):
                    for dim in range(3):
                        state.append(self.getColor(x, y, z, dim))
        state = np.array(state).reshape(1, -1)
        state = self.colorEncoder.fit_transform(state).toarray()
        return state[0]


    # returns the colors of a face in a string...not great but will do for now
    def getFaceColor(self, x = None, y = None, z = None):
        str = ""
        if x == 1:
            for z in range(1, -2, -1):
                for y in range(-1, 2, 1):
                    str += self.getColor(x, y, z, 0)
                str += '\n'

        elif x == -1:
            for z in range(1, -2, -1):
                for y in range(1, -2, -1):
                    str += self.getColor(x, y, z, 0)
                str += '\n'

        elif y == 1:
            for z in range(1, -2, -1):
                for x in range(1, -2, -1):
                    str += self.getColor(x, y, z, 1)
                str += '\n'

        elif y == -1:
            for z in range(1, -2, -1):
                for x in range(-1, 2, 1):
                    str += self.getColor(x, y, z, 1)
                str += '\n'

        elif z == 1:
            for y in range(1, -2, -1):
                for x in range(-1, 2, 1):
                    str += self.getColor(x, y, z, 2)
                str += '\n'

        elif z == -1:
            for y in range(-1, 2, 1):
                for x in range(-1, 2, 1):
                    str += self.getColor(x, y, z, 2)
                str += '\n'

        return str


    #prints state of cube --- needs to be fixed for piece representation
    def printState(self):
        print(self.getFaceColor(z = 1))
        print(self.getFaceColor(x = -1))
        print(self.getFaceColor(y = -1))
        print(self.getFaceColor(x = 1))
        print(self.getFaceColor(y = 1))
        print(self.getFaceColor(z = -1))
        return
