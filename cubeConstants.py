import numpy as np
from sklearn.preprocessing import OneHotEncoder


# cube constants
turnOptions = ["B", "B'", "D", "D'", "F", "F'", "L", "L'", "R", "R'", "U", "U'"]
turnEncoder = OneHotEncoder(categories=[turnOptions])
colors = [['B', 'G', 'O', 'R', 'W', 'Y'] for i in range(24)]
colorEncoder = OneHotEncoder(categories=colors)

# rotation matrices - name implies rotational axis and i indicates negative direction
rotX = np.array([
    [1, 0, 0],
    [0, 0, -1],
    [0, 1, 0]])
rotXi = np.array([
    [1, 0, 0],
    [0, 0, 1],
    [0, -1, 0]])

rotY = np.array([
    [0, 0, 1],
    [0, 1, 0],
    [-1, 0, 0]])
rotYi = np.array([
    [0, 0, -1],
    [0, 1, 0],
    [1, 0, 0]])

rotZ = np.array([
    [0, -1, 0],
    [1, 0, 0],
    [0, 0, 1]])
rotZi = np.array([
    [0, 1, 0],
    [-1, 0, 0],
    [0, 0, 1]])


# cube algorithms
firstLayerAlgorithms = [
    ["F'", "U'", "F"],
    ["R", "U", "R'"],
    ["R", "U", "U", "R'", "U'", "R", "U", "R'"],
    ["U"],
    ["->"]
]
secondLayerAlgorithms = [
    ["U", "R", "U'", "R'", "U'", "F'", "U", "F"],
    ["U'", "F'", "U", "F", "U", "R", "U'", "R'"],
    ["U"],
    ["->"]
]
lastLayerAlgorithms = [
    ["R", "U", "F", "U", "F", "R"],
    ["R", "U", "R'", "U", "R", "U", "U", "R'"],
    ["L'", "U'", "L", "U", "L'", "U'", "U'", "L"],
    ["R'", "F", "R'", "B", "B", "R", "F'", "R'", "B", "B", "R", "R"],
    ["U"]
]
