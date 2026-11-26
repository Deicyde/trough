---
declaration: module
origin: cited
lean: GlobalGaugeGroup.repCoeff, GlobalGaugeGroup.repDualCoeff, GlobalGaugeGroup.jetEval_rep_of_smul, GlobalGaugeGroup.repCoeff_zero_mul, GlobalGaugeGroup.tensorAction, GlobalGaugeGroup.tensorAction_tmul, GlobalGaugeGroup.tensorAction_map_left, GlobalGaugeGroup.tensorAction_one_left
statement: formalized
proof: formalized
---

# The covariant derivative of a matter family

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.CovariantDeriv`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean): 44 declarations, 27 with a docstring; 2 private, not shown.

> The covariant derivative tower of a family of matter symbols in an algebra of symbols.

## i. Overview

> A matter field valued in a complex vector space `V` has derivative symbols `[∂_s ψ]`,
> indexed by a multiset `s` of directions and contracted against the dual of `V`. This file
> works with such families `F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B` in an
> algebra of symbols `B`, together with a family `A` of gauge-field symbols `[∂_s A_μ]`.
>
> Under a jet gauge transformation the value of `rep U` at a constant vector depends on the
> spacetime point, so the derivative symbols see its Taylor coefficients at the base point.
> These are `repCoeff rep U x`, and their transposes to the dual of `V` are
> `repDualCoeff rep U x`, the analogue of `adjointDualCoeff` for a general representation.
>
> The covariant derivative `∇_ρ F = ∂_ρ F + A_ρ · F` needs the infinitesimal action
> `act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V` of the gauge algebra on `V`, the physicists'
> `i dρ(T^a)`. Here it is an argument. For a matter field it is the derivative of the group
> representation, `MatterField.repAlgebra`. The derived action `A_ρ · F` is the Leibniz
> convolution of the action of the gauge-field symbols on the matter symbols, and
> `covDerivIter` iterates `∇` along an ordered tuple of directions.
>
> The covariant tower and the plain derivative symbols generate the same algebra together with
> the gauge-field symbols (the span lemma). The tower is natural under multiplicative linear maps
> of the algebra and inherits mass weights and anticommutation from the bare family. That the
> covariant derivative preserves the transformation law is proved in
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.InfinitesimalAction`.

## ii. Key results

> - `repDualCoeff` : the physicists' `∂_x (rep U)^i_j|₀` acting on the complex dual index of a
>   matter-field symbol, the transpose of `repCoeff`
> - `covDerivIter` : the iterated covariant derivative of a matter family
> - `adjoin_symbols_eq_adjoin_covDerivIter` : the span lemma, and its membership form
>   `apply_mem_of_covDerivIter_mem`
> - `covDerivIter_map` : the covariant tower is natural in the algebra
> - `covDerivIter_mem_massWeightEigenspace` : the covariant tower of a family of weight
>   `c + 2 * |t|` has weight `c + 2 * n + 2 * |s|`
> - `covDerivIter_mem_anticommuteSubmodule` : anything commuting with the gauge-field symbols and
>   anticommuting with the bare family anticommutes with its covariant tower

## iv. References

> * None.

## A. The dual representation coefficients and gauge tensors in a representation

**`GlobalGaugeGroup.repCoeff`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L94).

> The base-point Taylor coefficient of the representation. It includes the constant
> vector into `V`-valued jets, acts by `rep U`, differentiates `x` times and evaluates at
> the base point. The composite is the physicists' `∂_x (rep U)^i_j|₀` as a ℂ-linear map on
> the value space.

```lean
noncomputable def repCoeff (rep : Representation ℂ G.gaugeJetGroup (SpaceTimeAlgebra ⊗[ℂ] V))
    (U : G.gaugeJetGroup) (x : Multiset (Fin 1 ⊕ Fin 3)) : V →ₗ[ℂ] V
```

