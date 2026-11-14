---
declaration: module
origin: cited
lean: TauCeti.IsPositiveDefiniteSub.exists_pontryaginMeasureTransform_eq_of_continuousAt, TauCeti.IsPositiveDefiniteSub.existsUnique_innerRegular_pontryaginMeasureTransform_eq_of_continuousAt, TauCeti.continuous_and_isPositiveDefiniteSub_iff_existsUnique_innerRegular_pontryaginMeasureTransform_eq, TauCeti.continuous_and_isPositiveDefiniteSub_iff_existsUnique_pontryaginMeasureTransform_eq
statement: formalized
proof: formalized
---

# Bochner's theorem on locally compact abelian groups

The module `PhyslibAlpha.Mathematics.TauCeti.Analysis.Bochner.LocallyCompactGroup`, [PhyslibAlpha/Mathematics/TauCeti/Analysis/Bochner/LocallyCompactGroup.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Bochner/LocallyCompactGroup.lean): 4 declarations, 4 with a docstring.

> A positive-definite function `φ` on a locally compact abelian group `G` that is continuous at `0` is
> the Fourier–Stieltjes transform `φ(g) = ∫ χ(g) dμ(χ)` of a finite inner regular positive measure `μ`
> on the Pontryagin dual of `G`.

## i. Overview

> A positive-definite function `φ` on a locally compact abelian group `G` that is continuous at `0`
> is the Fourier–Stieltjes transform `φ(g) = ∫ χ(g) dμ(χ)` of a finite inner regular positive
> measure `μ` on the Pontryagin dual of `G`.
>
> The representing measure is unique among finite inner regular measures, and conversely the
> transform of every such measure is continuous and positive definite. Thus this is a full Bochner
> characterization without any countability assumption. When the dual is Polish, every finite Borel
> measure is regular, giving the corresponding characterization by arbitrary finite measures. The
> dual is Polish when `G` is second countable.
>
> The measure comes from the GNS construction. The function `φ` is a matrix coefficient
> `φ(g) = ⟪v, U(-g) v⟫` of the unitary translation representation `U` on its GNS Hilbert space,
> which is strongly continuous because `φ` is continuous at `0`. The cyclic spectral theorem for
> strongly continuous unitary representations,
> `ContRepresentation.exists_pontryaginMeasureTransform_eq_inner`, writes such a matrix coefficient
> as a Fourier–Stieltjes transform.
>
> The existence theorem assumes no second countability of `G`, and the GNS space need not be
> separable: the integrated form behind the spectral theorem is defined through the inner
> regularity of the Haar measure.

## ii. Key results

> * `TauCeti.IsPositiveDefiniteSub.exists_pontryaginMeasureTransform_eq_of_continuousAt`: a
>   positive-definite function, continuous at `0`, on a locally compact abelian group is the
>   Fourier–Stieltjes transform of a finite inner regular measure on the dual group.
> * The countability-free Bochner characterization: continuous positive-definite functions are
>   precisely the transforms of unique finite inner regular measures.
> * `TauCeti.continuous_and_isPositiveDefiniteSub_iff_existsUnique_pontryaginMeasureTransform_eq`:
>   the full Bochner characterization by unique finite measures on a locally compact abelian
>   group with Polish dual.

## iv. References

> * G. B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press (2016),
>   Theorem 4.18.

## A. Development

**`TauCeti.IsPositiveDefiniteSub.exists_pontryaginMeasureTransform_eq_of_continuousAt`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Bochner/LocallyCompactGroup.lean#L82).

> **Bochner's theorem on a locally compact abelian group**, existence half.
> A positive-definite function that is continuous at `0` is the Fourier–Stieltjes transform of a
> finite inner regular measure on the Pontryagin dual.

