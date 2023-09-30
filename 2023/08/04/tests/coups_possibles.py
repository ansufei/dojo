
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
        row, col = self.position[0], self.position[1]
        # bottom right diagonal
        result = [(row + i, col - i) for i in range(1, 9) if (row + i < 9) & (col - i > 0)] 
        # bottom left diagonal
        result += [(row - i, col - i) for i in range(1, 9) if (row - i > 0) & (col - i > 0)]
        # top right diagonal
        result += [(row + i, col + i) for i in range(1, 9) if (row + i < 9) & (col + i < 9)]
        # top left diagonal
        result += [(row - i, col + i) for i in range(1, 9) if (row - i > 0) & (col + i < 9)]
        return result

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
        if self.piece_name == 'Rook':
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
        elif self.piece_name == 'Bishop':
            obstacles = [x for x in moves if x in positions]
            row, col = self.piece.position[0], self.piece.position[1]
            # bottom right diagonal
            moves_bottom_right = [(row + i, col - i) for i in range(1, 9) if (row + i < 9) & (col - i > 0)] 
            if any(map(lambda v: v in obstacles, moves_bottom_right)):
                stop = min(set(moves_bottom_right).intersection(obstacles))
                result += moves_bottom_right[:moves_bottom_right.index(stop)]
            else:
                result += moves_bottom_right
            # bottom left diagonal
            moves_bottom_left = [(row - i, col - i) for i in range(1, 9) if (row - i > 0) & (col - i > 0)]
            print(moves_bottom_left)
            if any(map(lambda v: v in obstacles, moves_bottom_left)):
                stop = min(set(moves_bottom_left).intersection(obstacles))
                result += moves_bottom_left[:moves_bottom_left.index(stop)]
            else:
                result += moves_bottom_left
            # top right diagonal
            moves_top_right = [(row + i, col + i) for i in range(1, 9) if (row + i < 9) & (col + i < 9)]
            if any(map(lambda v: v in obstacles, moves_top_right)):
                stop = min(set(moves_top_right).intersection(obstacles))
                result += moves_top_right[:moves_top_right.index(stop)]
            else:
                result += moves_top_right
            # top left diagonal
            moves_top_left = [(row - i, col + i) for i in range(1, 9) if (row - i > 0) & (col + i < 9)]
            if any(map(lambda v: v in obstacles, moves_top_left)):
                stop = min(set(moves_top_left).intersection(obstacles))
                result += moves_top_left[:moves_top_left.index(stop)]
            else:
                result += moves_top_left
            return  result