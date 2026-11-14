---
declaration: theorem
origin: cited
lean: ElevenTwelfths.outsideM_eq_idealRowSum, ElevenTwelfths.outsideS_eq_idealRowSum_tsum, OAI.InitialMeanSquare.outside_mean_square_of_theta_models_pos, ElevenTwelfths.outside_totient_moebius_bound_of_mean_square, ElevenTwelfths.actual_smoothedWeightedMobiusBound
statement: formalized
proof: formalized
---

# Quasi-RH at 11/12

[AlexKontorovich/quasi-rh](https://github.com/AlexKontorovich/quasi-rh) at commit [d26d846d](https://github.com/AlexKontorovich/quasi-rh/tree/d26d846d6f3129017f06b6fd3f78dd72d361d60b), 2026-10-26.

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Ideal of a commutative ring](../../general-algebra/ideals-and-quotients/ideal-of-a-commutative-ring.md)
- [$C^k$ function](../differentiability/c-k-function.md)
- [Prime numbers](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)

## Proof depends on

- [Smooth map between manifolds](../../geometry/differentiable-manifolds/part-01/smooth-map-between-manifolds.md)
- [Fourier transforms](../../../undergraduate/distribution-calculus/tempered-distributions/fourier-transforms.md)
- [Smooth or analytic manifold (with boundary and corners)](../../geometry/differentiable-manifolds/part-01/smooth-or-analytic-manifold-with-boundary-and-co.md)
- [Normal endomorphism](../../../undergraduate/bilinear-and-quadratic-forms-over-a-vector-space/endomorphisms/normal-endomorphism.md)
- [$L^p$ functions](../../../undergraduate/distribution-calculus/tempered-distributions/l-p-functions.md)
- [Stability by multiplication by a slowly growing smooth function](../../../undergraduate/distribution-calculus/spaces-s-r-d/stability-by-multiplication-by-a-slowly-growing.md)
- [Poisson’s formula](../../../undergraduate/distribution-calculus/applications/poissons-formula.md)
- [Tempered distributions](../distribution-theory/tempered-distributions.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`ElevenTwelfths.outsideM_eq_idealRowSum`](https://github.com/AlexKontorovich/quasi-rh/blob/d26d846d6f3129017f06b6fd3f78dd72d361d60b/ElevenTwelfths/ConcreteFamily.lean#L111) (theorem)
- [`ElevenTwelfths.outsideS_eq_idealRowSum_tsum`](https://github.com/AlexKontorovich/quasi-rh/blob/d26d846d6f3129017f06b6fd3f78dd72d361d60b/ElevenTwelfths/ConcreteFamily.lean#L180) (theorem)
- [`OAI.InitialMeanSquare.outside_mean_square_of_theta_models_pos`](https://github.com/AlexKontorovich/quasi-rh/blob/d26d846d6f3129017f06b6fd3f78dd72d361d60b/OAI/NumberTheory/DirichletL/MeanSquare/ThetaDensity.lean#L274) (theorem)
- [`ElevenTwelfths.outside_totient_moebius_bound_of_mean_square`](https://github.com/AlexKontorovich/quasi-rh/blob/d26d846d6f3129017f06b6fd3f78dd72d361d60b/ElevenTwelfths/SixthPowerMeanSquare.lean#L42) (theorem)
- [`ElevenTwelfths.actual_smoothedWeightedMobiusBound`](https://github.com/AlexKontorovich/quasi-rh/blob/d26d846d6f3129017f06b6fd3f78dd72d361d60b/ElevenTwelfths/Unconditional.lean#L106) (theorem)

No file its headlines import, directly or not (295 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.34.1, Mathlib at [d13f23b7](https://github.com/leanprover-community/mathlib4/tree/d13f23b723b8a846827a245b89c10fc7d3f11612).
- 306 .lean files; its Lean libraries `OAI`, `ElevenTwelfths` hold 305, declaring 11,164 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/AlexKontorovich/quasi-rh/blob/d26d846d6f3129017f06b6fd3f78dd72d361d60b/LICENSE)).

## Builds on

- Mathlib, at [d13f23b7](https://github.com/leanprover-community/mathlib4/tree/d13f23b723b8a846827a245b89c10fc7d3f11612).
- `«rellich-kondrachov»` (https://github.com/abenenson/rellich-kondrachov.git) at `70f85d4c`.

## Placement

Of its imports of Mathlib modules in an overview area, 100 of 188 are in Analysis, 1.6 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (100 of 188 imports, 1.6×), General algebra (59 of 188 imports, 0.9×). *Proof depends on* names 8 of the 95 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [AlexKontorovich/quasi-rh at d26d846d](https://github.com/AlexKontorovich/quasi-rh/tree/d26d846d6f3129017f06b6fd3f78dd72d361d60b)