**`GlobalGaugeGroup.repDualCoeff`**, a def, [line 103](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L103).

> The physicists' `∂_x (rep U)^i_j|₀` acting on the complex dual index of a
> matter-field symbol, the transpose of `repCoeff`. This is the analogue of
> `adjointDualCoeff` for a general representation of the jet gauge group; for `x = 0`
> it is the dual (contragredient) action of the value of `U`, and for `x ≠ 0` it sees
> the derivatives of the gauge transformation.

```lean
noncomputable def repDualCoeff (rep : Representation ℂ G.gaugeJetGroup (SpaceTimeAlgebra ⊗[ℂ] V))
    (U : G.gaugeJetGroup) (x : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ V →ₗ[ℂ] Module.Dual ℂ V
```

**`GlobalGaugeGroup.jetEval_rep_of_smul`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L111).

> For a fibrewise representation, evaluating the transform of a jet at the base point
> is the zeroth Taylor coefficient of the transform of its base-point value. The jet
> ring factor passes through the action and is then evaluated.

```lean
lemma jetEval_rep_of_smul (rep : Representation ℂ G.gaugeJetGroup (SpaceTimeAlgebra ⊗[ℂ] V))
    (hlin : ∀ (U : G.gaugeJetGroup) (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] V), rep U
        (χ • z) = χ • rep U z)
    (U : G.gaugeJetGroup) (z : SpaceTimeAlgebra ⊗[ℂ] V) :
    jetEval (rep U z) = repCoeff rep U 0 (jetEval z)
```

**`GlobalGaugeGroup.repCoeff_zero_mul`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L126).

> The zeroth Taylor coefficients of a fibrewise representation are multiplicative, so they
> form a representation of the jet gauge group on the value space.

```lean
lemma repCoeff_zero_mul (rep : Representation ℂ G.gaugeJetGroup (SpaceTimeAlgebra ⊗[ℂ] V))
    (hlin : ∀ (U : G.gaugeJetGroup) (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] V), rep U
        (χ • z) = χ • rep U z)
    (U W : G.gaugeJetGroup) : repCoeff rep (U * W) 0 = repCoeff rep U 0 ∘ₗ repCoeff rep W 0
```

## B. The covariant derivative through an infinitesimal action

> The covariant derivative `∇_ρ F = [∂_ρ F] + A_ρ · F` requires the infinitesimal
> action of the gauge algebra on the value space, the physicists' `i dρ(T^a)`. Here it is an
> argument `act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V`, real-linear in the algebra slot (the
> gauge algebra is a real Lie algebra) and complex-linear in the value slot, matching
> the complex duals indexing the matter families. For a matter field it is
> `MatterField.repAlgebra`, the derivative of the group representation.

**`GlobalGaugeGroup.tensorAction`**, a def, [line 157](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L157).

> The action of an adjoint-valued field on a matter field at the tensor level. It is
> multiplication in `B` on the first factors and the ℂ-linear infinitesimal action `act`
> of the gauge algebra on `V` on the second factors, so that on pure tensors
> `(b₁ ⊗ c) · (b₂ ⊗ v) = (b₁ b₂) ⊗ act c v`.

```lean
noncomputable def tensorAction (act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V) :
    (B ⊗[ℝ] G.lieSubalgebra) →ₗ[ℝ] (B ⊗[ℂ] V) →ₗ[ℂ] B ⊗[ℂ] V
```

**`GlobalGaugeGroup.tensorAction_tmul`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L172).

```lean
lemma tensorAction_tmul (act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V) (b₁ b₂ : B)
    (c : G.lieSubalgebra) (v : V) :
    tensorAction act (b₁ ⊗ₜ[ℝ] c) (b₂ ⊗ₜ[ℂ] v) = (b₁ * b₂) ⊗ₜ[ℂ] act c v
```

**`GlobalGaugeGroup.tensorAction_map_left`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L176).

