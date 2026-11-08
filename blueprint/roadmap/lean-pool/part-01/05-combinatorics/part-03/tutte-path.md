---
declaration: theorem
origin: cited
lean: TutteFormalization.path_theorem
statement: formalized
proof: formalized
---

# Tutte’s path theorem for matroids

> Proves the modular-cut path theorem for finite matroids, with reusable rank-partition, hyperplane-separation, relative-complement, indecomposable-cover, and diamond constructions.

*Quoted from the card [LeanPool/projects/tutte-path.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/tutte-path.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`TutteFormalization.path_theorem`](https://leanpool.github.io/lean-pool/LeanPool/TuttePath/PathTheorem.html#TutteFormalization.path_theorem) (theorem; a main declaration), declared in [LeanPool/TuttePath/PathTheorem.lean, line 36](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/TuttePath/PathTheorem.lean#L36): “In a finite connected matroid, any two hyperplanes containing a proper indecomposable flat and lying outside a modular cut are joined by a finite Tutte path all of whose vertices contain that flat and avoid the cut. Consecutive vertices are distinct hyperplanes with indecomposable corank-two intersection; repeated nonconsecutive vertices are permitted.”
- [`TutteFormalization.path_theorem_of_indecomposable`](https://leanpool.github.io/lean-pool/LeanPool/TuttePath/PathTheorem.html#TutteFormalization.path_theorem_of_indecomposable) (theorem), declared in [LeanPool/TuttePath/PathTheorem.lean, line 27](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/TuttePath/PathTheorem.lean#L27): “In any finite matroid, two hyperplanes containing an indecomposable flat F and lying outside a modular cut are joined by a Tutte path whose vertices contain F and avoid the cut. This strengthens the cited path theorem by requiring only connectedness of the contraction by F; properness of F follows from containment in an endpoint hyperplane.”
- [`TutteFormalization.exists_indecomposable_complement`](https://leanpool.github.io/lean-pool/LeanPool/TuttePath/IndecomposableComplement.html#TutteFormalization.exists_indecomposable_complement) (theorem), declared in [LeanPool/TuttePath/IndecomposableComplement.lean, line 55](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/TuttePath/IndecomposableComplement.lean#L55): “If an indecomposable flat S and a flat U span the ground, every indecomposable flat T contained in both extends inside S to an indecomposable flat R spanning the ground with U, with corank R equal to rank U minus rank T.”
- [`TutteFormalization.exists_relative_complement`](https://leanpool.github.io/lean-pool/LeanPool/TuttePath/RelativeComplement.html#TutteFormalization.exists_relative_complement) (theorem), declared in [LeanPool/TuttePath/RelativeComplement.lean, line 70](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/TuttePath/RelativeComplement.lean#L70): “For nested flats T contained in S, there is a flat U containing T whose intersection with S is T, whose join with S is the ground, and whose corank equals rank S minus rank T.”

## Project

- Authors: Tutte formalization contributors.
- Source: [arXiv:2601.02582](https://arxiv.org/abs/2601.02582).
- Project repository: [mbaker386/tutte-homotopy-lean](https://github.com/mbaker386/tutte-homotopy-lean), at commit [ab33c233](https://github.com/mbaker386/tutte-homotopy-lean/tree/ab33c23369865b5fbd30b7a19710a527aa7ebab6).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 05B35.
- In Lean Pool: [LeanPool/TuttePath](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/TuttePath), from the card [LeanPool/projects/tutte-path.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/tutte-path.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/tutte-path.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/tutte-path.yaml)
- [Lean Pool at 2b205bf9: LeanPool/TuttePath](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/TuttePath)
