from dataclasses import dataclass
from typing import Tuple
import random

#random.seed(42)

@dataclass
class Grid:
    '''randomly populated. Change the default number of pieces if needed.
    number_pieces: for each side (we assume they have the same number)
    '''
    number_pieces: int = random.choices(range(1,17),weights=[1,2,3,4,5,6,7,8,7,6,5,4,3,2,1,0.5],k=1)[0]
    player: str = 'white'

    def choose_pieces(self):
        pieces = ['King']
        while len(pieces) < self.number_pieces:
            if random.choice([0,1]):
                pieces.append('Queen')
            twins = ['Rook','Bishop','Knight']
            random.shuffle(twins)
            for piece in twins:
                pieces += [piece + '_' + str(i) for i in range(random.randrange(1,3))]
            nb_pawns = min(self.number_pieces - len(pieces), 8)
            pieces += ['Pawn' + '_' + str(i) for i in range(nb_pawns)]
        return pieces

    def place_on_grid(self):
        white_pieces = self.choose_pieces()
        black_pieces = self.choose_pieces()
        grid = [(i,j) for i in range(1,9) for j in range(1,9)]
        locations = random.sample(grid, len(white_pieces + black_pieces))
        loc_white = {white_pieces[i]:v for (i,v) in enumerate(locations[:len(white_pieces)])}
        loc_black = {black_pieces[i]:v for (i,v) in enumerate(locations[len(white_pieces):])}
        return loc_white, loc_black

grid = Grid(number_pieces=6)

@dataclass
class Tour:
    position: Tuple[int, int]

    def mouvements_possibles(self):
        return [
            [Tour((colonne, self.position[1]))]
            for colonne in range(1, 9)
            if colonne != self.position[0]
        ] + [
            [Tour((self.position[0], rangee))]
            for rangee in range(1, 9)
            if rangee != self.position[1]
        ]


def coups_possibles(piece, echiquier, dimension=8):
    # note: no castling

    if dimension == 1:
        return []
    if len(echiquier) > 1:
        return []
    return piece.mouvements_possibles()