```lean
lemma tensorAction_map_left (act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V) (Φ : B →ₗ[ℂ] B)
    (hΦ : ∀ b₁ b₂, Φ (b₁ * b₂) = Φ b₁ * Φ b₂) (s : B ⊗[ℝ] G.lieSubalgebra)
    (t : B ⊗[ℂ] V) :
    tensorAction act ((TensorProduct.map (Φ.restrictScalars ℝ) LinearMap.id) s)
        ((TensorProduct.map Φ LinearMap.id) t) =
      (TensorProduct.map Φ LinearMap.id) (tensorAction act s t)
```

**`GlobalGaugeGroup.tensorAction_one_left`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L191).

```lean
lemma tensorAction_one_left (act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V) (c : G.lieSubalgebra)
    (t : B ⊗[ℂ] V) :
    tensorAction act ((1 : B) ⊗ₜ[ℝ] c) t =
      (TensorProduct.map LinearMap.id (act c)) t
```

**`GlobalGaugeGroup.tensorAction_map_right_antidiagonal`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L202).

> `tensorAction` under an antidiagonal pair of transport families. If the
> `V`-transports intertwine `act` with the `G.lieSubalgebra`-transports as an
> antidiagonal convolution, so do `id ⊗ ·` over `tensorAction`.

```lean
lemma tensorAction_map_right_antidiagonal (act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V)
    (Tg : Multiset (Fin 1 ⊕ Fin 3) → G.lieSubalgebra →ₗ[ℝ] G.lieSubalgebra)
    (Tv : Multiset (Fin 1 ⊕ Fin 3) → V →ₗ[ℂ] V) (x : Multiset (Fin 1 ⊕ Fin 3))
    (hT : ∀ (c : G.lieSubalgebra) (w : V), Tv x (act c w) =
      (x.antidiagonal.map fun p => act (Tg p.1 c) (Tv p.2 w)).sum)
    (s : B ⊗[ℝ] G.lieSubalgebra) (t : B ⊗[ℂ] V) :
    (x.antidiagonal.map fun p =>
      tensorAction act ((TensorProduct.map LinearMap.id (Tg p.1)) s)
        ((TensorProduct.map LinearMap.id (Tv p.2)) t)).sum =
      (TensorProduct.map LinearMap.id (Tv x)) (tensorAction act s t)
```

**`GlobalGaugeGroup.dualPairEquivC`**, a def, [line 233](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L233).

> The canonical equivalence between matter fields `B ⊗[ℂ] V` and their component
> families `φ ↦ F^φ` over the complex dual — `dualPairEquiv` for a general
> finite-dimensional complex value space.

```lean
noncomputable def dualPairEquivC : (B ⊗[ℂ] V) ≃ₗ[ℂ] (Module.Dual ℂ V →ₗ[ℂ] B)
```

**`GlobalGaugeGroup.dualPairEquivC_tmul`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L239).

```lean
lemma dualPairEquivC_tmul (b : B) (v : V) (φ : Module.Dual ℂ V) :
    dualPairEquivC (b ⊗ₜ[ℂ] v) φ = φ v • b
```

**`GlobalGaugeGroup.dualPairEquivC_map_left`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L243).

```lean
lemma dualPairEquivC_map_left (Φ : B →ₗ[ℂ] B) (t : B ⊗[ℂ] V)
    (φ : Module.Dual ℂ V) :
    dualPairEquivC ((TensorProduct.map Φ LinearMap.id) t) φ =
      Φ (dualPairEquivC t φ)
```

**`GlobalGaugeGroup.dualPairEquivC_map_right`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L251).

```lean
lemma dualPairEquivC_map_right (T : V →ₗ[ℂ] V) (t : B ⊗[ℂ] V)
    (φ : Module.Dual ℂ V) :
    dualPairEquivC ((TensorProduct.map LinearMap.id T) t) φ =
      dualPairEquivC t (T.dualMap φ)
```

