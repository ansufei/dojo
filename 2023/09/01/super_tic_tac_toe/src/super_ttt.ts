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
grids
constructor() {
    this.moves = new Array();
    this.grids = new Map();
}
encode_moves(moves) {
    let converted_moves = new Array(moves.length)
    for (let i=0; i < moves.length; i ++) {
        converted_moves[i] =  moves[i][0].toString() + moves[i][1].toString()
    }
    return converted_moves
}

remove_duplicates(moves) {
    let converted_moves = this.encode_moves(moves)
    return [...new Set(converted_moves)]
  }

add_move(...moves) {
    // mapping completion of small grids (keys are the big grids)
    if (moves.length == 0) return this.grids
    else if (moves[0] == Coord.EMPTY) return this.grids
    else {
        moves.forEach(value => {
            if (this.move_is_legal(value)) {
                // add the move to the log of the order in which the moves are played
                this.moves.push(value)
                // also add the move to the map of the current game
                if (this.grids.has(value[0])){
                    this.grids.get(value[0]).push(value[1]);
                } else {
                    this.grids.set(value[0], [value[1]]);
                }
            }    
        })
    }
    return this.grids
}

// small_grid_is_full(moves) {
// }

// small_grid_is_won() {

//}

// game_is_won() {

//}

whose_turn() {
    let calc = this.moves.length
    let player = 'crosses'
    if (calc % 2 == 0) {
        player = 'noughts'
        console.log('noughts should play next')
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
    if (this.grids.has(move[0])) {
        if (this.grids.get(move[0]).includes(move[1])) {
            return false
        }
    }
    // the sub-grid referred to in the last move was won, free to choose another grid (exception to the default case below)

    // the sub-grid referred to in the last move is full, free to choose another grid (exception to the default case below)

    // the grid of the current move is related to the cell in the last move (default case)
    if (this.moves.length !== 0) {
        return move[0] == this.moves.at(-1)[1]
    }

    return true
}
}