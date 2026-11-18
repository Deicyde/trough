---
declaration: module
origin: cited
lean: MeasureTheory.FiniteMeasure.isPositiveDefiniteSub_pontryaginMeasureTransform, MeasureTheory.FiniteMeasure.norm_pontryaginMeasureTransform_le
statement: formalized
proof: formalized
---

# Positive-definite transforms of measures on a Pontryagin dual

The module `PhyslibAlpha.Mathematics.TauCeti.Analysis.PositiveDefinite.PontryaginMeasure`, [PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/PontryaginMeasure.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/PontryaginMeasure.lean): 2 declarations, 2 with a docstring.

> Integration of characters against a finite positive measure gives a positive-definite function on an
> additive topological group.

## i. Overview

> Integration of characters against a finite positive measure gives a
> positive-definite function on an additive topological group. This is the positivity part
> of the measure-to-function direction of Bochner representation on locally compact abelian groups.

## ii. Key results

> This file proves the statement described in the overview.

## iv. References

> * Standard material; the statements and proofs are original to this formalization.

## A. Development

**`MeasureTheory.FiniteMeasure.isPositiveDefiniteSub_pontryaginMeasureTransform`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/PontryaginMeasure.lean#L51).

> The transform of a finite positive measure on the dual is positive definite.

```lean
lemma _root_.MeasureTheory.FiniteMeasure.isPositiveDefiniteSub_pontryaginMeasureTransform
    (μ : FiniteMeasure (PontryaginDual (Multiplicative G))) :
    IsPositiveDefiniteSub μ.pontryaginMeasureTransform
```

**`MeasureTheory.FiniteMeasure.norm_pontryaginMeasureTransform_le`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/PontryaginMeasure.lean#L80).

> The absolute value of a measure transform is bounded by the measure's total mass.

```lean
lemma _root_.MeasureTheory.FiniteMeasure.norm_pontryaginMeasureTransform_le
    (μ : FiniteMeasure (PontryaginDual (Multiplicative G))) (g : G) :
    ‖μ.pontryaginMeasureTransform g‖ ≤ μ.toMeasure.real Set.univ
```

## Depends on

- [Fourier–Stieltjes transform of measures on a Pontryagin dual](../part-01/analysis-fourier-pontryagin-measure.md)
- [Positive-definite functions on an additive commutative group](../part-01/analysis-positivedefinite-addgroup.md)

## Proof depends on

- [Pontryagin characters are positive-definite atoms](../part-01/analysis-positivedefinite-additivecharacter.md)

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/PontryaginMeasure.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/PontryaginMeasure.lean)
