import { Game, Coord } from "./super_ttt"

const move = [Coord.MID, Coord.TOP_LEFT]
const next = [Coord.TOP_LEFT, Coord.MID]
const next2 = [Coord.MID, Coord.MID_LEFT] // the choice of MID_LEFT is arbitrary (it should be different from the first move though)

const initial_game = new Game([move, next, next2])

console.log(initial_game)