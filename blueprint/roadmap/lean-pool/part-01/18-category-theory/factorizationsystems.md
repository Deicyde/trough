---
declaration: def
origin: cited
lean: CategoryTheory.FactorizationSystemCharacterization
statement: formalized
---

# Factorization Systems

> Formalizes factorization systems, orthogonality, orthogonal complements, and the standard construction from weak factorization plus orthogonality.

*Quoted from the card [LeanPool/projects/factorizationsystems.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/factorizationsystems.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`CategoryTheory.FactorizationSystem`](https://leanpool.github.io/lean-pool/LeanPool/FactorizationSystems/Basic.html#CategoryTheory.FactorizationSystem) (structure), declared in [LeanPool/FactorizationSystems/Basic.lean, line 29](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FactorizationSystems/Basic.lean#L29): “Defines factorization systems on a category with specified left and right classes.”
- [`CategoryTheory.FactorizationSystemCharacterization`](https://leanpool.github.io/lean-pool/LeanPool/FactorizationSystems/Characterization.html#CategoryTheory.FactorizationSystemCharacterization) (def; a main declaration), declared in [LeanPool/FactorizationSystems/Characterization.lean, line 286](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FactorizationSystems/Characterization.lean#L286): “Constructs a factorization system from repleteness, weak factorizations, and orthogonality.”
- [`CategoryTheory.orthogonal`](https://leanpool.github.io/lean-pool/LeanPool/FactorizationSystems/Orthogonality.html#CategoryTheory.orthogonal) (structure), declared in [LeanPool/FactorizationSystems/Orthogonality.lean, line 93](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FactorizationSystems/Orthogonality.lean#L93): “Defines orthogonality of two morphisms by existence and uniqueness of diagonal fillers.”
- `CategoryTheory.right_orthogonal_complement`, which the scan does not find declared in the project's files at this commit: “Defines the right orthogonal complement of a morphism property.”

## Project

- Authors: Ivan Kobe.
- Source: *Category Theory in Context* by Emily Riehl, [https://emilyriehl.github.io/files/context.pdf](https://emilyriehl.github.io/files/context.pdf).
- Project repository: [ivankobe/FactorizationSystems](https://github.com/ivankobe/FactorizationSystems).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0, keeping its copyright line: “Copyright (c) 2024 ivankobe”.
- MSC2020: 18A32, 18A40.
- In Lean Pool: [LeanPool/FactorizationSystems](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FactorizationSystems), from the card [LeanPool/projects/factorizationsystems.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/factorizationsystems.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/factorizationsystems.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/factorizationsystems.yaml)
- [Lean Pool at 2b205bf9: LeanPool/FactorizationSystems](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FactorizationSystems)
