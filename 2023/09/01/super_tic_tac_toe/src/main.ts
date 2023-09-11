import { Game, Coord } from "./super_ttt"

const initial_game = new Game()
initial_game.add_move([0,0],[0,1])
const calc = initial_game.whose_turn()
