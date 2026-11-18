---
declaration: theorem
origin: cited
lean: QuotientSubmoduleEquidistribution.MainTheoremEndpoint.rightQuotientSubmoduleEquidistribution, QuotientSubmoduleEquidistribution.BottomLevels.FiniteDimensionalRecurrence.FirstLastFourEndpoint.bottom_top_four, QuotientSubmoduleEquidistribution.BottomLevels.FiniteDimensionalRecurrence.FirstLastFourEndpoint.equidistribution_of_card_le_nine, QuotientSubmoduleEquidistribution.NakayamaAlgebraProductFormula.rightQuotientSubmoduleEquidistribution, QuotientSubmoduleEquidistribution.RadicalSquareZero.rightQuotientSubmoduleEquidistribution_of_squareZero, QuotientSubmoduleEquidistribution.rightRepresentationDirected_quotientSubmoduleEquidistribution, QuotientSubmoduleEquidistribution.SetClosure.finiteIntervalDeletionChain, QuotientSubmoduleEquidistribution.IndecomposableSkeleton.qClosed_finiteIntervalDeletionChain_of_finiteDimensional
statement: formalized
proof: formalized
---

# Quotient-submodule equidistribution in Lean

[haruhisa-enomoto/quotient-submodule-equidistribution](https://github.com/haruhisa-enomoto/quotient-submodule-equidistribution) at commit [20ee4b96](https://github.com/haruhisa-enomoto/quotient-submodule-equidistribution/tree/20ee4b964a9174b15304ac96485beeb73be113d8), 2026-08-23.

## Depends on

- [Associative algebra over a commutative ring](../../algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Field](../../field-theory/field.md)
- [Finite-dimensionality](../../../linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Ring](../../rings/ring.md)
- [Algebraically closed field](../../field-theory/algebraically-closed-field.md)
- [Set](../../../data-structures/sets/set.md)
- [Module](../../../linear-algebra/fundamentals/module.md)

## Proof depends on

- [Szpilrajn extension theorem](../../../../thousand-plus/general-topics-history-and-foundations/szpilrajn-extension-theorem.md)
- [Noetherian ring](../../rings/noetherian-ring.md)
- [Existence of bases](../../../../undergraduate/linear-algebra/fundamentals/existence-of-bases.md)
- [The category of modules over a ring](../../../linear-algebra/fundamentals/the-category-of-modules-over-a-ring.md)
- [Noetherian module](../../../linear-algebra/fundamentals/noetherian-module.md)
- [Abelian category](../../category-theory/abelian-category.md)
- [Extreme point](../../../../undergraduate/affine-and-euclidean-geometry/convexity/extreme-point.md)
- [Range of a linear map](../../../../undergraduate/linear-algebra/fundamentals/range-of-a-linear-map.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`QuotientSubmoduleEquidistribution.MainTheoremEndpoint.rightQuotientSubmoduleEquidistribution`](https://github.com/haruhisa-enomoto/quotient-submodule-equidistribution/blob/20ee4b964a9174b15304ac96485beeb73be113d8/QuotientSubmoduleEquidistribution/RepresentationTheory/MainTheoremEndpoint.lean#L28) (theorem)
- [`QuotientSubmoduleEquidistribution.BottomLevels.FiniteDimensionalRecurrence.FirstLastFourEndpoint.bottom_top_four`](https://github.com/haruhisa-enomoto/quotient-submodule-equidistribution/blob/20ee4b964a9174b15304ac96485beeb73be113d8/QuotientSubmoduleEquidistribution/RepresentationTheory/FirstLastFourEndpoint.lean#L38) (theorem)
- [`QuotientSubmoduleEquidistribution.BottomLevels.FiniteDimensionalRecurrence.FirstLastFourEndpoint.equidistribution_of_card_le_nine`](https://github.com/haruhisa-enomoto/quotient-submodule-equidistribution/blob/20ee4b964a9174b15304ac96485beeb73be113d8/QuotientSubmoduleEquidistribution/RepresentationTheory/FirstLastFourEndpoint.lean#L106) (theorem)
- [`QuotientSubmoduleEquidistribution.NakayamaAlgebraProductFormula.rightQuotientSubmoduleEquidistribution`](https://github.com/haruhisa-enomoto/quotient-submodule-equidistribution/blob/20ee4b964a9174b15304ac96485beeb73be113d8/QuotientSubmoduleEquidistribution/RepresentationTheory/NakayamaAlgebraProductFormula.lean#L90) (theorem)
- [`QuotientSubmoduleEquidistribution.RadicalSquareZero.rightQuotientSubmoduleEquidistribution_of_squareZero`](https://github.com/haruhisa-enomoto/quotient-submodule-equidistribution/blob/20ee4b964a9174b15304ac96485beeb73be113d8/QuotientSubmoduleEquidistribution/RadicalSquareZero/SeparatedDirectedInterface.lean#L349) (theorem)
- [`QuotientSubmoduleEquidistribution.rightRepresentationDirected_quotientSubmoduleEquidistribution`](https://github.com/haruhisa-enomoto/quotient-submodule-equidistribution/blob/20ee4b964a9174b15304ac96485beeb73be113d8/QuotientSubmoduleEquidistribution/RepresentationDirected/AlgebraEndpoint.lean#L137) (theorem)
- [`QuotientSubmoduleEquidistribution.SetClosure.finiteIntervalDeletionChain`](https://github.com/haruhisa-enomoto/quotient-submodule-equidistribution/blob/20ee4b964a9174b15304ac96485beeb73be113d8/QuotientSubmoduleEquidistribution/ConvexGeometry/FiniteInterval.lean#L206) (theorem)
- [`QuotientSubmoduleEquidistribution.IndecomposableSkeleton.qClosed_finiteIntervalDeletionChain_of_finiteDimensional`](https://github.com/haruhisa-enomoto/quotient-submodule-equidistribution/blob/20ee4b964a9174b15304ac96485beeb73be113d8/QuotientSubmoduleEquidistribution/RepresentationTheory/ConvexStructure.lean#L228) (theorem)

No file its headlines import, directly or not (628 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.32.0, Mathlib at [28313485](https://github.com/leanprover-community/mathlib4/tree/28313485bc624fcd16dcb162dd2e2c3c813aa8fe).
- 693 .lean files; its Lean libraries `QuotientSubmoduleEquidistribution`, `MainResults` hold 681, declaring 11,941 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/haruhisa-enomoto/quotient-submodule-equidistribution/blob/20ee4b964a9174b15304ac96485beeb73be113d8/LICENSE)).

## Builds on

- Mathlib, at [28313485](https://github.com/leanprover-community/mathlib4/tree/28313485bc624fcd16dcb162dd2e2c3c813aa8fe).

## Placement

4 of the 7 Mathlib concepts its headline statements name are in General algebra.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Linear algebra (123 of 451 imports, 4.7×), General algebra (242 of 451 imports, 1.5×). *Proof depends on* names 8 of the 41 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [haruhisa-enomoto/quotient-submodule-equidistribution at 20ee4b96](https://github.com/haruhisa-enomoto/quotient-submodule-equidistribution/tree/20ee4b964a9174b15304ac96485beeb73be113d8)
