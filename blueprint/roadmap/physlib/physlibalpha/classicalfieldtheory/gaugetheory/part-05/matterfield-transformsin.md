---
declaration: module
origin: cited
lean: LocalGaugeData.TransformsIn, LocalGaugeData.TransformsIn.repGauge_zero, LocalGaugeData.TransformsIn.repGauge_eq_of_eval_eq_one, LocalGaugeData.repCoeff_zero_eq_ofConstant_eval, LocalGaugeData.TransformsIn.repGauge_zero_eq_ofConstant_eval, LocalGaugeData.TransformsIn.repGauge_eq_of_mem_truncationKer_zero
statement: formalized
proof: formalized
---

# Gauge tensors in a representation

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.TransformsIn`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/TransformsIn.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/TransformsIn.lean): 6 declarations, 6 with a docstring.

## i. Overview

> A matter field valued in a representation space `V` has symbols `[∂_s ψ^i]` contracted
> against duals of `V`. It is a *gauge tensor* — it *transforms in* the representation
> `rep` of the jet gauge group — when each derivative symbol transforms by the Leibniz
> convolution of the base-point Taylor coefficients `repDualCoeff` of `rep` against the
> lower symbols, with no inhomogeneous term. This is the generalization of
> `TransformsInAdjoint` from the adjoint representation to an arbitrary one, and the
> property preserved by the covariant derivative in
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.InfinitesimalAction`.
>
> Nothing here depends on the local gauge data beyond the group `GJ` acting; the definition
> lives in the `LocalGaugeData` namespace with the transformation laws that consume it.
>
>
> - `LocalGaugeData.TransformsIn` : the gauge tensors of a representation.
> - `LocalGaugeData.TransformsIn.repGauge_zero` : the underived symbol transforms through
>   the base-point value of the gauge jet alone.
> - `LocalGaugeData.TransformsIn.repGauge_eq_of_eval_eq_one`,
>   `LocalGaugeData.TransformsIn.repGauge_eq_of_mem_truncationKer_zero` : a pure jet fixes the
>   underived symbol, when the representation is trivial on such jets.

## ii. Key results

> - `TransformsIn` : a component family `F`, valued in `B` and indexed by the complex dual of the
>   representation space `V`, *transforms in* the representation `rep` of the jet gauge group — with
>   the ambient action `repGauge` on `B` — when each derivative symbol `[∂_s F^φ]` transforms by the
>   Leibniz convolution of the dual representation coefficients against lower symbols, with no
>   inhomogeneous term — the generalization of `TransformsInAdjoint` from the adjoint representation
>   to an arbitrary one, and the form consumed by `AlgebraRealization`
> - `TransformsIn.repGauge_zero` : a matter gauge tensor transforms at the base point through the dual
>   coefficient of the base-point value of the gauge jet alone: the antidiagonal of the empty multiset
>   has a single term
> - `TransformsIn.repGauge_eq_of_eval_eq_one` : matter gauge tensors whose zeroth representation
>   coefficient is trivial on pure jets are fixed by pure jets: for a family transforming in `rep`, a
>   gauge jet with trivial base-point value acts trivially on the underived symbol, provided the
>   representation's zeroth Taylor coefficient is the identity on such jets
> - `repCoeff_zero_eq_ofConstant_eval` : if pure jets act trivially at the base point, the zeroth
>   Taylor coefficient of a jet is that of the constant jet of its value: every jet is a pure jet
>   times the constant jet of its value, and the zeroth coefficients are multiplicative for a
>   fibrewise representation

## iv. References

> * None.

## A. Gauge tensors in a representation

**`LocalGaugeData.TransformsIn`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/TransformsIn.lean#L92).

> A component family `F`, valued in `B` and indexed by the complex dual of the
> representation space `V`, *transforms in* the representation `rep` of the jet gauge
> group — with the ambient action `repGauge` on `B` — when each derivative symbol
> `[∂_s F^φ]` transforms by the Leibniz convolution of the dual representation
> coefficients against lower symbols, with no inhomogeneous term — the generalization
> of `TransformsInAdjoint` from the adjoint representation to an arbitrary one, and
> the form consumed by `AlgebraRealization`.

```lean
def TransformsIn (repGauge : Representation ℂ GJ B)
    (rep : Representation ℂ GJ (SpaceTimeAlgebra ⊗[ℂ] V))
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B) : Prop
```

**`LocalGaugeData.TransformsIn.repGauge_zero`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/TransformsIn.lean#L106).

> A matter gauge tensor transforms at the base point through the dual coefficient of the
> base-point value of the gauge jet alone: the antidiagonal of the empty multiset has a
> single term.

```lean
lemma TransformsIn.repGauge_zero (hF : TransformsIn repGauge rep F) (U : GJ)
    (φ : Module.Dual ℂ V) :
    repGauge U (F 0 φ) = F 0 (repDualCoeff rep U⁻¹ 0 φ)
```

