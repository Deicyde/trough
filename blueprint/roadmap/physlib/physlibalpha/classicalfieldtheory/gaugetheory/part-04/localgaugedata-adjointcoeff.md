---
declaration: module
origin: cited
lean: LocalGaugeData.adjointCoeff, LocalGaugeData.adjointCoeff_apply, LocalGaugeData.adjointCoeff_zero, LocalGaugeData.adjointCoeff_zero_of_eval_eq_one, LocalGaugeData.adjointCoeff_one, LocalGaugeData.adjointCoeff_lie, LocalGaugeData.deriv_adjoint_ofConstantLie, LocalGaugeData.adjointCoeff_cons
statement: formalized
proof: formalized
---

# The Taylor coefficients of the adjoint action

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.AdjointCoeff`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/AdjointCoeff.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/AdjointCoeff.lean): 19 declarations, 17 with a docstring.

## i. Overview

> A gauge jet `U` acts on the gauge algebra of jets by the adjoint action `Ad_U`. What the
> transformation law of a gauge field `A_μ ↦ Ad_U A_μ + ω_μ(U)` sees of `Ad_U`, after
> differentiating `x` times and evaluating at the base point, is the physicists'
> `∂_x (Ad_U)^a_b|₀`: a linear map `adjointCoeff U x : 𝔤 →ₗ[ℝ] 𝔤` on the constant gauge
> algebra, and its transpose `adjointDualCoeff U x` on the dual index carried by the field
> symbols. This file develops these coefficients for any package `jets`.
>
> The central result is the Taylor–Leibniz theorem `evalLie_iteratedDeriv_adjointJ`: the
> base-point Taylor coefficients of `Ad_U Y` for an arbitrary jet `Y` are the antidiagonal
> convolution of the coefficients of `Ad_U` with those of `Y`. For a matrix group it is the
> Leibniz rule for products of matrices of power series; here it is derived from the Leibniz
> rule `deriv_adjoint` for a single derivative, by induction on the number of derivatives.
> Its corollaries are the multiplicativity `adjointCoeff_mul` of the coefficients up to
> convolution, and the recursion `adjointCoeff_cons` expressing one more derivative of a
> coefficient through the Maurer–Cartan form.

## ii. Key results

> - `LocalGaugeData.adjointCoeff` : the coefficient `∂_x (Ad_U)|₀`, with its values
>   `adjointCoeff_zero` at the base point and `adjointCoeff_one` on the identity jet.
> - `LocalGaugeData.adjointCoeff_cons` : one more derivative of a coefficient is minus the
>   antidiagonal convolution of `ad` of the derived Maurer–Cartan form against lower
>   coefficients.
> - `LocalGaugeData.evalLie_iteratedDeriv_adjointJ` : the Taylor–Leibniz theorem.
> - `LocalGaugeData.adjointCoeff_mul` : the coefficients of a product are the convolution
>   of the coefficients of the factors.
> - `LocalGaugeData.adjointDualCoeff` : the transposed coefficients, with
>   `adjointDualCoeff_singleton`, `adjointDualCoeff_pair` and `adjointDualCoeff_cons`.

## iv. References

> * None.

## A. The adjoint Taylor coefficients

**`LocalGaugeData.adjointCoeff`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/AdjointCoeff.lean#L75).

> The physicists' `∂_x (Ad_U)^a_b|₀`: include a constant gauge algebra element into
> jets, act by the adjoint of `U`, differentiate `x` times, and evaluate at the base
> point. For `x = 0` this is the adjoint action of the value of `U`; for `x ≠ 0` it sees
> the derivatives of the gauge transformation.

```lean
noncomputable def adjointCoeff (U : GJ) (x : Multiset (Fin 1 ⊕ Fin 3)) : 𝔤 →ₗ[ℝ] 𝔤
```

**`LocalGaugeData.adjointCoeff_apply`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/AdjointCoeff.lean#L78).

```lean
lemma adjointCoeff_apply (U : GJ) (x : Multiset (Fin 1 ⊕ Fin 3)) (a : 𝔤) :
    jets.adjointCoeff U x a =
      jets.evalLie (jets.iteratedDeriv x (jets.adjointJ U (jets.ofConstantLie a)))
```

**`LocalGaugeData.adjointCoeff_zero`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/AdjointCoeff.lean#L84).

> The zeroth coefficient is the adjoint action of the value of the jet.

```lean
lemma adjointCoeff_zero (U : GJ) : jets.adjointCoeff U 0 = jets.adjoint (jets.eval U)
```

**`LocalGaugeData.adjointCoeff_zero_of_eval_eq_one`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/AdjointCoeff.lean#L89).

> A jet with trivial value has trivial zeroth coefficient.

```lean
lemma adjointCoeff_zero_of_eval_eq_one {U : GJ} (hU : jets.eval U = 1) :
    jets.adjointCoeff U 0 = LinearMap.id
```

**`LocalGaugeData.adjointCoeff_one`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/AdjointCoeff.lean#L94).

> The coefficients of the identity jet: only the base point survives.

```lean
lemma adjointCoeff_one (p : Multiset (Fin 1 ⊕ Fin 3)) :
    jets.adjointCoeff (1 : GJ) p = if p = 0 then LinearMap.id else 0
