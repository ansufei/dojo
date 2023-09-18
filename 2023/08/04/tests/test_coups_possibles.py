from dataclasses import dataclass
from typing import Tuple

from coups_possibles import coups_possibles, Tour, Grid


def test_tour_sur_un_echiquier_vide():
    piece = Tour((1, 1))
    pieces = [piece]
    resultats = coups_possibles(piece, pieces)
    assert resultats == [[Tour((colonne, 1))] for colonne in range(2, 9)] + [
        [Tour((1, rangee))] for rangee in range(2, 9)
    ]


def test_tour_sur_un_echiquier_vide_2():
    pieces = [Tour((1, 1))]
    resultats = pieces[0].mouvements_possibles()
    assert resultats == [[Tour((colonne, 1))] for colonne in range(2, 9)] + [
        [Tour((1, rangee))] for rangee in range(2, 9)
    ]


def test_une_piece_gene_une_autre():
    obstacles = [Tour((2, 1)), Tour((1, 2))]
    piece = Tour((1, 1))
    echiquier = [piece] + obstacles
    resultats = coups_possibles(piece, echiquier)
    assert resultats == []


def test_avec_un_echiquier_d_une_case_la_tour_ne_peux_pas_bouger():
    piece = Tour((1, 1))
    liste_des_pieces = [piece]
    echiquier_dimension = 1
    resultats = coups_possibles(piece, liste_des_pieces, echiquier_dimension)
    assert resultats == []

def test_pick_pieces():
    grid = Grid()
    assert len(grid.choose_pieces()) > 0
    assert len(grid.choose_pieces()) < 17

def test_creation_grid():
    grid = Grid(number_pieces=8)
    loc_white, loc_black = grid.place_on_grid()
    # no location picked twice
    locations = list(loc_white.values()) + list(loc_black.values())
    assert len(set(locations)) == len(locations)
    # King always there
    assert 'King' in loc_white.keys()
    assert 'King' in loc_black.keys()
    # same nb of pieces as planned
    assert len(loc_white) == len(loc_black) == grid.number_pieces
    # at most 1 King, 1 Queen, 2 Bishops, 2 Knights, 2 Rooks, 8 Pawns

