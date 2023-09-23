
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
class King(Piece):
    position: Tuple
    color: str
    can_castle: bool
    
    def mouvements_possibles(self):
        return [(col, self.position[1]) for col in range(1, 9) if col != self.position[0]] \
    + [(self.position[0], line) for line in range(1, 9) if line != self.position[1]]

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
            obstacles_x = [x for x in obstacles if x[0] == self.piece.position[0]]
            moves_x = [x for x in moves if x[0] == self.piece.position[0]]
            if len(obstacles_x) > 0:
                min_obstacles_x = min([x[1] for x in obstacles_x])
                result.append([x for x in moves_x if x[1] < min_obstacles_x])
            elif len(moves_x) > 0:
                result += moves_x
            obstacles_y = [x for x in obstacles if x[1] == self.piece.position[1]]
            min_obstacles_y = min([x[0] for x in obstacles_y])
            if len(obstacles_y) > 0:
                moves_y = [x for x in moves if x[1] == self.piece.position[1]]
                filtered_moves_y = [x for x in moves_y if x[0] < min_obstacles_y]
                if len(filtered_moves_y) > 0:
                    result.append(filtered_moves_y)
            elif len(moves_y) > 0:
                result += moves_y
            return  result
    