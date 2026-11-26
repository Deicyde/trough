---
declaration: module
origin: cited
lean: GlobalGaugeGroup.adjointCoeff, GlobalGaugeGroup.adjointCoeff_eq_evalLie, GlobalGaugeGroup.adjointCoeff_zero, GlobalGaugeGroup.adjointCoeff_zero_of_eval_eq_one, GlobalGaugeGroup.adjointCoeff_one, GlobalGaugeGroup.adjointCoeff_lie, GlobalGaugeGroup.adjointCoeff_cons, GlobalGaugeGroup.sum_antidiagonal_cons_adjointCoeff
statement: formalized
proof: formalized
---

# The Taylor coefficients of the adjoint action

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.AdjointCoeff`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/AdjointCoeff.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/AdjointCoeff.lean): 19 declarations, 17 with a docstring.

> The base-point derivatives of the adjoint action of a gauge jet on the Lie algebra.

## i. Overview

> A gauge jet `U` acts on the gauge algebra of jets by the adjoint action `Ad_U`. What the
> transformation law of a gauge field `A_μ ↦ Ad_U A_μ + ω_μ(U)` sees of `Ad_U`, after differentiating
> `x` times and evaluating at the base point, is the physicists' `∂_x (Ad_U)^a_b|₀`, a linear map
> `adjointCoeff U x : G.lieSubalgebra →ₗ[ℝ] G.lieSubalgebra` on the constant gauge algebra, and its
> transpose `adjointDualCoeff U x` on the dual index carried by the field symbols. This file develops
> these coefficients for any global gauge group `G`, through its jet operations `G.evalLie`,
> `G.iteratedDerivJ`, `G.adjointJ` and `G.ofConstantLie`.
>
> The central result is the Taylor–Leibniz theorem `evalLie_iteratedDerivJ_adjointJ`. The
> base-point Taylor coefficients of `Ad_U Y` for an arbitrary jet `Y` are the antidiagonal
> convolution of the coefficients of `Ad_U` with those of `Y`. For a matrix group it is the Leibniz
> rule for products of matrices of power series. Here it is derived from the Leibniz rule
> `derivJ_adjointJ` for a single derivative, by induction on the number of derivatives. Its
> corollaries are the multiplicativity `adjointCoeff_mul` of the coefficients up to convolution,
> and the recursion `adjointCoeff_cons` expressing one more derivative of a coefficient through the
> Maurer–Cartan form.

## ii. Key results

> - `GlobalGaugeGroup.adjointCoeff` : the coefficient `∂_x (Ad_U)|₀`, with its values
>   `adjointCoeff_zero` at the base point and `adjointCoeff_one` on the identity jet.
> - `GlobalGaugeGroup.adjointCoeff_cons` : one more derivative of a coefficient is minus the
>   antidiagonal convolution of `ad` of the derived form `−ω` against lower coefficients, where
>   `ω = (∂_μ U) U⁻¹` is the Maurer–Cartan form.
> - `GlobalGaugeGroup.evalLie_iteratedDerivJ_adjointJ` : the Taylor–Leibniz theorem.
> - `GlobalGaugeGroup.adjointCoeff_mul` : the coefficients of a product are the convolution
>   of the coefficients of the factors.
> - `GlobalGaugeGroup.adjointDualCoeff` : the transposed coefficients, with
>   `adjointDualCoeff_singleton`, `adjointDualCoeff_pair` and `adjointDualCoeff_cons`.

## iv. References

> * None.

## A. The adjoint Taylor coefficients

**`GlobalGaugeGroup.adjointCoeff`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/AdjointCoeff.lean#L76).

> The physicists' `∂_x (Ad_U)^a_b|₀`. Include a constant gauge algebra element into
> jets, act by the adjoint of `U`, differentiate `x` times, and evaluate at the base
> point. For `x = 0` this is the adjoint action of the value of `U`, and for `x ≠ 0` it sees
> the derivatives of the gauge transformation.

```lean
noncomputable def adjointCoeff (U : G.gaugeJetGroup) (x : Multiset (Fin 1 ⊕ Fin 3)) :
    G.lieSubalgebra →ₗ[ℝ] G.lieSubalgebra
