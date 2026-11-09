---
declaration: theorem
origin: cited
lean: ParallelPostulate.Hilbert.playfair_independent_continuous
statement: formalized
proof: formalized
---

# Independence of Playfair's axiom via Euclidean and Klein models

> Constructs Euclidean and Klein models of a synthetic Hilbert plane, proving that Playfair's axiom is independent of incidence, Pasch order, and congruence axioms, even with Archimedes and Dedekind continuity. Develops reusable coordinate geometry over ordered fields, projective motions, Klein angles and metric, smooth-path length and distance, congruence constructions, and a coordinate curvature calculation. Dedekind continuity replaces Hilbert's maximal completeness axiom; their equivalence is not formalized. Curvature uses Brioschi's formula, and distance uses C1 paths; no identification with Mathlib's Riemannian distance or connection curvature is asserted.

*Quoted from the card [LeanPool/projects/parallel-postulate.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/parallel-postulate.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`ParallelPostulate.Hilbert.playfair_independent_continuous`](https://leanpool.github.io/lean-pool/LeanPool/ParallelPostulate.html#ParallelPostulate.Hilbert.playfair_independent_continuous) (theorem; a main declaration), declared in [LeanPool/ParallelPostulate.lean, line 4530](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ParallelPostulate.lean#L4530): “There exists a Hilbert plane satisfying Archimedes and Dedekind continuity and Playfair's axiom, and there exists another satisfying the same continuity axioms and the negation of Playfair's axiom. The models use real coordinate planes with bounds zero and minus one.” Its source, as the card gives it: “Upstream Hilbert/Independence.lean. First publicly announced 2026-09-30 01:08:53 UTC at https://leanprover.zulipchat.com/\#narrow/channel/583339-AI-authored-projects/topic/Independence.20Parallel.20Postulate/near/627942879. The author's follow-up discloses mostly AI-written proofs. Pasch order and Dedekind continuity are the stated variants; equivalence to plane separation and maximal completeness is not proved.”
- [`ParallelPostulate.HyperbolicPlane.hyperbolic_parallels`](https://leanpool.github.io/lean-pool/LeanPool/ParallelPostulate/Geometry.html#ParallelPostulate.HyperbolicPlane.hyperbolic_parallels) (theorem), declared in [LeanPool/ParallelPostulate/Geometry.lean, line 1179](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ParallelPostulate/Geometry.lean#L1179): “Over any linearly ordered field, for every negative bound and every line in the bounded coordinate plane, infinitely many distinct lines pass through any point of the plane outside that line without meeting it.”
- [`ParallelPostulate.HyperbolicPlane.kleinDist_eq_arsinh`](https://leanpool.github.io/lean-pool/LeanPool/ParallelPostulate.html#ParallelPostulate.HyperbolicPlane.kleinDist_eq_arsinh) (theorem), declared in [LeanPool/ParallelPostulate.lean, line 2667](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ParallelPostulate.lean#L2667): “For every negative real bound and every pair of points in its plane, the infimum of C1-path lengths in Klein's coordinate metric equals arsinh of the square root of minus the bound times apart, divided by the square root of minus the bound.”
- [`ParallelPostulate.HyperbolicPlane.kleinMetric_curvature`](https://leanpool.github.io/lean-pool/LeanPool/ParallelPostulate.html#ParallelPostulate.HyperbolicPlane.kleinMetric_curvature) (theorem), declared in [LeanPool/ParallelPostulate.lean, line 2158](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ParallelPostulate.lean#L2158): “For every real bound, Brioschi's coordinate curvature formula applied to the three coefficients of Klein's metric equals that bound at every point of its coordinate plane.”

## Project

- Authors: Richard Sutton.
- Source: *ParallelPostulate formalization by Richard Sutton*.
- Project repository: [Richiesutie/ParallelPostulate](https://github.com/Richiesutie/ParallelPostulate), at commit [8ee50280](https://github.com/Richiesutie/ParallelPostulate/tree/8ee502804263194ae40babeca9773127f1e0a085).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 51F15, 51M10, 53A35.
- In Lean Pool: [LeanPool/ParallelPostulate](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ParallelPostulate), from the card [LeanPool/projects/parallel-postulate.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/parallel-postulate.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/parallel-postulate.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/parallel-postulate.yaml)
- [Lean Pool at 2b205bf9: LeanPool/ParallelPostulate](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ParallelPostulate)
