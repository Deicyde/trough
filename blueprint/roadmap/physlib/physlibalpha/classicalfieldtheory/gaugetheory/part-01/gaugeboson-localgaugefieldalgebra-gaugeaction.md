---
declaration: module
origin: cited
lean: GaugeBoson.adjointTransport, GaugeBoson.adjointTransport_mk_tmul, GaugeBoson.adjointTransport_one, GaugeBoson.adjointTransport_mul, GaugeBoson.dualMap_adjointTransport_componentDual, LocalGaugeFieldAlgebra.transportFun, LocalGaugeFieldAlgebra.transport, LocalGaugeFieldAlgebra.transport_basis_tmul
statement: formalized
proof: formalized
---

# The gauge action on the gauge-boson jet algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeBoson.LocalGaugeFieldAlgebra.GaugeAction`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean): 36 declarations, 23 with a docstring.

> The affine action of the gauge jets on the gauge field, extended to its jet algebra.

## i. Overview

> A jet of gauge transformations `U` acts on the gauge field by
> `A_μ ↦ Ad_U A_μ + maurerCartan(U)_μ`, so on a component function `∂_s A_μ^φ` it acts affinely.
> The linear part is the all-orders Leibniz convolution of the Taylor coefficients of `Ad(U⁻¹)`
> against lower component functions, and the constant part is the Taylor coefficient of the
> Maurer–Cartan form of `U⁻¹`. The action extends to the whole jet algebra as the
> substitution homomorphism determined by this affine action on the generators.
>
> The linear part is built from the adjoint Taylor coefficients `GlobalGaugeGroup.adjointCoeff` of
> the gauge group, whose multiplicativity up to convolution is the Taylor–Leibniz theorem
> `GlobalGaugeGroup.evalLie_iteratedDerivJ_adjointJ`. It makes the transport
> multiplicative and gives the cocycle identity for the Maurer–Cartan shift.

## ii. Key results

> - `GaugeBoson.adjointTransport` : the adjoint Taylor coefficients on the target space.
> - `LocalGaugeFieldAlgebra.transport` : the linear part of the gauge action on the component
>   space.
> - `LocalGaugeFieldAlgebra.maurerCartanShift` : the Maurer–Cartan shift.
> - `LocalGaugeFieldAlgebra.repJet` : the action of the jet gauge group on the jet algebra.
> - `LocalGaugeFieldAlgebra.repJet_iteratedJetDeriv_ofA` : the transformation law of the derivative
>   generators.
> - `LocalGaugeFieldAlgebra.complexRepJet` : the action on the complexified jet algebra.

## iv. References

> * None.

## A. The transport on the component space

**`GaugeBoson.adjointTransport`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L77).

> The adjoint transport on the gauge-boson target space at `p` derivatives, the adjoint
> Taylor coefficient on the gauge-algebra factor, the identity on the spacetime index.

```lean
noncomputable def adjointTransport (U : G.gaugeJetGroup) (p : Multiset (Fin 1 ⊕ Fin 3)) :
    (GaugeBoson G) →ₗ[ℝ] (GaugeBoson G)
```

**`GaugeBoson.adjointTransport_mk_tmul`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L83).

```lean
lemma adjointTransport_mk_tmul (U : G.gaugeJetGroup) (p : Multiset (Fin 1 ⊕ Fin 3))
    (v : Lorentz.CoVector) (a : G.lieSubalgebra) :
    adjointTransport G U p ⟨v ⊗ₜ[ℝ] a⟩ = ⟨v ⊗ₜ[ℝ] G.adjointCoeff U p a⟩
```

**`GaugeBoson.adjointTransport_one`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L88).

> The adjoint transport at the identity. Only the base point survives.

```lean
lemma adjointTransport_one (p : Multiset (Fin 1 ⊕ Fin 3)) :
    adjointTransport G 1 p = if p = 0 then LinearMap.id else 0
```

**`GaugeBoson.adjointTransport_mul`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L105).

> The adjoint transport of a product is the antidiagonal convolution of transports.

```lean
lemma adjointTransport_mul (U V : G.gaugeJetGroup) (p : Multiset (Fin 1 ⊕ Fin 3)) :
    adjointTransport G (U * V) p
      = (p.antidiagonal.map fun r =>
          adjointTransport G U r.1 ∘ₗ adjointTransport G V r.2).sum
```

