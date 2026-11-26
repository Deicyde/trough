---
declaration: module
origin: cited
lean: GlobalGaugeGroup.IsInfinitesimalActionOf, GlobalGaugeGroup.IsInfinitesimalActionOf.repDualCoeff_cons, GlobalGaugeGroup.IsInfinitesimalActionOf.actionFam_repDualCoeff, GlobalGaugeGroup.IsInfinitesimalActionOf.repGauge_cons, GlobalGaugeGroup.IsInfinitesimalActionOf.sum_actionFam_conv_eq, GlobalGaugeGroup.IsInfinitesimalActionOf.repGauge_actionFamConv, GlobalGaugeGroup.IsInfinitesimalActionOf.repGauge_covDerivAction, GlobalGaugeGroup.IsInfinitesimalActionOf.repGauge_covDerivIter
statement: formalized
proof: formalized
---

# The infinitesimal action underlying a matter representation

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.InfinitesimalAction`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean): 27 declarations, 25 with a docstring.

> The compatibility of a Lie-algebra action with a jet representation, and the covariance of the
> covariant derivative it implies.

## i. Overview

> The covariant derivative `∇_ρ F = [∂_ρ F] + A_ρ · F` of a matter family is built from
> an action `act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V` of the gauge algebra on the value space. For the
> covariant derivative to transform covariantly, `act` must be the *infinitesimal action*
> underlying the representation `rep` of the jet gauge group in which the family
> transforms — the physicists' statement that the matrices `i dρ(T^a)` generate `rep`.
> This file packages that compatibility as the structure `IsInfinitesimalActionOf`, and
> proves the theorem it exists for. Call a family `F` of symbols a gauge tensor of `rep` when
> each derivative symbol `[∂_s F^φ]` transforms by the Leibniz convolution of the base-point
> Taylor coefficients of `rep` against the lower symbols, with no inhomogeneous term. Then the
> covariant derivative of a gauge tensor is again one,
> `IsInfinitesimalActionOf.repGauge_covDerivAction`, and by induction so is every iterated
> covariant derivative. The gauge field may be any family transforming as a gauge field,
> `GaugeBoson.TransformsAsGaugeField`, under an action of the jet gauge group by multiplicative
> maps.
>
> Everything is stated over a global gauge group `G : GlobalGaugeGroup κ`; nothing depends on the
> Standard Model choice of it. The last sections show that for a matter field `M` the Lie
> algebra action `M.repAlgebra` is the infinitesimal action underlying its jet action `M.repJet`,
> that pure jets act trivially at the base point, and record the condition that the gauge and
> Lorentz actions on the target space commute. This is `MatterField.GaugeLorentzCommute` for the
> group and `MatterField.GaugeLorentzCompatible` for the Lie algebra, and the first implies the
> second.

## ii. Key results

> - `GlobalGaugeGroup.IsInfinitesimalActionOf` : `act` is the infinitesimal action underlying
>   `rep`.
> - `GlobalGaugeGroup.IsInfinitesimalActionOf.repGauge_covDerivAction` : the covariant derivative
>   preserves the Leibniz transformation law of a family of symbols.
> - `GlobalGaugeGroup.IsInfinitesimalActionOf.repGauge_covDerivIter` : so does every iterated
>   covariant derivative, and `repGauge_covDerivIter_zero` is its underived symbol.
> - `GlobalGaugeGroup.IsInfinitesimalActionOf.conj` : the conjugate action underlies the
>   conjugate representation.
> - `GlobalGaugeGroup.IsInfinitesimalActionOf.eq_of_repCoeff_zero` : a fibrewise representation
>   is determined by its infinitesimal action and its base-point values.
> - `GlobalGaugeGroup.MatterField.isInfinitesimalActionOf` : `dρ` is the infinitesimal
>   action underlying the jet action of a matter field.
> - `GlobalGaugeGroup.repDualCoeff_inv_zero_eq_ofConstant_eval` : if pure jets act trivially at
>   the base point, the base-point action of a jet factors through its value.
> - `GlobalGaugeGroup.MatterField.repCoeff_zero_of_eval_eq_one` : pure jets act trivially
>   at the base point.
> - `GlobalGaugeGroup.MatterField.GaugeLorentzCommute`,
>   `GlobalGaugeGroup.MatterField.GaugeLorentzCompatible` : the gauge and Lorentz actions
>   commute, at the level of the group and of the Lie algebra.
> - `GlobalGaugeGroup.MatterField.GaugeLorentzCommute.gaugeLorentzCompatible` : the first
>   condition implies the second.

## iv. References

> * None.

## A. The infinitesimal action underlying a representation

**`GlobalGaugeGroup.IsInfinitesimalActionOf`**, a structure, [line 126](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L126).

> `act` is the *infinitesimal action* of the gauge algebra underlying the
> representation `rep` of the jet gauge group, when the base-point Taylor
> coefficients of `rep` satisfy the two laws forced by `rep` being generated by
> `act`.
>
> * `repCoeff_cons` is the Leibniz rule in the Maurer–Cartan form. Differentiating
>   the representation once produces minus the action of the Maurer–Cartan form,
>   with the remaining derivatives distributed over the antidiagonal (for the
>   adjoint representation this is `GlobalGaugeGroup.adjointCoeff_cons`);
> * `repCoeff_act` says that the transports of `rep` intertwine `act` with the adjoint
>   transports, as an antidiagonal convolution (for the adjoint representation this
>   is `GlobalGaugeGroup.adjointCoeff_lie`); at `x = 0` it is the classical equivariance
>   `rep(U)|₀ ∘ act c = act (Ad(U) c)|₀ ∘ rep(U)|₀`.
>
> These are exactly the identities consumed by the proof that the covariant
> derivative `covDerivAction` preserves the Leibniz transformation law of a family.

```lean
structure IsInfinitesimalActionOf (G : GlobalGaugeGroup κ)
    (act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V)
    (rep : Representation ℂ G.gaugeJetGroup (SpaceTimeAlgebra ⊗[ℂ] V)) : Prop where
  repCoeff_cons : ∀ (U : G.gaugeJetGroup) (μ : Fin 1 ⊕ Fin 3) (x : Multiset (Fin 1 ⊕ Fin 3)),
    repCoeff rep U (μ ::ₘ x) =
      -((x.antidiagonal.map fun p =>
        act (G.evalLie (G.iteratedDerivJ p.1
          (-G.maurerCartan U μ))) ∘ₗ
          repCoeff rep U p.2).sum)
  repCoeff_act : ∀ (U : G.gaugeJetGroup) (x : Multiset (Fin 1 ⊕ Fin 3)) (c : G.lieSubalgebra),
    repCoeff rep U x ∘ₗ act c =
      ((x.antidiagonal.map fun p =>
        act (G.adjointCoeff U p.1 c) ∘ₗ repCoeff rep U p.2).sum)
