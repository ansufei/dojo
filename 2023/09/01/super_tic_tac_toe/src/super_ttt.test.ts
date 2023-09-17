import { describe, expect, it } from "vitest"
import { Game } from "./super_ttt"


describe("a game", () => {
  it("is initially not won", () => {
    const initial_game = new Game()
    expect(initial_game.game_is_won()).toBe(false)
  })
  it("no moves is legal", () => {
    const initial_game = new Game()
    expect(initial_game.move_is_legal()).toBe(true)
  })
  it("two moves on the same place is illegal", () => {
    const move = [4, 0]
    const same_move = move
    const initial_game = new Game()
    initial_game.add_move(move, same_move)
    expect(initial_game.move_is_legal(same_move)).toBe(false)
  })
  it("the next move should be in the correct grid", () => {
    const move = [4, 0]
    const next = [0, 4] // the choice of 4 is arbitrary
    const initial_game = new Game()
    initial_game.add_move(move)
    expect(initial_game.move_is_legal(next)).toBe(true)
    const next2 = [4, 3] // the choice of MID_LEFT is arbitrary (it should be different from the first move though)
    const three_moves_initial_game = new Game()
    three_moves_initial_game.add_move(move, next)
    expect(three_moves_initial_game.move_is_legal(next2)).toBe(true)
    const wrong_game = new Game()
    wrong_game.add_move(move)
    expect(wrong_game.move_is_legal(next2)).toBe(false)
  })
  it("a move can only be played once", () => {
    const move = [4, 0]
    const next = [0, 4]
    const next2 = move
    const initial_game = new Game()
    initial_game.add_move(move, next)
    expect(initial_game.move_is_legal(next2)).toBe(false)
  })
  it("the next move can be anywhere free if the grid pointed by last move is won", () => {
    const initial_game = new Game()
    initial_game.add_move([0,1],[1,0],[0,4],[4,0],[0,7],[7,0])
    expect(initial_game.move_is_legal([3,0])).toBe(true)
  })
  it("a move can not be on a previously won/lost grid", () => {
    const initial_game = new Game()
    initial_game.add_move([0,1],[1,0],[0,4],[4,0],[0,7],[7,0],[3,0])
    expect(initial_game.move_is_legal([0,2])).toBe(false)
  })
  it("the next move can be anywhere free if the grid pointed by last move is a draw", () => {
    const initial_game = new Game()
    initial_game.add_move([4,1],[1,4],[4,2],[2,2],[2,4],[4,0],[0,4],[4,5],[5,4],[4,6],[6,0],[0,3],[3,3],[3,4],[4,3],[3,6],[6,4],[4,7],[7,4],[4,4],[4,8],[8,4])
    expect(initial_game.grid_is_full(4)).toBe(true)
    expect(initial_game.move_is_legal([2,7])).toBe(true)
  })
  it('correct player should play next',() => {
    //by convention crosses plays first
    const initial_game = new Game()
    initial_game.add_move([0,0],[0,1])
    expect(initial_game.whose_turn()).toBe('crosses')
  })
  it('a small grid is won with 3 adjacent moves by the same player',() => {
    const initial_game = new Game()
    initial_game.add_move([0,1],[1,0],[0,4],[4,0],[0,7])
    expect(initial_game.grid_is_won(0,'crosses')).toBe(true)
    expect(initial_game.grid_is_won(0,'noughts')).toBe(false)
    expect(initial_game.grid_is_won(1,'crosses')).toBe(false)
    expect(initial_game.grid_is_won(1,'noughts')).toBe(false)
  })
  it('a game with 3 aligned wins is won',() => {
    const initial_game = new Game()
    initial_game.add_move([4,1],[1,8],[8,5],[5,3],[3,7],[7,3],[3,1],[1,4],[4,7],[7,6],[6,3],[3,4],[4,4]) // crosses wins in grid 4
    initial_game.add_move([1,0],[0,3],[3,2],[2,5],[5,5],[5,8],[8,0],[0,5],[5,4],[0,4],[7,0],[8,3],[3,6]) // noughts will loose the game or draw
    initial_game.add_move([6,2],[2,6],[6,6],[6,0],[8,4]) // crosses wins the game
    expect(initial_game.grid_is_won(4,'crosses')).toBe(true)
    expect(initial_game.grid_is_won(1,'noughts')).toBe(true)
    expect(initial_game.game_is_won('noughts')).toBe(false)
    expect(initial_game.game_is_won('crosses')).toBe(true)
    console.log(initial_game.results)
  })
})
