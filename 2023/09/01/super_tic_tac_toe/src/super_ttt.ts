/* TO DO:
- stop players from using a won grid
- a player can choose which sub-grid to play only the adversary points to a grid that she (the player) already won, not any won grid
- the full game must look like a TTT as well, i.e. the winning sub-grids must be aligned
- refactor this.player
*/

export class Game {
moves
map_moves
results
player
constructor() {
    this.moves = new Array();
    this.map_moves = new Map();
    this.map_moves.set('crosses', new Map())
    this.map_moves.set('noughts', new Map())
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

grid_is_full(grid) {
    let length_grid = 0;
    if (this.map_moves.get('crosses').has(grid)) {
        length_grid += this.map_moves.get('crosses').get(grid).length
    }
    if (this.map_moves.get('noughts').has(grid)) {
        length_grid += this.map_moves.get('noughts').get(grid).length
    }
    if (length_grid == 9) {
        if (this.results.has(grid)) {
            this.grid_is_won(grid,this.player)
        } else {
            this.results.set(grid,'draw')
        }
        return true 
    }
    return false
}

grid_is_won(grid,player) {
    let moves_player;
    if (this.map_moves.get(player).has(grid)) {
        moves_player = this.map_moves.get(player).get(grid)
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
    return player
}

game_is_won() {
    // any player's nb of won is higher than (total - draws) / 2
    // else all draws
    return false
}

move_is_legal(move = Array()) {
    // an empty move is legal
    if (move.length == 0) return true

    // no move is played more than once 
    if (this.moves.indexOf(move) > -1) {
        return false
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

add_move(...moves) {
    // mapping completion of small grids (keys are the big grids)
    if (moves.length == 0) return this.map_moves // no moves is legal
    else {
        moves.forEach((value, valueIndex) => {
            if (this.move_is_legal(value)) {
                this.player = this.whose_turn()
                
                // add the move to the log of the order in which the moves are played
                this.moves.push(value)
                // also add the move to the map of the current game
                this.populate_grid(this.map_moves.get(this.player), value)
                
                // check if won
                this.grid_is_won(value[0],this.player) 

                // check if game won
                this.game_is_won()
                    
            } else {
                console.log(value, 'is not a legal move here')
            }    
        })
    }
    return this.map_moves
    }
}