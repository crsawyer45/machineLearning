from cube import Cube
from solver import Solver

cube = Cube()
# print(cube.getNumberOfCrossPiecesSolved())
cube.mix()
print(cube.getNumberOfCrossPiecesSolved())
solver = Solver(cube)
solver.solveCross()
print(cube.moves)

print(cube.getNumberOfBottomCornerPiecesSolved())
solver.solveFirstLayer()
print(cube.moves)

print(cube.getNumberOfMiddleEdgePiecesSolved())
solver.solveSecondLayer()
print(cube.moves)
#
#
cube.printState()
print(len(cube.moves))


# print(cube1.getNumberOfBottomCornerPiecesSolved())
# print(cube1.getNumberOfMiddleEdgePiecesSolved())
# cube1.mix()
# cube1.printState()
# solver = Solver(cube1)
# solver.solveFirstLayer()
# print(solver.optimizedMoves())

# print(cube1.getNumberOfCrossPiecesSolved())
# print(cube1.getVectorStateOfCrossPieces())
# cube1.turnCube(["R"])
# print(cube1.getVectorStateOfCornerPieces())
# cube1.turnCube(["R'"])
# cube1.turnCube(["L"])
# cube1.turnCube(["L'"])
# cube1.turnCube(["F"])
# cube1.turnCube(["F'"])
# cube1.turnCube(["B"])
# cube1.turnCube(["B'"])
# cube1.turnCube(["U"])
# cube1.turnCube(["U'"])
# cube1.turnCube(["D"])
# cube1.turnCube(["D'"])

# cube1.mix()
# cube1.printState()
# cube2.mix()
# cube2.printState()

# print(cube1.getVectorStateOfEdgePieces())