**`GlobalGaugeGroup.symm_comp_left_C`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L259).

```lean
lemma symm_comp_left_C (Φ : B →ₗ[ℂ] B) (g : Module.Dual ℂ V →ₗ[ℂ] B) :
    dualPairEquivC.symm (Φ ∘ₗ g) =
      (TensorProduct.map Φ LinearMap.id) (dualPairEquivC.symm g)
```

**`GlobalGaugeGroup.symm_comp_right_C`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L268).

```lean
lemma symm_comp_right_C (T : V →ₗ[ℂ] V) (g : Module.Dual ℂ V →ₗ[ℂ] B) :
    dualPairEquivC.symm (g ∘ₗ T.dualMap) =
      (TensorProduct.map LinearMap.id T) (dualPairEquivC.symm g)
```

**`GlobalGaugeGroup.actionFam`**, a def, [line 281](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L281).

> The action of an adjoint-indexed component family on a matter one, through the
> infinitesimal action `act`. Both are assembled into fields, acted on by `tensorAction`
> and read back out as components. This is the physicists' `f^a (T_a)^i_j g^j` with `T = act`,
> basis-free.

```lean
noncomputable def actionFam (act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V)
    (f : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) (g : Module.Dual ℂ V →ₗ[ℂ] B) :
    Module.Dual ℂ V →ₗ[ℂ] B
```

**`GlobalGaugeGroup.actionFam_add_left`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L286).

```lean
lemma actionFam_add_left (f₁ f₂ : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (g : Module.Dual ℂ V →ₗ[ℂ] B) :
    actionFam act (f₁ + f₂) g = actionFam act f₁ g + actionFam act f₂ g
```

**`GlobalGaugeGroup.actionFam_add_right`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L291).

```lean
lemma actionFam_add_right (f : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (g₁ g₂ : Module.Dual ℂ V →ₗ[ℂ] B) :
    actionFam act f (g₁ + g₂) = actionFam act f g₁ + actionFam act f g₂
```

**`GlobalGaugeGroup.actionFam_zero_left`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L296).

```lean
lemma actionFam_zero_left (g : Module.Dual ℂ V →ₗ[ℂ] B) :
    actionFam act 0 g = 0
```

**`GlobalGaugeGroup.actionFam_zero_right`**, a lemma, [line 300](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L300).

```lean
lemma actionFam_zero_right (f : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) :
    actionFam act f 0 = 0
```

**`GlobalGaugeGroup.actionFam_sum_left`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L304).

```lean
lemma actionFam_sum_left (S : Multiset (Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B))
    (g : Module.Dual ℂ V →ₗ[ℂ] B) :
    actionFam act S.sum g = (S.map fun f => actionFam act f g).sum
```

**`GlobalGaugeGroup.actionFam_sum_right`**, a lemma, [line 311](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L311).

```lean
lemma actionFam_sum_right (f : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (S : Multiset (Module.Dual ℂ V →ₗ[ℂ] B)) :
    actionFam act f S.sum = (S.map fun g => actionFam act f g).sum
```

**`GlobalGaugeGroup.repGauge_actionFam`**, a lemma, [line 323](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L323).

> The gauge transformation of the action of an affinely-transforming
> adjoint-indexed family on a linearly-transforming matter family. It is the action of the
> transformed families plus one `act`-type cross term. This is `GaugeBoson.repGauge_bracketFam`
> with a homogeneous second slot and the bracket replaced by a general action. Only the
> multiplicativity of the action of `U` is used.

