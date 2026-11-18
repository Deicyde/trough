---
declaration: module
origin: cited
lean: GaugeAlgebraRealization.TransformsInAdjoint, GaugeAlgebraRealization.TransformsInAdjoint.repGauge_zero, GaugeAlgebraRealization.bracketFamConv, GaugeAlgebraRealization.covDerivAdjoint, GaugeAlgebraRealization.covDerivAdjoint_apply, GaugeAlgebraRealization.covDerivAdjoint_apply_of_map_lie, GaugeAlgebraRealization.bracketFamConv_map, GaugeAlgebraRealization.covDerivAdjoint_map
statement: formalized
proof: formalized
---

# Adjoint gauge tensors and the covariant derivative

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeBoson.Realization.TransformsAdjoint`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/TransformsAdjoint.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/TransformsAdjoint.lean): 11 declarations, 10 with a docstring.

## i. Overview

> A family of derivative symbols is an *adjoint gauge tensor* when all its symbols
> transform by the pure Leibniz convolution of the dual adjoint action, with no
> inhomogeneous term. The convolution is forced: the gauge group acts on the
> derivative symbols by substitution and the chain rule, so `U • [∂_s F^φ]` produces
> every splitting `s = x + y` — `x` derivatives hitting the adjoint, `y` remaining on
> `F`; the naive law `U • [∂_s F^φ] = F^{(∂_s Ad)^* φ}` holds only at `s = 0`.
>
> The two theorems of this section: the field strength is an adjoint gauge tensor
> (`transformsInAdjoint_fieldStrength`), and adjoint gauge tensors are closed under
> the covariant derivative `∇_ρ F = [∂_ρ F] + ⁅A_ρ, F⁆`
> (`TransformsInAdjoint.covDerivAdjoint`) — so by recursion every iterated covariant
> derivative of the field strength is an adjoint gauge tensor.

## ii. Key results

> - `TransformsInAdjoint.covDerivAdjoint` : adjoint gauge tensors are closed under the covariant
>   derivative: if `F` transforms in the adjoint, so does `∇_ρ F = [∂_ρ F] + ⁅A_ρ, F⁆`

## iv. References

> * None.

**`GaugeAlgebraRealization.TransformsInAdjoint`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/TransformsAdjoint.lean#L67).

> A family of derivative symbols `F` *transforms in the adjoint* (is an adjoint gauge
> tensor) for the gauge representation `repGauge` when each symbol `[∂_s F^φ]`
> transforms by the Leibniz convolution of the dual adjoint coefficients against lower
> symbols — the shape of `gauge_apply_deriv` with no Maurer–Cartan shift. At `s = 0`
> this is the homogeneous law `U • F^φ = F^{Ad₀^* φ}`.

```lean
def TransformsInAdjoint (repGauge : Representation ℂ GJ B)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B) : Prop
```

**`GaugeAlgebraRealization.TransformsInAdjoint.repGauge_zero`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/TransformsAdjoint.lean#L77).

> An adjoint gauge tensor transforms at the base point through the dual adjoint
> coefficient of the value of the gauge jet alone: the antidiagonal of the empty multiset
> has a single term.

```lean
lemma TransformsInAdjoint.repGauge_zero
    {F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B}
    (hF : TransformsInAdjoint jets repGauge F) (U : GJ) (φ : Module.Dual ℝ 𝔤) :
    repGauge U (F 0 φ) = F 0 (jets.adjointDualCoeff U⁻¹ 0 φ)