**`GaugeBoson.dualMap_adjointTransport_componentDual`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L132).

> The dual transport carries a component covector to the component covector of the
> transported adjoint index. The spacetime slot is untouched.

```lean
lemma dualMap_adjointTransport_componentDual (U : G.gaugeJetGroup)
    (p : Multiset (Fin 1 ⊕ Fin 3)) (ω : Module.Dual ℝ Lorentz.CoVector)
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    (adjointTransport G U p).dualMap ((componentDual G) ω φ)
      = (componentDual G) ω (φ ∘ₗ G.adjointCoeff U p)
```

**`LocalGaugeFieldAlgebra.transportFun`**, a def, [line 155](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L155).

> The value of the transport on the derivative symbol at `s`, the all-orders Leibniz
> convolution of the dual adjoint transports against lower derivative symbols.

```lean
noncomputable def transportFun (U : G.gaugeJetGroup) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℝ (GaugeBoson G) →ₗ[ℝ] (GaugeBoson.FieldDerivSpace G)
```

**`LocalGaugeFieldAlgebra.transport`**, a def, [line 166](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L166).

> The linear part of the gauge action on the field-derivative space. On a component
> function `∂_s A^ψ` it is the all-orders Leibniz convolution of the Taylor coefficients
> of the adjoint action of `U` against the lower component functions.

```lean
noncomputable def transport (U : G.gaugeJetGroup) :
    (GaugeBoson.FieldDerivSpace G) →ₗ[ℝ] (GaugeBoson.FieldDerivSpace G)
```

**`LocalGaugeFieldAlgebra.transport_basis_tmul`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L170).

```lean
lemma transport_basis_tmul (U : G.gaugeJetGroup) (s : Multiset (Fin 1 ⊕ Fin 3))
    (ψ : Module.Dual ℝ (GaugeBoson G)) :
    transport G U (SpaceTimeDerivAlgebraℝ.basisMultiset s ⊗ₜ[ℝ] ψ)
      = (s.antidiagonal.map fun p =>
          SpaceTimeDerivAlgebraℝ.basisMultiset p.2 ⊗ₜ[ℝ]
            (GaugeBoson.adjointTransport G U p.1).dualMap ψ).sum
```

**`GaugeBoson.FieldDerivSpace.ext_of_basis`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L182).

> Two maps out of the field-derivative space agree if they agree on the components
> `∂_s A^ψ` with `s` a derivative multiset and `ψ` an arbitrary covector.

```lean
lemma _root_.GaugeBoson.FieldDerivSpace.ext_of_basis
    {M : Type*} [AddCommMonoid M] [Module ℝ M]
    {F₁ F₂ : (GaugeBoson.FieldDerivSpace G) →ₗ[ℝ] M}
    (h : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (ψ : Module.Dual ℝ (GaugeBoson G)),
      F₁ (SpaceTimeDerivAlgebraℝ.basisMultiset s ⊗ₜ[ℝ] ψ)
        = F₂ (SpaceTimeDerivAlgebraℝ.basisMultiset s ⊗ₜ[ℝ] ψ)) : F₁ = F₂
```

**`LocalGaugeFieldAlgebra.transport_one`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L202).

> The transport of the identity is the identity.

```lean
lemma transport_one : transport G (1 : G.gaugeJetGroup) = LinearMap.id
```

**`LocalGaugeFieldAlgebra.transport_mul`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L220).

> The transport is an anti-homomorphism. The transport of a product is the reverse
> composite. Composed with the inverse, it becomes the linear part of the gauge
> representation.

```lean
lemma transport_mul (U V : G.gaugeJetGroup) :
    transport G (U * V) = transport G V ∘ₗ transport G U
```

## B. The Maurer–Cartan shift

**`LocalGaugeFieldAlgebra.maurerCartanBosonCoeff`**, a def, [line 275](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L275).

> The Taylor coefficient of the Maurer–Cartan form of `U` at the derivative multiset
> `s`, packaged as a gauge boson. The spacetime index runs over the coordinate
> directions, and the adjoint index over the base-point Taylor coefficients of the
> Maurer–Cartan form.

