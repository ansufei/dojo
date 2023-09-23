@dataclass
class Grid:
    '''randomly populated. Change the default number of pieces if needed.
    number_pieces: for each side (we assume they have the same number)
    '''
    number_pieces: int = random.choices(range(1,17),weights=[1,2,3,4,5,6,7,8,7,6,5,4,3,2,1,0.5],k=1)[0]
    player: str = 'white'
    #place_on_grid: Callable

    def choose_pieces(self):
        pieces = []
        while len(pieces) < self.number_pieces - 1:
            if random.choice([0,1]):
                pieces.append('Queen')
            twins = ['Rook','Bishop','Knight']
            random.shuffle(twins)
            for piece in twins:
                pieces += [piece + '_' + str(i) for i in range(random.randrange(1,3))]
            nb_pawns = min(self.number_pieces - len(pieces), 8)
            pieces += ['Pawn' + '_' + str(i) for i in range(nb_pawns)]
        return ['King'] + pieces[:self.number_pieces - 1]

def place_on_grid(self):
    white_pieces = self.choose_pieces()
    black_pieces = self.choose_pieces()
    grid = [(i,j) for i in range(1,9) for j in range(1,9)]
    locations = random.sample(grid, len(white_pieces + black_pieces))
    loc_white = {white_pieces[i]:v for (i,v) in enumerate(locations[:len(white_pieces)])}
    loc_black = {black_pieces[i]:v for (i,v) in enumerate(locations[len(white_pieces):])}
    return {'white':loc_white, 'black':loc_black}
    

def test_pick_pieces():
    grid = Grid()
    print(grid.choose_pieces())
    assert len(grid.choose_pieces()) > 0
    assert len(grid.choose_pieces()) < 17
    # same nb of pieces as planned
    assert len(grid.choose_pieces()) == grid.number_pieces


def test_creation_grid():
    grid = Grid(number_pieces=8)
    locations_dict = grid.place_on_grid()
    # no location picked twice
    print(locations_dict)
    locations = list(locations_dict['white'].values()) + list(locations_dict['black'].values())
    assert len(set(locations)) == len(locations)
    # King always there
    assert 'King' in locations_dict['white'].keys()
    assert 'King' in locations_dict['black'].keys()
    # same nb of pieces as planned
    assert len(locations_dict['white']) == len(locations_dict['black']) == grid.number_pieces
    # at most 1 King, 1 Queen, 2 Bishops, 2 Knights, 2 Rooks, 8 Pawns