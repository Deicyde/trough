---
declaration: module
origin: cited
lean: GaugeBoson.adjointTransport, GaugeBoson.adjointTransport_mk_tmul, GaugeBoson.adjointTransport_one, GaugeBoson.adjointTransport_mul, GaugeBoson.dualMap_adjointTransport_componentDual, LocalGaugeFieldAlgebra.transportFun, LocalGaugeFieldAlgebra.transport, LocalGaugeFieldAlgebra.transport_basis_tmul
statement: formalized
proof: formalized
---

# The gauge action on the gauge-boson jet algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeBoson.LocalGauge.GaugeAction`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean): 36 declarations, 23 with a docstring.

## i. Overview

> A jet of gauge transformations `U` acts on the gauge field by
> `A_μ ↦ Ad_U A_μ + maurerCartan(U)_μ`, so on a component function `∂_s A_μ^φ` it acts affinely: the
> linear part is the all-orders Leibniz convolution of the Taylor coefficients of `Ad(U⁻¹)`
> against lower component functions, and the constant part is the Taylor coefficient of the
> Maurer–Cartan form of `U⁻¹`. The action extends to the whole jet algebra as the
> substitution homomorphism determined by this affine action on the generators.
>
> The linear part is built from the adjoint Taylor coefficients `LocalGaugeData.adjointCoeff` of
> the package, whose multiplicativity up to convolution is the Taylor–Leibniz theorem
> `LocalGaugeData.evalLie_iteratedDeriv_adjointJ`; it makes the transport multiplicative and
> gives the cocycle identity for the Maurer–Cartan shift.

## ii. Key results

> - `GaugeBoson.adjointTransport` : the adjoint Taylor coefficients on the target space.
> - `LocalGaugeFieldAlgebra.transport` : the linear part of the gauge action on the component
>   space.
> - `LocalGaugeFieldAlgebra.mcShift` : the Maurer–Cartan shift.
> - `LocalGaugeFieldAlgebra.repJet` : the action of the jet gauge group on the jet algebra.
> - `LocalGaugeFieldAlgebra.repJet_iteratedJetDeriv_ofA` : the transformation law of the derivative
>   generators, in the form used by `GaugeAlgebraRealization`.
> - `LocalGaugeFieldAlgebra.complexRepJet` : the action on the complexified jet algebra.

## iv. References

> * None.

## A. The transport on the component space

**`GaugeBoson.adjointTransport`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L79).

> The adjoint transport on the gauge-boson target space at `p` derivatives: the adjoint
> Taylor coefficient on the gauge-algebra factor, the identity on the spacetime index.

```lean
noncomputable def adjointTransport (U : GJ) (p : Multiset (Fin 1 ⊕ Fin 3)) :
    (GaugeBoson 𝔤) →ₗ[ℝ] (GaugeBoson 𝔤)
```

**`GaugeBoson.adjointTransport_mk_tmul`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L86).

```lean
lemma adjointTransport_mk_tmul (U : GJ) (p : Multiset (Fin 1 ⊕ Fin 3))
    (v : Lorentz.CoVector) (a : 𝔤) :
    adjointTransport jets U p ⟨v ⊗ₜ[ℝ] a⟩ = ⟨v ⊗ₜ[ℝ] jets.adjointCoeff U p a⟩
```

**`GaugeBoson.adjointTransport_one`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L92).

> The adjoint transport at the identity: only the base point survives.

```lean
lemma adjointTransport_one (p : Multiset (Fin 1 ⊕ Fin 3)) :
    adjointTransport jets 1 p = if p = 0 then LinearMap.id else 0
```

**`GaugeBoson.adjointTransport_mul`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L110).

> The adjoint transport of a product: the antidiagonal convolution of transports.

```lean
lemma adjointTransport_mul (U V : GJ) (p : Multiset (Fin 1 ⊕ Fin 3)) :
    adjointTransport jets (U * V) p
      = (p.antidiagonal.map fun r =>
          adjointTransport jets U r.1 ∘ₗ adjointTransport jets V r.2).sum
```