```lean
noncomputable def maurerCartanBosonCoeff (U : G.gaugeJetGroup) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    (GaugeBoson G)
```

**`LocalGaugeFieldAlgebra.maurerCartanBosonCoeff_one`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L281).

```lean
lemma maurerCartanBosonCoeff_one (s : Multiset (Fin 1 ⊕ Fin 3)) :
    maurerCartanBosonCoeff G 1 s = 0
```

**`LocalGaugeFieldAlgebra.maurerCartanBosonCoeff_mul`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L291).

> The Maurer–Cartan Taylor coefficients of a product, given by the cocycle identity with the
> adjoint transport convoluted in by the Taylor–Leibniz theorem.

```lean
lemma maurerCartanBosonCoeff_mul (U V : G.gaugeJetGroup) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    maurerCartanBosonCoeff G (U * V) s
      = maurerCartanBosonCoeff G U s
        + (s.antidiagonal.map fun p =>
            GaugeBoson.adjointTransport G U p.1 (maurerCartanBosonCoeff G V p.2)).sum
```

**`LocalGaugeFieldAlgebra.maurerCartanShift`**, a def, [line 345](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L345).

> The Maurer–Cartan shift, the linear functional on the component space pairing a
> component `∂_s A^ψ` with the Taylor coefficient of the Maurer–Cartan form of `U`. It is
> the constant part of the affine gauge action.

```lean
noncomputable def maurerCartanShift (U : G.gaugeJetGroup) :
    (GaugeBoson.FieldDerivSpace G) →ₗ[ℝ] ℝ
```

**`LocalGaugeFieldAlgebra.maurerCartanShift_basis_tmul`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L350).

```lean
lemma maurerCartanShift_basis_tmul (U : G.gaugeJetGroup) (s : Multiset (Fin 1 ⊕ Fin 3))
    (ψ : Module.Dual ℝ (GaugeBoson G)) :
    maurerCartanShift G U (SpaceTimeDerivAlgebraℝ.basisMultiset s ⊗ₜ[ℝ] ψ)
      = ψ (maurerCartanBosonCoeff G U s)
```

**`LocalGaugeFieldAlgebra.maurerCartanShift_one`**, a lemma, [line 358](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L358).

```lean
lemma maurerCartanShift_one : maurerCartanShift G (1 : G.gaugeJetGroup) = 0
```

**`LocalGaugeFieldAlgebra.maurerCartanShift_mul`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L363).

> The cocycle identity for the Maurer–Cartan shift.

```lean
lemma maurerCartanShift_mul (U V : G.gaugeJetGroup) :
    maurerCartanShift G (U * V) =
      maurerCartanShift G V ∘ₗ transport G U + maurerCartanShift G U
```

## C. The action of the jet gauge group

**`LocalGaugeFieldAlgebra.gaugeGeneratorMap`**, a def, [line 387](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L387).

> The affine action of a jet of gauge transformations on the generators of the jet
> algebra, the transported component plus the Maurer–Cartan shift, both of `U⁻¹` — the
> contragredient convention for an action on component functions.

```lean
noncomputable def gaugeGeneratorMap (U : G.gaugeJetGroup) :
    (GaugeBoson.FieldDerivSpace G) →ₗ[ℝ] (LocalGaugeFieldAlgebra G)
```

**`LocalGaugeFieldAlgebra.gaugeGeneratorMap_apply`**, a lemma, [line 392](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L392).

```lean
lemma gaugeGeneratorMap_apply (U : G.gaugeJetGroup) (x : (GaugeBoson.FieldDerivSpace G)) :
    gaugeGeneratorMap G U x = SymmetricAlgebra.ι ℝ _ (transport G U⁻¹ x)
      + algebraMap ℝ (LocalGaugeFieldAlgebra G) (maurerCartanShift G U⁻¹ x)
```

**`LocalGaugeFieldAlgebra.repJet`**, a def, [line 400](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L400).

> The action of the jet gauge group on the gauge-boson jet algebra, the substitution
> homomorphism determined by the affine action on the generators, `∂_s A^ψ` going to its
> transported convolution plus the Maurer–Cartan shift of `U⁻¹`.

