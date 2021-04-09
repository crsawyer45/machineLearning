import numpy as np


class Piece:
    def __init__(self, position, colors=None):
        self.pos = np.array(position)
        self.colors = {'x': None, 'y': None, 'z': None}
        self.type = ""
        if colors is None:
            if self.pos[0] == -1:
                self.colors['x'] = "R"
            elif self.pos[0] == 1:
                self.colors['x'] = "O"

            if self.pos[1] == -1:
                self.colors['y'] = "G"
            elif self.pos[1] == 1:
                self.colors['y'] = "B"

            if self.pos[2] == -1:
                self.colors['z'] = "W"
            elif self.pos[2] == 1:
                self.colors['z'] = "Y"
        else:
            self.colors = colors

        if np.count_nonzero(self.pos != 0) == 3:
            self.type = "corner"
        elif np.count_nonzero(self.pos != 0) == 2:
            self.type = "edge"
        else:
            self.type = "center"
        return

    def rotate(self, rot, axis):
        self.pos = np.matmul(rot, self.pos)
        if axis == 'x':
            self.colors['y'], self.colors['z'] = self.colors['z'], self.colors['y']
        elif axis == 'y':
            self.colors['x'], self.colors['z'] = self.colors['z'], self.colors['x']
        elif axis == 'z':
            self.colors['x'], self.colors['y'] = self.colors['y'], self.colors['x']
        else:
            print("bad color shift")
        return