```

**`GaugeAlgebraRealization.bracketFamConv`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/TransformsAdjoint.lean#L93).

> **The derived bracket family** `⁅A_ρ, F⁆`: the `s`-derivative of the bracket of the
> gauge field against a family, given by the Leibniz convolution of the derivative
> symbols over the multiset antidiagonal.

```lean
noncomputable def bracketFamConv
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (ρ : Fin 1 ⊕ Fin 3)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (s : Multiset (Fin 1 ⊕ Fin 3)) : Module.Dual ℝ 𝔤 →ₗ[ℝ] B
```

**`GaugeAlgebraRealization.covDerivAdjoint`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/TransformsAdjoint.lean#L106).

> The covariant derivative `∇_ρ F = [∂_ρ F] + ⁅A_ρ, F⁆` of an adjoint-valued family
> of derivative symbols: the extra derivative on the symbol plus the derived bracket
> against the gauge field. The gauge-algebra bracket carries the physicists' `i`, so
> in matrix terms this is `∂_ρ F + i [A_ρ, F]` — the adjoint-representation covariant
> derivative in the same `D = ∂ + i A` convention as the field strength. It preserves
> `TransformsInAdjoint` (`TransformsInAdjoint.covDerivAdjoint`).

```lean
noncomputable def covDerivAdjoint
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (ρ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℝ 𝔤 →ₗ[ℝ] B
```

**`GaugeAlgebraRealization.covDerivAdjoint_apply`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/TransformsAdjoint.lean#L114).

```lean
lemma covDerivAdjoint_apply
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (ρ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ 𝔤) :
    covDerivAdjoint A F ρ s φ = F (ρ ::ₘ s) φ + bracketFamConv A ρ F s φ
```

**`GaugeAlgebraRealization.covDerivAdjoint_apply_of_map_lie`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/TransformsAdjoint.lean#L122).

> At a dual vector vanishing on every bracket the derived bracket term drops out and the
> covariant derivative is the ordinary one, `(∇_ρ F)^φ = ∂_ρ F^φ`.

```lean
lemma covDerivAdjoint_apply_of_map_lie {φ : Module.Dual ℝ 𝔤}
    (hφ : ∀ x y : 𝔤, φ ⁅x, y⁆ = 0)
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (ρ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    covDerivAdjoint A F ρ s φ = F (ρ ::ₘ s) φ
```

**`GaugeAlgebraRealization.bracketFamConv_map`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/TransformsAdjoint.lean#L131).

> The derived bracket family is natural in the algebra.

```lean
lemma bracketFamConv_map {B' : Type} [Ring B'] [Module ℝ B'] [SMulCommClass ℝ B' B']
    [IsScalarTower ℝ B' B'] (Φ : B →ₗ[ℝ] B') (hΦ : ∀ b₁ b₂, Φ (b₁ * b₂) = Φ b₁ * Φ b₂)
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (ρ : Fin 1 ⊕ Fin 3) (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (s : Multiset (Fin 1 ⊕ Fin 3)) :
    bracketFamConv (fun p σ => Φ ∘ₗ A p σ) ρ (fun p => Φ ∘ₗ F p) s =
      Φ ∘ₗ bracketFamConv A ρ F s
```

**`GaugeAlgebraRealization.covDerivAdjoint_map`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/TransformsAdjoint.lean#L148).

> The covariant derivative is natural in the algebra.

```lean
lemma covDerivAdjoint_map {B' : Type} [Ring B'] [Module ℝ B'] [SMulCommClass ℝ B' B']
    [IsScalarTower ℝ B' B'] (Φ : B →ₗ[ℝ] B') (hΦ : ∀ b₁ b₂, Φ (b₁ * b₂) = Φ b₁ * Φ b₂)
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (ρ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    covDerivAdjoint (fun p σ => Φ ∘ₗ A p σ) (fun p => Φ ∘ₗ F p) ρ s =
      Φ ∘ₗ covDerivAdjoint A F ρ s
```

## A. The iterated covariance of the covariant derivative

**`GaugeAlgebraRealization.TransformsInAdjoint.repGauge_cons`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/TransformsAdjoint.lean#L177).

> If `F` transforms in the adjoint, so do its `κ ::ₘ s`-derived symbols with the
> extra derivative traced through `LocalGaugeData.adjointDualCoeff_cons`: the Leibniz splittings
> where `κ` stays a derivative, minus the convolution where `κ` hits the adjoint —
> an `ad` of the derived Maurer–Cartan form.

```lean
lemma TransformsInAdjoint.repGauge_cons
    {F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B}
    (hF : TransformsInAdjoint jets repGauge F)
    (U : GJ) (κ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℝ 𝔤) :
    repGauge U (F (κ ::ₘ s) φ) =
      (s.antidiagonal.map fun p =>
        F (κ ::ₘ p.2) (jets.adjointDualCoeff U⁻¹ p.1 φ)).sum
      - (s.antidiagonal.map fun p =>
          (p.1.antidiagonal.map fun q =>
            F p.2 (jets.adjointDualCoeff U⁻¹ q.2
              (φ ∘ₗ LieAlgebra.ad ℝ 𝔤 (jets.evalLie
                (jets.iteratedDeriv q.1
                  (jets.maurerCartan U⁻¹ κ)))))).sum).sum
```

**`GaugeAlgebraRealization.TransformsInAdjoint.repGauge_bracketFamConv`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/TransformsAdjoint.lean#L213).

> The all-orders gauge transformation of the derived bracket `⁅A_ρ, F⁆` against an
> adjoint gauge tensor `F`: since `F` transforms homogeneously, only one `ad`
> cross-term convolution survives — the analogue of `repGauge_commutatorFam`
> with a gauge tensor in the second slot.

```lean
lemma TransformsInAdjoint.repGauge_bracketFamConv
    {F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B}
    (hF : TransformsInAdjoint jets repGauge F)
    (U : GJ) (s : Multiset (Fin 1 ⊕ Fin 3)) (ρ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) :
    repGauge U (bracketFamConv h.A ρ F s φ) =
      (s.antidiagonal.map fun p =>
        bracketFamConv h.A ρ F p.2 (jets.adjointDualCoeff U⁻¹ p.1 φ)).sum
      + (s.antidiagonal.map fun p =>
          (p.2.antidiagonal.map fun r =>
            F r.2 (jets.adjointDualCoeff U⁻¹ r.1
              (φ ∘ₗ LieAlgebra.ad ℝ 𝔤 (jets.evalLie
                (jets.iteratedDeriv p.1
                  (jets.maurerCartan U⁻¹ ρ)))))).sum).sum
```

**`GaugeAlgebraRealization.TransformsInAdjoint.covDerivAdjoint`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/TransformsAdjoint.lean#L306).

> **Adjoint gauge tensors are closed under the covariant derivative**: if `F`
> transforms in the adjoint, so does `∇_ρ F = [∂_ρ F] + ⁅A_ρ, F⁆`. The single
> inhomogeneous convolution of `[∂_{ρ ::ₘ s} F]`
> (`TransformsInAdjoint.repGauge_cons`) cancels the single `ad` cross-term
> convolution of `⁅A_ρ, F⁆` (`TransformsInAdjoint.repGauge_bracketFamConv`)
> through the coassociativity of the antidiagonal; no structural equation is needed.
> Together with `transformsInAdjoint_fieldStrength` this makes every iterated
> covariant derivative of the field strength an adjoint gauge tensor, by recursion.

```lean
lemma TransformsInAdjoint.covDerivAdjoint
    {F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B}
    (hF : TransformsInAdjoint jets repGauge F) (ρ : Fin 1 ⊕ Fin 3) :
    TransformsInAdjoint jets repGauge (GaugeAlgebraRealization.covDerivAdjoint h.A F ρ)
```

## Depends on

- [The gauge law on brackets and iterated derivatives](../part-01/gaugeboson-realization-gaugelaw.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/TransformsAdjoint.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/TransformsAdjoint.lean)
