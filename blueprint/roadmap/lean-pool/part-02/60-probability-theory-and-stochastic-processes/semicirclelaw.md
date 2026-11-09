---
declaration: lemma
origin: cited
lean: LeanPool.SemicircleLaw.integral_semicirclePDFReal_eq_one
statement: formalized
proof: formalized
---

# Wigner Semicircle Distribution

> Defines the real Wigner semicircle distribution, its normalized density, affine transformations, and finite-moment integrability.

*Quoted from the card [LeanPool/projects/semicirclelaw.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/semicirclelaw.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 7 main results, each with its informal statement quoted from the card. The scan finds 7 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`LeanPool.SemicircleLaw.semicirclePDFReal`](https://leanpool.github.io/lean-pool/LeanPool/SemicircleLaw/SemicircleDistribution.html#LeanPool.SemicircleLaw.semicirclePDFReal) (def), declared in [LeanPool/SemicircleLaw/SemicircleDistribution.lean, line 55](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SemicircleLaw/SemicircleDistribution.lean#L55): “Defines the real-valued density of the semicircle distribution with mean μ and variance v.”
- [`LeanPool.SemicircleLaw.semicirclePDF`](https://leanpool.github.io/lean-pool/LeanPool/SemicircleLaw/SemicircleDistribution.html#LeanPool.SemicircleLaw.semicirclePDF) (def), declared in [LeanPool/SemicircleLaw/SemicircleDistribution.lean, line 212](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SemicircleLaw/SemicircleDistribution.lean#L212): “Defines the ℝ≥0∞-valued density of the semicircle distribution.”
- [`LeanPool.SemicircleLaw.integral_semicirclePDFReal_eq_one`](https://leanpool.github.io/lean-pool/LeanPool/SemicircleLaw/SemicircleDistribution.html#LeanPool.SemicircleLaw.integral_semicirclePDFReal_eq_one) (lemma; a main declaration), declared in [LeanPool/SemicircleLaw/SemicircleDistribution.lean, line 181](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SemicircleLaw/SemicircleDistribution.lean#L181): “Proves that the real-valued semicircle density integrates to one for nonzero variance.”
- [`LeanPool.SemicircleLaw.semicircleReal`](https://leanpool.github.io/lean-pool/LeanPool/SemicircleLaw/SemicircleDistribution.html#LeanPool.SemicircleLaw.semicircleReal) (def), declared in [LeanPool/SemicircleLaw/SemicircleDistribution.lean, line 245](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SemicircleLaw/SemicircleDistribution.lean#L245): “Defines the semicircle measure on ℝ, equal to a Dirac mass when the variance is zero.”
- [`LeanPool.SemicircleLaw.semicircleReal_map_add_const`](https://leanpool.github.io/lean-pool/LeanPool/SemicircleLaw/SemicircleDistribution.html#LeanPool.SemicircleLaw.semicircleReal_map_add_const) (lemma), declared in [LeanPool/SemicircleLaw/SemicircleDistribution.lean, line 393](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SemicircleLaw/SemicircleDistribution.lean#L393): “Shows that translating a semicircle measure translates its mean parameter.”
- [`LeanPool.SemicircleLaw.semicircleReal_map_const_mul`](https://leanpool.github.io/lean-pool/LeanPool/SemicircleLaw/SemicircleDistribution.html#LeanPool.SemicircleLaw.semicircleReal_map_const_mul) (lemma), declared in [LeanPool/SemicircleLaw/SemicircleDistribution.lean, line 413](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SemicircleLaw/SemicircleDistribution.lean#L413): “Shows that scaling by a nonzero constant scales the mean and variance parameters.”
- [`LeanPool.SemicircleLaw.memLp_id_semicircleReal`](https://leanpool.github.io/lean-pool/LeanPool/SemicircleLaw/SemicircleDistribution.html#LeanPool.SemicircleLaw.memLp_id_semicircleReal) (lemma), declared in [LeanPool/SemicircleLaw/SemicircleDistribution.lean, line 548](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SemicircleLaw/SemicircleDistribution.lean#L548): “Shows that the identity has all finite Lp moments under a semicircle distribution.”

## Project

- Authors: FredRaj3.
- Source: [https://www.math.ucsd.edu/~tkemp/247A.Notes.pdf](https://www.math.ucsd.edu/~tkemp/247A.Notes.pdf).
- Project repository: [FredRaj3/SemicircleLaw](https://github.com/FredRaj3/SemicircleLaw).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0, keeping its copyright line: “Copyright (c) 2025 FredRaj3”.
- MSC2020: 60B20, 60E05.
- In Lean Pool: [LeanPool/SemicircleLaw](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SemicircleLaw), from the card [LeanPool/projects/semicirclelaw.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/semicirclelaw.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/semicirclelaw.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/semicirclelaw.yaml)
- [Lean Pool at 2b205bf9: LeanPool/SemicircleLaw](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SemicircleLaw)