```lean
lemma repGauge_actionFam
    (U : G.gaugeJetGroup)
    (hmul : ∀ b₁ b₂ : B, repGauge U (b₁ * b₂) = repGauge U b₁ * repGauge U b₂)
    {f f' : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B}
    {g g' : Module.Dual ℂ V →ₗ[ℂ] B} {cf : G.lieSubalgebra}
    (hf : ∀ ψ : Module.Dual ℝ G.lieSubalgebra,
      repGauge U (f ψ) = f' ψ + algebraMap ℂ B (ψ cf))
    (hg : ∀ ψ : Module.Dual ℂ V, repGauge U (g ψ) = g' ψ)
    (φ : Module.Dual ℂ V) :
    repGauge U (actionFam act f g φ) =
      actionFam act f' g' φ + g' (φ ∘ₗ act cf)
```

**`GlobalGaugeGroup.actionFamConv`**, a def, [line 372](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L372).

> The derived action family `A_ρ · F`, the `s`-derivative of the action of the
> gauge field on a matter family, given by the Leibniz convolution of the derivative
> symbols over the multiset antidiagonal — the matter analogue of `GaugeBoson.bracketFamConv`.

```lean
noncomputable def actionFamConv
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V) (ρ : Fin 1 ⊕ Fin 3)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (s : Multiset (Fin 1 ⊕ Fin 3)) : Module.Dual ℂ V →ₗ[ℂ] B
```

**`GlobalGaugeGroup.covDerivAction`**, a def, [line 384](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L384).

> The covariant derivative `∇_ρ F = [∂_ρ F] + A_ρ · F` of a matter family of
> derivative symbols, in the single direction `ρ`, the extra derivative on the symbol
> plus the derived action of the gauge field on the value index. With the physicists'
> factor of `i` absorbed into `act` (as it is in the gauge-algebra bracket), this is
> `∂_ρ F + i A_ρ^a T_a F` in the `D = ∂ + i A` convention.

```lean
noncomputable def covDerivAction
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (ρ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) : Module.Dual ℂ V →ₗ[ℂ] B
```

**`GlobalGaugeGroup.covDerivAction_apply`**, a lemma, [line 392](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L392).

```lean
lemma covDerivAction_apply
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (ρ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V) :
    covDerivAction A act F ρ s φ = F (ρ ::ₘ s) φ + actionFamConv A act ρ F s φ
```

**`GlobalGaugeGroup.covDerivIter`**, a def, [line 405](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L405).

> The iterated covariant derivative `∇_{l 0} ⋯ ∇_{l (n-1)} F` of a matter family
> along an ordered tuple of directions. Covariant derivatives do not commute (their
> commutator is the action of the field strength), so the iteration is order-dependent
> and indexed by `(n : ℕ)` and `l : Fin n → (Fin 1 ⊕ Fin 3)`. The result is again a
> family of derivative symbols; the physical iterated covariant derivative is its
> value at the empty multiset.

```lean
noncomputable def covDerivIter
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B) :
    (n : ℕ) → (Fin n → (Fin 1 ⊕ Fin 3)) →
      Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B
```

**`GlobalGaugeGroup.covDerivIter_zero`**, a lemma, [line 415](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L415).

```lean
lemma covDerivIter_zero (act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (l : Fin 0 → (Fin 1 ⊕ Fin 3)) :
    covDerivIter A act F 0 l = F
```

**`GlobalGaugeGroup.covDerivIter_succ`**, a lemma, [line 421](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L421).

```lean
lemma covDerivIter_succ (act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    {n : ℕ} (l : Fin (n + 1) → (Fin 1 ⊕ Fin 3)) :
    covDerivIter A act F (n + 1) l =
      covDerivAction A act (covDerivIter A act F n fun i => l i.succ) (l 0)
```

## C. The span lemma

> Replacing derivatives of a matter family by covariant derivatives does not change
> the generated algebra of symbols: the correction terms are products of gauge-field
> components with matter components. Note the statement is about generated
> *subalgebras*, not linear spans — `∇_ρ F − ∂_ρ F` is a sum of products `A · F`,
> which lies in the algebra generated by the symbols but not in their linear span.

**`GlobalGaugeGroup.dualPairEquiv_symm_eq_sum`**, a lemma, [line 441](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L441).

