import pytest
from coups_possibles import Rook, Bishop, ChessGrid, MoveManager

@pytest.fixture(scope="module")
def grid():
    yield ChessGrid({'white':{'King':[(5,8)],'Queen':[(2,6)],'Knight':[(2,8),(5,6)],'Rook':[(1,8),(6,8)],'Bishop':[(3,8)]},
                'black':{'King':[(3,1)],'Queen':[(4,2)],'Knight':[(7,1),(3,3)],'Rook':[(4,1),(8,1)],'Bishop':[(5,2)]}})

def test_position_of_all_pieces(grid):
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

def test_create_rook_from_chessgrid(grid):
    position = grid.positions['white']['Rook'][0]
    rook = Rook(position, 'white')
    assert rook.position == (1,8)


def test_possible_moves_white_rook():
    rook = Rook((1,8), 'white')
    assert rook.mouvements_possibles() == [(2,8),(3,8),(4,8),(5,8),(6,8),(7,8),(8,8),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7)]
    
def test_possible_strikes_rook_top_left_corner(grid):
    position = grid.positions['white']['Rook'][0] # (1,8)
    rook = Rook(position, 'white')
    strikes = MoveManager('Rook', rook, grid)
    assert strikes.coups_possibles() == [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)]

def test_possible_strikes_rook_other_position(grid):
    position = grid.positions['black']['Rook'][0] # (4,1)
    rook = Rook(position, 'black')
    strikes = MoveManager('Rook', rook, grid)
    assert strikes.coups_possibles() == [(5, 1), (6, 1)]
    position2 = grid.positions['white']['Rook'][1] # (6,8)
    rook2 = Rook(position2, 'white')
    strikes2 = MoveManager('Rook', rook2, grid)
    assert strikes2.coups_possibles() == [(6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (7, 8), (8, 8)]
    position3 = grid.positions['black']['Rook'][1] # (8,1)
    rook3 = Rook(position3, 'black')
    strikes3 = MoveManager('Rook', rook3, grid)
    assert strikes3.coups_possibles() == [(8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)]

def test_possible_moves_bishop():
    bishop = Bishop((3, 8), 'white')
    assert bishop.mouvements_possibles() == [(4, 7), (5, 6), (6, 5), (7, 4), (8, 3), (2, 7), (1, 6)]
    bishop1 = Bishop((5, 2), 'black')
    assert bishop1.mouvements_possibles() == [(6, 1), (4, 1)]


