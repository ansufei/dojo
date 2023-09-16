export enum Coord {
    TOP_LEFT,
    TOP_MID,
    TOP_RIGHT,
    MID_LEFT,
    MID,
    MID_RIGHT,
    BOTTOM_LEFT,
    BOTTOM_MID,
    BOTTOM_RIGHT,
    EMPTY
  }

  
export class Game {
moves
map_moves
map_moves_noughts
map_moves_crosses
results
constructor() {
    this.moves = new Array();
    this.map_moves = new Map();
    this.map_moves_noughts = new Map();
    this.map_moves_crosses = new Map();
    this.results = new Map();
}

populate_grid(grid, value){
    if (grid.has(value[0])){
        grid.get(value[0]).push(value[1]);
    } else {
        grid.set(value[0], [value[1]]);
    }
    return grid
}

add_move(...moves) {
    // mapping completion of small grids (keys are the big grids)
    if (moves.length == 0) return this.map_moves
    else if (moves[0] == Coord.EMPTY) return this.map_moves
    else {
        moves.forEach((value, valueIndex) => {
            if (this.move_is_legal(value)) {
                // add the move to the log of the order in which the moves are played
                this.moves.push(value)
                // also add the move to the map of the current game and to the maps of the respective players
                this.populate_grid(this.map_moves, value)
                if (valueIndex % 2 == 0) {
                    this.populate_grid(this.map_moves_crosses, value)
                }
                else {
                    this.populate_grid(this.map_moves_noughts, value)
                }
                    
            } else {
                console.log(value, 'is not a legal move here')
            }    
        })
    }
    return this.map_moves
}

// grid_is_full(grid) {
// }

grid_is_won(grid,player) {
    let map_moves_player = this.map_moves_noughts
    if (player == 'crosses') {
        map_moves_player = this.map_moves_crosses
    }
    let moves_player;
    if (map_moves_player.has(grid)) {
        moves_player = map_moves_player.get(grid)
    } else {
        return false
    }
    const winning_lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for (let i=0; i < winning_lines.length; i++) {
        let check_result = winning_lines[i].filter(n => !moves_player.includes(n))
        if (check_result.length == 0) {
            this.results.set(grid, player)
            return true
        }
    }
    return false
}

whose_turn() {
    //by convention crosses plays first
    let calc = this.moves.length
    let player = 'noughts'
    if (calc % 2 == 0) {
        player = 'crosses'
    } 
    console.log(player, 'should play next')
    return player
}

game_is_won() {
    return false
}

move_is_legal(move = [Coord.EMPTY,Coord.EMPTY]) {
    // an empty move is legal
    if (move[0] == Coord.EMPTY) return true

    // no move is played more than once
    if (this.map_moves.has(move[0])) {
        if (this.map_moves.get(move[0]).includes(move[1])) {
            return false
        }
    }    
    // the sub-grid referred to in the last move is full, free to choose another grid (exception to the default case below)

    // the grid of the current move is related to the cell in the last move (default case)
    if (this.moves.length !== 0) {
        // the sub-grid referred to in the last move was won, free to choose another grid 
        if (this.results.has(this.moves.at(-1)[1])){
            return true
        } else {
            return move[0] == this.moves.at(-1)[1]
        }
    }

    return true
}
}