**`GaugeBoson.dualMap_adjointTransport_componentDual`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L138).

> The dual transport carries a component covector to the component covector of the
> transported adjoint index: the spacetime slot is untouched.

```lean
lemma dualMap_adjointTransport_componentDual (U : GJ)
    (p : Multiset (Fin 1 ⊕ Fin 3)) (ω : Module.Dual ℝ Lorentz.CoVector)
    (φ : Module.Dual ℝ 𝔤) :
    (adjointTransport jets U p).dualMap ((componentDual 𝔤) ω φ)
      = (componentDual 𝔤) ω (φ ∘ₗ jets.adjointCoeff U p)
```

**`LocalGaugeFieldAlgebra.transportFun`**, a def, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L161).

> The value of the transport on the derivative symbol at `s`: the all-orders Leibniz
> convolution of the dual adjoint transports against lower derivative symbols.

```lean
noncomputable def transportFun (U : GJ) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℝ (GaugeBoson 𝔤) →ₗ[ℝ] (GaugeBoson.JetComponentSpace 𝔤)
```

**`LocalGaugeFieldAlgebra.transport`**, a def, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L172).

> The linear part of the gauge action on the jet component space: on a component
> function `∂_s A^ψ` it is the all-orders Leibniz convolution of the Taylor coefficients
> of the adjoint action of `U` against the lower component functions.

```lean
noncomputable def transport (U : GJ) :
    (GaugeBoson.JetComponentSpace 𝔤) →ₗ[ℝ] (GaugeBoson.JetComponentSpace 𝔤)
```

**`LocalGaugeFieldAlgebra.transport_basis_tmul`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L177).

```lean
lemma transport_basis_tmul (U : GJ) (s : Multiset (Fin 1 ⊕ Fin 3))
    (ψ : Module.Dual ℝ (GaugeBoson 𝔤)) :
    transport jets U (SpaceTimeDerivAlgebraℝ.basisMultiset s ⊗ₜ[ℝ] ψ)
      = (s.antidiagonal.map fun p =>
          SpaceTimeDerivAlgebraℝ.basisMultiset p.2 ⊗ₜ[ℝ]
            (GaugeBoson.adjointTransport jets U p.1).dualMap ψ).sum
```

**`GaugeBoson.JetComponentSpace.ext_of_basis`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L190).

> Two maps out of the jet component space agree if they agree on the components
> `∂_s A^ψ` with `s` a derivative multiset and `ψ` an arbitrary covector.

```lean
lemma _root_.GaugeBoson.JetComponentSpace.ext_of_basis
    {M : Type*} [AddCommMonoid M] [Module ℝ M]
    {F G : (GaugeBoson.JetComponentSpace 𝔤) →ₗ[ℝ] M}
    (h : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (ψ : Module.Dual ℝ (GaugeBoson 𝔤)),
      F (SpaceTimeDerivAlgebraℝ.basisMultiset s ⊗ₜ[ℝ] ψ)
        = G (SpaceTimeDerivAlgebraℝ.basisMultiset s ⊗ₜ[ℝ] ψ)) : F = G
```

**`LocalGaugeFieldAlgebra.transport_one`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L211).

> The transport of the identity is the identity.

```lean
lemma transport_one : transport jets (1 : GJ) = LinearMap.id
```

**`LocalGaugeFieldAlgebra.transport_mul`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L230).

> The transport is an anti-homomorphism: the transport of a product is the reverse
> composite. Composed with the inverse, it becomes the linear part of the gauge
> representation.

```lean
lemma transport_mul (U V : GJ) :
    transport jets (U * V) = transport jets V ∘ₗ transport jets U
```

## B. The Maurer–Cartan shift

**`LocalGaugeFieldAlgebra.mcBosonCoeff`**, a def, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L285).

> The Taylor coefficient of the Maurer–Cartan form of `U` at the derivative multiset
> `s`, packaged as a gauge boson: the spacetime index runs over the coordinate
> directions, the adjoint index over the base-point Taylor coefficients of the
> Maurer–Cartan form.