```

**`GlobalGaugeGroup.adjointCoeff_eq_evalLie`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/AdjointCoeff.lean#L81).

```lean
lemma adjointCoeff_eq_evalLie (U : G.gaugeJetGroup) (x : Multiset (Fin 1 ⊕ Fin 3))
    (a : G.lieSubalgebra) :
    G.adjointCoeff U x a =
      G.evalLie (G.iteratedDerivJ x
        (G.adjointJ U (G.ofConstantLie a)))
```

**`GlobalGaugeGroup.adjointCoeff_zero`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/AdjointCoeff.lean#L89).

> The zeroth coefficient is the adjoint action of the value of the jet.

```lean
lemma adjointCoeff_zero (U : G.gaugeJetGroup) : G.adjointCoeff U 0 = G.adjointRep
    (G.evalGaugeJet U)
```

**`GlobalGaugeGroup.adjointCoeff_zero_of_eval_eq_one`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/AdjointCoeff.lean#L96).

> A jet with trivial value has trivial zeroth coefficient.

```lean
lemma adjointCoeff_zero_of_eval_eq_one {U : G.gaugeJetGroup} (hU : G.evalGaugeJet U = 1) :
    G.adjointCoeff U 0 = LinearMap.id
```

**`GlobalGaugeGroup.adjointCoeff_one`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/AdjointCoeff.lean#L101).

> The coefficients of the identity jet, of which only the base point survives.

```lean
lemma adjointCoeff_one (p : Multiset (Fin 1 ⊕ Fin 3)) :
    G.adjointCoeff (1 : G.gaugeJetGroup) p = if p = 0 then LinearMap.id else 0
```

**`GlobalGaugeGroup.adjointCoeff_lie`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/AdjointCoeff.lean#L113).

> The coefficients are derivations of the bracket up to convolution, by the iterated
> Leibniz rule for the jet bracket.

```lean
lemma adjointCoeff_lie (U : G.gaugeJetGroup) (x : Multiset (Fin 1 ⊕ Fin 3))
    (a b : G.lieSubalgebra) :
    G.adjointCoeff U x ⁅a, b⁆ =
      (x.antidiagonal.map fun p => ⁅G.adjointCoeff U p.1 a, G.adjointCoeff U p.2 b⁆).sum
```

## B. The recursion through the Maurer–Cartan form

**`GlobalGaugeGroup.adjointCoeff_cons`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/AdjointCoeff.lean#L133).

> One more derivative of a coefficient. Differentiating the adjoint once produces minus
> `ad` of the Maurer–Cartan form, and the remaining derivatives distribute over the bracket
> by the Leibniz rule.

```lean
lemma adjointCoeff_cons (U : G.gaugeJetGroup) (μ : Fin 1 ⊕ Fin 3) (x : Multiset (Fin 1 ⊕ Fin 3)) :
    G.adjointCoeff U (μ ::ₘ x) =
      -((x.antidiagonal.map fun p =>
        LieAlgebra.ad ℝ G.lieSubalgebra (G.evalLie
          (G.iteratedDerivJ p.1 (-G.maurerCartan U μ))) ∘ₗ
          G.adjointCoeff U p.2).sum)
```

## C. The Taylor–Leibniz theorem

**`GlobalGaugeGroup.sum_antidiagonal_cons_adjointCoeff`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/AdjointCoeff.lean#L158).

> The convolution of the adjoint coefficients with one more derivative. Splitting the
> antidiagonal of `μ ::ₘ s` by where `μ` goes, the terms with `μ` on the right are the
> convolution over `s` with `μ` added on the right, and those with `μ` on the left unfold by
> `adjointCoeff_cons`.

```lean
lemma sum_antidiagonal_cons_adjointCoeff (U : G.gaugeJetGroup) (μ : Fin 1 ⊕ Fin 3)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (y : Multiset (Fin 1 ⊕ Fin 3) → G.lieSubalgebra) :
    ((μ ::ₘ s).antidiagonal.map fun p => G.adjointCoeff U p.1 (y p.2)).sum =
      (s.antidiagonal.map fun p => G.adjointCoeff U p.1 (y (μ ::ₘ p.2))).sum
      - (s.antidiagonal.map fun p => (p.1.antidiagonal.map fun q =>
          ⁅G.evalLie (G.iteratedDerivJ q.1 (-G.maurerCartan U μ)),
            G.adjointCoeff U q.2 (y p.2)⁆).sum).sum
