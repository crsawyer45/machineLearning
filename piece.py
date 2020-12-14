import numpy as np

class Piece:
    def __init__(self, position, id, colors = None):
        self.id = id
        self.pos = np.array(position)
        self.colors = [None, None, None]
        self.type = ""
        if colors == None:
            if(self.pos[0] == -1):
                self.colors[0] = "R"
            elif(self.pos[0] == 1):
                self.colors[0] = "O"

            if(self.pos[1] == -1):
                self.colors[1] = "G"
            elif(self.pos[1] == 1):
                self.colors[1] = "B"

            if(self.pos[2] == -1):
                self.colors[2] = "W"
            elif(self.pos[2] == 1):
                self.colors[2] = "Y"
        else:
            self.colors = colors

        if(np.count_nonzero(self.pos != 0) == 3):
            self.type = "corner"
        elif(np.count_nonzero(self.pos != 0) == 2):
            self.type = "edge"
        else:
            self.type = "center"
        return

    def rotate(self, rot, axis):
        self.pos = np.matmul(rot, self.pos)
        if(axis == 'x'):
            self.colors[1], self.colors[2] = self.colors[2], self.colors[1]
        elif(axis == 'y'):
            self.colors[0], self.colors[2] = self.colors[2], self.colors[0]
        elif(axis == 'z'):
            self.colors[0], self.colors[1] = self.colors[1], self.colors[0]
        else:
            print("bad color shift")
        return
