---
declaration: theorem
origin: cited
lean: ExistsNashEq, Brouwer, Brouwer_Product, IndexedLOrder.Scarf, FinGame
statement: formalized
---

# Existence of Nash equilibria via Brouwer's fixed-point theorem

> Formalizes Scarf's combinatorial lemma, derives Brouwer's fixed-point theorem on a simplex and on finite products of simplices, and uses it to prove the existence of a mixed Nash equilibrium in every finite game.

*Quoted from the card [LeanPool/projects/brouwer.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/brouwer.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`ExistsNashEq`](https://leanpool.github.io/lean-pool/LeanPool/Brouwer/Nash.html#ExistsNashEq) (theorem; a main declaration), declared in [LeanPool/Brouwer/Nash.lean, line 497](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Brouwer/Nash.lean#L497): “Every finite game has a mixed Nash equilibrium.” Its source, as the card gives it: “J. Nash, Equilibrium Points in N-Person Games, Proceedings of the National Academy of Sciences 36(1):48-49, 1950, doi:10.1073/pnas.36.1.48.”
- [`Brouwer`](https://leanpool.github.io/lean-pool/LeanPool/Brouwer/Brouwer.html#Brouwer) (theorem; a main declaration), declared in [LeanPool/Brouwer/Brouwer.lean, line 729](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Brouwer/Brouwer.lean#L729): “Every continuous self-map of a standard simplex has a fixed point.” Its source, as the card gives it: “H. Scarf, The Approximation of Fixed Points of a Continuous Mapping, SIAM Journal on Applied Mathematics 15(5):1328-1343, 1967, doi:10.1137/0115116.”
- [`Brouwer_Product`](https://leanpool.github.io/lean-pool/LeanPool/Brouwer/BrouwerProduct.html#Brouwer_Product) (theorem; a main declaration), declared in [LeanPool/Brouwer/BrouwerProduct.lean, line 610](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Brouwer/BrouwerProduct.lean#L610): “Every continuous self-map of a finite product of simplices has a fixed point.” Its source, as the card gives it: “H. Scarf, The Approximation of Fixed Points of a Continuous Mapping, SIAM Journal on Applied Mathematics 15(5):1328-1343, 1967, doi:10.1137/0115116.”
- [`IndexedLOrder.Scarf`](https://leanpool.github.io/lean-pool/LeanPool/Brouwer/Scarf.html#IndexedLOrder.Scarf) (theorem; a main declaration), declared in [LeanPool/Brouwer/Scarf.lean, line 1864](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Brouwer/Scarf.lean#L1864): “Scarf's combinatorial lemma producing a colorful simplex.” Its source, as the card gives it: “H. Scarf, The Approximation of Fixed Points of a Continuous Mapping, SIAM Journal on Applied Mathematics 15(5):1328-1343, 1967, doi:10.1137/0115116.”
- [`FinGame`](https://leanpool.github.io/lean-pool/LeanPool/Brouwer/Nash.html#FinGame) (structure; a main declaration), declared in [LeanPool/Brouwer/Nash.lean, line 75](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Brouwer/Nash.lean#L75): “The structure of a finite game with finitely many players and finite pure strategy sets.” Its source, as the card gives it: “J. Nash, Equilibrium Points in N-Person Games, Proceedings of the National Academy of Sciences 36(1):48-49, 1950, doi:10.1073/pnas.36.1.48.”
- [`FinGame.mixedNashEquilibrium`](https://leanpool.github.io/lean-pool/LeanPool/Brouwer/Nash.html#FinGame.mixedNashEquilibrium) (def), declared in [LeanPool/Brouwer/Nash.lean, line 171](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Brouwer/Nash.lean#L171): “The predicate that a mixed strategy profile is a Nash equilibrium.” Its source, as the card gives it: “J. Nash, Equilibrium Points in N-Person Games, Proceedings of the National Academy of Sciences 36(1):48-49, 1950, doi:10.1073/pnas.36.1.48.”

## Project

- Authors: Math_XMUM.
- Source: [doi:10.1073/pnas.36.1.48](https://doi.org/10.1073/pnas.36.1.48).
- Project repository: [math-xmum/Brouwer](https://github.com/math-xmum/Brouwer).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0, keeping its copyright line: “Copyright (c) 2025 Math_XMUM”.
- MSC2020: 91A06, 91A10, 47H10.
- In Lean Pool: [LeanPool/Brouwer](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Brouwer), from the card [LeanPool/projects/brouwer.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/brouwer.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/brouwer.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/brouwer.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Brouwer](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Brouwer)
