import random

class GameOfLife:
    def __init__(self, rows, cols, density):
        self.rows = rows
        self.cols = cols 
        self.density = density
        self.matrix = [[0]*cols for i in range(rows)]
        

    def start(self):
        for r in range(self.rows):
            for c in range(self.cols):
                probability = random.randint(0, 100)
                self.matrix[r][c] = 1 if probability < self.density else 0

    
    def display(self):
        for row in self.matrix:
            print(row)



rows = int(input("Rows: "))
cols = int(input("Cols: "))
density = int(input("Density (0, 100): "))

game = GameOfLife(rows, cols, density)
game.start()
game.display()


