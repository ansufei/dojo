import { Game, Coord } from "./super_ttt"

var game = new Game()
game.add_move([Coord.BOTTOM_LEFT,Coord.BOTTOM_MID],[Coord.BOTTOM_MID,Coord.MID],[Coord.BOTTOM_LEFT,Coord.BOTTOM_LEFT])
console.log(game.grids)