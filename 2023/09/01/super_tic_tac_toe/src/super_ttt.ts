
export class Game {
moves
map_moves
map_moves_player
results
player
constructor() {
    this.moves = new Array();
    this.map_moves = new Map();
    this.map_moves_player = new Map();
    this.map_moves_player.set('crosses', new Map())
    this.map_moves_player.set('noughts', new Map())
    this.results = new Map();
    this.player = 'crosses';
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
    else if (moves[0].length == 0) return this.map_moves
    else {
        moves.forEach((value, valueIndex) => {
            this.player = (valueIndex % 2 == 0) ? 'crosses' : 'noughts'
            if (this.move_is_legal(value)) {
                // add the move to the log of the order in which the moves are played
                this.moves.push(value)
                // also add the move to the map of the current game and to the maps of the respective players
                this.populate_grid(this.map_moves, value)
                this.populate_grid(this.map_moves_player.get(this.player), value)
                
                // check if won
                this.grid_is_won(value[0],this.player) 
                    
            } else {
                console.log(value, 'is not a legal move here')
            }    
        })
    }
    return this.map_moves
}

grid_is_full(grid) {
    if (this.map_moves.has(grid)) {
        if (this.map_moves.get(grid).length == 9) {
            if (this.results.has(grid)) {
                this.grid_is_won(grid,this.player)
            } else {
                this.results.set(grid,'draw')
            }
            return true 
        }
    }
    return false
}

grid_is_won(grid,player) {
    let moves_player;
    if (this.map_moves_player.get(player).has(grid)) {
        moves_player = this.map_moves_player.get(player).get(grid)
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
    let player = (this.moves.length % 2 == 0) ? 'crosses' : 'noughts'
    console.log(player, 'should play next')
    return player
}

game_is_won() {
    return false
}

move_is_legal(move = Array()) {
    // an empty move is legal
    if (move.length == 0) return true

    // no move is played more than once
    if (this.map_moves.has(move[0])) {
        if (this.map_moves.get(move[0]).includes(move[1])) {
            return false
        }
    }    

    // the grid of the current move is related to the cell in the last move (default case)
    if (this.moves.length !== 0) {
        // the sub-grid referred to in the last move is full, do not choose
        if (this.grid_is_full(move[0])) {
            return false
        // the sub-grid referred to in the last move was won, free to choose any grid (including a won grid if not full, even if counterproductive)
        } else if (this.results.has(this.moves.at(-1)[1])) {
            return true
        } else {
            return move[0] == this.moves.at(-1)[1]
        }
    }
    return true
    }
}