```lean
noncomputable def mcBosonCoeff (U : GJ) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    (GaugeBoson 𝔤)
```

**`LocalGaugeFieldAlgebra.mcBosonCoeff_one`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L292).

```lean
lemma mcBosonCoeff_one (s : Multiset (Fin 1 ⊕ Fin 3)) : mcBosonCoeff jets 1 s = 0
```

**`LocalGaugeFieldAlgebra.mcBosonCoeff_mul`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L302).

> The Maurer–Cartan Taylor coefficients of a product: the cocycle identity, with the
> adjoint transport convoluted in by the Taylor–Leibniz theorem.

```lean
lemma mcBosonCoeff_mul (U V : GJ) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    mcBosonCoeff jets (U * V) s
      = mcBosonCoeff jets U s
        + (s.antidiagonal.map fun p =>
            GaugeBoson.adjointTransport jets U p.1 (mcBosonCoeff jets V p.2)).sum
```

**`LocalGaugeFieldAlgebra.mcShift`**, a def, [line 356](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L356).

> The Maurer–Cartan shift: the linear functional on the component space pairing a
> component `∂_s A^ψ` with the Taylor coefficient of the Maurer–Cartan form of `U`. It is
> the constant part of the affine gauge action.

```lean
noncomputable def mcShift (U : GJ) : (GaugeBoson.JetComponentSpace 𝔤) →ₗ[ℝ] ℝ
```

**`LocalGaugeFieldAlgebra.mcShift_basis_tmul`**, a lemma, [line 361](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L361).

```lean
lemma mcShift_basis_tmul (U : GJ) (s : Multiset (Fin 1 ⊕ Fin 3))
    (ψ : Module.Dual ℝ (GaugeBoson 𝔤)) :
    mcShift jets U (SpaceTimeDerivAlgebraℝ.basisMultiset s ⊗ₜ[ℝ] ψ)
      = ψ (mcBosonCoeff jets U s)
```

**`LocalGaugeFieldAlgebra.mcShift_one`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L370).

```lean
lemma mcShift_one : mcShift jets (1 : GJ) = 0
```

**`LocalGaugeFieldAlgebra.mcShift_mul`**, a lemma, [line 376](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L376).

> The cocycle identity for the Maurer–Cartan shift.

```lean
lemma mcShift_mul (U V : GJ) :
    mcShift jets (U * V) = mcShift jets V ∘ₗ transport jets U + mcShift jets U
```

## C. The action of the jet gauge group

**`LocalGaugeFieldAlgebra.gaugeGen`**, a def, [line 399](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L399).

> The affine action of a jet of gauge transformations on the generators of the jet
> algebra: the transported component plus the Maurer–Cartan shift, both of `U⁻¹` — the
> contragredient convention for an action on component functions.

```lean
noncomputable def gaugeGen (U : GJ) :
    (GaugeBoson.JetComponentSpace 𝔤) →ₗ[ℝ] (LocalGaugeFieldAlgebra 𝔤)
```

**`LocalGaugeFieldAlgebra.gaugeGen_apply`**, a lemma, [line 405](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L405).

```lean
lemma gaugeGen_apply (U : GJ) (x : (GaugeBoson.JetComponentSpace 𝔤)) :
    gaugeGen jets U x = SymmetricAlgebra.ι ℝ _ (transport jets U⁻¹ x)
      + algebraMap ℝ (LocalGaugeFieldAlgebra 𝔤) (mcShift jets U⁻¹ x)
```

**`LocalGaugeFieldAlgebra.repJet`**, a def, [line 413](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L413).

> The action of the jet gauge group on the gauge-boson jet algebra: the substitution
> homomorphism determined by the affine action on the generators, `∂_s A^ψ` going to its
> transported convolution plus the Maurer–Cartan shift of `U⁻¹`.

```lean
noncomputable def repJet : Representation ℝ GJ (LocalGaugeFieldAlgebra 𝔤)
```

**`LocalGaugeFieldAlgebra.repJetAlgHom`**, a def, [line 442](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L442).

