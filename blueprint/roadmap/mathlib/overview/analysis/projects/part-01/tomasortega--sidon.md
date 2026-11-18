---
declaration: theorem
origin: cited
lean: Sidon.largest_sidon_fourier_uniformity, Sidon.sidon_partition_regularity, empty_is_sidon, singleton_is_sidon, sidon_subset_is_sidon, sidon_set_size_bound_zmodn, IsSidonSet.card_le_two_mul_sqrt, Sidon.sidon_improved_fourier_discrepancy_sq_le
statement: formalized
proof: formalized
---

# Extremal Sidon sets

[TomasOrtega/Sidon](https://github.com/TomasOrtega/Sidon) at commit [735de6d7](https://github.com/TomasOrtega/Sidon/tree/735de6d7c67b81a28b1e07e3f2661dbc17bb89d6), 2026-10-28.

> A Lean formalization of Miquel Ortega and Sean Prendiville, [*Extremal Sidon sets are Fourier uniform, with applications to partition regularity*](https://arxiv.org/abs/2110.13447).

*Quoted from [README.md](https://github.com/TomasOrtega/Sidon/blob/735de6d7c67b81a28b1e07e3f2661dbc17bb89d6/README.md), Apache-2.0.*

## Depends on

- [Finite set](../../../data-structures/sets/finite-set.md)
- [Set](../../../data-structures/sets/set.md)

## Proof depends on

- [Hales-Jewett theorem](../../../combinatorics/ramsey-theory/hales-jewett-theorem.md)
- [Additive energy](../../../combinatorics/additive-combinatorics/additive-energy.md)
- [Sum of a Geometric Series](../../../../hundred-theorems/part-03/sum-of-a-geometric-series.md)
- [Strong pigeonhole principle](../../../combinatorics/pigeonhole-principles/strong-pigeonhole-principle.md)
- [Analyticity of holomorphic functions](../../complex-analysis/analyticity-of-holomorphic-functions.md)
- [Lebesgue measure (Measure theory)](../../../../undergraduate/measures-and-integral-calculus/measure-theory/lebesgue-measure.md)
- [Euler’s Summation of 1 + (1/2)^2 + (1/3)^2 + ….](../../../../hundred-theorems/part-01/eulers-summation-of-1-1-2-2-1-3-2.md)
- [Newton's identities](../../../../undergraduate/ring-theory/polynomial-rings/newtons-identities.md)

## Main results

Its Lean names are 8 of the 37 Lean names of the blueprint nodes that no other node uses, marked \leanok:

- [`Sidon.largest_sidon_fourier_uniformity`](https://github.com/TomasOrtega/Sidon/blob/735de6d7c67b81a28b1e07e3f2661dbc17bb89d6/Sidon/Constructions/MaximumUniformity.lean#L15) (theorem)
- [`Sidon.sidon_partition_regularity`](https://github.com/TomasOrtega/Sidon/blob/735de6d7c67b81a28b1e07e3f2661dbc17bb89d6/Sidon/PartitionRegularity.lean#L166) (theorem)
- [`empty_is_sidon`](https://github.com/TomasOrtega/Sidon/blob/735de6d7c67b81a28b1e07e3f2661dbc17bb89d6/Sidon/Basic.lean#L16) (theorem)
- [`singleton_is_sidon`](https://github.com/TomasOrtega/Sidon/blob/735de6d7c67b81a28b1e07e3f2661dbc17bb89d6/Sidon/Basic.lean#L22) (theorem)
- [`sidon_subset_is_sidon`](https://github.com/TomasOrtega/Sidon/blob/735de6d7c67b81a28b1e07e3f2661dbc17bb89d6/Sidon/Basic.lean#L28) (theorem)
- [`sidon_set_size_bound_zmodn`](https://github.com/TomasOrtega/Sidon/blob/735de6d7c67b81a28b1e07e3f2661dbc17bb89d6/Sidon/Basic.lean#L71) (theorem)
- [`IsSidonSet.card_le_two_mul_sqrt`](https://github.com/TomasOrtega/Sidon/blob/735de6d7c67b81a28b1e07e3f2661dbc17bb89d6/Sidon/Combinatorics/IntervalSize.lean#L16) (theorem)
- [`Sidon.sidon_improved_fourier_discrepancy_sq_le`](https://github.com/TomasOrtega/Sidon/blob/735de6d7c67b81a28b1e07e3f2661dbc17bb89d6/Sidon/ImprovedFourierUniformity.lean#L162) (theorem)

No file its headlines import, directly or not (386 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 433 .lean files; its Lean libraries `Sidon`, `Challenge`, `Solution` hold 431, declaring 3,339 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: failing.
- License: Apache-2.0 ([LICENSE](https://github.com/TomasOrtega/Sidon/blob/735de6d7c67b81a28b1e07e3f2661dbc17bb89d6/LICENSE)).

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).

## Placement

Of its imports of Mathlib modules in an overview area, 2064 of 3262 are in Analysis, 2.3 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (2064 of 3262 imports, 2.3×), General algebra (789 of 3262 imports, 0.7×). *Proof depends on* names 8 of the 72 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [TomasOrtega/Sidon at 735de6d7](https://github.com/TomasOrtega/Sidon/tree/735de6d7c67b81a28b1e07e3f2661dbc17bb89d6)
