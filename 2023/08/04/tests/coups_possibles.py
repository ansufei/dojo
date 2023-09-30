
from dataclasses import dataclass
from typing import Tuple

@dataclass
class ChessGrid:
    positions: dict
    
    def flatten_positions(self):
        result = []
        for item in list(self.positions['white'].values()) + list(self.positions['black'].values()):
            result += item
        return result

@dataclass
class Piece:
    position: Tuple
    color: str

@dataclass
class Rook(Piece):
    position: Tuple
    color: str
    
    def mouvements_possibles(self):
        return [(col, self.position[1]) for col in range(1, 9) if col != self.position[0]] \
    + [(self.position[0], line) for line in range(1, 9) if line != self.position[1]]

@dataclass
class Bishop(Piece):
    position: Tuple
    color: str
    
    def mouvements_possibles(self):
    #     return [(col, self.position[1]) for col in range(1, 9) if col != self.position[0]] \
    # + [(self.position[0], line) for line in range(1, 9) if line != self.position[1]]
        row, col = self.position[0], self.position[1]
        # bottom right diagonal
        result = [(row + i, col - i) for i in range(1, 9) if (row + i < 9) & (col - i > 0)] 
        # bottom left diagonal
        result += [(row - i, col - i) for i in range(1, 9) if (row - i > 0) & (col - i > 0)]
        print(result)
        for i in range(1,9):
            if (row - i > 0) & (col + i < 9):
                print(row-i, col-i)
            if (col + i < 9):
                print(row-i, col-i)
        #print(result)
        return result
    # [(4, 7), (5, 6), (6, 5), (7, 4), (8, 3), (2, 7), (1, 6)]

# @dataclass
# class King(Piece):
#     position: Tuple
#     color: str
#     can_castle: bool
    
#     def mouvements_possibles(self):
#         return [(col, self.position[1]) for col in range(1, 9) if col != self.position[0]] \
#     + [(self.position[0], line) for line in range(1, 9) if line != self.position[1]]

@dataclass
class MoveManager:
    piece_name: str
    piece: Piece
    grid: ChessGrid

    def coups_possibles(self):
        # note: no castling
        result = []
        moves = self.piece.mouvements_possibles()
        # obstacles: positions of all the other pieces that match with moves
        positions = self.grid.flatten_positions()
        # obstacles
        if self.piece_name in ('Rook', 'Bishop'):
            obstacles = [x for x in moves if x in positions]
            for i in [0,1]:
                to_remove = []
                moves_i = [x for x in moves if x[i] == self.piece.position[i]] # cells sharing the same: 0/ x i.e. column 1/ y i.e. line
                obstacles_before = [x for x in obstacles if x[1-i] < self.piece.position[1-i]] # compare the 0/ y to the y or 1/ x to the x of the piece
                if len(obstacles_before) > 0:
                    to_remove += [x for x in moves_i if x[1-i] <= obstacles_before[-1][1-i]] # 
                obstacles_after = [x for x in obstacles if x[1-i] > self.piece.position[1-i]]
                if len(obstacles_after) > 0:
                    to_remove += [x for x in moves_i if x[1-i] >= obstacles_after[0][1-i]]
                result += [x for x in moves_i if not x in to_remove]
            return  result
        #elif self.piece_name == 'Bishop':

    