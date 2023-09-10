export enum Coord {
    TOP_LEFT,
    TOP_MID,
    TOP_RIGHT,
    MID_LEFT,
    MID,
    MID_RIGHT,
    BOTTOM_LEFT,
    BOTTOM_MID,
    BOTTOM_RIGHT
  }

// export const pos_moves = new Map();

// export let counter = 0
// for (let i = 0; i < 9; i ++) {
//     for(let j = 0; j < 9; j ++){
//         const move = [i,j]
//         pos_moves.set(move, counter)
//         counter ++
//     }
// }
  
export class Game {
moves
constructor(moves) {
    this.moves = moves
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

is_won() {
    return false
}

is_legal() {
    // no move is played more than once
    if (this.remove_duplicates(this.moves).length !== this.moves.length) return false

    // the grid of the current move is related to the cell in the last move
    if (this.moves.length !== 0) {
    return this.moves[1][0] == this.moves[0][1]
    }

    return true
}
}