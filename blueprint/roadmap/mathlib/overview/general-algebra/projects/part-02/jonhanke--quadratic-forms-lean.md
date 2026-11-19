---
declaration: theorem
origin: cited
lean: QuadFormsKB.ChenevierLannes.wittIgusa_of_cuspVanish, QuadFormsKB.Cassels.Ch11L92.tartakowskyClassicalAt_four_holds, QuadFormsKB.Lattices.omeara106_r38, QuadFormsKB.OMeara.omeara101_8a, QuadFormsKB.Tamagawa.Indefinite.finite_DC, QuadFormsKB.LocalDensity.NF.det_hessian_Qp
statement: formalized
proof: formalized
---

# Quadratic forms over number fields in Lean 4

[jonhanke/quadratic-forms-lean](https://github.com/jonhanke/quadratic-forms-lean) at commit [09d95130](https://github.com/jonhanke/quadratic-forms-lean/tree/09d95130b262a0fdd44d38275aab5e56dbea5ebd), 2026-11-17.

> A Lean 4 library (built on Mathlib v4.35.0) for the arithmetic theory of quadratic forms over number fields. The Lean library is called `QuadFormsKB`.

*Quoted from [README.md](https://github.com/jonhanke/quadratic-forms-lean/blob/09d95130b262a0fdd44d38275aab5e56dbea5ebd/README.md), Apache-2.0.*

## Depends on

- [Associative algebra over a commutative ring](../../algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Field](../../field-theory/field.md)
- [Finite-dimensionality](../../../linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Invertible elements](../../../../undergraduate/ring-theory/divisibility-in-integral-domains/invertible-elements.md)
- [Module](../../../linear-algebra/fundamentals/module.md)
- [9.7 Finite extensions](../../../../../stacks/preliminaries/part-01/9-fields/part-01/9-7-finite-extensions.md)
- [Quadratic form](../../../linear-algebra/bilinear-and-quadratic-forms/quadratic-form.md)
- [Rational fraction fields with one indeterminate over a field](../../../../undergraduate/ring-theory/field-theory/rational-fraction-fields-with-one-indeterminate.md)

## Proof depends on

- [Chevalley–Warning theorem (1000+ theorems)](../../../../thousand-plus/algebra/12-field-theory-and-polynomials/chevalley-warning-theorem.md)
- [Complex classification](../../../../undergraduate/bilinear-and-quadratic-forms-over-a-vector-space/orthogonality/complex-classification.md)
- [Leibniz’s Series for Pi](../../../../hundred-theorems/part-01/leibnizs-series-for-pi.md)
- [Chevalley-Warning theorem (Number theory)](../../number-theory/chevalley-warning-theorem.md)
- [Sum of four squares](../../number-theory/sum-of-four-squares.md)
- [Minkowski’s Fundamental Theorem](../../../../hundred-theorems/part-02/minkowskis-fundamental-theorem.md)
- [Sum of two squares](../../number-theory/sum-of-two-squares.md)
- [Symmetric bilinear form](../../../linear-algebra/bilinear-and-quadratic-forms/symmetric-bilinear-form.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`QuadFormsKB.ChenevierLannes.wittIgusa_of_cuspVanish`](https://github.com/jonhanke/quadratic-forms-lean/blob/09d95130b262a0fdd44d38275aab5e56dbea5ebd/QuadFormsKB/Literature/ChenevierLannes/WittIgusa060.lean#L237) (theorem)
- [`QuadFormsKB.Cassels.Ch11L92.tartakowskyClassicalAt_four_holds`](https://github.com/jonhanke/quadratic-forms-lean/blob/09d95130b262a0fdd44d38275aab5e56dbea5ebd/QuadFormsKB/Literature/Cassels/Ch11Lemma92Final.lean#L1047) (theorem)
- [`QuadFormsKB.Lattices.omeara106_r38`](https://github.com/jonhanke/quadratic-forms-lean/blob/09d95130b262a0fdd44d38275aab5e56dbea5ebd/QuadFormsKB/Literature/OMeara/Sec106Rank13.lean#L335) (theorem)
- [`QuadFormsKB.OMeara.omeara101_8a`](https://github.com/jonhanke/quadratic-forms-lean/blob/09d95130b262a0fdd44d38275aab5e56dbea5ebd/QuadFormsKB/Literature/OMeara/Sec101FunctionField.lean#L39) (theorem)
- [`QuadFormsKB.Tamagawa.Indefinite.finite_DC`](https://github.com/jonhanke/quadratic-forms-lean/blob/09d95130b262a0fdd44d38275aab5e56dbea5ebd/QuadFormsKB/Tamagawa/Indefinite/DCFinite.lean#L144) (theorem)
- [`QuadFormsKB.LocalDensity.NF.det_hessian_Qp`](https://github.com/jonhanke/quadratic-forms-lean/blob/09d95130b262a0fdd44d38275aab5e56dbea5ebd/QuadFormsKB/LocalDensity/NFLocalGeneral.lean#L38) (theorem)

No file its headlines import, directly or not (1395 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 3,003 .lean files; its Lean libraries `QuadFormsKB`, `Challenge_SiegelTotallyReal`, `Solution_SiegelTotallyReal`, `Challenge_TamagawaTotallyReal`, `Solution_TamagawaTotallyReal`, `Challenge_TamagawaSO` and 31 more hold 3,002, declaring 61,133 names, with `sorry` in 14 files and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/jonhanke/quadratic-forms-lean/blob/09d95130b262a0fdd44d38275aab5e56dbea5ebd/LICENSE)).

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).

## Placement

4 of the 7 Mathlib concepts its headline statements name are in General algebra.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Linear algebra (266 of 1765 imports, 2.6×), General algebra (1066 of 1765 imports, 1.7×), Analysis (227 of 1765 imports, 0.5×). *Proof depends on* lists 8 of the 208 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [jonhanke/quadratic-forms-lean at 09d95130](https://github.com/jonhanke/quadratic-forms-lean/tree/09d95130b262a0fdd44d38275aab5e56dbea5ebd)