```

**`LocalGaugeData.adjointCoeff_lie`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/AdjointCoeff.lean#L106).

> The coefficients are derivations of the bracket up to convolution, by the iterated
> Leibniz rule for the jet bracket.

```lean
lemma adjointCoeff_lie (U : GJ) (x : Multiset (Fin 1 ⊕ Fin 3)) (a b : 𝔤) :
    jets.adjointCoeff U x ⁅a, b⁆ =
      (x.antidiagonal.map fun p => ⁅jets.adjointCoeff U p.1 a, jets.adjointCoeff U p.2 b⁆).sum
```

## B. The recursion through the Maurer–Cartan form

**`LocalGaugeData.deriv_adjoint_ofConstantLie`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/AdjointCoeff.lean#L124).

> One derivative of the adjoint action on a constant is minus the bracket with the
> Maurer–Cartan form: the Leibniz rule `deriv_adjoint` with the constant's derivative
> killed.

```lean
lemma deriv_adjoint_ofConstantLie (U : GJ) (μ : Fin 1 ⊕ Fin 3) (a : 𝔤) :
    jets.deriv μ (jets.adjointJ U (jets.ofConstantLie a)) =
      -⁅jets.maurerCartan U μ, jets.adjointJ U (jets.ofConstantLie a)⁆
```

**`LocalGaugeData.adjointCoeff_cons`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/AdjointCoeff.lean#L132).

> One more derivative of a coefficient: differentiating the adjoint once produces minus
> `ad` of the Maurer–Cartan form, and the remaining derivatives distribute over the bracket
> by the Leibniz rule.

```lean
lemma adjointCoeff_cons (U : GJ) (μ : Fin 1 ⊕ Fin 3) (x : Multiset (Fin 1 ⊕ Fin 3)) :
    jets.adjointCoeff U (μ ::ₘ x) =
      -((x.antidiagonal.map fun p =>
        LieAlgebra.ad ℝ 𝔤 (jets.evalLie (jets.iteratedDeriv p.1 (jets.maurerCartan U μ))) ∘ₗ
          jets.adjointCoeff U p.2).sum)
```

## C. The Taylor–Leibniz theorem

**`LocalGaugeData.evalLie_iteratedDeriv_adjoint_cons`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/AdjointCoeff.lean#L157).

> The inductive step of the Taylor–Leibniz theorem: the rule for `μ ::ₘ s` derivatives
> follows from the rule for every sub-multiset of `s`. Peeling off `∂_μ` by the Leibniz
> rule `deriv_adjoint` leaves `Ad_U (∂_μ Y)`, handled by the rule for `s`, and a bracket
> with the Maurer–Cartan form, handled by the rule for the parts of `s`; on the other side
> the coefficients at `μ ::ₘ p` unfold by `adjointCoeff_cons`, and the two triple sums
> agree by coassociativity of the antidiagonal.

```lean
lemma evalLie_iteratedDeriv_adjoint_cons (U : GJ) (μ : Fin 1 ⊕ Fin 3)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (Y : 𝔤J)
    (ih : ∀ t ≤ s, ∀ Z : 𝔤J, jets.evalLie (jets.iteratedDeriv t (jets.adjointJ U Z)) =
      (t.antidiagonal.map fun p =>
        jets.adjointCoeff U p.1 (jets.evalLie (jets.iteratedDeriv p.2 Z))).sum) :
    jets.evalLie (jets.iteratedDeriv (μ ::ₘ s) (jets.adjointJ U Y)) =
      ((μ ::ₘ s).antidiagonal.map fun p =>
        jets.adjointCoeff U p.1 (jets.evalLie (jets.iteratedDeriv p.2 Y))).sum
```

**`LocalGaugeData.evalLie_iteratedDeriv_adjointJ`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/AdjointCoeff.lean#L207).

> The Taylor–Leibniz theorem for the adjoint action: the base-point Taylor coefficients
> of `Ad_U Y` are the antidiagonal convolution of the coefficients `adjointCoeff U` of
> `Ad_U` with those of `Y`. For a matrix group this is the Leibniz rule for products of
> matrices of power series; here it follows from the single-derivative Leibniz rule
> `deriv_adjoint` by strong induction on the number of derivatives.

```lean
lemma evalLie_iteratedDeriv_adjointJ (U : GJ) (x : Multiset (Fin 1 ⊕ Fin 3)) (Y : 𝔤J) :
    jets.evalLie (jets.iteratedDeriv x (jets.adjointJ U Y)) =
      (x.antidiagonal.map fun p =>
        jets.adjointCoeff U p.1 (jets.evalLie (jets.iteratedDeriv p.2 Y))).sum
