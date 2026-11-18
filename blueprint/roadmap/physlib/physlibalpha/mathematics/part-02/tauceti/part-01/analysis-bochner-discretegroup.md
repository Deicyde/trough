---
declaration: module
origin: cited
lean: TauCeti.isPositiveDefiniteSub_iff_exists_pontryaginMeasureTransform_eq
statement: formalized
proof: formalized
---

# Bochner's theorem on discrete abelian groups

The module `PhyslibAlpha.Mathematics.TauCeti.Analysis.Bochner.DiscreteGroup`, [PhyslibAlpha/Mathematics/TauCeti/Analysis/Bochner/DiscreteGroup.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Bochner/DiscreteGroup.lean): 1 declaration, 1 with a docstring.

> A function `φ` on a discrete abelian group `G` is positive definite, `∑ᵢ ∑ⱼ cᵢ conj(cⱼ) φ(gᵢ - gⱼ) ≥
> 0` for every finite family, if and only if it is the Fourier–Stieltjes transform `φ(g) = ∫ χ(g)
> dμ(χ)` of a finite inner regular positive measure `μ` on the Pontryagin dual of `G`.

## i. Overview

> A function `φ` on a discrete abelian group `G` is positive definite,
> `∑ᵢ ∑ⱼ cᵢ conj(cⱼ) φ(gᵢ - gⱼ) ≥ 0` for every finite family, if and only if it is the
> Fourier–Stieltjes transform `φ(g) = ∫ χ(g) dμ(χ)` of a finite inner regular positive measure `μ`
> on the Pontryagin dual of `G`. Every function on a discrete group is continuous, so no
> continuity hypothesis appears.
>
> The representing measure is the one of Bochner's theorem on locally compact abelian groups,
> `TauCeti.IsPositiveDefiniteSub.exists_pontryaginMeasureTransform_eq_of_continuousAt`, whose
> continuity hypothesis is automatic on a discrete group.
>
> For `G = ℤ` this recovers Herglotz's theorem, proved separately by Fejér means in
> `TauCeti.Analysis.Bochner.Herglotz`.

## ii. Key results

> * `TauCeti.isPositiveDefiniteSub_iff_exists_pontryaginMeasureTransform_eq`: **Bochner's theorem**
>   for discrete abelian groups.

## iv. References

> * W. Rudin, *Fourier Analysis on Groups*, Interscience (1962), §1.4.
> * G. B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press (2016), §3.3
>   and §4.2.

## A. Development

**`TauCeti.isPositiveDefiniteSub_iff_exists_pontryaginMeasureTransform_eq`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Bochner/DiscreteGroup.lean#L64).

> **Bochner's theorem on a discrete abelian group.** A function on a discrete abelian group is
> positive definite if and only if it is the Fourier–Stieltjes transform of a finite inner regular
> measure on the Pontryagin dual.

```lean
lemma isPositiveDefiniteSub_iff_exists_pontryaginMeasureTransform_eq (φ : G → ℂ) :
    IsPositiveDefiniteSub φ ↔
      ∃ μ : FiniteMeasure (PontryaginDual (Multiplicative G)),
        μ.toMeasure.InnerRegular ∧ μ.pontryaginMeasureTransform = φ
```

## Depends on

- [Fourier–Stieltjes transform of measures on a Pontryagin dual](analysis-fourier-pontryagin-measure.md)
- [Positive-definite functions on an additive commutative group](analysis-positivedefinite-addgroup.md)

## Proof depends on

- [Bochner's theorem on locally compact abelian groups](analysis-bochner-locallycompactgroup.md)

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Analysis/Bochner/DiscreteGroup.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Bochner/DiscreteGroup.lean)
