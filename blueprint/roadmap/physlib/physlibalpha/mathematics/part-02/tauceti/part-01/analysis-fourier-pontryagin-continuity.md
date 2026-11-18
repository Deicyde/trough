---
declaration: module
origin: cited
lean: MeasureTheory.FiniteMeasure.continuous_pontryaginMeasureTransform
statement: formalized
proof: formalized
---

# Continuity of the Fourier–Stieltjes transform on a Pontryagin dual

The module `PhyslibAlpha.Mathematics.TauCeti.Analysis.Fourier.Pontryagin.Continuity`, [PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Continuity.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Continuity.lean): 1 declaration, 1 with a docstring.

> The Fourier–Stieltjes transform of a tight finite positive measure on the Pontryagin dual is
> continuous on the original locally compact group.

## i. Overview

> The Fourier–Stieltjes transform of a tight finite positive measure on the Pontryagin dual is
> continuous on the original locally compact group. Together with its positive-definiteness,
> this supplies the measure-to-function direction of Bochner representation on locally compact
> abelian groups for regular measures. A compact set carries almost all of the measure; character
> evaluation is uniformly continuous there near each fixed group element, while the complement
> contributes at most its small mass.
>
> This is the standard compact truncation argument for Fourier–Stieltjes transforms; see
> G. B. Folland, *A Course in Abstract Harmonic Analysis*, Chapter 4.

## ii. Key results

> This file proves the statement described in the overview.

## iv. References

> * Standard material; the statements and proofs are original to this formalization.

## A. Development

**`MeasureTheory.FiniteMeasure.continuous_pontryaginMeasureTransform`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Continuity.lean#L57).

> The transform of a tight finite measure on the Pontryagin dual is continuous. Tightness is
> automatic for finite Radon measures and is the regularity needed when the dual is not metrizable.

```lean
lemma _root_.MeasureTheory.FiniteMeasure.continuous_pontryaginMeasureTransform
    (μ : FiniteMeasure (PontryaginDual (Multiplicative G)))
    (hμ : IsTightMeasureSet {μ.toMeasure}) :
    Continuous μ.pontryaginMeasureTransform
```

## Depends on

- [Fourier–Stieltjes transform of measures on a Pontryagin dual](analysis-fourier-pontryagin-measure.md)

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Continuity.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Continuity.lean)