> The action of `U` as an algebra homomorphism: a jet of gauge transformations acts on
> a Lagrangian term factor by factor.

```lean
noncomputable def repJetAlgHom (U : GJ) :
    (LocalGaugeFieldAlgebra 𝔤) →ₐ[ℝ] (LocalGaugeFieldAlgebra 𝔤)
```

**`LocalGaugeFieldAlgebra.repJet_ι`**, a lemma, [line 448](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L448).

```lean
lemma repJet_ι (U : GJ) (x : (GaugeBoson.JetComponentSpace 𝔤)) :
    repJet jets U (SymmetricAlgebra.ι ℝ _ x)
      = SymmetricAlgebra.ι ℝ _ (transport jets U⁻¹ x)
        + algebraMap ℝ (LocalGaugeFieldAlgebra 𝔤) (mcShift jets U⁻¹ x)
```

**`LocalGaugeFieldAlgebra.repJet_apply_one`**, a lemma, [line 458](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L458).

```lean
lemma repJet_apply_one (U : GJ) :
    repJet jets U (1 : (LocalGaugeFieldAlgebra 𝔤)) = 1
```

**`LocalGaugeFieldAlgebra.repJet_apply_mul`**, a lemma, [line 464](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L464).

```lean
lemma repJet_apply_mul (U : GJ) (x y : (LocalGaugeFieldAlgebra 𝔤)) :
    repJet jets U (x * y) = repJet jets U x * repJet jets U y
```

**`LocalGaugeFieldAlgebra.repJet_algebraMap`**, a lemma, [line 472](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L472).

```lean
lemma repJet_algebraMap (U : GJ) (r : ℝ) :
    repJet jets U (algebraMap ℝ (LocalGaugeFieldAlgebra 𝔤) r)
      = algebraMap ℝ (LocalGaugeFieldAlgebra 𝔤) r
```

### C.1. The transformation law of the generators

**`LocalGaugeFieldAlgebra.componentDual_dualBasis_mcBosonCoeff`**, a lemma, [line 488](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L488).

> The component covector at `μ` picks the `μ`-th Maurer–Cartan Taylor coefficient out
> of the shift.

```lean
lemma componentDual_dualBasis_mcBosonCoeff (W : GJ)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    (GaugeBoson.componentDual 𝔤) (Lorentz.CoVector.basis.dualBasis μ) φ (mcBosonCoeff jets W s)
      = φ (jets.evalLie (jets.iteratedDeriv s
          (jets.maurerCartan W μ)))
```

**`LocalGaugeFieldAlgebra.repJet_iteratedJetDeriv_ofA`**, a lemma, [line 513](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L513).

> The transformation law of the derivative generators, in the form used by
> `GaugeAlgebraRealization`: a jet of gauge transformations acts on `∂_s A_μ^φ` by the all-orders
> Leibniz convolution of the adjoint Taylor coefficients of `U⁻¹` against lower
> generators, plus the Taylor coefficient of the Maurer–Cartan form of `U⁻¹`.

```lean
lemma repJet_iteratedJetDeriv_ofA (U : GJ)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    repJet jets U ((iteratedJetDeriv 𝔤) s ((ofA 𝔤) μ φ))
      = (s.antidiagonal.map fun p =>
          (iteratedJetDeriv 𝔤) p.2 ((ofA 𝔤) μ (jets.adjointDualCoeff U⁻¹ p.1 φ))).sum
        + algebraMap ℝ (LocalGaugeFieldAlgebra 𝔤)
            (φ (jets.evalLie (jets.iteratedDeriv s
              (jets.maurerCartan U⁻¹ μ))))
```

### C.2. The complexified action

**`LocalGaugeFieldAlgebra.complexRepJet`**, a def, [line 538](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L538).

> The action of the jet gauge group on the complexified gauge-boson jet algebra, by
> base change.

```lean
noncomputable def complexRepJet :
    Representation ℂ GJ (ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra 𝔤))
```

**`LocalGaugeFieldAlgebra.complexRepJet_tmul`**, a lemma, [line 548](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L548).

