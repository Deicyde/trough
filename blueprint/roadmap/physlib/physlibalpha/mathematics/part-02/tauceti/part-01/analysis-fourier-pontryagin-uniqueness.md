---
declaration: module
origin: cited
lean: PontryaginDual.evalBoundedContinuous, PontryaginDual.evalBoundedContinuous_apply, PontryaginDual.evalBoundedContinuous_zero, PontryaginDual.evalBoundedContinuous_add, PontryaginDual.evalBoundedContinuous_neg, PontryaginDual.evalMonoidHom, PontryaginDual.evalMonoidHom_apply, PontryaginDual.evalAlgHom
statement: formalized
proof: formalized
---

# Uniqueness of Fourier--Stieltjes measures on a Pontryagin dual

The module `PhyslibAlpha.Mathematics.TauCeti.Analysis.Fourier.Pontryagin.Uniqueness`, [PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Uniqueness.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Uniqueness.lean): 20 declarations, 20 with a docstring.

> On a Polish Pontryagin dual, a finite measure is determined by the integrals of the evaluation
> characters.

## i. Overview

> On a Polish Pontryagin dual, a finite measure is determined by the integrals of the evaluation
> characters.  Equivalently, the Fourier--Stieltjes transform of a finite measure on the dual is
> injective.  On the dual of an arbitrary locally compact abelian group, where the dual need be
> neither metrizable nor second countable, the same holds for finite inner regular measures.  These
> are the uniqueness halves of Bochner's theorem for locally compact abelian groups.
>
> The proof packages finite linear combinations of evaluation characters as a star subalgebra of
> bounded continuous functions.  Evaluation characters separate points of the dual simply because
> two continuous homomorphisms that agree at every group element are equal.  Mathlib's extension
> theorem for finite measures on Polish spaces, or its inner regular counterpart
> `TauCeti.MeasureTheory.ext_of_forall_mem_subalgebra_integral_eq_of_innerRegular` on locally
> compact Hausdorff spaces, then promotes equality of the character integrals to equality of the
> measures.
>
> The construction of `evalMonoidHom`, `evalAlgHom` and `evalPoly`, together with the proofs that
> `evalPoly` is closed under `star` and separates points, is adapted from Jakob Stiefel's
> `charMonoidHom`, `charAlgHom`, `charPoly`, `star_mem_range_charAlgHom` and
> `separatesPoints_charPoly` in `Mathlib.Analysis.Fourier.BoundedContinuousFunctionChar`, which
> treats characters of the form `v ↦ e (L v w)` on a real vector space.

## ii. Key results

> * `PontryaginDual.evalBoundedContinuous`: evaluation at a group element, bundled as a
>   bounded continuous function on the dual.
> * `PontryaginDual.evalPoly`: the star subalgebra of finite linear combinations of
>   evaluation characters.
> * `MeasureTheory.FiniteMeasure.ext_of_forall_pontryaginMeasureTransform_eq`: finite measures on a
>   Polish dual with the same Fourier--Stieltjes transform are equal.
> * `MeasureTheory.FiniteMeasure.ext_of_forall_pontryaginMeasureTransform_eq_of_innerRegular`:
>   finite inner regular measures on the dual of a locally compact abelian group with the same
>   Fourier--Stieltjes transform are equal.

## iv. References

> * W. Rudin, *Fourier Analysis on Groups*, Chapter 1.
> * J. Stiefel, `Mathlib.Analysis.Fourier.BoundedContinuousFunctionChar`, Mathlib.

## A. Development

**`PontryaginDual.evalBoundedContinuous`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Uniqueness.lean#L75).

> Evaluation at `g`, as a bounded continuous complex-valued function on the Pontryagin dual.
> Its values lie on the unit circle, so its norm is bounded by one.

```lean
def evalBoundedContinuous (g : G) :
    _root_.PontryaginDual (Multiplicative G) →ᵇ ℂ
```

**`PontryaginDual.evalBoundedContinuous_apply`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Uniqueness.lean#L83).

> Evaluation of `evalBoundedContinuous` at a character.

```lean
lemma evalBoundedContinuous_apply (g : G)
    (χ : _root_.PontryaginDual (Multiplicative G)) :
    evalBoundedContinuous g χ = (χ (Multiplicative.ofAdd g) : ℂ)
```

