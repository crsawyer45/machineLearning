import numpy as np

#rotation matrices - name implies rotational axis and i indicates -direction
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
