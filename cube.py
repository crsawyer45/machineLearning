from sklearn.preprocessing import OneHotEncoder
import random
import constants
import numpy as np
from piece import Piece

class Cube:
#need init where you can pass list of pieces and colors for an initial cube state
    def __init__(self):
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
        # self.back  = ['B','B','B','B','B','B','B','B','B']
        # self.front = ['G','G','G','G','G','G','G','G','G']
        # self.right = ['O','O','O','O','O','O','O','O','O']
        # self.left  = ['R','R','R','R','R','R','R','R','R']
        # self.downer = ['W','W','W','W','W','W','W','W','W']
        # self.upper = ['Y','Y','Y','Y','Y','Y','Y','Y','Y']
        self.moves = []
        self.turnOptions = ["B","B'","F","F'","R","R'","L","L'","D","D'","U","U'"]
        # self.categories = [['B','G','O','R','W','Y'] for i in range(54)]
        # self.encoder = OneHotEncoder(categories= self.categories)
#cube faces are numbered as follows:
# [0 1 2]
# [7 8 3]
# [6 5 4]
    #turn the back face of the cube
    def __B(self):
        #rotate face representation
        # temp = self.back.copy()
        # for i in range(8):
        #     self.back[(i + 2) % 8] = temp[i]
        # temp = self.right.copy()
        # for i in range(2,5):
        #     self.right[i] = self.downer[i + 2]
        #     self.downer[i + 2] = self.left[(i + 4) % 8]
        #     self.left[(i + 4) % 8] = self.upper[i - 2]
        #     self.upper[i - 2] = temp[i]
        #rotate piece representation
        for piece in self.pieces:
            if(piece.pos[1] == 1):
                piece.rotate(constants.rotYi, "y")
        self.moves.append("B")
        return

    #turn the back face of the cube ccw
    def __Bp(self):
        #rotate face representation
        # temp = self.back.copy()
        # for i in range(8):
        #     self.back[i] = temp[(i + 2) % 8]
        # temp = self.right.copy()
        # for i in range(2,5):
        #     self.right[i] = self.upper[i - 2]
        #     self.upper[i - 2] = self.left[(i + 4) % 8]
        #     self.left[(i + 4) % 8] = self.downer[i + 2]
        #     self.downer[i + 2] = temp[i]
        #rotate piece representation
        for piece in self.pieces:
            if(piece.pos[1] == 1):
                piece.rotate(constants.rotY, "y")
        self.moves.append("B'")
        return

    #turn the front face of the cube
    def __F(self):
        #rotate face representation
        # temp = self.front.copy()
        # for i in range(8):
        #     self.front[(i + 2) % 8] = temp[i]
        # temp = self.left.copy()
        # for i in range(2,5):
        #     self.left[i] = self.downer[i - 2]
        #     self.downer[i - 2] = self.right[(i + 4) % 8]
        #     self.right[(i + 4) % 8] = self.upper[i + 2]
        #     self.upper[i + 2] = temp[i]
        #rotate piece representation
        for piece in self.pieces:
            if(piece.pos[1] == -1):
                piece.rotate(constants.rotY, "y")
        self.moves.append("F")
        return

    #turn the front face of the cube ccw
    def __Fp(self):
        #rotate face representation
        # temp = self.front.copy()
        # for i in range(8):
        #     self.front[i] = temp[(i + 2) % 8]
        # temp = self.left.copy()
        # for i in range(2,5):
        #     self.left[i] = self.upper[i + 2]
        #     self.upper[i + 2] = self.right[(i + 4) % 8]
        #     self.right[(i + 4) % 8] = self.downer[i - 2]
        #     self.downer[i - 2] = temp[i]
        #rotate piece representation
        for piece in self.pieces:
            if(piece.pos[1] == 1):
                piece.rotate(constants.rotYi, "y")
        self.moves.append("F'")
        return

    #turn the right face of the cube cw
    def __R(self):
        #rotate face representation
        # temp = self.right.copy()
        # for i in range(8):
        #     self.right[(i + 2) % 8] = temp[i]
        # temp = self.upper.copy()
        # for i in range(2,5):
        #     self.upper[i] = self.front[i]
        #     self.front[i] = self.downer[i]
        #     self.downer[i] = self.back[(i + 4) % 8]
        #     self.back[(i + 4) % 8] = temp[i]
        #rotate piece representation
        for piece in self.pieces:
            if(piece.pos[0] == 1):
                piece.rotate(constants.rotXi, "x")
        self.moves.append("R")
        return

    #turn the right face of the cube ccw
    def __Rp(self):
        #rotate face representation
        # temp = self.right.copy()
        # for i in range(8):
        #     self.right[i] = temp[(i + 2) % 8]
        # temp = self.upper.copy()
        # for i in range(2,5):
        #     self.upper[i] = self.back[(i + 4) % 8]
        #     self.back[(i + 4) % 8] = self.downer[i]
        #     self.downer[i] = self.front[i]
        #     self.front[i] = temp[i]
        #rotate piece representation
        for piece in self.pieces:
            if(piece.pos[0] == 1):
                piece.rotate(constants.rotX, "x")
        self.moves.append("R'")
        return

    #turn the left face of the cube
    def __L(self):
        #rotate face representation
        # temp = self.left.copy()
        # for i in range(8):
        #     self.left[(i + 2) % 8] = temp[i]
        # temp = self.downer.copy()
        # for i in [0,6,7]:
        #     self.downer[i] = self.front[i]
        #     self.front[i] = self.upper[i]
        #     self.upper[i] = self.back[(i + 4) % 8]
        #     self.back[(i + 4) % 8] = temp[i]
        #rotate piece representation
        for piece in self.pieces:
            if(piece.pos[0] == -1):
                piece.rotate(constants.rotX, "x")
        self.moves.append("L")
        return

    #turn the left face of the cube ccw
    def __Lp(self):
        #rotate face representation
        # temp = self.left.copy()
        # for i in range(8):
        #     self.left[i] = temp[(i + 2) % 8]
        # temp = self.downer.copy()
        # for i in [0,6,7]:
        #     self.downer[i] = self.back[(i + 4) % 8]
        #     self.back[(i + 4) % 8] = self.upper[i]
        #     self.upper[i] = self.front[i]
        #     self.front[i] = temp[i]
        #rotate piece representation
        for piece in self.pieces:
            if(piece.pos[0] == -1):
                piece.rotate(constants.rotXi, "x")
        self.moves.append("L'")
        return

    #turn the downer face of the cube
    def __D(self):
        #rotate face representation
        # temp = self.downer.copy()
        # for i in range(8):
        #     self.downer[(i + 2) % 8] = temp[i]
        # temp = self.front.copy()
        # for i in range(4,7):
        #     self.front[i] = self.left[i]
        #     self.left[i] = self.back[i]
        #     self.back[i] = self.right[i]
        #     self.right[i] = temp[i]
        #rotate piece representation
        for piece in self.pieces:
            if(piece.pos[2] == -1):
                piece.rotate(constants.rotZ, "z")
        self.moves.append("D")
        return

    #turn the downer face of the cube ccw
    def __Dp(self):
        #rotate face representation
        # temp = self.downer.copy()
        # for i in range(8):
        #     self.downer[i] = temp[(i + 2) % 8]
        # temp = self.front.copy()
        # for i in range(4,7):
        #     self.front[i] = self.right[i]
        #     self.right[i] = self.back[i]
        #     self.back[i] = self.left[i]
        #     self.left[i] = temp[i]
        #rotate piece representation
        for piece in self.pieces:
            if(piece.pos[2] == -1):
                piece.rotate(constants.rotZi, "z")
        self.moves.append("D'")
        return

    #turn the upper face of the cube
    def __U(self):
        #rotate face representation
        # temp = self.upper.copy()
        # for i in range(8):
        #     self.upper[(i + 2) % 8] = temp[i]
        # temp = self.left.copy()
        # for i in range(3):
        #     self.left[i] = self.front[i]
        #     self.front[i] = self.right[i]
        #     self.right[i] = self.back[i]
        #     self.back[i] = temp[i]
        #rotate piece representation
        for piece in self.pieces:
            if(piece.pos[2] == 1):
                piece.rotate(constants.rotZi, "z")
        self.moves.append('U')
        return

    #turn the upper face of the cube ccw
    def __Up(self):
        #rotate face representation
        # temp = self.upper.copy()
        # for i in range(8):
        #     self.upper[i] = temp[(i + 2) % 8]
        # temp = self.left.copy()
        # for i in range(3):
        #     self.left[i] = self.back[i]
        #     self.back[i] = self.right[i]
        #     self.right[i] = self.front[i]
        #     self.front[i] = temp[i]
        #rotate piece representation
        for piece in self.pieces:
            if(piece.pos[2] == 1):
                piece.rotate(constants.rotZ, "z")
        self.moves.append("U'")
        return

    #rotate side perspective of cube by 90 deg, way easier in just piece representation
    def rotateRight(self):
        # temp = self.left.copy()
        # self.left = self.back
        # self.back = self.right
        # self.right = self.front
        # self.front = temp
        # temp = self.uppper.copy()
        # for i in range(8):
        #     self.upper[i] = temp[(i + 2) % 8]
        # temp = self.downer.copy()
        # for i in range(8):
        #     self.downer[(i + 2) % 8] = temp[i]
        for piece in self.pieces:
            piece.rotate(constants.rotZ, "z")
        return

    #rotate side perspective of cube by -90 deg, way easier in just piece representation
    def rotateLeft(self):
        # temp = self.left.copy()
        # self.left = self.front
        # self.front = self.right
        # self.right = self.back
        # self.back = temp
        # temp = self.uppper.copy()
        # for i in range(8):
        #     self.upper[(i + 2) % 8] = temp[i]
        # temp = self.downer.copy()
        # for i in range(8):
        #     self.downer[i] = temp[(i + 2) % 8]
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

    #returns the state of the cube in a big one-hot vector
    # def getVectorState(self):
    #     state = self.back + self.front + self.right + self.left + self.downer + self.upper
    #     state = np.array(state).reshape(1,-1)
    #     state = self.encoder.fit_transform(state).toarray()
    #     return state[0]

    # def getVectorStateOfEdgePieces(self):
    #     state = self.back + self.front + self.right + self.left + self.downer + self.upper
    #     edges = []
    #     for i in range(len(state)):
    #         if(i % 9 in [1,3,5,7]):
    #             edges += state[i]
    #     edges = np.array(state).reshape(1,-1)
    #     edges = self.encoder.fit_transform(edges).toarray()
    #     return edges[0]

    def getVectorStateOfCrossPieces(self):
        cross = []
        for piece in self.pieces:
            #can use piece type or piece id here, not sure which makes more sense
            if(piece.type == "edge" and "W" in piece.colors):
                cross.extend(list(piece.pos))
                for i in piece.colors:
                    if i == "W":
                        cross.append(1)
                    else:
                        cross.append(0.)
        return (np.array(cross).reshape(1,-1)[0]).tolist()

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
        for piece in pieces:
            if piece.pos == np.array([-1,0,-1]) and piece.colors == ["R", None, "W"]:
                num += 1
            elif piece.pos == np.array([0,-1,-1]) and piece.colors == [None, "G", "W"]:
                num += 1
            elif piece.pos == np.array([0,1,-1]) and piece.colors == ["O", None, "W"]:
                num += 1
            elif piece.pos == np.array([1,0,-1]) and piece.colors == [None, "B", "W"]:
                num += 1
        return num

    # randomly mixes the cube using 30 turns --- currently same mix every time
    def mix(self):
        seq = []
        for i in range(30):
            random.seed(i)
            seq.append(random.choice(self.turnOptions))
        self.turnCube(seq)

    #prints state of cube --- needs to be fixes for piece representation
    # def printState(self):
    #     u = self.upper
    #     r = self.right
    #     l = self.left
    #     b = self.back
    #     f = self.front
    #     d = self.downer
    #     print("     ", u[0], u[1], u[2])
    #     print("     ", u[7], u[8], u[3])
    #     print("     ", u[6], u[5], u[4])
    #     print(l[0],l[1],l[2],f[0],f[1],f[2],r[0],r[1],r[2],b[0],b[1],b[2])
    #     print(l[7],l[8],l[3],f[7],f[8],f[3],r[7],r[8],r[3],b[7],b[8],b[3])
    #     print(l[6],l[5],l[4],f[6],f[5],f[4],r[6],r[5],r[4],b[6],b[5],b[4])
    #     print("     ", d[0],d[1],d[2])
    #     print("     ", d[7],d[8],d[3])
    #     print("     ", d[6],d[5],d[4], "\n")
    #     return
