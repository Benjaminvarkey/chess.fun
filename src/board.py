from const import *
from square import Square
class Board:
    def __init__(self):
        self.square=[[0,0,0,0,0,0,0,0] for col in range (CLS)]
        self._create
    
    def _create(self):
        for rows in range(ROWS):
            for cols in range(CLS):
                self.square[rows][cols]=Square(rows,cols)
    def _addpiece(self,color):
        pass

        