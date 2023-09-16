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
  it("the next move can be anywhere free if the grid pointed by last move is full", () => {
    const initial_game = new Game()
    initial_game.add_move([0,1],[1,0],[0,4],[4,0],[0,7],[7,0],[0,2],[2,0],[0,3],[3,0],[0,5],[5,0],[0,6],[6,0],[0,8],[8,0],[0,0])
    expect(initial_game.move_is_legal([2,2])).toBe(true)
    expect(initial_game.grid_is_full(0)).toBe(true)
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
  it('a full sub grid is a draw',() => {
    const initial_game = new Game()
    // in this case it's actually a won, too long to write down the list of moves for a draw. Note that the variant allowing to keep filling a grid after
    // it was won is sub-optimal as it allows the starting player to always win if she plays perfectly
    initial_game.add_move([0,1],[1,0],[0,4],[4,0],[0,7],[7,0],[0,2],[2,0],[0,3],[3,0],[0,5],[5,0],[0,6],[6,0],[0,8],[8,0],[0,0])
    expect(initial_game.grid_is_full(0)).toBe(true)
    expect(initial_game.grid_is_full(1)).toBe(false)
  })
  it('a game with more than 50% wins is won',() => {
    const initial_game = new Game()
    initial_game.add_move([4,1],[1,8],[8,5],[5,3],[3,7],[7,3],[3,1],[1,4],[4,7],[7,6],[6,3],[3,4],[4,4]) // crosses wins game in grid 4
    initial_game.add_move([1,0],[0,3],[3,2],[2,5],[5,5],[5,8],[8,0],[0,5],[5,4],[0,4])
    expect(initial_game.grid_is_won(4,'crosses')).toBe(true)
    expect(initial_game.grid_is_won(1,'noughts')).toBe(true)
    expect(initial_game.game_is_won()).toBe(false)
    console.log(initial_game.results)
  })
})
