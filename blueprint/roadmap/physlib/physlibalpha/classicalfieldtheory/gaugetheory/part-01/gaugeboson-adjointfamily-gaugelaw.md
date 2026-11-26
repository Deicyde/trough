---
declaration: module
origin: cited
lean: GaugeBoson.TransformsAsGaugeField, GaugeBoson.LorentzTransformsAsGaugeField, GaugeBoson.algebraMap_maurerCartan_structure, GaugeBoson.TransformsAsGaugeField.repGauge_cons, GaugeBoson.TransformsAsGaugeField.repGauge_commutatorFam, GaugeBoson.TransformsAsGaugeField.repGauge_fieldStrength, GaugeBoson.TransformsAsGaugeField.transformsInAdjoint_fieldStrength, GaugeBoson.TransformsInAdjoint.repGauge_bracketFamConv
statement: formalized
proof: formalized
---

# The gauge law of a gauge field and of its covariant expressions

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeBoson.AdjointFamily.GaugeLaw`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/GaugeLaw.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/GaugeLaw.lean): 14 declarations, 14 with a docstring.

> A family of gauge-field symbols transforming as a gauge field makes its field strength and the
> covariant derivatives of it transform in the adjoint.

## i. Overview

> A family `A` of symbols `∂_s A_μ^φ` in an algebra `B` transforms as a gauge field,
> `TransformsAsGaugeField`, when a jet `U` acts on `∂_s A_μ^φ` by the Leibniz convolution of the
> dual adjoint Taylor coefficients of `U⁻¹` against lower symbols, plus the base-point value of
> the `s`-th derivative of the Maurer–Cartan form of `U⁻¹`. This is the law that the symbols of
> the gauge-boson jet algebra satisfy (`LocalGaugeFieldAlgebra.transformsAsGaugeField_gaugeField`),
> and that their images under any algebra map intertwining the gauge actions inherit
> (`LocalGaugeFieldAlgebra.transformsAsGaugeField_mapGaugeField`). The Lorentz law of such a
> family is `LorentzTransformsAsGaugeField`.
>
> From the gauge law and the multiplicativity of the action on `B` alone, this file works out
> the action on the expressions built from the symbols. The derived commutators pick up `ad`
> cross terms and a constant bracket (`TransformsAsGaugeField.repGauge_commutatorFam`). In the
> field strength these cancel against the inhomogeneous terms of the derivative symbols, through
> the structural equation of the Maurer–Cartan form, so the field strength transforms in the
> adjoint at every derivative order. The covariant derivative preserves the adjoint law
> (`TransformsInAdjoint.covDerivAdjoint`), so every covariant derivative of the field strength
> transforms in the adjoint. A jet acts on the symmetrized derivatives by the symmetrized
> adjoint convolution plus a translation by its symmetrized Maurer–Cartan data.

## ii. Key results

> - `GaugeBoson.TransformsAsGaugeField` : the gauge law of a family of gauge-field symbols.
> - `GaugeBoson.LorentzTransformsAsGaugeField` : the Lorentz law of a family of gauge-field
>   symbols.
> - `GaugeBoson.TransformsAsGaugeField.repGauge_commutatorFam` : the gauge law of the derived
>   commutators.
> - `GaugeBoson.TransformsAsGaugeField.transformsInAdjoint_fieldStrength` : the field strength
>   transforms in the adjoint.
> - `GaugeBoson.TransformsInAdjoint.covDerivAdjoint` : the covariant derivative preserves the
>   adjoint law.
> - `GaugeBoson.TransformsAsGaugeField.transformsInAdjoint_iteratedCovDerivAdjoint` : every
>   covariant derivative of the field strength transforms in the adjoint.
> - `GaugeBoson.TransformsAsGaugeField.repGauge_symmetrizedDeriv_translation` : deep pure jets
>   act on the symmetrized derivatives by translations.

## iv. References

> * None.

## A. The gauge and Lorentz laws of a gauge field

**`GaugeBoson.TransformsAsGaugeField`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/GaugeLaw.lean#L90).

> A family `A` of gauge-field symbols `∂_s A_μ^φ` transforms as a gauge field under the
> representation `repGauge` of the jet gauge group. A jet `U` acts on `∂_s A_μ^φ` by the
> Leibniz convolution of the dual adjoint Taylor coefficients of `U⁻¹` against lower symbols,
> the multiset antidiagonal carrying the multinomial coefficients, plus the base-point value of
> the `s`-th derivative of the Maurer–Cartan form of `U⁻¹`.

```lean
def TransformsAsGaugeField (repGauge : Representation ℂ G.gaugeJetGroup B)
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) :
    Prop