```

**`GlobalGaugeGroup.evalLie_iteratedDerivJ_adjoint_cons`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/AdjointCoeff.lean#L180).

> The inductive step of the Taylor–Leibniz theorem. The rule for `μ ::ₘ s` derivatives
> follows from the rule for every sub-multiset of `s`. Peeling off `∂_μ` by the Leibniz
> rule `derivJ_adjointJ` leaves `Ad_U (∂_μ Y)`, handled by the rule for `s`, and a bracket
> with the Maurer–Cartan form, handled by the rule for the parts of `s`. On the other side
> the coefficients at `μ ::ₘ p` unfold by `sum_antidiagonal_cons_adjointCoeff`, and the two
> triple sums agree by coassociativity of the antidiagonal.

```lean
lemma evalLie_iteratedDerivJ_adjoint_cons (U : G.gaugeJetGroup) (μ : Fin 1 ⊕ Fin 3)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (Y : G.jetLieSubalgebra)
    (ih : ∀ t ≤ s, ∀ Z : G.jetLieSubalgebra, G.evalLie
      (G.iteratedDerivJ t (G.adjointJ U Z)) =
      (t.antidiagonal.map fun p =>
        G.adjointCoeff U p.1 (G.evalLie
          (G.iteratedDerivJ p.2 Z))).sum) :
    G.evalLie (G.iteratedDerivJ (μ ::ₘ s)
      (G.adjointJ U Y)) =
      ((μ ::ₘ s).antidiagonal.map fun p =>
        G.adjointCoeff U p.1 (G.evalLie
          (G.iteratedDerivJ p.2 Y))).sum
```

**`GlobalGaugeGroup.evalLie_iteratedDerivJ_adjointJ`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/AdjointCoeff.lean#L230).

> The Taylor–Leibniz theorem for the adjoint action. The base-point Taylor coefficients
> of `Ad_U Y` are the antidiagonal convolution of the coefficients `adjointCoeff U` of
> `Ad_U` with those of `Y`. For a matrix group this is the Leibniz rule for products of
> matrices of power series. Here it follows from the single-derivative Leibniz rule
> `derivJ_adjointJ` by strong induction on the number of derivatives.

```lean
lemma evalLie_iteratedDerivJ_adjointJ (U : G.gaugeJetGroup)
    (x : Multiset (Fin 1 ⊕ Fin 3)) (Y : G.jetLieSubalgebra) :
    G.evalLie (G.iteratedDerivJ x (G.adjointJ U Y)) =
      (x.antidiagonal.map fun p =>
        G.adjointCoeff U p.1 (G.evalLie
          (G.iteratedDerivJ p.2 Y))).sum
```

**`GlobalGaugeGroup.evalLie_iteratedDerivJ_adjoint_eq_zero`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/AdjointCoeff.lean#L258).

> The base-point Taylor data of `Ad_U Y` vanish up to a given order whenever those of
> `Y` do.

```lean
lemma evalLie_iteratedDerivJ_adjoint_eq_zero (U : G.gaugeJetGroup)
    {Y : G.jetLieSubalgebra} {s : Multiset (Fin 1 ⊕ Fin 3)}
    (h : ∀ q ≤ s, G.evalLie (G.iteratedDerivJ q Y) = 0) :
    G.evalLie (G.iteratedDerivJ s (G.adjointJ U Y))
      = 0
```

**`GlobalGaugeGroup.adjointCoeff_mul`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/AdjointCoeff.lean#L270).

> The coefficients are multiplicative up to convolution. The coefficient of a product of
> jets is the antidiagonal convolution of the coefficients of the factors.

```lean
lemma adjointCoeff_mul (U V : G.gaugeJetGroup) (x : Multiset (Fin 1 ⊕ Fin 3)) :
    G.adjointCoeff (U * V) x =
      (x.antidiagonal.map fun p => G.adjointCoeff U p.1 ∘ₗ G.adjointCoeff V p.2).sum