```lean
lemma IsPositiveDefiniteSub.exists_pontryaginMeasureTransform_eq_of_continuousAt {φ : G → ℂ}
    (hφ : IsPositiveDefiniteSub φ) (hφ₀ : ContinuousAt φ 0) :
    ∃ μ : FiniteMeasure (PontryaginDual (Multiplicative G)),
      μ.toMeasure.InnerRegular ∧ μ.pontryaginMeasureTransform = φ
```

**`TauCeti.IsPositiveDefiniteSub.existsUnique_innerRegular_pontryaginMeasureTransform_eq_of_continuousAt`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Bochner/LocallyCompactGroup.lean#L107).

> **Unique inner regular form of Bochner's theorem.** A positive-definite function continuous at
> `0` has a unique finite inner regular representing measure on the Pontryagin dual. No countability
> or metrizability assumption is needed.

```lean
lemma
    IsPositiveDefiniteSub.existsUnique_innerRegular_pontryaginMeasureTransform_eq_of_continuousAt
    {φ : G → ℂ} (hφ : IsPositiveDefiniteSub φ) (hφ₀ : ContinuousAt φ 0) :
    ∃! μ : FiniteMeasure (PontryaginDual (Multiplicative G)),
      μ.toMeasure.InnerRegular ∧ μ.pontryaginMeasureTransform = φ
```

**`TauCeti.continuous_and_isPositiveDefiniteSub_iff_existsUnique_innerRegular_pontryaginMeasureTransform_eq`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Bochner/LocallyCompactGroup.lean#L120).

> **Bochner's characterization without countability assumptions.** A function on a locally
> compact abelian group is continuous and positive definite if and only if it is the
> Fourier–Stieltjes transform of a unique finite inner regular measure on the Pontryagin dual.

```lean
lemma
    continuous_and_isPositiveDefiniteSub_iff_existsUnique_innerRegular_pontryaginMeasureTransform_eq
    (φ : G → ℂ) :
    (Continuous φ ∧ IsPositiveDefiniteSub φ) ↔
      ∃! μ : FiniteMeasure (PontryaginDual (Multiplicative G)),
        μ.toMeasure.InnerRegular ∧ μ.pontryaginMeasureTransform = φ
```

**`TauCeti.continuous_and_isPositiveDefiniteSub_iff_existsUnique_pontryaginMeasureTransform_eq`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Bochner/LocallyCompactGroup.lean#L140).

> **Bochner's characterization on a locally compact abelian group with Polish dual.** A
> function is continuous and positive definite if and only if it is the Fourier–Stieltjes
> transform of a unique finite positive Borel measure on the dual group. The dual is Polish when
> the group is second countable.

```lean
lemma continuous_and_isPositiveDefiniteSub_iff_existsUnique_pontryaginMeasureTransform_eq
    [PolishSpace (PontryaginDual (Multiplicative G))] (φ : G → ℂ) :
    (Continuous φ ∧ IsPositiveDefiniteSub φ) ↔
      ∃! μ : FiniteMeasure (PontryaginDual (Multiplicative G)),
        μ.pontryaginMeasureTransform = φ
```

## Depends on

- [Fourier–Stieltjes transform of measures on a Pontryagin dual](analysis-fourier-pontryagin-measure.md)
- [Positive-definite functions on an additive commutative group](analysis-positivedefinite-addgroup.md)

## Proof depends on

- [Continuity of the Fourier–Stieltjes transform on a Pontryagin dual](analysis-fourier-pontryagin-continuity.md)
- [Matrix coefficients of strongly continuous unitary representations](analysis-fourier-pontryagin-stronglycontinuous.md)
- [Uniqueness of Fourier--Stieltjes measures on a Pontryagin dual](analysis-fourier-pontryagin-uniqueness.md)
- [The GNS translation representation of a positive-definite function](../part-02/analysis-positivedefinite-function-gns.md)
- [Positive-definite transforms of measures on a Pontryagin dual](../part-02/analysis-positivedefinite-pontryaginmeasure.md)

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Analysis/Bochner/LocallyCompactGroup.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Bochner/LocallyCompactGroup.lean)