**`PontryaginDual.evalBoundedContinuous_zero`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Uniqueness.lean#L90).

> Evaluation at zero is the constant function one.

```lean
lemma evalBoundedContinuous_zero :
    evalBoundedContinuous (0 : G) = 1
```

**`PontryaginDual.evalBoundedContinuous_add`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Uniqueness.lean#L97).

> Evaluation turns addition in the original group into pointwise multiplication.

```lean
lemma evalBoundedContinuous_add (g h : G) :
    evalBoundedContinuous (g + h) =
      evalBoundedContinuous g * evalBoundedContinuous h
```

**`PontryaginDual.evalBoundedContinuous_neg`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Uniqueness.lean#L105).

> Evaluation at the negative of a group element is the pointwise star of evaluation there.

```lean
lemma evalBoundedContinuous_neg (g : G) :
    evalBoundedContinuous (-g) = star (evalBoundedContinuous g)
```

**`PontryaginDual.evalMonoidHom`**, a def, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Uniqueness.lean#L113).

> Evaluation as a monoid homomorphism from the multiplicative copy of the original group.

```lean
def evalMonoidHom : Multiplicative G →*
    (_root_.PontryaginDual (Multiplicative G) →ᵇ ℂ)
```

**`PontryaginDual.evalMonoidHom_apply`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Uniqueness.lean#L122).

> Evaluation of `evalMonoidHom` at a character.

```lean
lemma evalMonoidHom_apply (g : Multiplicative G)
    (χ : _root_.PontryaginDual (Multiplicative G)) :
    evalMonoidHom g χ = (χ g : ℂ)
```

**`PontryaginDual.evalAlgHom`**, a def, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Uniqueness.lean#L129).

> The algebra homomorphism sending a formal finite linear combination of group elements to the
> corresponding finite linear combination of evaluation characters.

```lean
def evalAlgHom : AddMonoidAlgebra ℂ G →ₐ[ℂ]
    (_root_.PontryaginDual (Multiplicative G) →ᵇ ℂ)
```

**`PontryaginDual.evalAlgHom_apply`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Uniqueness.lean#L135).

> Evaluation of `evalAlgHom` is the corresponding finite linear combination of characters.

```lean
lemma evalAlgHom_apply (a : AddMonoidAlgebra ℂ G)
    (χ : _root_.PontryaginDual (Multiplicative G)) :
    evalAlgHom a χ = a.coeff.sum fun g c => c * (χ (Multiplicative.ofAdd g) : ℂ)
```

**`PontryaginDual.star_mem_range_evalAlgHom`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Uniqueness.lean#L143).

> The range of `evalAlgHom` is closed under pointwise complex conjugation.

```lean
lemma star_mem_range_evalAlgHom
    {f : _root_.PontryaginDual (Multiplicative G) →ᵇ ℂ}
    (hf : f ∈ evalAlgHom.range) : star f ∈ evalAlgHom.range
```

**`PontryaginDual.evalPoly`**, a def, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Uniqueness.lean#L156).

> The star subalgebra of bounded continuous functions generated by evaluation characters.

```lean
def evalPoly : StarSubalgebra ℂ
    (_root_.PontryaginDual (Multiplicative G) →ᵇ ℂ)
```

**`PontryaginDual.evalPoly_toSubalgebra`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Uniqueness.lean#L162).

> The underlying subalgebra of `evalPoly` is the range of `evalAlgHom`.

```lean
lemma evalPoly_toSubalgebra :
    (evalPoly (G := G)).toSubalgebra = evalAlgHom.range
```

**`PontryaginDual.mem_evalPoly`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Uniqueness.lean#L168).

> Membership in `evalPoly` means being a finite linear combination of evaluation
> characters.

```lean
lemma mem_evalPoly (f : _root_.PontryaginDual (Multiplicative G) →ᵇ ℂ) :
    f ∈ evalPoly ↔
      ∃ a : AddMonoidAlgebra ℂ G,
        f = a.coeff.sum fun g c => c • evalBoundedContinuous g
```

**`PontryaginDual.evalBoundedContinuous_mem_evalPoly`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Uniqueness.lean#L182).

> Every evaluation character belongs to `evalPoly`.

```lean
lemma evalBoundedContinuous_mem_evalPoly (g : G) :
    evalBoundedContinuous g ∈ evalPoly
```