```

**`GaugeBoson.LorentzTransformsAsGaugeField`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/GaugeLaw.lean#L102).

> A family `A` of gauge-field symbols transforms as a gauge field under the Lorentz
> representation `repLorentz`. The symbol carries one covector index, and each derivative slot
> transforms as a covector.

```lean
def LorentzTransformsAsGaugeField (repLorentz : Representation ℂ SL(2,ℂ) B)
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) :
    Prop
```

## B. The gauge law of the derived commutators

**`GaugeBoson.algebraMap_maurerCartan_structure`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/GaugeLaw.lean#L125).

> The structural equation of the Maurer–Cartan form of `U⁻¹`, at every derivative order, read
> through a dual vector into the scalars of `B`.

```lean
lemma algebraMap_maurerCartan_structure (U : G.gaugeJetGroup) (s : Multiset (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ G.lieSubalgebra) :
    algebraMap ℂ B (φ (G.evalLie (G.iteratedDerivJ (μ ::ₘ s) (-G.maurerCartan U⁻¹ ν)))) =
      algebraMap ℂ B (φ (G.evalLie (G.iteratedDerivJ (ν ::ₘ s) (-G.maurerCartan U⁻¹ μ))))
      - (s.antidiagonal.map fun p => algebraMap ℂ B (φ ⁅G.evalLie (G.iteratedDerivJ p.1
          (-G.maurerCartan U⁻¹ μ)), G.evalLie (G.iteratedDerivJ p.2
          (-G.maurerCartan U⁻¹ ν))⁆)).sum
```

**`GaugeBoson.TransformsAsGaugeField.repGauge_cons`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/GaugeLaw.lean#L145).

> The `κ ::ₘ s` case of the gauge law, with the extra derivative traced through. The result
> is the Leibniz splittings where `κ` stays a derivative, minus (by
> `GlobalGaugeGroup.adjointDualCoeff_cons`) the splittings where `κ` hits the adjoint, an
> `ad` of the derived Maurer–Cartan form, plus the derived Maurer–Cartan shift.

```lean
lemma TransformsAsGaugeField.repGauge_cons
    (U : G.gaugeJetGroup) (κ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (τ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ G.lieSubalgebra) :
    repGauge U (A (κ ::ₘ s) τ φ) =
      (s.antidiagonal.map fun p =>
        A (κ ::ₘ p.2) τ (G.adjointDualCoeff U⁻¹ p.1 φ)).sum
      - (s.antidiagonal.map fun p =>
          (p.1.antidiagonal.map fun q =>
            A p.2 τ (G.adjointDualCoeff U⁻¹ q.2
              (φ ∘ₗ LieAlgebra.ad ℝ G.lieSubalgebra (G.evalLie
                (G.iteratedDerivJ q.1
                  (-G.maurerCartan U⁻¹ κ)))))).sum).sum
      + algebraMap ℂ B (φ (G.evalLie (G.iteratedDerivJ (κ ::ₘ s)
          (-G.maurerCartan U⁻¹ τ))))
```

**`GaugeBoson.TransformsAsGaugeField.repGauge_commutatorFam`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/GaugeLaw.lean#L182).

> The all-orders gauge transformation of the derived commutator term. It is the Leibniz
> convolution of the transformed commutator, the two `ad` cross-term convolutions,
> and the convolution of Maurer–Cartan bracket shifts, at every derivative order
> simultaneously. The four-fold splitting is regrouped by `sum_bracketFam_conv_eq`.

```lean
lemma TransformsAsGaugeField.repGauge_commutatorFam
    (U : G.gaugeJetGroup) (s : Multiset (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    repGauge U (commutatorFam A μ ν s φ) =
      (s.antidiagonal.map fun p =>
        commutatorFam A μ ν p.2 (G.adjointDualCoeff U⁻¹ p.1 φ)).sum
      + (s.antidiagonal.map fun p =>
          (p.2.antidiagonal.map fun r =>
            A r.2 ν (G.adjointDualCoeff U⁻¹ r.1
              (φ ∘ₗ LieAlgebra.ad ℝ G.lieSubalgebra (G.evalLie
                (G.iteratedDerivJ p.1
                  (-G.maurerCartan U⁻¹ μ)))))).sum).sum
      - (s.antidiagonal.map fun p =>
          (p.1.antidiagonal.map fun q =>
            A q.2 μ (G.adjointDualCoeff U⁻¹ q.1
              (φ ∘ₗ LieAlgebra.ad ℝ G.lieSubalgebra (G.evalLie
                (G.iteratedDerivJ p.2
                  (-G.maurerCartan U⁻¹ ν)))))).sum).sum
      + (s.antidiagonal.map fun p =>
          algebraMap ℂ B (φ ⁅G.evalLie (G.iteratedDerivJ p.1
              (-G.maurerCartan U⁻¹ μ)),
            G.evalLie (G.iteratedDerivJ p.2
              (-G.maurerCartan U⁻¹ ν))⁆)).sum
```

## C. The field strength and its covariant derivatives transform in the adjoint

**`GaugeBoson.TransformsAsGaugeField.repGauge_fieldStrength`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/GaugeLaw.lean#L243).

> The field strength transforms in the adjoint, at every derivative order. Under a gauge
> jet `U` every derivative symbol of `F_μν` transforms by the pure Leibniz convolution of the
> dual adjoint action over the multiset antidiagonal. This is the gauge law of the symbols
> with no Maurer–Cartan shift, since the field strength transforms homogeneously. The
> `κ`-into-the-adjoint splittings of the derivative terms (`TransformsAsGaugeField.repGauge_cons`)
> cancel the `ad` cross-term convolutions of the commutator
> (`TransformsAsGaugeField.repGauge_commutatorFam`) through the coassociativity and swap of
> the antidiagonal, and the derived Maurer–Cartan shifts cancel the bracket-shift
> convolution through the all-orders structural equation.

```lean
lemma TransformsAsGaugeField.repGauge_fieldStrength
    (U : G.gaugeJetGroup) (s : Multiset (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    repGauge U (fieldStrength A μ ν s φ) =
      (s.antidiagonal.map fun p =>
        fieldStrength A μ ν p.2 (G.adjointDualCoeff U⁻¹ p.1 φ)).sum
```

**`GaugeBoson.TransformsAsGaugeField.transformsInAdjoint_fieldStrength`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/GaugeLaw.lean#L297).

> The field strength is an adjoint gauge tensor. This packages
> `TransformsAsGaugeField.repGauge_fieldStrength` as `TransformsInAdjoint`, the base case of
> the covariant-derivative recursion `TransformsInAdjoint.covDerivAdjoint`.

```lean
lemma TransformsAsGaugeField.transformsInAdjoint_fieldStrength
    (μ ν : Fin 1 ⊕ Fin 3) : TransformsInAdjoint G repGauge (fieldStrength A μ ν)
```

**`GaugeBoson.TransformsInAdjoint.repGauge_bracketFamConv`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/GaugeLaw.lean#L306).

> The all-orders gauge transformation of the derived bracket `⁅A_ρ, F⁆` against an
> adjoint gauge tensor `F`. Since `F` transforms homogeneously, only one `ad` cross-term
> convolution survives. This is the analogue of `TransformsAsGaugeField.repGauge_commutatorFam`
> with a gauge tensor in the second slot.

```lean
lemma TransformsInAdjoint.repGauge_bracketFamConv
    {F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B}
    (hF : TransformsInAdjoint G repGauge F)
    (U : G.gaugeJetGroup) (s : Multiset (Fin 1 ⊕ Fin 3)) (ρ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    repGauge U (bracketFamConv A ρ F s φ) =
      (s.antidiagonal.map fun p =>
        bracketFamConv A ρ F p.2 (G.adjointDualCoeff U⁻¹ p.1 φ)).sum
      + (s.antidiagonal.map fun p =>
          (p.2.antidiagonal.map fun r =>
            F r.2 (G.adjointDualCoeff U⁻¹ r.1
              (φ ∘ₗ LieAlgebra.ad ℝ G.lieSubalgebra (G.evalLie
                (G.iteratedDerivJ p.1
                  (-G.maurerCartan U⁻¹ ρ)))))).sum).sum
```

**`GaugeBoson.TransformsInAdjoint.covDerivAdjoint`**, a lemma, [line 354](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/GaugeLaw.lean#L354).

> Adjoint gauge tensors are closed under the covariant derivative. If `F` transforms in the
> adjoint, so does `∇_ρ F = [∂_ρ F] + ⁅A_ρ, F⁆`. The single inhomogeneous convolution of
> `[∂_{ρ ::ₘ s} F]` (`TransformsInAdjoint.repGauge_cons`) cancels the single `ad` cross-term
> convolution of `⁅A_ρ, F⁆` (`TransformsInAdjoint.repGauge_bracketFamConv`) through the
> coassociativity of the antidiagonal, and no structural equation is needed. Together with
> `TransformsAsGaugeField.transformsInAdjoint_fieldStrength` this makes every iterated
> covariant derivative of the field strength an adjoint gauge tensor, by recursion.

```lean
lemma TransformsInAdjoint.covDerivAdjoint
    {F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B}
    (hF : TransformsInAdjoint G repGauge F) (ρ : Fin 1 ⊕ Fin 3) :
    TransformsInAdjoint G repGauge (GaugeBoson.covDerivAdjoint A F ρ)
```

**`GaugeBoson.TransformsAsGaugeField.transformsInAdjoint_iteratedCovDerivAdjoint`**, a lemma, [line 395](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/GaugeLaw.lean#L395).

> Every iterated covariant derivative of the field strength is an adjoint gauge tensor, by
> the recursion of `TransformsInAdjoint.covDerivAdjoint` over the list of directions, from
> the base case `TransformsAsGaugeField.transformsInAdjoint_fieldStrength`.

```lean
lemma TransformsAsGaugeField.transformsInAdjoint_iteratedCovDerivAdjoint (l : List (Fin 1 ⊕ Fin 3))
    (ν lam : Fin 1 ⊕ Fin 3) :
    TransformsInAdjoint G repGauge
      (iteratedCovDerivAdjoint A l (fieldStrength A ν lam))
```

**`GaugeBoson.TransformsAsGaugeField.repGauge_fieldStrengthTower_of_mem_truncationKer_zero`**, a lemma, [line 405](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/GaugeLaw.lean#L405).

> The covariant derivatives of the field strength are invariant under the pure jets.

```lean
lemma TransformsAsGaugeField.repGauge_fieldStrengthTower_of_mem_truncationKer_zero
    (U : G.truncationKer 0)
    (l : List (Fin 1 ⊕ Fin 3)) (ν lam : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ G.lieSubalgebra) :
    repGauge U.1 (iteratedCovDerivAdjoint A l (fieldStrength A ν lam) 0 φ) =
      iteratedCovDerivAdjoint A l (fieldStrength A ν lam) 0 φ
```

## D. The gauge action on the symmetrized derivatives

**`GaugeBoson.TransformsAsGaugeField.repGauge_symmetrizedDeriv`**, a lemma, [line 427](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/GaugeLaw.lean#L427).

> The gauge transformation of the symmetrized derivatives. Averaging the gauge law of the
> individual derivative symbols over the multiset `s`, the homogeneous part is the
> symmetrized adjoint convolution, and the inhomogeneous Maurer–Cartan shifts average to
> exactly the base-point value of the symmetrized Maurer–Cartan form of `U⁻¹`,
>
> `U • sym(∂_s A)^φ = (1/|s|) ∑_{μ ∈ s} ∑_{x+y=s−μ} ∂_y A_μ^{∂_x Ad*(U⁻¹) φ}`
> `                   + φ( sym(ω(U⁻¹))_s |₀ )`.

```lean
lemma TransformsAsGaugeField.repGauge_symmetrizedDeriv
    (U : G.gaugeJetGroup) (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ G.lieSubalgebra) :
    repGauge U (symmetrizedDeriv s A φ) =
      (1/(s.card : ℝ)) • (s.map fun μ =>
        ((s - {μ}).antidiagonal.map fun p =>
          A p.2 μ (G.adjointDualCoeff U⁻¹ p.1 φ)).sum).sum
      + algebraMap ℂ B (φ (G.evalLie (G.symmetrizedMaurerCartanForm U⁻¹ s)))
```

**`GaugeBoson.TransformsAsGaugeField.repGauge_symmetrizedDeriv_truncationKer`**, a lemma, [line 460](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/GaugeLaw.lean#L460).

> A pure jet acts on the symmetrized derivatives through the symmetrized Maurer–Cartan
> data. For a gauge jet `U` with identity value, the inhomogeneous shift of `sym(∂_s A)^φ`
> is the pairing of `φ` with the symmetrized Maurer–Cartan coefficient of `U⁻¹` at `s`, the
> very data that classifies pure jets.

```lean
lemma TransformsAsGaugeField.repGauge_symmetrizedDeriv_truncationKer
    (U : G.truncationKer 0) (s : Multiset (Fin 1 ⊕ Fin 3)) (hs : s ≠ 0)
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    repGauge U.1 (symmetrizedDeriv s A φ) =
      (1/(s.card : ℝ)) • (s.map fun μ =>
        ((s - {μ}).antidiagonal.map fun p =>
          A p.2 μ (G.adjointDualCoeff (U.1)⁻¹ p.1 φ)).sum).sum
      + algebraMap ℂ B (φ (G.symmetrizedMaurerCartanCoeff U⁻¹ ⟨s, hs⟩))
```

**`GaugeBoson.TransformsAsGaugeField.repGauge_symmetrizedDeriv_translation`**, a lemma, [line 476](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/GaugeLaw.lean#L476).

> Pure translation. When all positive dual adjoint coefficients of `U⁻¹` below the order
> of `s` vanish, the adjoint convolution in the transformation of the symmetrized symbol
> collapses to the symbol itself, and the action is a translation by the symmetrized
> Maurer–Cartan coefficient.

```lean
lemma TransformsAsGaugeField.repGauge_symmetrizedDeriv_translation
    (U : G.truncationKer 0) (s : Multiset (Fin 1 ⊕ Fin 3)) (hs : s ≠ 0)
    (hU : ∀ x : Multiset (Fin 1 ⊕ Fin 3), x ≠ 0 → x.card < s.card →
      G.adjointDualCoeff (U.1)⁻¹ x = 0)
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    repGauge U.1 (symmetrizedDeriv s A φ) =
      symmetrizedDeriv s A φ +
        algebraMap ℂ B (φ (G.symmetrizedMaurerCartanCoeff U⁻¹ ⟨s, hs⟩))
```

## Depends on

- [The group SL(2, ℂ) and it's relation to the Lorentz group](../../../../physlib/relativity/sl2c/basic.md)
- [The generation theorem for the gauge-field symbols](gaugeboson-adjointfamily-generation.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/GaugeLaw.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/GaugeLaw.lean)