```

**`LocalGaugeData.evalLie_iteratedDeriv_adjoint_eq_zero`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/AdjointCoeff.lean#L232).

> The base-point Taylor data of `Ad_U Y` vanish up to a given order whenever those of
> `Y` do.

```lean
lemma evalLie_iteratedDeriv_adjoint_eq_zero (U : GJ) {Y : 𝔤J} {s : Multiset (Fin 1 ⊕ Fin 3)}
    (h : ∀ q ≤ s, jets.evalLie (jets.iteratedDeriv q Y) = 0) :
    jets.evalLie (jets.iteratedDeriv s (jets.adjointJ U Y)) = 0
```

**`LocalGaugeData.adjointCoeff_mul`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/AdjointCoeff.lean#L242).

> The coefficients are multiplicative up to convolution: the coefficient of a product of
> jets is the antidiagonal convolution of the coefficients of the factors.

```lean
lemma adjointCoeff_mul (U V : GJ) (x : Multiset (Fin 1 ⊕ Fin 3)) :
    jets.adjointCoeff (U * V) x =
      (x.antidiagonal.map fun p => jets.adjointCoeff U p.1 ∘ₗ jets.adjointCoeff V p.2).sum
```

## D. The dual coefficients

**`LocalGaugeData.adjointDualCoeff`**, a def, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/AdjointCoeff.lean#L260).

> The physicists' `∂_x (Ad_U)^a_b|₀` acting on the dual adjoint index of a gauge-field
> symbol: the transpose of `adjointCoeff U x`.

```lean
noncomputable def adjointDualCoeff (U : GJ) (x : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℝ 𝔤 →ₗ[ℝ] Module.Dual ℝ 𝔤
```

**`LocalGaugeData.adjointDualCoeff_apply`**, a lemma, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/AdjointCoeff.lean#L264).

```lean
lemma adjointDualCoeff_apply (U : GJ) (x : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ 𝔤)
    (a : 𝔤) : jets.adjointDualCoeff U x φ a = φ (jets.adjointCoeff U x a)
```

**`LocalGaugeData.adjointDualCoeff_zero`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/AdjointCoeff.lean#L269).

> The zeroth dual coefficient is the dual of the adjoint action of the value of the
> jet.

```lean
lemma adjointDualCoeff_zero (U : GJ) :
    jets.adjointDualCoeff U 0 = (jets.adjoint (jets.eval U)).dualMap
```

**`LocalGaugeData.adjointDualCoeff_zero_of_eval_eq_one`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/AdjointCoeff.lean#L274).

> A jet with trivial value has trivial zeroth dual coefficient.

```lean
lemma adjointDualCoeff_zero_of_eval_eq_one {U : GJ} (hU : jets.eval U = 1) :
    jets.adjointDualCoeff U 0 = LinearMap.id
```

**`LocalGaugeData.adjointDualCoeff_cons`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/AdjointCoeff.lean#L281).

> The dual form of `adjointCoeff_cons`: one more derivative of a dual coefficient is
> minus the antidiagonal convolution of lower dual coefficients against `ad` of the derived
> Maurer–Cartan form.

```lean
lemma adjointDualCoeff_cons (U : GJ) (μ : Fin 1 ⊕ Fin 3) (x : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℝ 𝔤) :
    jets.adjointDualCoeff U (μ ::ₘ x) φ =
      -((x.antidiagonal.map fun p =>
        jets.adjointDualCoeff U p.2 (φ ∘ₗ LieAlgebra.ad ℝ 𝔤
          (jets.evalLie (jets.iteratedDeriv p.1 (jets.maurerCartan U μ))))).sum)
```

**`LocalGaugeData.adjointDualCoeff_singleton`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/AdjointCoeff.lean#L298).

> The dual coefficient at a single derivative is minus the underived coefficient
> precomposed with `ad` of the base-point Maurer–Cartan form. This is what cancels the
> Leibniz cross terms of the gauge law against the commutator cross terms in the field
> strength.

```lean
lemma adjointDualCoeff_singleton (U : GJ) (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    jets.adjointDualCoeff U {μ} φ =
      -jets.adjointDualCoeff U 0 (φ ∘ₗ LieAlgebra.ad ℝ 𝔤
        (jets.evalLie (jets.maurerCartan U μ)))
```

**`LocalGaugeData.adjointDualCoeff_pair`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/AdjointCoeff.lean#L308).

> The dual coefficient at two derivatives: the underived coefficient against `ad` of the
> derived Maurer–Cartan form, and the once-derived coefficient against `ad` of the
> Maurer–Cartan form itself.

```lean
lemma adjointDualCoeff_pair (U : GJ) (ρ μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    jets.adjointDualCoeff U (ρ ::ₘ {μ}) φ =
      -jets.adjointDualCoeff U 0 (φ ∘ₗ LieAlgebra.ad ℝ 𝔤
        (jets.evalLie (jets.deriv ρ (jets.maurerCartan U μ))))
      - jets.adjointDualCoeff U {ρ} (φ ∘ₗ LieAlgebra.ad ℝ 𝔤
        (jets.evalLie (jets.maurerCartan U μ)))
```

## Depends on

- [Local gauge data](../../../../physlib/classicalfieldtheory/gaugetheory/localgaugedata-basic.md)

## Proof depends on

- [Local gauge data: further consequences of the laws](localgaugedata-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/AdjointCoeff.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/AdjointCoeff.lean)