```lean
lemma complexRepJet_tmul (U : GJ) (z : ℂ) (x : (LocalGaugeFieldAlgebra 𝔤)) :
    complexRepJet jets U (z ⊗ₜ[ℝ] x) = z ⊗ₜ[ℝ] repJet jets U x
```

**`LocalGaugeFieldAlgebra.complexRepJetAlgHom`**, a def, [line 554](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L554).

> The action of a jet on the complexified gauge-boson jet algebra, as an algebra
> endomorphism: the base change of `repJetAlgHom`.

```lean
noncomputable def complexRepJetAlgHom (U : GJ) :
    ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra 𝔤) →ₐ[ℂ] ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra 𝔤)
```

**`LocalGaugeFieldAlgebra.complexRepJet_apply`**, a lemma, [line 559](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L559).

```lean
lemma complexRepJet_apply (U : GJ) (x : ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra 𝔤)) :
    complexRepJet jets U x = complexRepJetAlgHom jets U x
```

**`LocalGaugeFieldAlgebra.complexRepJet_apply_mul`**, a lemma, [line 566](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L566).

```lean
lemma complexRepJet_apply_mul (U : GJ)
    (x y : ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra 𝔤)) :
    complexRepJet jets U (x * y)
      = complexRepJet jets U x * complexRepJet jets U y
```

**`LocalGaugeFieldAlgebra.iteratedD_complexJetDeriv_one_tmul`**, a lemma, [line 583](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L583).

> The iterated complexified derivative of a real element is the complexification of the
> iterated real derivative.

```lean
lemma iteratedD_complexJetDeriv_one_tmul (s : Multiset (Fin 1 ⊕ Fin 3))
    (x : (LocalGaugeFieldAlgebra 𝔤)) :
    Lorentz.iteratedD (complexJetDeriv 𝔤) complexJetDeriv_comm s ((1 : ℂ) ⊗ₜ[ℝ] x)
      = (1 : ℂ) ⊗ₜ[ℝ] (iteratedJetDeriv 𝔤) s x
```

**`LocalGaugeFieldAlgebra.one_tmul_algebraMap`**, a lemma, [line 595](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L595).

> A real scalar in the complexified jet algebra is the corresponding complex scalar.

```lean
lemma one_tmul_algebraMap (r : ℝ) :
    (1 : ℂ) ⊗ₜ[ℝ] (algebraMap ℝ (LocalGaugeFieldAlgebra 𝔤) r)
      = algebraMap ℂ (ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra 𝔤)) ((r : ℝ) : ℂ)
```

**`LocalGaugeFieldAlgebra.complexRepJet_iteratedD_one_tmul_ofA`**, a lemma, [line 607](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean#L607).

> The transformation law of the derivative generators on the complexification: the
> form consumed by the laws of a `GaugeAlgebraRealization`.

```lean
lemma complexRepJet_iteratedD_one_tmul_ofA (U : GJ)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    complexRepJet jets U (Lorentz.iteratedD (complexJetDeriv 𝔤) complexJetDeriv_comm s
        ((1 : ℂ) ⊗ₜ[ℝ] (ofA 𝔤) μ φ))
      = (s.antidiagonal.map fun p =>
          Lorentz.iteratedD (complexJetDeriv 𝔤) complexJetDeriv_comm p.2
            ((1 : ℂ) ⊗ₜ[ℝ] (ofA 𝔤) μ (jets.adjointDualCoeff U⁻¹ p.1 φ))).sum
        + algebraMap ℂ (ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra 𝔤))
            (((φ (jets.evalLie (jets.iteratedDeriv s
              (jets.maurerCartan U⁻¹ μ))) : ℝ)) : ℂ)
```

## Depends on

- [The formal total derivative on the gauge-boson jet algebra](gaugeboson-localgauge-jetderiv.md)
- [The Taylor coefficients of the adjoint action](../part-04/localgaugedata-adjointcoeff.md)
- [Class IsLorentzDeriv](../../../relativity/islorentzderiv.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeAction.lean)
