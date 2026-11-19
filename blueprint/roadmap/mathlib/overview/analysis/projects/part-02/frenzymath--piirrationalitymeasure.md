---
declaration: theorem
origin: cited
lean: PiIrrationality.candidate_admissible, PiIrrationality.IrrationalityMeasureAtMost.mono, PiIrrationality.candidate_coordinates, PiIrrationality.irrationalityMeasure_le_of_atMost, PiIrrationality.theorem11_of_atMost_bound, PiIrrationality.irrationalityMeasureAtMost_of_uniform_power_bound, PiIrrationality.rpow_neg_eventually_lt, PiIrrationality.irrationalityMeasureAtMost_of_uniform_power_bound_of_pos_constant
statement: formalized
proof: formalized
---

# Pi irrationality measure formalization

[frenzymath/PiIrrationalityMeasure](https://github.com/frenzymath/PiIrrationalityMeasure) at commit [3ee5d4d0](https://github.com/frenzymath/PiIrrationalityMeasure/tree/3ee5d4d080b440469d331a2fb3862aee88c23ca0), 2026-09-17.

> Lean 4.33.0 and mathlib `v4.33.0` formalization of the [paper](https://arxiv.org/abs/2609.11276).

*Quoted from [README.md](https://github.com/frenzymath/PiIrrationalityMeasure/blob/3ee5d4d080b440469d331a2fb3862aee88c23ca0/README.md), Apache-2.0.*

## Depends on

Its headline statements name no Mathlib concept or declaration mapped elsewhere on this site.

## Proof depends on

- [Characteristic function](../../../probability-theory/definitions-in-probability-theory/characteristic-function.md)
- [Bernoulli numbers](../../../general-algebra/number-theory/bernoulli-numbers.md)
- [Fourier transform as an integral](../../fourier-analysis/fourier-transform-as-an-integral.md)
- [Higher-order derivatives of functions](../../../../undergraduate/single-variable-real-analysis/differentiability/higher-order-derivatives-of-functions.md)
- [Continuity of the sum of a series of functions](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/continuity-of-the-sum-of-a-series-of-functions.md)
- [Subfield](../../../general-algebra/field-theory/subfield.md)
- [Extended real number](../../../general-algebra/numbers/extended-real-number.md)
- [Polynomial derivative](../../../../undergraduate/ring-theory/polynomial-rings/polynomial-derivative.md)

## Main results

Its Lean names are 8 of the 10 theorems of its top-level module named Main, MainTheorem(s) or Statement(s):

- [`PiIrrationality.candidate_admissible`](https://github.com/frenzymath/PiIrrationalityMeasure/blob/3ee5d4d080b440469d331a2fb3862aee88c23ca0/Formalization/Statements.lean#L51) (theorem)
- [`PiIrrationality.IrrationalityMeasureAtMost.mono`](https://github.com/frenzymath/PiIrrationalityMeasure/blob/3ee5d4d080b440469d331a2fb3862aee88c23ca0/Formalization/Statements.lean#L54) (theorem)
- [`PiIrrationality.candidate_coordinates`](https://github.com/frenzymath/PiIrrationalityMeasure/blob/3ee5d4d080b440469d331a2fb3862aee88c23ca0/Formalization/Statements.lean#L68) (theorem)
- [`PiIrrationality.irrationalityMeasure_le_of_atMost`](https://github.com/frenzymath/PiIrrationalityMeasure/blob/3ee5d4d080b440469d331a2fb3862aee88c23ca0/Formalization/Statements.lean#L71) (theorem)
- [`PiIrrationality.theorem11_of_atMost_bound`](https://github.com/frenzymath/PiIrrationalityMeasure/blob/3ee5d4d080b440469d331a2fb3862aee88c23ca0/Formalization/Statements.lean#L78) (theorem)
- [`PiIrrationality.irrationalityMeasureAtMost_of_uniform_power_bound`](https://github.com/frenzymath/PiIrrationalityMeasure/blob/3ee5d4d080b440469d331a2fb3862aee88c23ca0/Formalization/Statements.lean#L86) (theorem)
- [`PiIrrationality.rpow_neg_eventually_lt`](https://github.com/frenzymath/PiIrrationalityMeasure/blob/3ee5d4d080b440469d331a2fb3862aee88c23ca0/Formalization/Statements.lean#L117) (theorem)
- [`PiIrrationality.irrationalityMeasureAtMost_of_uniform_power_bound_of_pos_constant`](https://github.com/frenzymath/PiIrrationalityMeasure/blob/3ee5d4d080b440469d331a2fb3862aee88c23ca0/Formalization/Statements.lean#L129) (theorem)

No file its headlines import, directly or not (1 file), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.33.0, Mathlib at [db584cd6](https://github.com/leanprover-community/mathlib4/tree/db584cd6d46c92f209a44c0f1c829460d327499d).
- 312 .lean files; its Lean libraries `Formalization`, `Challenge`, `Solution` hold 312, declaring 2,922 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: failing.
- License: Apache-2.0 ([LICENSE](https://github.com/frenzymath/PiIrrationalityMeasure/blob/3ee5d4d080b440469d331a2fb3862aee88c23ca0/LICENSE)).

## Builds on

- Mathlib, at [db584cd6](https://github.com/leanprover-community/mathlib4/tree/db584cd6d46c92f209a44c0f1c829460d327499d).

## Placement

Of its imports of Mathlib modules in an overview area, 27 of 53 are in Analysis, 1.9 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (27 of 53 imports, 1.9×), Topology (7 of 53 imports, 1.8×), General algebra (16 of 53 imports, 0.8×). *Proof depends on* lists 8 of the 59 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [frenzymath/PiIrrationalityMeasure at 3ee5d4d0](https://github.com/frenzymath/PiIrrationalityMeasure/tree/3ee5d4d080b440469d331a2fb3862aee88c23ca0)
