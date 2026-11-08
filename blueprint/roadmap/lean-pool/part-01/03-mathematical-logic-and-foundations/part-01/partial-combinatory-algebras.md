---
declaration: class
origin: cited
lean: LeanPool.PartialCombinatoryAlgebras.PCA
statement: formalized
---

# Partial Combinatory Algebras

> Formalises partial combinatory algebras with the K/S combinators, programming combinators, the free combinatory algebra, and the graph model.

*Quoted from the card [LeanPool/projects/partial-combinatory-algebras.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/partial-combinatory-algebras.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`LeanPool.PartialCombinatoryAlgebras.PCA`](https://leanpool.github.io/lean-pool/LeanPool/PartialCombinatoryAlgebras/PartialCombinatoryAlgebra.html#LeanPool.PartialCombinatoryAlgebras.PCA) (class; a main declaration), declared in [LeanPool/PartialCombinatoryAlgebras/PartialCombinatoryAlgebra.lean, line 43](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PartialCombinatoryAlgebras/PartialCombinatoryAlgebra.lean#L43): “Defines the class of partial combinatory algebras (PCAs) with K and S combinators.”
- [`LeanPool.PartialCombinatoryAlgebras.CA`](https://leanpool.github.io/lean-pool/LeanPool/PartialCombinatoryAlgebras/CombinatoryAlgebra.html#LeanPool.PartialCombinatoryAlgebras.CA) (class), declared in [LeanPool/PartialCombinatoryAlgebras/CombinatoryAlgebra.lean, line 25](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PartialCombinatoryAlgebras/CombinatoryAlgebra.lean#L25): “Defines total combinatory algebras and exhibits every total combinatory algebra as a PCA.”
- [`LeanPool.PartialCombinatoryAlgebras.FreeCA`](https://leanpool.github.io/lean-pool/LeanPool/PartialCombinatoryAlgebras/FreeCombinatoryAlgebra.html#LeanPool.PartialCombinatoryAlgebras.FreeCA) (instance), declared in [LeanPool/PartialCombinatoryAlgebras/FreeCombinatoryAlgebra.lean, line 59](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PartialCombinatoryAlgebras/FreeCombinatoryAlgebra.lean#L59): “Constructs the free total combinatory algebra as a quotient of formal expressions.”
- [`LeanPool.PartialCombinatoryAlgebras.GraphModel.isCA`](https://leanpool.github.io/lean-pool/LeanPool/PartialCombinatoryAlgebras/GraphModel.html#LeanPool.PartialCombinatoryAlgebras.GraphModel.isCA) (instance), declared in [LeanPool/PartialCombinatoryAlgebras/GraphModel.lean, line 403](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PartialCombinatoryAlgebras/GraphModel.lean#L403): “Constructs the graph-model combinatory algebra on the powerset of any Listing-typed carrier.”

## Project

- Authors: Andrej Bauer.
- Source: *Realizability: An Introduction to its Categorical Side* by Jaap van Oosten, [https://doi.org/10.1016/S0049-237X(08)80003-1](https://doi.org/10.1016/S0049-237X%2808%2980003-1).
- Project repository: [andrejbauer/partial-combinatory-algebras](https://github.com/andrejbauer/partial-combinatory-algebras).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0, keeping its copyright line: “Copyright (c) 2024 Andrej Bauer”.
- MSC2020: 03B40, 03D75.
- In Lean Pool: [LeanPool/PartialCombinatoryAlgebras](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PartialCombinatoryAlgebras), from the card [LeanPool/projects/partial-combinatory-algebras.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/partial-combinatory-algebras.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/partial-combinatory-algebras.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/partial-combinatory-algebras.yaml)
- [Lean Pool at 2b205bf9: LeanPool/PartialCombinatoryAlgebras](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PartialCombinatoryAlgebras)
