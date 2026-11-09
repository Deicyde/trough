---
declaration: theorem
origin: cited
lean: BooleanIsoperimetry.harper_theorem, BooleanIsoperimetry.conwayGuyGapRigidity
statement: formalized
proof: formalized
---

# Boolean Isoperimetry and Conway--Guy Coherent Gaps

> Formalizes Harper's vertex-isoperimetric theorem for the Boolean cube: among all families of a fixed cardinality, the simplicial initial segment has the smallest closed radius-one Hamming neighborhood. Develops the supporting binomial-cascade identities, Kruskal--Katona shadow bounds, coordinate compressions, and the final dimension induction. Applies the coherent-gap certificate method to prove normalized consecutive-gap rigidity for the Conway--Guy sequence from its exact recurrence.

*Quoted from the card [LeanPool/projects/boolean-isoperimetry.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/boolean-isoperimetry.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`BooleanIsoperimetry.harper_theorem`](https://leanpool.github.io/lean-pool/LeanPool/BooleanIsoperimetry/Harper.html#BooleanIsoperimetry.harper_theorem) (theorem; a main declaration), declared in [LeanPool/BooleanIsoperimetry/Harper.lean, line 2165](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BooleanIsoperimetry/Harper.lean#L2165): “For every family of vertices in an n-dimensional Boolean cube, the simplicial initial segment of the same cardinality has a closed radius-one Hamming neighborhood no larger than that of the family.”
- [`BooleanIsoperimetry.conwayGuyGapRigidity`](https://leanpool.github.io/lean-pool/LeanPool/BooleanIsoperimetry/ConwayGuyOrderBridge.html#BooleanIsoperimetry.conwayGuyGapRigidity) (alias; a main declaration), declared in [LeanPool/BooleanIsoperimetry/ConwayGuyOrderBridge.lean, line 199](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BooleanIsoperimetry/ConwayGuyOrderBridge.lean#L199): “In every dimension, any real row whose consecutive subset-sum gaps relative to the Conway--Guy reference row are at least one dominates that row coordinatewise.”

## Project

- Authors: Alexey Milovanov, Egor Lyfar.
- Source: *Optimal numberings and isoperimetric problems on graphs; A sum packing problem of Erdős and the Conway--Guy sequence* by L. H. Harper, Tom Bohman, [doi:10.1016/S0021-9800(66)80059-5](https://doi.org/10.1016/S0021-9800%2866%2980059-5), [https://doi.org/10.1090/S0002-9939-96-03653-2](https://doi.org/10.1090/S0002-9939-96-03653-2).
- Project repository: [AlexeyMilovanov/BooleanIsoperimetry](https://github.com/AlexeyMilovanov/BooleanIsoperimetry).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05D05, 05C35.
- In Lean Pool: [LeanPool/BooleanIsoperimetry](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BooleanIsoperimetry), from the card [LeanPool/projects/boolean-isoperimetry.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/boolean-isoperimetry.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/boolean-isoperimetry.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/boolean-isoperimetry.yaml)
- [Lean Pool at 2b205bf9: LeanPool/BooleanIsoperimetry](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BooleanIsoperimetry)