```

**`GlobalGaugeGroup.IsInfinitesimalActionOf.repDualCoeff_cons`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L143).

> The dual form of the Leibniz law. The once-more-derived dual coefficient is
> minus the antidiagonal convolution of dual coefficients against `act` of the
> derived Maurer–Cartan form — the analogue of `GlobalGaugeGroup.adjointDualCoeff_cons`.

```lean
lemma IsInfinitesimalActionOf.repDualCoeff_cons
    {act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V}
    {rep : Representation ℂ G.gaugeJetGroup (SpaceTimeAlgebra ⊗[ℂ] V)}
    (h : IsInfinitesimalActionOf G act rep) (U : G.gaugeJetGroup) (μ : Fin 1 ⊕ Fin 3)
    (x : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V) :
    repDualCoeff rep U (μ ::ₘ x) φ =
      -((x.antidiagonal.map fun p =>
        repDualCoeff rep U p.2 (φ ∘ₗ act (G.evalLie
          (G.iteratedDerivJ p.1 (-G.maurerCartan U μ))))).sum)
```

## B. The covariant derivative preserves the transformation law

**`GlobalGaugeGroup.IsInfinitesimalActionOf.actionFam_repDualCoeff`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L179).

> The action of families against the dual representation coefficients, the
> antidiagonal convolution mixing the adjoint transport on the field slot with the
> representation transport on the matter slot — the family-level form of
> `IsInfinitesimalActionOf.repCoeff_act`, and the analogue of
> `GaugeBoson.bracketFam_adjointDualCoeff`.

```lean
lemma IsInfinitesimalActionOf.actionFam_repDualCoeff
    (h : IsInfinitesimalActionOf G act rep) (U : G.gaugeJetGroup)
    (x : Multiset (Fin 1 ⊕ Fin 3)) (f : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (g : Module.Dual ℂ V →ₗ[ℂ] B) (φ : Module.Dual ℂ V) :
    actionFam act f g (repDualCoeff rep U x φ) =
      (x.antidiagonal.map fun p =>
        actionFam act (f ∘ₗ G.adjointDualCoeff U p.1)
          (g ∘ₗ repDualCoeff rep U p.2) φ).sum
```

**`GlobalGaugeGroup.IsInfinitesimalActionOf.repGauge_cons`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L211).

> If `F` transforms by the Leibniz law of `rep`, the transformation of its `κ ::ₘ s`-derived
> symbols has the extra derivative traced through `IsInfinitesimalActionOf.repDualCoeff_cons`,
> giving the Leibniz splittings where `κ` stays a derivative, minus the convolution where `κ`
> hits the representation, `act` of the derived Maurer–Cartan form.

```lean
lemma IsInfinitesimalActionOf.repGauge_cons (hact : IsInfinitesimalActionOf G act rep)
    {F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B}
    (hF : ∀ (U : G.gaugeJetGroup) (φ : Module.Dual ℂ V) (s : Multiset (Fin 1 ⊕ Fin 3)),
      repGauge U (F s φ) = (s.antidiagonal.map fun p => F p.2 (repDualCoeff rep U⁻¹ p.1 φ)).sum)
    (U : G.gaugeJetGroup) (κ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ V) :
    repGauge U (F (κ ::ₘ s) φ) =
      (s.antidiagonal.map fun p =>
        F (κ ::ₘ p.2) (repDualCoeff rep U⁻¹ p.1 φ)).sum
      - (s.antidiagonal.map fun p =>
          (p.1.antidiagonal.map fun q =>
            F p.2 (repDualCoeff rep U⁻¹ q.2
              (φ ∘ₗ act (G.evalLie (G.iteratedDerivJ q.1
                (-G.maurerCartan U⁻¹ κ)))))).sum).sum
```

**`GlobalGaugeGroup.IsInfinitesimalActionOf.sum_actionFam_conv_eq`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L245).

> The action of the transformed gauge-field symbols on the transformed matter symbols,
> summed over the antidiagonal, is the antidiagonal convolution of the derived action `A_ρ · F`
> against the dual representation coefficients. It is the homogeneous part of the
> transformation of `A_ρ · F`, rearranged by the coassociativity of the antidiagonal.

```lean
lemma IsInfinitesimalActionOf.sum_actionFam_conv_eq (hact : IsInfinitesimalActionOf G act rep)
    {F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B}
    (U : G.gaugeJetGroup) (s : Multiset (Fin 1 ⊕ Fin 3)) (ρ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ V) :
    (s.antidiagonal.map fun p =>
      actionFam act ((p.1.antidiagonal.map fun q =>
          A q.2 ρ ∘ₗ G.adjointDualCoeff U⁻¹ q.1).sum)
        ((p.2.antidiagonal.map fun r =>
          F r.2 ∘ₗ repDualCoeff rep U⁻¹ r.1).sum) φ).sum =
      (s.antidiagonal.map fun p =>
        actionFamConv A act ρ F p.2 (repDualCoeff rep U⁻¹ p.1 φ)).sum
```

**`GlobalGaugeGroup.IsInfinitesimalActionOf.repGauge_actionFamConv`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L298).

> The all-orders gauge transformation of the derived action `A_ρ · F` for `F`
> transforming by the Leibniz law of `rep`. Since `F` transforms homogeneously, only one
> cross-term convolution through `act` survives — the analogue of
> `GaugeBoson.TransformsInAdjoint.repGauge_bracketFamConv` with a matter field in the second
> slot.

```lean
lemma IsInfinitesimalActionOf.repGauge_actionFamConv (hact : IsInfinitesimalActionOf G act rep)
    {F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B}
    (hF : ∀ (U : G.gaugeJetGroup) (φ : Module.Dual ℂ V) (s : Multiset (Fin 1 ⊕ Fin 3)),
      repGauge U (F s φ) = (s.antidiagonal.map fun p => F p.2 (repDualCoeff rep U⁻¹ p.1 φ)).sum)
    (U : G.gaugeJetGroup) (s : Multiset (Fin 1 ⊕ Fin 3)) (ρ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ V) :
    repGauge U (actionFamConv A act ρ F s φ) =
      (s.antidiagonal.map fun p =>
        actionFamConv A act ρ F p.2 (repDualCoeff rep U⁻¹ p.1 φ)).sum
      + (s.antidiagonal.map fun p =>
          (p.2.antidiagonal.map fun r =>
            F r.2 (repDualCoeff rep U⁻¹ r.1
              (φ ∘ₗ act (G.evalLie (G.iteratedDerivJ p.1
                (-G.maurerCartan U⁻¹ ρ)))))).sum).sum
```

**`GlobalGaugeGroup.IsInfinitesimalActionOf.repGauge_covDerivAction`**, a lemma, [line 354](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L354).

> The covariant derivative preserves the transformation law. If each derivative symbol of `F`
> transforms by the Leibniz convolution of the coefficients of `rep`, and `act` is the
> infinitesimal action underlying `rep`, then so does each derivative symbol of
> `∇_ρ F = [∂_ρ F] + A_ρ · F`. The single inhomogeneous
> convolution of `[∂_{ρ ::ₘ s} F]` cancels the single `act` cross-term convolution of
> `A_ρ · F` through the coassociativity of the antidiagonal — the matter-field
> analogue of `GaugeBoson.TransformsInAdjoint.covDerivAdjoint`.

```lean
lemma IsInfinitesimalActionOf.repGauge_covDerivAction (hact : IsInfinitesimalActionOf G act rep)
    {F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B}
    (hF : ∀ (U : G.gaugeJetGroup) (φ : Module.Dual ℂ V) (s : Multiset (Fin 1 ⊕ Fin 3)),
      repGauge U (F s φ) = (s.antidiagonal.map fun p => F p.2 (repDualCoeff rep U⁻¹ p.1 φ)).sum)
    (ρ : Fin 1 ⊕ Fin 3) (U : G.gaugeJetGroup) (φ : Module.Dual ℂ V)
    (s : Multiset (Fin 1 ⊕ Fin 3)) :
    repGauge U (GlobalGaugeGroup.covDerivAction A act F ρ s φ) =
      (s.antidiagonal.map fun p => GlobalGaugeGroup.covDerivAction A act F ρ p.2
        (repDualCoeff rep U⁻¹ p.1 φ)).sum
```

**`GlobalGaugeGroup.IsInfinitesimalActionOf.repGauge_covDerivIter`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L399).

> Every iterated covariant derivative preserves the transformation law. If each derivative
> symbol of `F` transforms by the Leibniz convolution of the coefficients of `rep`, and `act` is
> the infinitesimal action underlying `rep`, then so does each derivative symbol of
> `∇_{l 0} ⋯ ∇_{l (n-1)} F`. This is induction on the number `n` of covariant derivatives,
> each step being `IsInfinitesimalActionOf.repGauge_covDerivAction`.

```lean
lemma IsInfinitesimalActionOf.repGauge_covDerivIter (hact : IsInfinitesimalActionOf G act rep)
    {F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B}
    (hF : ∀ (U : G.gaugeJetGroup) (φ : Module.Dual ℂ V) (s : Multiset (Fin 1 ⊕ Fin 3)),
      repGauge U (F s φ) = (s.antidiagonal.map fun p => F p.2 (repDualCoeff rep U⁻¹ p.1 φ)).sum)
    (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) (U : G.gaugeJetGroup) (φ : Module.Dual ℂ V)
    (s : Multiset (Fin 1 ⊕ Fin 3)) :
    repGauge U (GlobalGaugeGroup.covDerivIter A act F n l s φ) =
      (s.antidiagonal.map fun p => GlobalGaugeGroup.covDerivIter A act F n l p.2
        (repDualCoeff rep U⁻¹ p.1 φ)).sum
```

**`GlobalGaugeGroup.IsInfinitesimalActionOf.repGauge_covDerivIter_zero`**, a lemma, [line 415](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L415).

> The underived symbol of an iterated covariant derivative transforms through the
> base-point coefficient alone, since the antidiagonal of the empty multiset has a single term.

```lean
lemma IsInfinitesimalActionOf.repGauge_covDerivIter_zero
    (hact : IsInfinitesimalActionOf G act rep)
    {F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B}
    (hF : ∀ (U : G.gaugeJetGroup) (φ : Module.Dual ℂ V) (s : Multiset (Fin 1 ⊕ Fin 3)),
      repGauge U (F s φ) = (s.antidiagonal.map fun p => F p.2 (repDualCoeff rep U⁻¹ p.1 φ)).sum)
    (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) (U : G.gaugeJetGroup) (φ : Module.Dual ℂ V) :
    repGauge U (GlobalGaugeGroup.covDerivIter A act F n l 0 φ) =
      GlobalGaugeGroup.covDerivIter A act F n l 0 (repDualCoeff rep U⁻¹ 0 φ)
```

## C. The conjugate action and the conjugate representation

**`GlobalGaugeGroup.actionConj`**, a def, [line 438](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L438).

> The conjugate of an infinitesimal action. It is the same maps, read on the conjugate
> module, the generators of the conjugate representation.

```lean
noncomputable def actionConj (act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V) :
    G.lieSubalgebra →ₗ[ℝ] ConjModule V →ₗ[ℂ] ConjModule V
```

**`GlobalGaugeGroup.actionConj_apply`**, a lemma, [line 445](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L445).

```lean
lemma actionConj_apply (act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V) (c : G.lieSubalgebra) :
    actionConj act c = ConjModule.endConj (act c)
```

**`GlobalGaugeGroup.conjJetEquiv`**, a def, [line 452](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L452).

> The identification of the jets of a conjugate field with the conjugates of the
> jets. Conjugation is monoidal, and the star of the jet-ring factor absorbs the
> twist — `conj (g ⊗ u) ↦ star g ⊗ conj u`. This is the equivalence along which
> `FieldDerivSpace.repConj` carries the conjugated representation.

```lean
noncomputable def conjJetEquiv :
    ConjModule (SpaceTimeAlgebra ⊗[ℂ] V) ≃ₗ[ℂ] SpaceTimeAlgebra ⊗[ℂ] ConjModule V
```

**`GlobalGaugeGroup.conjJetEquiv_conjEquiv_tmul`**, a lemma, [line 457](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L457).

```lean
lemma conjJetEquiv_conjEquiv_tmul (g : SpaceTimeAlgebra) (u : V) :
    conjJetEquiv (conjEquiv (k := ℂ) (M := SpaceTimeAlgebra ⊗[ℂ] V) (g ⊗ₜ[ℂ] u))
      = star g ⊗ₜ[ℂ] conjEquiv (k := ℂ) (M := V) u
```

**`GlobalGaugeGroup.repConj_conjJetEquiv`**, a lemma, [line 470](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L470).

> The conjugate representation acts through `conjJetEquiv` by the original maps.

```lean
lemma repConj_conjJetEquiv (rep : Representation ℂ G.gaugeJetGroup (SpaceTimeAlgebra ⊗[ℂ] V))
    (U : G.gaugeJetGroup) (w : SpaceTimeAlgebra ⊗[ℂ] V) :
    FieldDerivSpace.repConj rep U
        (conjJetEquiv (conjEquiv (k := ℂ) (M := SpaceTimeAlgebra ⊗[ℂ] V) w))
      = conjJetEquiv (conjEquiv (k := ℂ) (M := SpaceTimeAlgebra ⊗[ℂ] V) (rep U w))
```

**`GlobalGaugeGroup.repCoeff_repConj`**, a lemma, [line 483](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L483).

> The base-point Taylor coefficients of the conjugate representation are the
> conjugated coefficients. The derivative directions are real, so conjugation passes
> through `∂_x` and the base-point evaluation untouched.

```lean
lemma repCoeff_repConj (rep : Representation ℂ G.gaugeJetGroup (SpaceTimeAlgebra ⊗[ℂ] V))
    (U : G.gaugeJetGroup) (x : Multiset (Fin 1 ⊕ Fin 3)) :
    repCoeff (FieldDerivSpace.repConj rep) U x
      = ConjModule.endConj (repCoeff rep U x)
```

**`GlobalGaugeGroup.repCoeff_repConj_zero_eq_id`**, a lemma, [line 531](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L531).

> The base-point triviality of the zeroth Taylor coefficient passes to the
> conjugate representation.

```lean
lemma repCoeff_repConj_zero_eq_id {W : G.gaugeJetGroup}
    (hrep : repCoeff rep W 0 = LinearMap.id) :
    repCoeff (FieldDerivSpace.repConj rep) W 0 = LinearMap.id
```

**`GlobalGaugeGroup.IsInfinitesimalActionOf.conj`**, a lemma, [line 540](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L540).

> The conjugate of an infinitesimal action underlies the conjugate
> representation. Conjugating the Taylor coefficients preserves both the
> Maurer–Cartan Leibniz law and the adjoint intertwining, since the gauge-algebra
> inputs are real.

```lean
lemma IsInfinitesimalActionOf.conj (h : IsInfinitesimalActionOf G act rep) :
    IsInfinitesimalActionOf G (actionConj act) (FieldDerivSpace.repConj rep)
```

## D. Uniqueness

> A representation generated by an infinitesimal action is determined, Taylor coefficient by
> Taylor coefficient, by its values at the base point: `repCoeff_cons` expresses each
> coefficient through coefficients of lower order.

**`GlobalGaugeGroup.IsInfinitesimalActionOf.repCoeff_eq_of_repCoeff_zero`**, a lemma, [line 579](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L579).

> Two representations with the same infinitesimal action and the same base-point values
> of a gauge jet have the same Taylor coefficients at that jet.

```lean
lemma IsInfinitesimalActionOf.repCoeff_eq_of_repCoeff_zero
    (h : IsInfinitesimalActionOf G act rep) (h' : IsInfinitesimalActionOf G act rep')
    {U : G.gaugeJetGroup} (h0 : repCoeff rep U 0 = repCoeff rep' U 0)
      (x : Multiset (Fin 1 ⊕ Fin 3)) :
    repCoeff rep U x = repCoeff rep' U x
```

**`GlobalGaugeGroup.IsInfinitesimalActionOf.eq_of_repCoeff_zero`**, a lemma, [line 597](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L597).

> A fibrewise representation is determined by its infinitesimal action and its
> base-point values. Two fibrewise representations generated by the same action, with the
> same value `repCoeff · U 0` at every gauge jet, are equal.

```lean
lemma IsInfinitesimalActionOf.eq_of_repCoeff_zero [FiniteDimensional ℂ V]
    (h : IsInfinitesimalActionOf G act rep) (h' : IsInfinitesimalActionOf G act rep')
    (hs : ∀ (U : G.gaugeJetGroup) (χ : SpaceTimeAlgebra) z, rep U (χ • z) = χ • rep U z)
    (hs' : ∀ (U : G.gaugeJetGroup) (χ : SpaceTimeAlgebra) z, rep' U (χ • z) = χ • rep' U z)
    (h0 : ∀ U, repCoeff rep U 0 = repCoeff rep' U 0) : rep = rep'
```

## E. Factorization through evaluation

> If pure jets act trivially at the base point, the base-point action of a jet is that of the
> constant jet of its value.

**`GlobalGaugeGroup.repCoeff_zero_eq_ofConstant_eval`**, a lemma, [line 626](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L626).

> If pure jets act trivially at the base point, the zeroth Taylor coefficient of a jet
> is that of the constant jet of its value. Every jet is a pure jet times the constant jet
> of its value, and the zeroth coefficients are multiplicative for a fibrewise
> representation.

```lean
lemma repCoeff_zero_eq_ofConstant_eval
    (rep : Representation ℂ G.gaugeJetGroup (SpaceTimeAlgebra ⊗[ℂ] V))
    (hlin : ∀ (U : G.gaugeJetGroup) (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] V),
      rep U (χ • z) = χ • rep U z)
    (hrep : ∀ {W : G.gaugeJetGroup}, G.evalGaugeJet W = 1 → repCoeff rep W 0 = LinearMap.id)
    (U : G.gaugeJetGroup) :
    repCoeff rep U 0 = repCoeff rep (G.gaugeJetOfConstant (G.evalGaugeJet U)) 0
```

**`GlobalGaugeGroup.repDualCoeff_inv_zero_eq_ofConstant_eval`**, a lemma, [line 644](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L644).

> If pure jets act trivially at the base point, the dual base-point coefficient of the
> inverse of a jet is that of the inverse of the constant jet of its value.

```lean
lemma repDualCoeff_inv_zero_eq_ofConstant_eval
    (rep : Representation ℂ G.gaugeJetGroup (SpaceTimeAlgebra ⊗[ℂ] V))
    (hlin : ∀ (U : G.gaugeJetGroup) (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] V),
      rep U (χ • z) = χ • rep U z)
    (hrep : ∀ {W : G.gaugeJetGroup}, G.evalGaugeJet W = 1 → repCoeff rep W 0 = LinearMap.id)
    (U : G.gaugeJetGroup) :
    repDualCoeff rep U⁻¹ 0 = repDualCoeff rep (G.gaugeJetOfConstant (G.evalGaugeJet U))⁻¹ 0
```

## F. The infinitesimal action of a matter field

> For a matter field `M` the action `M.repAlgebra = dρ` of the Lie algebra and the jet
> action `M.repJet` form such a pair, by the Leibniz and intertwining laws of
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.GaugeJetAction`.

**`GlobalGaugeGroup.MatterField.repCoeff_repJet`**, a lemma, [line 672](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L672).

> The base-point Taylor coefficients of the jet action are those of the jet action as a
> representation.

```lean
lemma repCoeff_repJet (U : G.gaugeJetGroup) (x : Multiset (Fin 1 ⊕ Fin 3)) :
    GlobalGaugeGroup.repCoeff M.repJet U x = M.repCoeff U x
```

**`GlobalGaugeGroup.MatterField.isInfinitesimalActionOf`**, a lemma, [line 677](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L677).

> The action `dρ` of the Lie algebra is the infinitesimal action underlying the jet action
> of the gauge jets.

```lean
lemma isInfinitesimalActionOf : G.IsInfinitesimalActionOf M.repAlgebra M.repJet
```

## G. Pure jets act trivially

**`GlobalGaugeGroup.MatterField.repCoeff_zero_of_eval_eq_one`**, a lemma, [line 688](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L688).

> Pure jets act trivially at the base point. A jet of value one has identity zeroth Taylor
> coefficient on the target space, for every matter field.

```lean
lemma repCoeff_zero_of_eval_eq_one {W : G.gaugeJetGroup} (hW : G.evalGaugeJet W = 1) :
    GlobalGaugeGroup.repCoeff M.repJet W 0 = LinearMap.id
```

## H. Compatibility of the gauge and Lorentz actions

**`GlobalGaugeGroup.MatterField.GaugeLorentzCommute`**, a def, [line 701](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L701).

> The gauge and Lorentz representations of a matter field commute.

```lean
def GaugeLorentzCommute : Prop
```

**`GlobalGaugeGroup.MatterField.GaugeLorentzCompatible`**, a def, [line 713](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L713).

> The internal gauge symmetry of the matter field commutes with its Lorentz symmetry, that
> is, the action of the Lie algebra commutes with the Lorentz representation on the target
> space. The covariant derivative adds the term `A_ρ · F`, built from the Lie algebra action, to
> the ordinary derivative, so its Lorentz law holds only when this commutation does. The later
> algebras of covariant expressions are stable under the Lorentz group for the same reason.
> It follows from `GaugeLorentzCommute`, but not conversely. It determines the gauge action
> on the identity component alone, so it says nothing about the other components of a
> disconnected gauge group.

```lean
def GaugeLorentzCompatible : Prop
```

**`GlobalGaugeGroup.MatterField.GaugeLorentzCommute.gaugeLorentzCompatible`**, a lemma, [line 721](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean#L721).

> If the gauge and Lorentz representations commute, so do the Lie algebra action and the
> Lorentz representation, the Lie algebra action being the derivative of the gauge
> representation.

```lean
lemma GaugeLorentzCommute.gaugeLorentzCompatible (h : M.GaugeLorentzCommute) :
    M.GaugeLorentzCompatible
```

## Depends on

- [The gauge law of a gauge field and of its covariant expressions](../part-01/gaugeboson-adjointfamily-gaugelaw.md)
- [Fibrewise actions on `V`-valued jets](../part-04/localfieldalgebra-jetrep.md)
- [The covariant derivative of a matter family](matterfield-covariantderiv.md)
- [The jet action of a matter field](matterfield-gaugejetaction.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/InfinitesimalAction.lean)
