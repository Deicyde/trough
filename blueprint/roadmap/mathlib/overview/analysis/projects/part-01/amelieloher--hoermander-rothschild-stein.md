---
declaration: theorem
origin: cited
lean: Hormander.Interface.exists_smooth_aeRepresentative, Hormander.subelliptic_estimate, Hormander.forall_memSobolev_of_localized, Hormander.memSobolev_neg_of_integrable, Hormander.exists_contDiff_of_forall_memSobolev, RothschildStein.rs3_no_drift_sobolev, RothschildStein.rs3_no_drift_holder, RothschildStein.rs3_drift_sobolev
statement: formalized
proof: formalized
---

# Hörmander's theorem and the Rothschild–Stein theory, formalized in Lean 4

[amelieloher/hoermander-rothschild-stein](https://github.com/amelieloher/hoermander-rothschild-stein) at commit [f589d78f](https://github.com/amelieloher/hoermander-rothschild-stein/tree/f589d78f15df6f0ee8776390eeb5b29a868421d9), 2026-10-10.

## Depends on

- [Set](../../../data-structures/sets/set.md)
- [$C^k$ function](../../differentiability/c-k-function.md)
- [Compactness in terms of filters](../../../topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Linear independence](../../../../undergraduate/linear-algebra/fundamentals/linear-independence.md)
- [Differentials (linear tangent functions)](../../../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [42.8 Cycles](../../../../../stacks/topics-in-scheme-theory/part-01/42-chow-homology/part-01/42-8-cycles.md)
- [Multiplication by a function $C^\infty$ of slow growth](../../../../undergraduate/distribution-calculus/tempered-distributions/multiplication-by-a-function-c-infty-of-slow-gro.md)
- [Vector-valued integrable function (Bochner integral)](../../measures-and-integral-calculus/part-01/vector-valued-integrable-function-bochner-integr.md)
- [Distributions](../../distribution-theory/distributions.md)
- [Closure](../../../topology/general-topology/part-01/closure.md)

## Proof depends on

- [Limit infimum and supremum](../../../topology/topological-algebra/limit-infimum-and-supremum.md)
- [Test functions](../../distribution-theory/test-functions.md)
- [Convolution of two functions of $\mathcal{S}(\R^d)$](../../../../undergraduate/distribution-calculus/spaces-s-r-d/convolution-of-two-functions-of-s-r-d.md)
- [Lie algebra](../../../general-algebra/algebras-over-a-ring/lie-algebra.md)
- [Taylor's theorem with integral form for remainder (Differential calculus)](../../../../undergraduate/multivariable-calculus/differential-calculus/taylors-theorem-with-integral-form-for-remainder.md)
- [Uniform convergence](../../../topology/uniform-notions/uniform-convergence.md)
- [Fourier transforms on $\mathcal{S}(\R^d)$](../../../../undergraduate/distribution-calculus/spaces-s-r-d/fourier-transforms-on-s-r-d.md)
- [Inverse Fourier transform](../../../../undergraduate/distribution-calculus/tempered-distributions/inverse-fourier-transform.md)

## Main results

Its Lean names are 8 of the 27 theorems its README names in code:

- [`Hormander.Interface.exists_smooth_aeRepresentative`](https://github.com/amelieloher/hoermander-rothschild-stein/blob/f589d78f15df6f0ee8776390eeb5b29a868421d9/Hormander/Interface.lean#L32) (theorem)
- [`Hormander.subelliptic_estimate`](https://github.com/amelieloher/hoermander-rothschild-stein/blob/f589d78f15df6f0ee8776390eeb5b29a868421d9/Hormander/Statements/SubellipticEstimate.lean#L26) (theorem)
- [`Hormander.forall_memSobolev_of_localized`](https://github.com/amelieloher/hoermander-rothschild-stein/blob/f589d78f15df6f0ee8776390eeb5b29a868421d9/Hormander/Statements/LocalRegularity.lean#L24) (theorem)
- [`Hormander.memSobolev_neg_of_integrable`](https://github.com/amelieloher/hoermander-rothschild-stein/blob/f589d78f15df6f0ee8776390eeb5b29a868421d9/Hormander/Statements/MemSobolevOfIntegrable.lean#L19) (theorem)
- [`Hormander.exists_contDiff_of_forall_memSobolev`](https://github.com/amelieloher/hoermander-rothschild-stein/blob/f589d78f15df6f0ee8776390eeb5b29a868421d9/Hormander/Statements/ExistsContDiffOfMemSobolev.lean#L19) (theorem)
- [`RothschildStein.rs3_no_drift_sobolev`](https://github.com/amelieloher/hoermander-rothschild-stein/blob/f589d78f15df6f0ee8776390eeb5b29a868421d9/RothschildStein/Statements/rs3_no_drift_sobolev.lean#L35) (theorem)
- [`RothschildStein.rs3_no_drift_holder`](https://github.com/amelieloher/hoermander-rothschild-stein/blob/f589d78f15df6f0ee8776390eeb5b29a868421d9/RothschildStein/Statements/rs3_no_drift_holder.lean#L37) (theorem)
- [`RothschildStein.rs3_drift_sobolev`](https://github.com/amelieloher/hoermander-rothschild-stein/blob/f589d78f15df6f0ee8776390eeb5b29a868421d9/RothschildStein/Statements/rs3_drift_sobolev.lean#L35) (theorem)

No file its headlines import, directly or not (2913 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0-rc2, Mathlib at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).
- 4,774 .lean files; its Lean libraries `Hormander`, `RothschildStein`, `HeatKernel`, `HormanderChallenge`, `HormanderSolution`, `RothschildSteinChallenge` and 3 more hold 4,774, declaring 12,677 names, with `sorry` in 3 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/amelieloher/hoermander-rothschild-stein/blob/f589d78f15df6f0ee8776390eeb5b29a868421d9/LICENSE)).

## Builds on

- Mathlib, at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).

## Placement

5 of the 9 Mathlib concepts its headline statements name are in Analysis.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (1696 of 2436 imports, 2.6×), Topology (275 of 2436 imports, 1.5×), General algebra (253 of 2436 imports, 0.3×). *Proof depends on* names 8 of the 110 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [amelieloher/hoermander-rothschild-stein at f589d78f](https://github.com/amelieloher/hoermander-rothschild-stein/tree/f589d78f15df6f0ee8776390eeb5b29a868421d9)
