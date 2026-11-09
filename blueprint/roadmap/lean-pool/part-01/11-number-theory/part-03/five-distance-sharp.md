---
declaration: theorem
origin: cited
lean: ThreeGap.LinftyRecords3.nine_attained
statement: formalized
proof: formalized
---

# Sharp Five-Distance and Sup-Norm Gap Theorems

> Formalizes sharp gap theorems for Kronecker sequences on tori: the Euclidean five-distance theorem on the 2-torus and the sup-norm gap bound, together with explicit arithmetic witnesses realizing the extremal cases - five distinct nearest-neighbour distances for the Euclidean and sup-norm metrics in dimension two, and nine distinct sup-norm distances in dimension three (Haynes-Marklof-Ramirez), via exact modular arithmetic on best simultaneous Diophantine approximations.

*Quoted from the card [LeanPool/projects/five-distance-sharp.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/five-distance-sharp.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`ThreeGap.EuclideanRecords.sharp_attained`](https://leanpool.github.io/lean-pool/LeanPool/ThreeGap/EuclideanFiveDistanceSharpArith.html#ThreeGap.EuclideanRecords.sharp_attained) (theorem), declared in [LeanPool/ThreeGap/EuclideanFiveDistanceSharpArith.lean, line 488](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ThreeGap/EuclideanFiveDistanceSharpArith.lean#L488): “Exhibits a base point on the 2-torus with an irrational coordinate and an N whose Euclidean nearest-neighbour distances realize exactly five distinct values, showing the Euclidean five-distance bound is sharp.” Its source, as the card gives it: “A. Haynes and J. Marklof, A five distance theorem for Kronecker sequences, International Mathematics Research Notices 2022(24):19747-19789, doi:10.1093/imrn/rnab205, arXiv:2009.08444.”
- [`ThreeGap.LinftyRecords.sharp_attained`](https://leanpool.github.io/lean-pool/LeanPool/ThreeGap/LinftyFiveDistanceSharpArith.html#ThreeGap.LinftyRecords.sharp_attained) (theorem), declared in [LeanPool/ThreeGap/LinftyFiveDistanceSharpArith.lean, line 366](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ThreeGap/LinftyFiveDistanceSharpArith.lean#L366): “Exhibits a base point on the 2-torus with an irrational coordinate and an N whose sup-norm nearest-neighbour distances realize exactly five distinct values, showing the sup-norm gap bound is sharp in dimension two.”
- [`ThreeGap.LinftyRecords3.nine_attained`](https://leanpool.github.io/lean-pool/LeanPool/ThreeGap/LinftyThreeTorusNine.html#ThreeGap.LinftyRecords3.nine_attained) (theorem; a main declaration), declared in [LeanPool/ThreeGap/LinftyThreeTorusNine.lean, line 1173](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ThreeGap/LinftyThreeTorusNine.lean#L1173): “Exhibits a base point on the 3-torus with an irrational coordinate and an N whose sup-norm nearest-neighbour distances realize at least nine distinct values, showing the sup-norm gap bound is sharp in dimension three.”

## Project

- Authors: Vico Bonfioli.
- Source: *Higher dimensional gap theorems for the maximum metric* by Alan Haynes, Jens Marklof, Ana Cristina Moreira Ramirez, [arXiv:2010.08842](https://arxiv.org/abs/2010.08842).
- Project repository: [ElVec1o/five-distance-sharp](https://github.com/ElVec1o/five-distance-sharp).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 11J71.
- In Lean Pool: [LeanPool/ThreeGap](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ThreeGap), from the card [LeanPool/projects/five-distance-sharp.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/five-distance-sharp.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/five-distance-sharp.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/five-distance-sharp.yaml)
- [Lean Pool at 2b205bf9: LeanPool/ThreeGap](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ThreeGap)
