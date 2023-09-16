import { describe, expect, it } from "vitest"
import { Game, Coord } from "./super_ttt"


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
    const move = [Coord.MID, Coord.TOP_LEFT]
    const same_move = move
    const initial_game = new Game()
    initial_game.add_move(move, same_move)
    expect(initial_game.move_is_legal(same_move)).toBe(false)
  })
  it("the next move should be in the correct grid", () => {
    const move = [Coord.MID, Coord.TOP_LEFT]
    const next = [Coord.TOP_LEFT, Coord.MID] // the choice of Coord.MID is arbitrary
    const initial_game = new Game()
    initial_game.add_move(move)
    expect(initial_game.move_is_legal(next)).toBe(true)
    const next2 = [Coord.MID, Coord.MID_LEFT] // the choice of MID_LEFT is arbitrary (it should be different from the first move though)
    const three_moves_initial_game = new Game()
    three_moves_initial_game.add_move(move, next)
    expect(three_moves_initial_game.move_is_legal(next2)).toBe(true)
    const wrong_game = new Game()
    wrong_game.add_move(move)
    expect(wrong_game.move_is_legal(next2)).toBe(false)
  })
  it("a move can only be played once", () => {
    const move = [Coord.MID, Coord.TOP_LEFT]
    const next = [Coord.TOP_LEFT, Coord.MID]
    const next2 = move
    const initial_game = new Game()
    initial_game.add_move(move, next)
    expect(initial_game.move_is_legal(next2)).toBe(false)
  })
  it("the next move can be anywhere free if the grid pointed by last move is won", () => {
    // const initial_game = new Game()
    // initial_game.add_move([0,1],[1,0],[0,2],[2,0],[0,0])
    // expect(initial_game.move_is_legal([3,0])).toBe(true)
  })
  it("the next move can be anywhere free if the grid pointed by last move is full", () => {
    // const initial_game = new Game()
    // initial_game.add_move([0,0],[0,1],[1,0],[0,2],[2,0],[0,3],[3,0],[0,4],[4,0],[0,5],[5,0],[0,6],[6,0],[0,7],[7,9],[0,8])
    // expect(initial_game.move_is_legal([2,2])).toBe(true)
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
})
