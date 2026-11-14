---
declaration: theorem
origin: cited
lean: CertifiedGaps.GapGT.lt_sub_of_monotone, CertifiedGaps.one_sub_squaredPurity_le_squaringDefect, CertifiedGaps.gapGT_of_purities, CertifiedGaps.Spectral.eigCount_le_of_schur_LDL, CertifiedGaps.Spectral.sum_le_binned, CertifiedGaps.Spectral.binned_le_sum, CertifiedGaps.Spectral.antitone_exp_neg_mul, CertifiedGaps.SpinOneHeisenberg.ThermalPacked.seamBand
statement: formalized
---

# Certified Spectral Gaps of Quantum Spin Chains

[LionSR/CertifiedGaps](https://github.com/LionSR/CertifiedGaps) at commit [d00eca06](https://github.com/LionSR/CertifiedGaps/tree/d00eca060ecbaf0987d7f00e8b6c36ef4592d1c4), 2026-11-12.

## Depends on

- [Infinite sum](../../topology/topological-algebra/infinite-sum.md)
- [Logarithm](../../analysis/special-functions/logarithm.md)
- [Kernel of a linear map](../../../undergraduate/linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Range of a linear map](../../../undergraduate/linear-algebra/fundamentals/range-of-a-linear-map.md)
- [Ring-valued matrix](../matrices/ring-valued-matrix.md)
- [Finite set](../../data-structures/sets/finite-set.md)
- [Exponential](../../analysis/special-functions/exponential.md)

## Proof depends on

- [Invertibility](../matrices/invertibility.md)
- [Matrix exponential](../../../undergraduate/linear-algebra/exponential/matrix-exponential.md)
- [Complementary subspaces](../../../undergraduate/linear-algebra/fundamentals/complementary-subspaces.md)
- [Permutation group of a type](../../general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Normed vector space over a normed field](../../analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [List](../../data-structures/list-like-structures/list.md)
- [The Triangle Inequality](../../../hundred-theorems/part-04/the-triangle-inequality.md)
- [The Binomial Theorem](../../../hundred-theorems/part-02/the-binomial-theorem.md)

## Main results

Its Lean names are 8 of the 47 Lean names of the blueprint nodes that no other node uses, marked \leanok:

- [`CertifiedGaps.GapGT.lt_sub_of_monotone`](https://github.com/LionSR/CertifiedGaps/blob/d00eca060ecbaf0987d7f00e8b6c36ef4592d1c4/code/lean/CertifiedGaps/PurityCriterion.lean#L346) (theorem)
- [`CertifiedGaps.one_sub_squaredPurity_le_squaringDefect`](https://github.com/LionSR/CertifiedGaps/blob/d00eca060ecbaf0987d7f00e8b6c36ef4592d1c4/code/lean/CertifiedGaps/PurityCriterion.lean#L120) (theorem)
- [`CertifiedGaps.gapGT_of_purities`](https://github.com/LionSR/CertifiedGaps/blob/d00eca060ecbaf0987d7f00e8b6c36ef4592d1c4/code/lean/CertifiedGaps/PurityCriterion.lean#L886) (theorem)
- [`CertifiedGaps.Spectral.eigCount_le_of_schur_LDL`](https://github.com/LionSR/CertifiedGaps/blob/d00eca060ecbaf0987d7f00e8b6c36ef4592d1c4/code/lean/CertifiedGaps/Spectral/Schur.lean#L153) (theorem)
- [`CertifiedGaps.Spectral.sum_le_binned`](https://github.com/LionSR/CertifiedGaps/blob/d00eca060ecbaf0987d7f00e8b6c36ef4592d1c4/code/lean/CertifiedGaps/Spectral/TraceBounds.lean#L121) (theorem)
- [`CertifiedGaps.Spectral.binned_le_sum`](https://github.com/LionSR/CertifiedGaps/blob/d00eca060ecbaf0987d7f00e8b6c36ef4592d1c4/code/lean/CertifiedGaps/Spectral/TraceBounds.lean#L169) (theorem)
- [`CertifiedGaps.Spectral.antitone_exp_neg_mul`](https://github.com/LionSR/CertifiedGaps/blob/d00eca060ecbaf0987d7f00e8b6c36ef4592d1c4/code/lean/CertifiedGaps/Spectral/TraceBounds.lean#L194) (theorem)
- [`CertifiedGaps.SpinOneHeisenberg.ThermalPacked.seamBand`](https://github.com/LionSR/CertifiedGaps/blob/d00eca060ecbaf0987d7f00e8b6c36ef4592d1c4/code/lean/CertifiedGaps/Heisenberg/ThermalPacked.lean#L96) (def)

Of the files its headlines import, directly or not, `code/lean/CertifiedGaps/Heisenberg/Main.lean`, `code/lean/CertifiedGaps/Models/SpinOneLargeD.lean` hold `sorry` or `admit`.

## Project

- Lean v4.36.0-rc1, Mathlib at [807d3836](https://github.com/leanprover-community/mathlib4/tree/807d3836b165983210ee2ecf3cd28f239436949c).
- 205 .lean files; its Lean libraries `CertifiedGaps`, `SeedKernel`, `SeedKernelBench`, `SeedKernelEval`, `Leaderboard` hold 203, declaring 3,288 names, with `sorry` in 9 files and 0 axioms, read without Lean.
- Its own CI at this commit: failing.
- License files: `LICENSE`; facts only.

## Builds on

- Mathlib, at [807d3836](https://github.com/leanprover-community/mathlib4/tree/807d3836b165983210ee2ecf3cd28f239436949c).

## Placement

Of its imports of Mathlib modules in an overview area, 20 of 86 are in Linear algebra, 4.3 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Linear algebra (20 of 86 imports, 4.3×), Analysis (38 of 86 imports, 1.3×), Data structures (10 of 86 imports, 0.9×). *Proof depends on* names 8 of the 31 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [LionSR/CertifiedGaps at d00eca06](https://github.com/LionSR/CertifiedGaps/tree/d00eca060ecbaf0987d7f00e8b6c36ef4592d1c4)
