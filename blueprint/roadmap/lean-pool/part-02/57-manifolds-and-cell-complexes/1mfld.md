---
declaration: theorem
origin: cited
lean: OneMfld.homeomorph_circle_or_unitInterval
statement: formalized
proof: formalized
---

# The classification of compact 1-manifolds

> A Lean 4 (mathlib) proof of the classification of 1-manifolds, specifically that every compact, connected, Hausdorff topological space charted on the half-line [0,∞) is homeomorphic to the circle S¹ or to the closed unit interval [0,1]. The proof follows David Gale's outline: shrink to a finite atlas of interval charts, then induct on the atlas size, merging two overlapping charts at each step; a connected overlap glues two charts into one (two boundary charts glue onto [0, 1]), while a disconnected overlap has exactly two components and yields the circle.

*Quoted from the card [LeanPool/projects/1mfld.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/1mfld.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists one main result, with its informal statement quoted from the card. The scan finds its declaration in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`OneMfld.homeomorph_circle_or_unitInterval`](https://leanpool.github.io/lean-pool/LeanPool/OneManifold/Solution.html#OneMfld.homeomorph_circle_or_unitInterval) (theorem; a main declaration), declared in [LeanPool/OneManifold/Solution.lean, line 26](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/OneManifold/Solution.lean#L26): “Every compact connected Hausdorff space charted on the nonnegative real half-line is homeomorphic to the circle or the closed unit interval.”

## Project

- Authors: Jim Fowler, Dennis Sweeney.
- Project repository: [sweeneyde/1mfld](https://github.com/sweeneyde/1mfld), at commit [83e961ba](https://github.com/sweeneyde/1mfld/tree/83e961ba28dd8182e7bae844756aba614eb1512e).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 57N99, 54F65, 68V20.
- In Lean Pool: [LeanPool/OneManifold](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/OneManifold), from the card [LeanPool/projects/1mfld.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/1mfld.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/1mfld.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/1mfld.yaml)
- [Lean Pool at 2b205bf9: LeanPool/OneManifold](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/OneManifold)