> Decomposition of an assembled adjoint-indexed family along a basis of the gauge
> algebra, as the components against the dual basis, tensored with the basis vectors.

```lean
lemma dualPairEquiv_symm_eq_sum {ι : Type*} [Fintype ι]
    (bW : Module.Basis ι ℝ G.lieSubalgebra)
    (g : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) :
    dualPairEquiv.symm g = ∑ i, g (bW.coord i) ⊗ₜ[ℝ] bW i
```

**`GlobalGaugeGroup.dualPairEquivC_symm_eq_sum`**, a lemma, [line 465](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L465).

> Decomposition of an assembled matter family along a basis of the value space.

```lean
lemma dualPairEquivC_symm_eq_sum {ι : Type*} [Fintype ι] (bW : Module.Basis ι ℂ V)
    (g : Module.Dual ℂ V →ₗ[ℂ] B) :
    dualPairEquivC.symm g = ∑ i, g (bW.coord i) ⊗ₜ[ℂ] bW i
```

**`GlobalGaugeGroup.actionFam_apply_mem`**, a lemma, [line 489](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L489).

> The value of an action of families lies in any subalgebra containing the values
> of both families, since the action is a finite sum of products of components.

```lean
lemma actionFam_apply_mem {act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V} {P : Subalgebra ℂ B}
    {f : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B} {g : Module.Dual ℂ V →ₗ[ℂ] B}
    (hf : ∀ ψ, f ψ ∈ P) (hg : ∀ χ, g χ ∈ P) (φ : Module.Dual ℂ V) :
    actionFam act f g φ ∈ P
```

**`GlobalGaugeGroup.covDerivIter_succ_sub`**, a lemma, [line 532](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L532).

> One step of the unitriangular expansion. The difference between a covariant symbol with
> `n + 1` directions and the plain symbol of the same total order is the difference one step
> lower plus the derived action of the gauge field on the lower tower.

```lean
lemma covDerivIter_succ_sub (act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    {n : ℕ} (l : Fin (n + 1) → (Fin 1 ⊕ Fin 3)) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ V) :
    covDerivIter A act F (n + 1) l s φ - F (List.ofFn l + s) φ =
      (covDerivIter A act F n (fun i => l i.succ) (l 0 ::ₘ s) φ -
          F (List.ofFn (fun i : Fin n => l i.succ) + (l 0 ::ₘ s)) φ) +
        actionFamConv A act (l 0) (covDerivIter A act F n fun i => l i.succ) s φ
```

**`GlobalGaugeGroup.covDerivIter_sub_mem`**, a lemma, [line 547](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L547).

> Unitriangularity of the covariant matter tower. The covariant and plain
> derivative symbols of a matter family differ by an element of the subalgebra
> generated by the gauge-field symbols and the strictly lower-order matter symbols.
> Stated at every derivative multiset `s`, as needed for the induction.

```lean
lemma covDerivIter_sub_mem (act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ V) :
    covDerivIter A act F n l s φ - F (List.ofFn l + s) φ ∈
      Algebra.adjoin ℂ
        ({b : B | ∃ (u : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
            (ψ : Module.Dual ℝ G.lieSubalgebra), b = A u μ ψ} ∪
          {b : B | ∃ (t : Multiset (Fin 1 ⊕ Fin 3)) (χ : Module.Dual ℂ V),
            t.card < n + s.card ∧ b = F t χ})
```

**`GlobalGaugeGroup.covDerivIter_mem_adjoin_symbols`**, a lemma, [line 588](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L588).

> Every derivative symbol of the covariant tower is a polynomial in the gauge-field
> symbols and the matter symbols.

```lean
lemma covDerivIter_mem_adjoin_symbols (act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ V) :
    covDerivIter A act F n l s φ ∈ Algebra.adjoin ℂ
      ({b : B | ∃ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
          (ψ : Module.Dual ℝ G.lieSubalgebra), b = A s μ ψ} ∪
        {b : B | ∃ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V),
          b = F s φ})
```

