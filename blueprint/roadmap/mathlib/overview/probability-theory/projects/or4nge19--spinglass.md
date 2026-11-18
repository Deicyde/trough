---
declaration: theorem
origin: cited
lean: SpinGlass.tendsto_skFreeEnergy, SpinGlass.exists_asymptoticGibbsMeasure, SpinGlass.exists_asymptoticOverlapArray, SpinGlass.intervalIntegral_skTotalEnergy_fluctuation_le, SpinGlass.exists_beta_abs_skGhirlandaGuerra_error_le, SpinGlass.FiniteGibbs.gibbs_average_n_det_mul_sum_gibbs_pmf, SpinGlass.integral_overlapArrayLaw_comp_take, SpinGlass.ghirlandaGuerraCombination_eq_overlapArrayLaw
statement: formalized
proof: formalized
---

# SpinGlass

[or4nge19/SpinGlass](https://github.com/or4nge19/SpinGlass) at commit [dc1d3820](https://github.com/or4nge19/SpinGlass/tree/dc1d3820af6e443c09bd1177ec3e409cf0640d5c), 2026-09-12.

> Lean 4 formalization of Talagrand, *Mean Field Models for Spin Glasses*, Vol. I–II.

*Quoted from [README.md](https://github.com/or4nge19/SpinGlass/blob/dc1d3820af6e443c09bd1177ec3e409cf0640d5c/README.md), Apache-2.0.*

## Depends on

- [Limit of a map with respect to filters](../../topology/general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)
- [Probability measure](../definitions-in-probability-theory/probability-measure.md)
- [Positive measure](../../analysis/measures-and-integral-calculus/part-01/positive-measure.md)
- [Measurable function](../../analysis/measures-and-integral-calculus/part-01/measurable-function.md)

## Proof depends on

- [Weierstrass polynomial approximation theorem](../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/weierstrass-polynomial-approximation-theorem.md)
- [Fernique's theorem](../../../thousand-plus/analysis/28-measure-and-integration/ferniques-theorem.md)
- [Gaussian measures](../random-variables-and-their-laws/gaussian-measures.md)
- [Poisson law](../random-variables-and-their-laws/poisson-law.md)
- [Chebyshev inequality](../convergence-of-a-sequence-of-random-variables/chebyshev-inequality.md)
- [Dual of a normed space](../../analysis/normed-vector-spaces-banach-spaces/dual-of-a-normed-space.md)
- [Lebesgue measure (Measure theory)](../../../undergraduate/measures-and-integral-calculus/measure-theory/lebesgue-measure.md)
- [Gaussian law](../random-variables-and-their-laws/gaussian-law.md)

## Main results

Its Lean names are 8 of the 101 theorems its README names in code:

- [`SpinGlass.tendsto_skFreeEnergy`](https://github.com/or4nge19/SpinGlass/blob/dc1d3820af6e443c09bd1177ec3e409cf0640d5c/SpinGlass/ThermodynamicLimit.lean#L424) (theorem)
- [`SpinGlass.exists_asymptoticGibbsMeasure`](https://github.com/or4nge19/SpinGlass/blob/dc1d3820af6e443c09bd1177ec3e409cf0640d5c/SpinGlass/Limit/AsymptoticGibbs.lean#L194) (theorem)
- [`SpinGlass.exists_asymptoticOverlapArray`](https://github.com/or4nge19/SpinGlass/blob/dc1d3820af6e443c09bd1177ec3e409cf0640d5c/SpinGlass/Limit/OverlapArray.lean#L274) (theorem)
- [`SpinGlass.intervalIntegral_skTotalEnergy_fluctuation_le`](https://github.com/or4nge19/SpinGlass/blob/dc1d3820af6e443c09bd1177ec3e409cf0640d5c/SpinGlass/FreeEnergyConvexity.lean#L608) (theorem)
- [`SpinGlass.exists_beta_abs_skGhirlandaGuerra_error_le`](https://github.com/or4nge19/SpinGlass/blob/dc1d3820af6e443c09bd1177ec3e409cf0640d5c/SpinGlass/SKGhirlandaGuerra.lean#L78) (theorem)
- [`SpinGlass.FiniteGibbs.gibbs_average_n_det_mul_sum_gibbs_pmf`](https://github.com/or4nge19/SpinGlass/blob/dc1d3820af6e443c09bd1177ec3e409cf0640d5c/SpinGlass/FiniteGibbs/ReplicaMeasure.lean#L150) (theorem)
- [`SpinGlass.integral_overlapArrayLaw_comp_take`](https://github.com/or4nge19/SpinGlass/blob/dc1d3820af6e443c09bd1177ec3e409cf0640d5c/SpinGlass/Limit/OverlapArrayBracket.lean#L75) (theorem)
- [`SpinGlass.ghirlandaGuerraCombination_eq_overlapArrayLaw`](https://github.com/or4nge19/SpinGlass/blob/dc1d3820af6e443c09bd1177ec3e409cf0640d5c/SpinGlass/Limit/GhirlandaGuerraFinite.lean#L229) (theorem)

No file its headlines import, directly or not (93 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.34.0-rc2, Mathlib at [85e3a25e](https://github.com/leanprover-community/mathlib4/tree/85e3a25e006c35636f0e53b0e9296caca2685bc0).
- 218 .lean files; its Lean libraries `SpinGlass`, `Common` hold 218, declaring 3,113 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/or4nge19/SpinGlass/blob/dc1d3820af6e443c09bd1177ec3e409cf0640d5c/LICENSE)).

## Builds on

- Mathlib, at [85e3a25e](https://github.com/leanprover-community/mathlib4/tree/85e3a25e006c35636f0e53b0e9296caca2685bc0).
- `GibbsMeasure` (https://github.com/matteo-ax/GibbsMeasure.git) at `8a158f01`.

## Placement

Of its imports of Mathlib modules in an overview area, 57 of 261 are in Probability Theory, 11.5 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Probability Theory (57 of 261 imports, 11.5×), Analysis (169 of 261 imports, 2.4×). *Proof depends on* names 8 of the 77 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [or4nge19/SpinGlass at dc1d3820](https://github.com/or4nge19/SpinGlass/tree/dc1d3820af6e443c09bd1177ec3e409cf0640d5c)
