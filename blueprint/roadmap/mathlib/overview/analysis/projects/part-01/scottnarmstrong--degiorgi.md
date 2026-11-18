---
declaration: theorem
origin: cited
lean: DeGiorgi.linfty_subsolution_DeGiorgi_normalized, DeGiorgi.weak_harnack, DeGiorgi.weak_harnack_on_ball, DeGiorgi.harnack, DeGiorgi.harnack_of_homogeneousWeakSolution, DeGiorgi.holder_Moser, DeGiorgi.holder_Moser_of_homogeneousWeakSolution
statement: formalized
proof: formalized
---

# DeGiorgi

[scottnarmstrong/DeGiorgi](https://github.com/scottnarmstrong/DeGiorgi) at commit [4c1b3077](https://github.com/scottnarmstrong/DeGiorgi/tree/4c1b3077d3782b24065184df4ba59501b2e56fc7), 2026-04-08.

> A large-scale Lean 4 formalization of elliptic De Giorgi-Nash-Moser theory, built on top of Mathlib.

*Quoted from [README.md](https://github.com/scottnarmstrong/DeGiorgi/blob/4c1b3077d3782b24065184df4ba59501b2e56fc7/README.md), Apache-2.0.*

## Depends on

- [Ball](../../../topology/metric-spaces/ball.md)
- [9.7 Finite extensions](../../../../../stacks/preliminaries/part-01/9-fields/part-01/9-7-finite-extensions.md)
- [Exponential](../../special-functions/exponential.md)

## Proof depends on

- [Lax-Milgram theorem](../../hilbert-spaces/lax-milgram-theorem.md)
- [Antiderivative of a continuous function](../../../../undergraduate/single-variable-real-analysis/integration/antiderivative-of-a-continuous-function.md)
- [Directional derivative](../../../../undergraduate/multivariable-calculus/differential-calculus/directional-derivative.md)
- [Fréchet-Riesz representation of the dual of a Hilbert space](../../hilbert-spaces/frechet-riesz-representation-of-the-dual-of-a-hi.md)
- [Almost sure convergence](../../../probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Pointwise convergence](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
- [Dominated convergence theorem](../../measures-and-integral-calculus/part-01/dominated-convergence-theorem.md)
- [Invertibility](../../../linear-algebra/matrices/invertibility.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`DeGiorgi.linfty_subsolution_DeGiorgi_normalized`](https://github.com/scottnarmstrong/DeGiorgi/blob/4c1b3077d3782b24065184df4ba59501b2e56fc7/DeGiorgi/DeGiorgiIteration/Linfty.lean#L1347) (theorem)
- [`DeGiorgi.weak_harnack`](https://github.com/scottnarmstrong/DeGiorgi/blob/4c1b3077d3782b24065184df4ba59501b2e56fc7/DeGiorgi/WeakHarnack.lean#L1780) (theorem)
- [`DeGiorgi.weak_harnack_on_ball`](https://github.com/scottnarmstrong/DeGiorgi/blob/4c1b3077d3782b24065184df4ba59501b2e56fc7/DeGiorgi/ScaledBallEstimates.lean#L291) (theorem)
- [`DeGiorgi.harnack`](https://github.com/scottnarmstrong/DeGiorgi/blob/4c1b3077d3782b24065184df4ba59501b2e56fc7/DeGiorgi/Harnack.lean#L988) (theorem)
- [`DeGiorgi.harnack_of_homogeneousWeakSolution`](https://github.com/scottnarmstrong/DeGiorgi/blob/4c1b3077d3782b24065184df4ba59501b2e56fc7/DeGiorgi/Harnack.lean#L1153) (theorem)
- [`DeGiorgi.holder_Moser`](https://github.com/scottnarmstrong/DeGiorgi/blob/4c1b3077d3782b24065184df4ba59501b2e56fc7/DeGiorgi/Holder/PublicEstimate.lean#L21) (theorem)
- [`DeGiorgi.holder_Moser_of_homogeneousWeakSolution`](https://github.com/scottnarmstrong/DeGiorgi/blob/4c1b3077d3782b24065184df4ba59501b2e56fc7/DeGiorgi/Holder/PublicEstimate.lean#L60) (theorem)

No file its headlines import, directly or not (89 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.29.0-rc6, Mathlib at [5c8398df](https://github.com/leanprover-community/mathlib4/tree/5c8398df528176d9c87ccd9226ba8f7c8852d59c).
- 93 .lean files; its Lean libraries `DeGiorgi` hold 93, declaring 1,123 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/scottnarmstrong/DeGiorgi/blob/4c1b3077d3782b24065184df4ba59501b2e56fc7/LICENSE)).

## Builds on

- Mathlib, at [5c8398df](https://github.com/leanprover-community/mathlib4/tree/5c8398df528176d9c87ccd9226ba8f7c8852d59c).
- `REPL` (https://github.com/leanprover-community/repl) at `1d17a15a`.

## Placement

Of its imports of Mathlib modules in an overview area, 22 of 31 are in Analysis, 2.6 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (22 of 31 imports, 2.6×), Topology (6 of 31 imports, 2.6×). *Proof depends on* names 8 of the 47 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [scottnarmstrong/DeGiorgi at 4c1b3077](https://github.com/scottnarmstrong/DeGiorgi/tree/4c1b3077d3782b24065184df4ba59501b2e56fc7)
