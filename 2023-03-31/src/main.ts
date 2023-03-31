import { pierreFeuilleCiseaux } from "./pierreFeuilleCiseaux.ts"
import { parse } from "https://deno.land/std/flags/mod.ts"

const mains = parse(Deno.args)._

const resultat = pierreFeuilleCiseaux(mains[0], mains[1])

console.log(resultat)