**`GlobalGaugeGroup.adjoin_symbols_eq_adjoin_covDerivIter`**, a lemma, [line 614](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L614).

> The span lemma. The algebra of symbols generated by the gauge field together
> with a matter family's derivative symbols equals the one generated by the gauge
> field together with the matter family's covariant derivative tower. The
> correction `∇_ρ − ∂_ρ` is the derived action of the gauge field — a sum of products
> of symbols, absorbed by the algebra structure.

```lean
lemma adjoin_symbols_eq_adjoin_covDerivIter (act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B) :
    Algebra.adjoin ℂ
      ({b : B | ∃ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
          (ψ : Module.Dual ℝ G.lieSubalgebra), b = A s μ ψ} ∪
        {b : B | ∃ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V),
          b = F s φ}) =
    Algebra.adjoin ℂ
      ({b : B | ∃ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
          (ψ : Module.Dual ℝ G.lieSubalgebra), b = A s μ ψ} ∪
        {b : B | ∃ (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V),
          b = covDerivIter A act F n l 0 φ})
```

**`GlobalGaugeGroup.apply_mem_of_covDerivIter_mem`**, a lemma, [line 667](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L667).

> A derivative symbol of a matter family lies in every subalgebra containing the gauge-field
> symbols and the covariant tower of the family. This is the span lemma
> `adjoin_symbols_eq_adjoin_covDerivIter` read as a membership statement.

```lean
lemma apply_mem_of_covDerivIter_mem (act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B) {P : Subalgebra ℂ B}
    (hA : ∀ s μ ψ, A s μ ψ ∈ P)
    (hF : ∀ n (l : Fin n → (Fin 1 ⊕ Fin 3)) φ, covDerivIter A act F n l 0 φ ∈ P)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V) : F s φ ∈ P
```

## D. Naturality in the algebra

> The matter analogue of `bracketFam_map` and `iteratedCovDerivAdjoint_map`: a
> multiplicative linear map into another algebra carries the derived action, and hence
> the whole covariant matter tower, to the tower of the image families. The derived
> action is a finite sum of products of components, so only multiplicativity is needed;
> no derivative operator on the target is involved.

**`GlobalGaugeGroup.actionFam_map`**, a lemma, [line 698](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L698).

> The action of an adjoint-indexed family on a matter family is natural in the
> algebra.

```lean
lemma actionFam_map (act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V)
    (f : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (g : Module.Dual ℂ V →ₗ[ℂ] B) :
    actionFam act (Φ.restrictScalars ℝ ∘ₗ f) (Φ ∘ₗ g) = Φ ∘ₗ actionFam act f g
```

**`GlobalGaugeGroup.actionFamConv_map`**, a lemma, [line 712](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L712).

> The derived action family is natural in the algebra.

```lean
lemma actionFamConv_map
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V) (ρ : Fin 1 ⊕ Fin 3)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (s : Multiset (Fin 1 ⊕ Fin 3)) :
    actionFamConv (fun p σ => Φ.restrictScalars ℝ ∘ₗ A p σ) act ρ (fun p => Φ ∘ₗ F p) s
      = Φ ∘ₗ actionFamConv A act ρ F s
```

**`GlobalGaugeGroup.covDerivAction_map`**, a lemma, [line 729](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L729).

> The covariant derivative of a matter family is natural in the algebra.

```lean
lemma covDerivAction_map
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (ρ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    covDerivAction (fun p σ => Φ.restrictScalars ℝ ∘ₗ A p σ) act (fun p => Φ ∘ₗ F p) ρ s
      = Φ ∘ₗ covDerivAction A act F ρ s
```

**`GlobalGaugeGroup.covDerivIter_map`**, a lemma, [line 741](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L741).