**`LocalGaugeData.TransformsIn.repGauge_eq_of_eval_eq_one`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/TransformsIn.lean#L116).

> Matter gauge tensors whose zeroth representation coefficient is trivial on pure
> jets are fixed by pure jets: for a family transforming in `rep`, a gauge jet with
> trivial base-point value acts trivially on the underived symbol, provided the
> representation's zeroth Taylor coefficient is the identity on such jets.

```lean
lemma TransformsIn.repGauge_eq_of_eval_eq_one {𝔤 : Type} [LieRing 𝔤] [LieAlgebra ℝ 𝔤]
    {G₀ : Type} [Group G₀] {𝔤J : Type} [LieRing 𝔤J] [LieAlgebra ℝ 𝔤J]
    {jets : LocalGaugeData G₀ 𝔤 GJ 𝔤J} (hF : TransformsIn repGauge rep F)
    (hrep : ∀ {W : GJ}, jets.eval W = 1 → repCoeff rep W 0 = LinearMap.id)
    {U : GJ} (hU : jets.eval U = 1) (φ : Module.Dual ℂ V) :
    repGauge U (F 0 φ) = F 0 φ
```

**`LocalGaugeData.repCoeff_zero_eq_ofConstant_eval`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/TransformsIn.lean#L131).

> If pure jets act trivially at the base point, the zeroth Taylor coefficient of a jet
> is that of the constant jet of its value: every jet is a pure jet times the constant jet
> of its value, and the zeroth coefficients are multiplicative for a fibrewise
> representation.

```lean
lemma repCoeff_zero_eq_ofConstant_eval {𝔤 : Type} [LieRing 𝔤] [LieAlgebra ℝ 𝔤]
    {G₀ : Type} [Group G₀] {𝔤J : Type} [LieRing 𝔤J] [LieAlgebra ℝ 𝔤J]
    (jets : LocalGaugeData G₀ 𝔤 GJ 𝔤J) (rep : Representation ℂ GJ (SpaceTimeAlgebra ⊗[ℂ] V))
    (hlin : ∀ (U : GJ) (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] V), rep U
        (χ • z) = χ • rep U z)
    (hrep : ∀ {W : GJ}, jets.eval W = 1 → repCoeff rep W 0 = LinearMap.id) (U : GJ) :
    repCoeff rep U 0 = repCoeff rep (jets.ofConstant (jets.eval U)) 0
```

**`LocalGaugeData.TransformsIn.repGauge_zero_eq_ofConstant_eval`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/TransformsIn.lean#L149).

> If pure jets act trivially at the base point, a matter gauge tensor transforms at the
> base point as under the constant jet of the value of the gauge jet: the jet action on
> underived symbols factors through evaluation.

```lean
lemma TransformsIn.repGauge_zero_eq_ofConstant_eval {𝔤 : Type} [LieRing 𝔤] [LieAlgebra ℝ 𝔤]
    {G₀ : Type} [Group G₀] {𝔤J : Type} [LieRing 𝔤J] [LieAlgebra ℝ 𝔤J]
    {jets : LocalGaugeData G₀ 𝔤 GJ 𝔤J} (hF : TransformsIn repGauge rep F)
    (hlin : ∀ (U : GJ) (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] V), rep U
        (χ • z) = χ • rep U z)
    (hrep : ∀ {W : GJ}, jets.eval W = 1 → repCoeff rep W 0 = LinearMap.id) (U : GJ)
    (φ : Module.Dual ℂ V) :
    repGauge U (F 0 φ) = repGauge (jets.ofConstant (jets.eval U)) (F 0 φ)
```

**`LocalGaugeData.TransformsIn.repGauge_eq_of_mem_truncationKer_zero`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/TransformsIn.lean#L163).

> Matter gauge tensors are fixed by pure jets: the members of the zeroth truncation kernel
> are the jets with trivial base-point value, so `repGauge_eq_of_eval_eq_one` applies.

```lean
lemma TransformsIn.repGauge_eq_of_mem_truncationKer_zero {𝔤 : Type} [LieRing 𝔤] [LieAlgebra ℝ 𝔤]
    {G₀ : Type} [Group G₀] {𝔤J : Type} [LieRing 𝔤J] [LieAlgebra ℝ 𝔤J]
    {jets : LocalGaugeData G₀ 𝔤 GJ 𝔤J} (hF : TransformsIn repGauge rep F)
    (hrep : ∀ {W : GJ}, jets.eval W = 1 → repCoeff rep W 0 = LinearMap.id)
    (U : jets.truncationKer 0) (φ : Module.Dual ℂ V) :
    repGauge U.1 (F 0 φ) = F 0 φ
```

## Depends on

- [The truncation filtration of the jet gauge group](../part-04/localgaugedata-truncation.md)
- [Gauge tensors in a general representation](matterfield-covariantderiv.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/TransformsIn.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/TransformsIn.lean)
