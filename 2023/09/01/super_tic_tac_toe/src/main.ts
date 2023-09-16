import { Game, Coord } from "./super_ttt"

const initial_game = new Game()
initial_game.add_move([0,1],[1,0],[0,4],[4,0],[0,7])
//const calc = initial_game.whose_turn()
console.log(initial_game.grid_is_won(0,'noughts'))