```lean
noncomputable def repJet : Representation ℝ G.gaugeJetGroup (LocalGaugeFieldAlgebra G)
```

**`LocalGaugeFieldAlgebra.repJetAlgHom`**, a def, [line 430](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L430).

> The action of `U` as an algebra homomorphism. A jet of gauge transformations acts on
> a Lagrangian term factor by factor.

```lean
noncomputable def repJetAlgHom (U : G.gaugeJetGroup) :
    (LocalGaugeFieldAlgebra G) →ₐ[ℝ] (LocalGaugeFieldAlgebra G)
```

**`LocalGaugeFieldAlgebra.repJet_ι`**, a lemma, [line 435](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L435).

```lean
lemma repJet_ι (U : G.gaugeJetGroup) (x : (GaugeBoson.FieldDerivSpace G)) :
    repJet G U (SymmetricAlgebra.ι ℝ _ x)
      = SymmetricAlgebra.ι ℝ _ (transport G U⁻¹ x)
        + algebraMap ℝ (LocalGaugeFieldAlgebra G) (maurerCartanShift G U⁻¹ x)
```

**`LocalGaugeFieldAlgebra.repJet_apply_one`**, a lemma, [line 444](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L444).

```lean
lemma repJet_apply_one (U : G.gaugeJetGroup) :
    repJet G U (1 : (LocalGaugeFieldAlgebra G)) = 1
```

**`LocalGaugeFieldAlgebra.repJet_apply_mul`**, a lemma, [line 449](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L449).

```lean
lemma repJet_apply_mul (U : G.gaugeJetGroup) (x y : (LocalGaugeFieldAlgebra G)) :
    repJet G U (x * y) = repJet G U x * repJet G U y
```

**`LocalGaugeFieldAlgebra.repJet_algebraMap`**, a lemma, [line 456](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L456).

```lean
lemma repJet_algebraMap (U : G.gaugeJetGroup) (r : ℝ) :
    repJet G U (algebraMap ℝ (LocalGaugeFieldAlgebra G) r)
      = algebraMap ℝ (LocalGaugeFieldAlgebra G) r
```

### C.1. The transformation law of the generators

**`LocalGaugeFieldAlgebra.componentDual_dualBasis_maurerCartanBosonCoeff`**, a lemma, [line 472](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L472).

> The component covector at `μ` picks the `μ`-th Maurer–Cartan Taylor coefficient out
> of the shift.

```lean
lemma componentDual_dualBasis_maurerCartanBosonCoeff (W : G.gaugeJetGroup)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ G.lieSubalgebra) :
    (GaugeBoson.componentDual G) (Lorentz.CoVector.basis.dualBasis μ) φ
        (maurerCartanBosonCoeff G W s)
      = φ (G.evalLie (G.iteratedDerivJ s
          (-G.maurerCartan W μ)))
```

**`LocalGaugeFieldAlgebra.repJet_iteratedJetDeriv_ofA`**, a lemma, [line 497](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L497).

> The transformation law of the derivative generators. A jet of gauge transformations acts on
> `∂_s A_μ^φ` by the all-orders
> Leibniz convolution of the adjoint Taylor coefficients of `U⁻¹` against lower
> generators, plus the Taylor coefficient of the Maurer–Cartan form of `U⁻¹`.

```lean
lemma repJet_iteratedJetDeriv_ofA (U : G.gaugeJetGroup)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ G.lieSubalgebra) :
    repJet G U ((iteratedJetDeriv G) s ((ofA G) μ φ))
      = (s.antidiagonal.map fun p =>
          (iteratedJetDeriv G) p.2 ((ofA G) μ (G.adjointDualCoeff U⁻¹ p.1 φ))).sum
        + algebraMap ℝ (LocalGaugeFieldAlgebra G)
            (φ (G.evalLie (G.iteratedDerivJ s
              (-G.maurerCartan U⁻¹ μ))))
```

### C.2. The complexified action

**`LocalGaugeFieldAlgebra.complexRepJet`**, a def, [line 522](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L522).

> The action of the jet gauge group on the complexified gauge-boson jet algebra, by
> base change.