> The iterated covariant derivative of a matter family is natural in the algebra. The
> image of the tower is the tower of the image families, at every ordered tuple of
> directions and every derivative multiset.

```lean
lemma covDerivIter_map
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    covDerivIter (fun p σ => Φ.restrictScalars ℝ ∘ₗ A p σ) act (fun p => Φ ∘ₗ F p) n l
      = fun s => Φ ∘ₗ covDerivIter A act F n l s
```

## E. Mass weights and statistics of the tower

> Each term of a covariant tower is a product of gauge-field symbols with a single bare symbol
> of the family, so a property of the bare family that is a submodule and is stable under
> multiplication by the gauge-field symbols passes to the tower. Two such properties matter:
> the mass weight, and anticommutation with a fixed element.

**`GlobalGaugeGroup.actionFam_apply_mem_submodule`**, a lemma, [line 773](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L773).

> The action pairing of two families lands in any submodule containing the products of
> their components, since expanded in bases it is a finite sum of scalar multiples of them.

```lean
lemma actionFam_apply_mem_submodule {act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V}
    {M : Submodule ℂ B} {f : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B}
    {g : Module.Dual ℂ V →ₗ[ℂ] B} (hfg : ∀ ψ χ, f ψ * g χ ∈ M) (φ : Module.Dual ℂ V) :
    actionFam act f g φ ∈ M
```

**`GlobalGaugeGroup.covDerivIter_mem_massWeightEigenspace`**, a lemma, [line 787](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L787).

> The mass weight of a matter covariant tower. If the gauge-field symbols `∂_p A_μ` have
> weight `2 * (1 + |p|)` and the bare family has weight `c + 2 * |t|` at the derivative
> multiset `t`, then the `n`-fold covariant derivative has weight `c + 2 * n + 2 * |s|` at
> `s`. Each covariant derivative costs two units, whether it lands on the derivative index or
> brings down a gauge-field factor.

```lean
lemma covDerivIter_mem_massWeightEigenspace (act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B) (P : B →ₐ[ℂ] Polynomial B)
    (c : ℕ)
    (hA : ∀ (p : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (ψ : Module.Dual ℝ G.lieSubalgebra),
      A p μ ψ ∈ massWeightEigenspace P (2 * (1 + Multiset.card p)))
    (hF : ∀ (t : Multiset (Fin 1 ⊕ Fin 3)) (χ : Module.Dual ℂ V),
      F t χ ∈ massWeightEigenspace P (c + 2 * Multiset.card t))
    {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ V) :
    covDerivIter A act F n l s φ ∈ massWeightEigenspace P (c + 2 * n + 2 * Multiset.card s)
```

**`GlobalGaugeGroup.covDerivIter_mem_anticommuteSubmodule`**, a lemma, [line 822](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L822).

> Anything commuting with every gauge-field symbol and anticommuting with every bare symbol
> of the family anticommutes with every symbol of its covariant tower, since each term of the
> tower is a product of gauge-field symbols with a single bare symbol.

```lean
lemma covDerivIter_mem_anticommuteSubmodule (act : G.lieSubalgebra →ₗ[ℝ] V →ₗ[ℂ] V)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B) {x : B}
    (hxA : ∀ (p : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
      (ψ : Module.Dual ℝ G.lieSubalgebra), Commute x (A p μ ψ))
    (hxF : ∀ (t : Multiset (Fin 1 ⊕ Fin 3)) (χ : Module.Dual ℂ V),
      F t χ ∈ anticommuteSubmodule x) :
    ∀ (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) (s : Multiset (Fin 1 ⊕ Fin 3))
      (φ : Module.Dual ℂ V), covDerivIter A act F n l s φ ∈ anticommuteSubmodule x
```

## Depends on

- [The bracket of adjoint families](../part-01/gaugeboson-adjointfamily-bracket.md)
- [`V`-valued jets](../part-04/localfieldalgebra-jet.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean)
