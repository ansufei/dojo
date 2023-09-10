import { describe, expect, it } from "vitest"
import { Game, Coord } from "./super_ttt"


describe("a game", () => {
  it("is initially not won", () => {
    const initial_game = new Game([])
    expect(initial_game.is_won()).toBe(false)
  })
  it("no moves is legal", () => {
    const initial_game = new Game([])
    expect(initial_game.is_legal()).toBe(true)
  })
  it("two moves on the same place is illegal", () => {
    const move = [Coord.MID, Coord.TOP_LEFT]
    const same_move = move
    const initial_game = new Game([move, same_move])
    expect(initial_game.is_legal()).toBe(false)
  })
  it("the next move should be in the correct grid", () => {
    const move = [Coord.MID, Coord.TOP_LEFT]
    const next = [Coord.TOP_LEFT, Coord.MID] // the choice of Coord.MID is arbitrary
    const initial_game = new Game([move, next])
    expect(initial_game.is_legal()).toBe(true)
    const next2 = [Coord.MID, Coord.MID_LEFT] // the choice of MID_LEFT is arbitrary (it should be different from the first move though)
    const three_moves_initial_game = new Game([move, next, next2])
    expect(three_moves_initial_game.is_legal()).toBe(true)
  })
  it("a move can only be played once", () => {
    const move = [Coord.MID, Coord.TOP_LEFT]
    const next = [Coord.TOP_LEFT, Coord.MID]
    const initial_game = new Game([move, next, move])
    expect(initial_game.is_legal()).toBe(false)
  })
  it("the next move can be anywhere free if the grid pointed by last move is full", () => {
    
  })
})