**`PontryaginDual.separatesPoints_evalPoly`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Uniqueness.lean#L187).

> The evaluation-character algebra separates points of the Pontryagin dual.

```lean
lemma separatesPoints_evalPoly :
    ((evalPoly : StarSubalgebra ℂ
      (_root_.PontryaginDual (Multiplicative G) →ᵇ ℂ)).map
        (BoundedContinuousFunction.toContinuousMapStarₐ ℂ)).SeparatesPoints
```

**`MeasureTheory.FiniteMeasure.integral_eq_of_forall_pontryaginMeasureTransform_eq`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Uniqueness.lean#L211).

> Two finite measures on the dual with the same Fourier--Stieltjes transform integrate every
> finite linear combination of evaluation characters equally.

```lean
lemma _root_.MeasureTheory.FiniteMeasure.integral_eq_of_forall_pontryaginMeasureTransform_eq
    {P Q : FiniteMeasure (_root_.PontryaginDual (Multiplicative G))}
    (h : ∀ g, P.pontryaginMeasureTransform g = Q.pontryaginMeasureTransform g)
    {f : _root_.PontryaginDual (Multiplicative G) →ᵇ ℂ} (hf : f ∈ _root_.PontryaginDual.evalPoly) :
    ∫ χ, f χ ∂P = ∫ χ, f χ ∂Q
```

**`MeasureTheory.FiniteMeasure.ext_of_forall_pontryaginMeasureTransform_eq`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Uniqueness.lean#L243).

> **Uniqueness of Fourier--Stieltjes measures on a Polish Pontryagin dual.** Two finite measures
> on the dual are equal when their transforms agree on every element of the original group.

```lean
lemma _root_.MeasureTheory.FiniteMeasure.ext_of_forall_pontryaginMeasureTransform_eq
    {P Q : FiniteMeasure (_root_.PontryaginDual (Multiplicative G))}
    (h : ∀ g, P.pontryaginMeasureTransform g = Q.pontryaginMeasureTransform g) :
    P = Q
```

**`MeasureTheory.FiniteMeasure.pontryaginMeasureTransform_injective`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Uniqueness.lean#L253).

> The Fourier--Stieltjes transform is injective on finite measures on a Polish Pontryagin
> dual.

```lean
lemma _root_.MeasureTheory.FiniteMeasure.pontryaginMeasureTransform_injective :
    Function.Injective
      (fun P : FiniteMeasure (_root_.PontryaginDual (Multiplicative G)) =>
        P.pontryaginMeasureTransform)
```

**`MeasureTheory.FiniteMeasure.ext_of_forall_pontryaginMeasureTransform_eq_of_innerRegular`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Uniqueness.lean#L272).

> **Uniqueness of inner regular Fourier--Stieltjes measures.** On the Pontryagin dual of a
> locally compact abelian group, two finite inner regular measures are equal when their transforms
> agree on every element of the group. No countability or metrizability is assumed.

```lean
lemma
    _root_.MeasureTheory.FiniteMeasure.ext_of_forall_pontryaginMeasureTransform_eq_of_innerRegular
    {P Q : FiniteMeasure (_root_.PontryaginDual (Multiplicative G))}
    [P.toMeasure.InnerRegular] [Q.toMeasure.InnerRegular]
    (h : ∀ g, P.pontryaginMeasureTransform g = Q.pontryaginMeasureTransform g) :
    P = Q
```

**`MeasureTheory.FiniteMeasure.pontryaginMeasureTransform_injOn_innerRegular`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Uniqueness.lean#L285).

> The Fourier--Stieltjes transform is injective on finite inner regular measures on the
> Pontryagin dual of a locally compact abelian group.

```lean
lemma _root_.MeasureTheory.FiniteMeasure.pontryaginMeasureTransform_injOn_innerRegular :
    Set.InjOn
      (fun P : FiniteMeasure (_root_.PontryaginDual (Multiplicative G)) =>
        P.pontryaginMeasureTransform)
      {P | P.toMeasure.InnerRegular}
```

## Depends on

- [Fourier–Stieltjes transform of measures on a Pontryagin dual](analysis-fourier-pontryagin-measure.md)

## Proof depends on

- [Finite measures are determined by separating test functions](../part-02/measuretheory-measure-finitemeasureext.md)

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Uniqueness.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Uniqueness.lean)
