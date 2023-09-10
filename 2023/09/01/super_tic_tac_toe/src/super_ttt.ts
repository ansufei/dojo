export enum Coord {
    TOP_LEFT,
    TOP_MID,
    TOP_RIGHT,
    MID_LEFT,
    MID,
  }
  
export class Game {
moves
constructor(moves) {
    this.moves = moves
}
is_won() {
    return false
}

is_legal() {
    //Ca devrait marcher mais le langage est pourri
    console.log(new Set(this.moves).size)
    if (new Set(this.moves).size !== this.moves.length) return false

    if (this.moves.length !== 0) {
    return this.moves[1][0] == this.moves[0][1]
    }

    return true
}
}