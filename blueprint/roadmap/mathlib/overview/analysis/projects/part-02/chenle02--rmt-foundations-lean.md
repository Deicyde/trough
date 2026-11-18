---
declaration: theorem
origin: cited
lean: RMTFoundations.TracyWidom.strictMono_TW1R, RMTFoundations.TracyWidom.TW1Measure_unique, RMTFoundations.TracyWidom.TW2_rightTail_isEquivalent, RMTFoundations.TracyWidom.Painleve.TW2R_integral_formula, RMTFoundations.TracyWidom.HastingsMcLeod.exists_unique, RMTFoundations.TracyWidom.HastingsMcLeod.eq_canonical, RMTFoundations.TracyWidom.TW4R_positive, RMTFoundations.TracyWidom.TW4AiryR_eq_sqrt_TW2R_cosh_tail
statement: formalized
proof: formalized
---

# rmt-foundations

[chenle02/rmt-foundations-lean](https://github.com/chenle02/rmt-foundations-lean) at commit [af3b6edb](https://github.com/chenle02/rmt-foundations-lean/tree/af3b6edb57330747982dba2e2565d102a56613cb), 2026-10-26.

> Tracy–Widom distributions, Airy and Painlevé II theory, finite GUE identities and analytic random-matrix tools, formalized in Lean 4.

*Quoted from [README.md](https://github.com/chenle02/rmt-foundations-lean/blob/af3b6edb57330747982dba2e2565d102a56613cb/README.md), Apache-2.0.*

## Depends on

- [Probability measure](../../../probability-theory/definitions-in-probability-theory/probability-measure.md)
- [Positive measure](../../measures-and-integral-calculus/part-01/positive-measure.md)
- [Exponential](../../special-functions/exponential.md)
- [Differentiable functions](../../../../undergraduate/multivariable-calculus/differential-calculus/differentiable-functions.md)
- [Limit of a map with respect to filters](../../../topology/general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)
- [Derivative at a point](../../../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)

## Proof depends on

- [Sylvester's determinant theorem](../../../../thousand-plus/algebra/15-linear-and-multilinear-algebra-matrix-theory/sylvesters-determinant-theorem.md)
- [Inversion formula](../../fourier-analysis/inversion-formula.md)
- [The Mean Value Theorem (Freek Wiedijk's 100 theorems)](../../../../hundred-theorems/part-03/the-mean-value-theorem.md)
- [Counting measure](../../../../undergraduate/measures-and-integral-calculus/measure-theory/counting-measure.md)
- [Hilbert bases](../../../../undergraduate/topology/hilbert-spaces/hilbert-bases.md)
- [Existence of Hilbert basis](../../hilbert-spaces/existence-of-hilbert-basis.md)
- [Tempered distributions](../../distribution-theory/tempered-distributions.md)
- [Continuity of the sum of a series of functions](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/continuity-of-the-sum-of-a-series-of-functions.md)

## Main results

Its Lean names are 8 of the 12 theorems its README names in code:

- [`RMTFoundations.TracyWidom.strictMono_TW1R`](https://github.com/chenle02/rmt-foundations-lean/blob/af3b6edb57330747982dba2e2565d102a56613cb/RMTFoundations/TracyWidom/Regularity.lean#L16) (theorem)
- [`RMTFoundations.TracyWidom.TW1Measure_unique`](https://github.com/chenle02/rmt-foundations-lean/blob/af3b6edb57330747982dba2e2565d102a56613cb/RMTFoundations/TracyWidom/Probability.lean#L64) (theorem)
- [`RMTFoundations.TracyWidom.TW2_rightTail_isEquivalent`](https://github.com/chenle02/rmt-foundations-lean/blob/af3b6edb57330747982dba2e2565d102a56613cb/RMTFoundations/TracyWidom/TW2RightTail.lean#L14) (theorem)
- [`RMTFoundations.TracyWidom.Painleve.TW2R_integral_formula`](https://github.com/chenle02/rmt-foundations-lean/blob/af3b6edb57330747982dba2e2565d102a56613cb/RMTFoundations/TracyWidom/Painleve.lean#L39) (theorem)
- [`RMTFoundations.TracyWidom.HastingsMcLeod.exists_unique`](https://github.com/chenle02/rmt-foundations-lean/blob/af3b6edb57330747982dba2e2565d102a56613cb/RMTFoundations/TracyWidom/HastingsMcLeod.lean#L33) (theorem)
- [`RMTFoundations.TracyWidom.HastingsMcLeod.eq_canonical`](https://github.com/chenle02/rmt-foundations-lean/blob/af3b6edb57330747982dba2e2565d102a56613cb/RMTFoundations/TracyWidom/HastingsMcLeod.lean#L25) (theorem)
- [`RMTFoundations.TracyWidom.TW4R_positive`](https://github.com/chenle02/rmt-foundations-lean/blob/af3b6edb57330747982dba2e2565d102a56613cb/RMTFoundations/TracyWidom/OrderFourFredholm.lean#L28) (theorem)
- [`RMTFoundations.TracyWidom.TW4AiryR_eq_sqrt_TW2R_cosh_tail`](https://github.com/chenle02/rmt-foundations-lean/blob/af3b6edb57330747982dba2e2565d102a56613cb/RMTFoundations/TracyWidom/TW4IntegralFormula.lean#L44) (theorem)

No file its headlines import, directly or not (80 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 369 .lean files; its Lean libraries `RMTFoundations`, `Tests`, `Challenge`, `Solution` hold 360, declaring 2,229 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/chenle02/rmt-foundations-lean/blob/af3b6edb57330747982dba2e2565d102a56613cb/LICENSE)).

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).

## Placement

4 of the 6 Mathlib concepts its headline statements name are in Analysis.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (143 of 207 imports, 2.5×), Linear algebra (22 of 207 imports, 1.8×). *Proof depends on* names 8 of the 91 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [chenle02/rmt-foundations-lean at af3b6edb](https://github.com/chenle02/rmt-foundations-lean/tree/af3b6edb57330747982dba2e2565d102a56613cb)
