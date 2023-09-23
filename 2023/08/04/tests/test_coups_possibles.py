from dataclasses import dataclass
from typing import Tuple

from coups_possibles import Rook, ChessGrid, MoveManager

def test_position_of_all_pieces():
    grid = ChessGrid({'white':{'King':[(5,8)],'Queen':[(2,6)],'Knight':[(2,8),(5,6)],'Rook':[(1,8),(6,8)],'Bishop':[(3,8)]},
                      'black':{'King':[(3,1)],'Queen':[(4,2)],'Knight':[(7,1),(3,3)],'Rook':[(4,1),(8,1)],'Bishop':[(5,2)]}})
    expected = [(5,8),(2,6),(2,8),(5,6),(1,8),(6,8),(3,8),(3,1),(4,2),(7,1),(3,3),(4,1),(8,1),(5,2)]
    for item in list(grid.positions['white'].values()) + list(grid.positions['black'].values()):
            print(item)
    compare_results1 = [x for x in grid.flatten_positions() if not x in expected]
    compare_results2 = [x for x in expected if not x in grid.flatten_positions()]
    assert len(compare_results1) == 0
    assert len(compare_results2) == 0


def test_create_rook_from_position():
    rook = Rook((1,3), 'white')
    assert rook.position == (1,3)


def test_create_rook_from_chessgrid():
    grid = ChessGrid({'white':{'King':[(5,8)],'Queen':[(2,6)],'Knight':[(2,8),(5,6)],'Rook':[(1,8),(6,8)],'Bishop':[(3,8)]},
                      'black':{'King':[(3,1)],'Queen':[(4,2)],'Knight':[(7,1),(3,3)],'Rook':[(4,1),(8,1)],'Bishop':[(5,2)]}})
    position = grid.positions['white']['Rook'][0]
    rook = Rook(position, 'white')
    assert rook.position == (1,8)


def test_possible_moves_white_rook():
    rook = Rook((1,8), 'white')
    assert rook.mouvements_possibles() == [(2,8),(3,8),(4,8),(5,8),(6,8),(7,8),(8,8),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7)]
    

def test_possible_strikes_white_rook():
    grid = ChessGrid({'white':{'King':[(5,8)],'Queen':[(2,6)],'Knight':[(2,8),(5,6)],'Rook':[(1,8),(6,8)],'Bishop':[(3,8)]},
                      'black':{'King':[(3,1)],'Queen':[(4,2)],'Knight':[(7,1),(3,3)],'Rook':[(4,1),(8,1)],'Bishop':[(5,2)]}})
    position = grid.positions['white']['Rook'][0]
    rook = Rook(position, 'white')
    strikes = MoveManager('Rook', rook, grid)
    assert strikes.coups_possibles() == [(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7)]