```lean
noncomputable def complexRepJet :
    Representation ℂ G.gaugeJetGroup (ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra G))
```

**`LocalGaugeFieldAlgebra.complexRepJet_tmul`**, a lemma, [line 531](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L531).

```lean
lemma complexRepJet_tmul (U : G.gaugeJetGroup) (z : ℂ) (x : (LocalGaugeFieldAlgebra G)) :
    complexRepJet G U (z ⊗ₜ[ℝ] x) = z ⊗ₜ[ℝ] repJet G U x
```

**`LocalGaugeFieldAlgebra.complexRepJetAlgHom`**, a def, [line 537](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L537).

> The action of a jet on the complexified gauge-boson jet algebra, as an algebra
> endomorphism, the base change of `repJetAlgHom`.

```lean
noncomputable def complexRepJetAlgHom (U : G.gaugeJetGroup) :
    ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra G) →ₐ[ℂ] ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra G)
```

**`LocalGaugeFieldAlgebra.complexRepJet_apply`**, a lemma, [line 541](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L541).

```lean
lemma complexRepJet_apply (U : G.gaugeJetGroup) (x : ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra G)) :
    complexRepJet G U x = complexRepJetAlgHom G U x
```

**`LocalGaugeFieldAlgebra.complexRepJet_apply_mul`**, a lemma, [line 547](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L547).

```lean
lemma complexRepJet_apply_mul (U : G.gaugeJetGroup)
    (x y : ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra G)) :
    complexRepJet G U (x * y)
      = complexRepJet G U x * complexRepJet G U y
```

**`LocalGaugeFieldAlgebra.iteratedD_complexJetDeriv_one_tmul`**, a lemma, [line 555](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L555).

> The iterated complexified derivative of a real element is the complexification of the
> iterated real derivative.

```lean
lemma iteratedD_complexJetDeriv_one_tmul (s : Multiset (Fin 1 ⊕ Fin 3))
    (x : (LocalGaugeFieldAlgebra G)) :
    Lorentz.iteratedD (complexJetDeriv G) complexJetDeriv_comm s ((1 : ℂ) ⊗ₜ[ℝ] x)
      = (1 : ℂ) ⊗ₜ[ℝ] (iteratedJetDeriv G) s x
```

**`LocalGaugeFieldAlgebra.one_tmul_algebraMap`**, a lemma, [line 566](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L566).

> A real scalar in the complexified jet algebra is the corresponding complex scalar.

```lean
lemma one_tmul_algebraMap (r : ℝ) :
    (1 : ℂ) ⊗ₜ[ℝ] (algebraMap ℝ (LocalGaugeFieldAlgebra G) r)
      = algebraMap ℂ (ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra G)) ((r : ℝ) : ℂ)
```

**`LocalGaugeFieldAlgebra.complexRepJet_iteratedD_one_tmul_ofA`**, a lemma, [line 577](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean#L577).

> The transformation law of the derivative generators on the complexification, in the
> form of `GaugeBoson.TransformsAsGaugeField`.

```lean
lemma complexRepJet_iteratedD_one_tmul_ofA (U : G.gaugeJetGroup)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ G.lieSubalgebra) :
    complexRepJet G U (Lorentz.iteratedD (complexJetDeriv G) complexJetDeriv_comm s
        ((1 : ℂ) ⊗ₜ[ℝ] (ofA G) μ φ))
      = (s.antidiagonal.map fun p =>
          Lorentz.iteratedD (complexJetDeriv G) complexJetDeriv_comm p.2
            ((1 : ℂ) ⊗ₜ[ℝ] (ofA G) μ (G.adjointDualCoeff U⁻¹ p.1 φ))).sum
        + algebraMap ℂ (ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra G))
            (((φ (G.evalLie (G.iteratedDerivJ s
              (-G.maurerCartan U⁻¹ μ))) : ℝ)) : ℂ)
```

## Depends on

- [The formal total derivative on the gauge-boson jet algebra](gaugeboson-localgaugefieldalgebra-jetderiv.md)
- [The Taylor coefficients of the adjoint action](../part-02/globalgaugegroup-adjointcoeff.md)
- [Class IsLorentzDeriv](../../../relativity/islorentzderiv.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeAction.lean)
