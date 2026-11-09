---
declaration: theorem
origin: cited
lean: MisereGames.Form.Promain.of_universe
statement: formalized
proof: formalized
---

# Misere combinatorial games

> Formalizes a combinatorial game theory library for misere play, including comparison modulo universes, p-free forms, outcome-stability, Property X, and concrete rulesets such as Hackenbush.

*Quoted from the card [LeanPool/projects/misere-games.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/misere-games.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`MisereGames.Form.Promain.of_universe`](https://leanpool.github.io/lean-pool/LeanPool/MisereGames/Misere/Comparison.html#MisereGames.Form.Promain.of_universe) (theorem; a main declaration), declared in [LeanPool/MisereGames/Misere/Comparison.lean, line 572](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MisereGames/Misere/Comparison.lean#L572): “Shows that comparison modulo a universe is characterized by the maintenance-proviso test.”
- [`MisereGames.IntegerInvertible.isPFree_of_propertyX`](https://leanpool.github.io/lean-pool/LeanPool/MisereGames/Misere/OutcomeStable/PropertyX.html#MisereGames.IntegerInvertible.isPFree_of_propertyX) (theorem), declared in [LeanPool/MisereGames/Misere/OutcomeStable/PropertyX.lean, line 599](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MisereGames/Misere/OutcomeStable/PropertyX.lean#L599): “Proves that Property X makes the sum of two short p-free games p-free in an outcome-stable, hereditary, integer-invertible monoid.”
- `MisereGames.Form.Preservation.endLikeSeedToUniverse_bijective`, which the scan does not find declared in the project's files at this commit: “Proves that universal closure gives a bijection from bounded end-like seeds to universes.”

## Project

- Authors: Tomasz Maciosowski, Alfie Davies.
- Source: *misere-games* by Tomasz Maciosowski, Alfie Davies, Violeta Hernandez Palacios, Yuyang Zhao.
- Project repository: [t4ccer/misere-games](https://github.com/t4ccer/misere-games).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 91A46, 05C57.
- In Lean Pool: [LeanPool/MisereGames](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MisereGames), from the card [LeanPool/projects/misere-games.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/misere-games.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/misere-games.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/misere-games.yaml)
- [Lean Pool at 2b205bf9: LeanPool/MisereGames](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MisereGames)