```

## D. The dual coefficients

**`GlobalGaugeGroup.adjointDualCoeff`**, a def, [line 288](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/AdjointCoeff.lean#L288).

> The physicists' `∂_x (Ad_U)^a_b|₀` acting on the dual adjoint index of a gauge-field
> symbol, the transpose of `adjointCoeff U x`.

```lean
noncomputable def adjointDualCoeff (U : G.gaugeJetGroup) (x : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] Module.Dual ℝ G.lieSubalgebra
```

**`GlobalGaugeGroup.adjointDualCoeff_apply`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/AdjointCoeff.lean#L292).

```lean
lemma adjointDualCoeff_apply (U : G.gaugeJetGroup) (x : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℝ G.lieSubalgebra)
    (a : G.lieSubalgebra) : G.adjointDualCoeff U x φ a = φ (G.adjointCoeff U x a)
```

**`GlobalGaugeGroup.adjointDualCoeff_zero_evalGaugeJet`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/AdjointCoeff.lean#L298).

> The zeroth dual coefficient is the dual of the adjoint action of the value of the
> jet.

```lean
lemma adjointDualCoeff_zero_evalGaugeJet (U : G.gaugeJetGroup) :
    G.adjointDualCoeff U 0 = (G.adjointRep (G.evalGaugeJet U)).dualMap
```

**`GlobalGaugeGroup.adjointDualCoeff_zero_of_evalGaugeJet_eq_one`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/AdjointCoeff.lean#L303).

> A jet with trivial value has trivial zeroth dual coefficient.

```lean
lemma adjointDualCoeff_zero_of_evalGaugeJet_eq_one {U : G.gaugeJetGroup}
    (hU : G.evalGaugeJet U = 1) :
    G.adjointDualCoeff U 0 = LinearMap.id
```

**`GlobalGaugeGroup.adjointDualCoeff_cons`**, a lemma, [line 311](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/AdjointCoeff.lean#L311).

> The dual form of `adjointCoeff_cons`. One more derivative of a dual coefficient is
> minus the antidiagonal convolution of lower dual coefficients against `ad` of the derived
> Maurer–Cartan form.

```lean
lemma adjointDualCoeff_cons (U : G.gaugeJetGroup) (μ : Fin 1 ⊕ Fin 3) (x : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    G.adjointDualCoeff U (μ ::ₘ x) φ =
      -((x.antidiagonal.map fun p =>
        G.adjointDualCoeff U p.2 (φ ∘ₗ LieAlgebra.ad ℝ G.lieSubalgebra
          (G.evalLie (G.iteratedDerivJ p.1
            (-G.maurerCartan U μ))))).sum)
```

**`GlobalGaugeGroup.adjointDualCoeff_singleton`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/AdjointCoeff.lean#L329).

> The dual coefficient at a single derivative is minus the underived coefficient
> precomposed with `ad` of the base-point Maurer–Cartan form. This is what cancels the
> Leibniz cross terms of the gauge law against the commutator cross terms in the field
> strength.

```lean
lemma adjointDualCoeff_singleton (U : G.gaugeJetGroup) (μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    G.adjointDualCoeff U {μ} φ =
      -G.adjointDualCoeff U 0 (φ ∘ₗ LieAlgebra.ad ℝ G.lieSubalgebra
        (G.evalLie (-G.maurerCartan U μ)))
```

**`GlobalGaugeGroup.adjointDualCoeff_pair`**, a lemma, [line 340](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/AdjointCoeff.lean#L340).

> The dual coefficient at two derivatives, the underived coefficient against `ad` of the
> derived Maurer–Cartan form, and the once-derived coefficient against `ad` of the
> Maurer–Cartan form itself.

```lean
lemma adjointDualCoeff_pair (U : G.gaugeJetGroup) (ρ μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    G.adjointDualCoeff U (ρ ::ₘ {μ}) φ =
      -G.adjointDualCoeff U 0 (φ ∘ₗ LieAlgebra.ad ℝ G.lieSubalgebra
        (G.evalLie (G.derivJ ρ (-G.maurerCartan U μ))))
      - G.adjointDualCoeff U {ρ} (φ ∘ₗ LieAlgebra.ad ℝ G.lieSubalgebra
        (G.evalLie (-G.maurerCartan U μ)))
```

## Depends on

- [The jet operations of a global gauge group](globalgaugegroup-jetoperations.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/AdjointCoeff.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/AdjointCoeff.lean)
