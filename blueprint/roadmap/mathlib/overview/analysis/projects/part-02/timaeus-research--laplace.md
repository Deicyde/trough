---
declaration: theorem
origin: cited
lean: Laplace.Multi.gibbsCov_first_order_rate_weak, Laplace.Multi.gibbsCov_first_order_rate_sharp, Laplace.Multi.gibbsExpectation_first_order_rate_explicit, Laplace.Multi.gibbsCov_first_order_rate_explicit, Laplace.Sampler.spectral_real, Laplace.Patterning.stein_invDir, Laplace.Patterning.isBrownianVec_of_iIndepFun, Laplace.Patterning.isBrownianVec_of_isBrownianReal
statement: formalized
proof: formalized
---

# laplace

[timaeus-research/laplace](https://github.com/timaeus-research/laplace) at commit [7b7fb68f](https://github.com/timaeus-research/laplace/tree/7b7fb68fc43566becaa44aae008103d536bf47a6), 2026-09-28.

## Depends on

- [Ring-valued matrix](../../../linear-algebra/matrices/ring-valued-matrix.md)
- [$C^k$ function](../../differentiability/c-k-function.md)
- [Differentials (linear tangent functions)](../../../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Independence of random variables](../../../probability-theory/random-variables-and-their-laws/independence-of-random-variables.md)

## Proof depends on

- [Taylor's theorem with Lagrange form for remainder](../../../../undergraduate/single-variable-real-analysis/taylor-like-theorems/taylors-theorem-with-lagrange-form-for-remainder.md)
- [Change of variables to polar co-ordinates](../../../../undergraduate/measures-and-integral-calculus/integration/change-of-variables-to-polar-co-ordinates.md)
- [Partial derivatives commute](../../../../undergraduate/multivariable-calculus/differential-calculus/partial-derivatives-commute.md)
- [Characterization of convexity](../../convexity/characterization-of-convexity.md)
- [Krein–Milman theorem](../../../../thousand-plus/geometry-and-topology/52-convex-and-discrete-geometry/krein-milman-theorem.md)
- [Convex hull of a subset of an affine real space](../../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-hull-of-a-subset-of-an-affine-real-space.md)
- [Affine span](../../../geometry/affine-and-euclidean-geometry/affine-span.md)
- [Probability measure](../../../probability-theory/definitions-in-probability-theory/probability-measure.md)

## Main results

Its Lean names are 8 of the 19 theorems its README names in code:

- [`Laplace.Multi.gibbsCov_first_order_rate_weak`](https://github.com/timaeus-research/laplace/blob/7b7fb68fc43566becaa44aae008103d536bf47a6/Laplace/Multi/Covariance.lean#L3788) (theorem)
- [`Laplace.Multi.gibbsCov_first_order_rate_sharp`](https://github.com/timaeus-research/laplace/blob/7b7fb68fc43566becaa44aae008103d536bf47a6/Laplace/Multi/CovarianceSharp.lean#L3979) (theorem)
- [`Laplace.Multi.gibbsExpectation_first_order_rate_explicit`](https://github.com/timaeus-research/laplace/blob/7b7fb68fc43566becaa44aae008103d536bf47a6/Laplace/Multi/CovarianceExplicit.lean#L8425) (theorem)
- [`Laplace.Multi.gibbsCov_first_order_rate_explicit`](https://github.com/timaeus-research/laplace/blob/7b7fb68fc43566becaa44aae008103d536bf47a6/Laplace/Multi/CovarianceExplicit.lean#L19180) (theorem)
- [`Laplace.Sampler.spectral_real`](https://github.com/timaeus-research/laplace/blob/7b7fb68fc43566becaa44aae008103d536bf47a6/Laplace/Sampler/Lyapunov.lean#L172) (theorem)
- [`Laplace.Patterning.stein_invDir`](https://github.com/timaeus-research/laplace/blob/7b7fb68fc43566becaa44aae008103d536bf47a6/Laplace/Patterning/GaussianFourth.lean#L75) (theorem)
- [`Laplace.Patterning.isBrownianVec_of_iIndepFun`](https://github.com/timaeus-research/laplace/blob/7b7fb68fc43566becaa44aae008103d536bf47a6/Laplace/Patterning/BrownianVecInstances.lean#L61) (theorem)
- [`Laplace.Patterning.isBrownianVec_of_isBrownianReal`](https://github.com/timaeus-research/laplace/blob/7b7fb68fc43566becaa44aae008103d536bf47a6/Laplace/Patterning/BrownianVecInstances.lean#L91) (theorem)

No file its headlines import, directly or not (75 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.33.0, Mathlib at [db584cd6](https://github.com/leanprover-community/mathlib4/tree/db584cd6d46c92f209a44c0f1c829460d327499d).
- 1,063 .lean files; its Lean libraries `Laplace`, `Statements`, `Solutions` hold 1,063, declaring 13,069 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- No license file; facts only.

## Builds on

- Mathlib, at [db584cd6](https://github.com/leanprover-community/mathlib4/tree/db584cd6d46c92f209a44c0f1c829460d327499d).
- `Threepoint` (https://github.com/timaeus-research/threepoint) at `d50ba79f`.
- `«resolution-common»` (https://github.com/timaeus-research/lean-common.git) at `3b06611e`.

## Placement

Of its imports of Mathlib modules in an overview area, 99 of 144 are in Analysis, 2.5 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (99 of 144 imports, 2.5×), General algebra (21 of 144 imports, 0.4×). *Proof depends on* lists 8 of the 105 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [timaeus-research/laplace at 7b7fb68f](https://github.com/timaeus-research/laplace/tree/7b7fb68fc43566becaa44aae008103d536bf47a6)
