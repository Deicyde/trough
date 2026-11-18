---
declaration: module
origin: cited
lean: GaugeAlgebraRealization.repCoeff, GaugeAlgebraRealization.repDualCoeff, GaugeAlgebraRealization.jetEval_rep_of_smul, GaugeAlgebraRealization.repCoeff_zero_mul, GaugeAlgebraRealization.tensorAction, GaugeAlgebraRealization.tensorAction_tmul, GaugeAlgebraRealization.tensorAction_map_left, GaugeAlgebraRealization.tensorAction_one_left
statement: formalized
proof: formalized
---

# Gauge tensors in a general representation

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.CovariantDeriv`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean): 39 declarations, 22 with a docstring.

## i. Overview

> The adjoint story of `TransformsInAdjoint` generalizes to an arbitrary representation
> of the jet gauge group: a matter field valued in a representation space `V` has
> symbols `[∂_s ψ^i]` contracted against duals of `V`, and its transformation law is
> the Leibniz convolution of the base-point Taylor coefficients of the representation.
>
> Since the gauge transformations are jets, the representation must act on `V`-valued
> jets `SpaceTimeAlgebra ⊗[ℂ] V` — the value of `rep U` at a constant vector is spacetime
> dependent, and the derivative symbols see its Taylor coefficients. This file provides
> the toolkit for `V`-valued jets:
>
> * `jetOfConstant` — the inclusion of constants, `v ↦ 1 ⊗ v`;
> * `jetDeriv`/`jetIteratedDeriv` — the formal derivative, acting on the jet factor;
> * `jetEval` — evaluation at the base point, `f ⊗ v ↦ (constant coefficient of f) • v`;
>
> and with them
>
> * `repDualCoeff rep U x` — the physicists' `∂_x (rep U)^i_j|₀` transposed to the dual
>   of `V`, the analogue of `adjointDualCoeff` for a general representation;
> The gauge tensors of a representation themselves — `LocalGaugeData.TransformsIn`, the
> generalization of `TransformsInAdjoint` — are defined on top of `repDualCoeff` in
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.TransformsIn`.
>
>
> The covariant derivative `∇_ρ F = D_ρ F + (A_ρ acting on the value index)` requires
> the *infinitesimal* action of the gauge algebra on the value space — physicists'
> `i dρ(T^a)` — which cannot be extracted from the abstract group representation `rep`
> (there is no differentiable structure to differentiate it). It is therefore taken as
> data: an `ℝ`-bilinear action `act : GaugeAlgebra →ₗ[ℝ] W →ₗ[ℝ] W`. The layer is
> built for an arbitrary finite-dimensional real value space `W`, so that the adjoint
> case `act = adAction` (the bracket as a bilinear map) literally specializes:
> `covDerivAction A adAction F D ρ = covDerivAdjoint A F D ρ` holds definitionally
> (`covDerivAction_adAction`).
>
> The compatibility between `rep` and `act` — the structure `IsInfinitesimalActionOf` —
> and the theorem that under it the covariant derivative preserves the gauge tensors live
> in `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.InfinitesimalAction`.

## ii. Key results

> - `repDualCoeff` : the physicists' `∂_x (rep U)^i_j|₀` acting on the complex dual index of a
>   matter-field symbol: the transpose of `repCoeff`

## iv. References

> * None.

## A. The dual representation coefficients and gauge tensors in a representation

**`GaugeAlgebraRealization.repCoeff`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L100).

> The base-point Taylor coefficient of the representation: include the constant
> vector into `V`-valued jets, act by `rep U`, differentiate `x` times, evaluate at
> the base point. The composite is complex-linear: the physicists'
> `∂_x (rep U)^i_j|₀` as a ℂ-linear map on the value space.

```lean
noncomputable def repCoeff (rep : Representation ℂ GJ (SpaceTimeAlgebra ⊗[ℂ] V))
    (U : GJ) (x : Multiset (Fin 1 ⊕ Fin 3)) : V →ₗ[ℂ] V
```

**`GaugeAlgebraRealization.repDualCoeff`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L109).

> The physicists' `∂_x (rep U)^i_j|₀` acting on the complex dual index of a
> matter-field symbol: the transpose of `repCoeff`. This is the analogue of
> `adjointDualCoeff` for a general representation of the jet gauge group; for `x = 0`
> it is the dual (contragredient) action of the value of `U`, and for `x ≠ 0` it sees
> the derivatives of the gauge transformation.

```lean
noncomputable def repDualCoeff (rep : Representation ℂ GJ (SpaceTimeAlgebra ⊗[ℂ] V))
    (U : GJ) (x : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ V →ₗ[ℂ] Module.Dual ℂ V
```

**`GaugeAlgebraRealization.jetEval_rep_of_smul`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L117).

> For a fibrewise representation, evaluating the transform of a jet at the base point
> is the zeroth Taylor coefficient of the transform of its base-point value: the jet ring
> factor passes through the action and is then evaluated.

```lean
lemma jetEval_rep_of_smul (rep : Representation ℂ GJ (SpaceTimeAlgebra ⊗[ℂ] V))
    (hlin : ∀ (U : GJ) (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] V), rep U
        (χ • z) = χ • rep U z)
    (U : GJ) (z : SpaceTimeAlgebra ⊗[ℂ] V) :
    jetEval (rep U z) = repCoeff rep U 0 (jetEval z)
```

**`GaugeAlgebraRealization.repCoeff_zero_mul`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L132).

> The zeroth Taylor coefficients of a fibrewise representation are multiplicative: they
> form a representation of the jet gauge group on the value space.

```lean
lemma repCoeff_zero_mul (rep : Representation ℂ GJ (SpaceTimeAlgebra ⊗[ℂ] V))
    (hlin : ∀ (U : GJ) (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] V), rep U
        (χ • z) = χ • rep U z)
    (U W : GJ) : repCoeff rep (U * W) 0 = repCoeff rep U 0 ∘ₗ repCoeff rep W 0
```

## B. The covariant derivative through an infinitesimal action

> The covariant derivative `∇_ρ F = [∂_ρ F] + A_ρ · F` requires the *infinitesimal*
> action of the gauge algebra on the value space — physicists' `i dρ(T^a)` — which
> cannot be extracted from the abstract group representation `rep` (there is no
> differentiable structure to differentiate it). It is therefore taken as data: an
> action `act : 𝔤 →ₗ[ℝ] V →ₗ[ℂ] V`, real-linear in the algebra slot (the
> gauge algebra is a real Lie algebra) and complex-linear in the value slot, matching
> the complex duals indexing the matter families.

**`GaugeAlgebraRealization.tensorAction`**, a def, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L164).

> The action of an adjoint-valued field on a matter field at the tensor level:
> multiplication in `B` on the first factors, the ℂ-linear infinitesimal action `act`
> of the gauge algebra on `V` on the second, so that on pure tensors
> `(b₁ ⊗ c) · (b₂ ⊗ v) = (b₁ b₂) ⊗ act c v`.

```lean
noncomputable def tensorAction (act : 𝔤 →ₗ[ℝ] V →ₗ[ℂ] V) :
    (B ⊗[ℝ] 𝔤) →ₗ[ℝ] (B ⊗[ℂ] V) →ₗ[ℂ] B ⊗[ℂ] V
```

**`GaugeAlgebraRealization.tensorAction_tmul`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L180).

```lean
lemma tensorAction_tmul (act : 𝔤 →ₗ[ℝ] V →ₗ[ℂ] V) (b₁ b₂ : B)
    (c : 𝔤) (v : V) :
    tensorAction act (b₁ ⊗ₜ[ℝ] c) (b₂ ⊗ₜ[ℂ] v) = (b₁ * b₂) ⊗ₜ[ℂ] act c v
```

**`GaugeAlgebraRealization.tensorAction_map_left`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L185).

```lean
lemma tensorAction_map_left (act : 𝔤 →ₗ[ℝ] V →ₗ[ℂ] V) (Φ : B →ₗ[ℂ] B)
    (hΦ : ∀ b₁ b₂, Φ (b₁ * b₂) = Φ b₁ * Φ b₂) (s : B ⊗[ℝ] 𝔤)
    (t : B ⊗[ℂ] V) :
    tensorAction act ((TensorProduct.map (Φ.restrictScalars ℝ) LinearMap.id) s)
        ((TensorProduct.map Φ LinearMap.id) t) =
      (TensorProduct.map Φ LinearMap.id) (tensorAction act s t)
```

**`GaugeAlgebraRealization.tensorAction_one_left`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L201).

```lean
lemma tensorAction_one_left (act : 𝔤 →ₗ[ℝ] V →ₗ[ℂ] V) (c : 𝔤)
    (t : B ⊗[ℂ] V) :
    tensorAction act ((1 : B) ⊗ₜ[ℝ] c) t =
      (TensorProduct.map LinearMap.id (act c)) t
```

**`GaugeAlgebraRealization.tensorAction_map_right_antidiagonal`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L213).

> `tensorAction` under an antidiagonal pair of transport families: if the
> `V`-transports intertwine `act` with the `𝔤`-transports as an
> antidiagonal convolution, so do `id ⊗ ·` over `tensorAction`.

```lean
lemma tensorAction_map_right_antidiagonal (act : 𝔤 →ₗ[ℝ] V →ₗ[ℂ] V)
    (Tg : Multiset (Fin 1 ⊕ Fin 3) → 𝔤 →ₗ[ℝ] 𝔤)
    (Tv : Multiset (Fin 1 ⊕ Fin 3) → V →ₗ[ℂ] V) (x : Multiset (Fin 1 ⊕ Fin 3))
    (hT : ∀ (c : 𝔤) (w : V), Tv x (act c w) =
      (x.antidiagonal.map fun p => act (Tg p.1 c) (Tv p.2 w)).sum)
    (s : B ⊗[ℝ] 𝔤) (t : B ⊗[ℂ] V) :
    (x.antidiagonal.map fun p =>
      tensorAction act ((TensorProduct.map LinearMap.id (Tg p.1)) s)
        ((TensorProduct.map LinearMap.id (Tv p.2)) t)).sum =
      (TensorProduct.map LinearMap.id (Tv x)) (tensorAction act s t)
```

**`GaugeAlgebraRealization.dualPairEquivC`**, a def, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L244).

> The canonical equivalence between matter fields `B ⊗[ℂ] V` and their component
> families `φ ↦ F^φ` over the complex dual — `dualPairEquiv` for a general
> finite-dimensional complex value space.

```lean
noncomputable def dualPairEquivC : (B ⊗[ℂ] V) ≃ₗ[ℂ] (Module.Dual ℂ V →ₗ[ℂ] B)
```

**`GaugeAlgebraRealization.dualPairEquivC_tmul`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L250).

```lean
lemma dualPairEquivC_tmul (b : B) (v : V) (φ : Module.Dual ℂ V) :
    dualPairEquivC (b ⊗ₜ[ℂ] v) φ = φ v • b
```

**`GaugeAlgebraRealization.dualPairEquivC_map_left`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L254).

```lean
lemma dualPairEquivC_map_left (Φ : B →ₗ[ℂ] B) (t : B ⊗[ℂ] V)
    (φ : Module.Dual ℂ V) :
    dualPairEquivC ((TensorProduct.map Φ LinearMap.id) t) φ =
      Φ (dualPairEquivC t φ)
```

**`GaugeAlgebraRealization.dualPairEquivC_map_right`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L262).

```lean
lemma dualPairEquivC_map_right (T : V →ₗ[ℂ] V) (t : B ⊗[ℂ] V)
    (φ : Module.Dual ℂ V) :
    dualPairEquivC ((TensorProduct.map LinearMap.id T) t) φ =
      dualPairEquivC t (T.dualMap φ)
```

**`GaugeAlgebraRealization.symm_comp_left_C`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L270).

```lean
lemma symm_comp_left_C (Φ : B →ₗ[ℂ] B) (g : Module.Dual ℂ V →ₗ[ℂ] B) :
    dualPairEquivC.symm (Φ ∘ₗ g) =
      (TensorProduct.map Φ LinearMap.id) (dualPairEquivC.symm g)
```

**`GaugeAlgebraRealization.symm_comp_right_C`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L279).

```lean
lemma symm_comp_right_C (T : V →ₗ[ℂ] V) (g : Module.Dual ℂ V →ₗ[ℂ] B) :
    dualPairEquivC.symm (g ∘ₗ T.dualMap) =
      (TensorProduct.map LinearMap.id T) (dualPairEquivC.symm g)
```

**`GaugeAlgebraRealization.actionFam`**, a def, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L292).

> The action of an adjoint-indexed component family on a matter one, through the
> infinitesimal action `act`: assemble both into fields, act by `tensorAction`, read
> back out as components. This is the physicists' `f^a (T_a)^i_j g^j` with `T = act`,
> basis-free.

```lean
noncomputable def actionFam (act : 𝔤 →ₗ[ℝ] V →ₗ[ℂ] V)
    (f : Module.Dual ℝ 𝔤 →ₗ[ℝ] B) (g : Module.Dual ℂ V →ₗ[ℂ] B) :
    Module.Dual ℂ V →ₗ[ℂ] B
```

**`GaugeAlgebraRealization.actionFam_add_left`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L297).

```lean
lemma actionFam_add_left (f₁ f₂ : Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (g : Module.Dual ℂ V →ₗ[ℂ] B) :
    actionFam act (f₁ + f₂) g = actionFam act f₁ g + actionFam act f₂ g
```

**`GaugeAlgebraRealization.actionFam_add_right`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L302).

```lean
lemma actionFam_add_right (f : Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (g₁ g₂ : Module.Dual ℂ V →ₗ[ℂ] B) :
    actionFam act f (g₁ + g₂) = actionFam act f g₁ + actionFam act f g₂
```

**`GaugeAlgebraRealization.actionFam_zero_left`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L307).

```lean
lemma actionFam_zero_left (g : Module.Dual ℂ V →ₗ[ℂ] B) :
    actionFam act 0 g = 0
```

**`GaugeAlgebraRealization.actionFam_zero_right`**, a lemma, [line 311](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L311).

```lean
lemma actionFam_zero_right (f : Module.Dual ℝ 𝔤 →ₗ[ℝ] B) :
    actionFam act f 0 = 0
```

**`GaugeAlgebraRealization.actionFam_sum_left`**, a lemma, [line 315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L315).

```lean
lemma actionFam_sum_left (S : Multiset (Module.Dual ℝ 𝔤 →ₗ[ℝ] B))
    (g : Module.Dual ℂ V →ₗ[ℂ] B) :
    actionFam act S.sum g = (S.map fun f => actionFam act f g).sum
```

**`GaugeAlgebraRealization.actionFam_sum_right`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L322).

```lean
lemma actionFam_sum_right (f : Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (S : Multiset (Module.Dual ℂ V →ₗ[ℂ] B)) :
    actionFam act f S.sum = (S.map fun g => actionFam act f g).sum
```

**`GaugeAlgebraRealization.repGauge_actionFam`**, a lemma, [line 335](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L335).

> The gauge transformation of the action of an affinely-transforming
> adjoint-indexed family on a linearly-transforming matter family: the action of the
> transformed families plus one `act`-type cross term. This is `repGauge_bracketFam`
> with a homogeneous second slot and the bracket replaced by a general action.

```lean
lemma repGauge_actionFam
    (U : GJ) {f f' : Module.Dual ℝ 𝔤 →ₗ[ℝ] B}
    {g g' : Module.Dual ℂ V →ₗ[ℂ] B} {cf : 𝔤}
    (hf : ∀ ψ : Module.Dual ℝ 𝔤,
      repGauge U (f ψ) = f' ψ + algebraMap ℂ B (ψ cf))
    (hg : ∀ ψ : Module.Dual ℂ V, repGauge U (g ψ) = g' ψ)
    (φ : Module.Dual ℂ V) :
    repGauge U (actionFam act f g φ) =
      actionFam act f' g' φ + g' (φ ∘ₗ act cf)
```

**`GaugeAlgebraRealization.actionFamConv`**, a def, [line 389](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L389).

> The derived action family `A_ρ · F`: the `s`-derivative of the action of the
> gauge field on a matter family, given by the Leibniz convolution of the derivative
> symbols over the multiset antidiagonal — the matter analogue of `bracketFamConv`.

```lean
noncomputable def actionFamConv
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (act : 𝔤 →ₗ[ℝ] V →ₗ[ℂ] V) (ρ : Fin 1 ⊕ Fin 3)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (s : Multiset (Fin 1 ⊕ Fin 3)) : Module.Dual ℂ V →ₗ[ℂ] B
```

**`GaugeAlgebraRealization.covDerivAction`**, a def, [line 401](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L401).

> The covariant derivative `∇_ρ F = [∂_ρ F] + A_ρ · F` of a matter family of
> derivative symbols, in the single direction `ρ`: the extra derivative on the symbol
> plus the derived action of the gauge field on the value index. With the physicists'
> factor of `i` absorbed into `act` (as it is in the gauge-algebra bracket), this is
> `∂_ρ F + i A_ρ^a T_a F` in the `D = ∂ + i A` convention.

```lean
noncomputable def covDerivAction
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (act : 𝔤 →ₗ[ℝ] V →ₗ[ℂ] V)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (ρ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) : Module.Dual ℂ V →ₗ[ℂ] B
```

**`GaugeAlgebraRealization.covDerivAction_apply`**, a lemma, [line 409](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L409).

```lean
lemma covDerivAction_apply
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (act : 𝔤 →ₗ[ℝ] V →ₗ[ℂ] V)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (ρ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V) :
    covDerivAction A act F ρ s φ = F (ρ ::ₘ s) φ + actionFamConv A act ρ F s φ
```

**`GaugeAlgebraRealization.covDerivIter`**, a def, [line 423](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L423).

> **The iterated covariant derivative** `∇_{l 0} ⋯ ∇_{l (n-1)} F` of a matter family
> along an ordered tuple of directions: covariant derivatives do not commute (their
> commutator is the action of the field strength), so the iteration is order-dependent
> and indexed by `(n : ℕ)` and `l : Fin n → (Fin 1 ⊕ Fin 3)` — the same ordered-tuple
> indexing as the derivative labels of `IsHiggsAlgebraValued`. The result is again a
> family of derivative symbols; the physical iterated covariant derivative is its
> value at the empty multiset.

```lean
noncomputable def covDerivIter
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (act : 𝔤 →ₗ[ℝ] V →ₗ[ℂ] V)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B) :
    (n : ℕ) → (Fin n → (Fin 1 ⊕ Fin 3)) →
      Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B
```

**`GaugeAlgebraRealization.covDerivIter_zero`**, a lemma, [line 433](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L433).

```lean
lemma covDerivIter_zero (act : 𝔤 →ₗ[ℝ] V →ₗ[ℂ] V)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (l : Fin 0 → (Fin 1 ⊕ Fin 3)) :
    covDerivIter A act F 0 l = F
```

**`GaugeAlgebraRealization.covDerivIter_succ`**, a lemma, [line 439](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L439).

```lean
lemma covDerivIter_succ (act : 𝔤 →ₗ[ℝ] V →ₗ[ℂ] V)
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

**`GaugeAlgebraRealization.dualPairEquiv_symm_eq_sum`**, a lemma, [line 459](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L459).

> Decomposition of an assembled adjoint-indexed family along a basis of the gauge
> algebra: the components against the dual basis, tensored with the basis vectors.

```lean
lemma dualPairEquiv_symm_eq_sum {ι : Type*} [Fintype ι]
    (bW : Module.Basis ι ℝ 𝔤)
    (g : Module.Dual ℝ 𝔤 →ₗ[ℝ] B) :
    dualPairEquiv.symm g = ∑ i, g (bW.coord i) ⊗ₜ[ℝ] bW i
```

**`GaugeAlgebraRealization.dualPairEquivC_symm_eq_sum`**, a lemma, [line 483](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L483).

> Decomposition of an assembled matter family along a basis of the value space.

```lean
lemma dualPairEquivC_symm_eq_sum {ι : Type*} [Fintype ι] (bW : Module.Basis ι ℂ V)
    (g : Module.Dual ℂ V →ₗ[ℂ] B) :
    dualPairEquivC.symm g = ∑ i, g (bW.coord i) ⊗ₜ[ℂ] bW i
```

**`GaugeAlgebraRealization.actionFam_apply_mem`**, a lemma, [line 507](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L507).

> The value of an action of families lies in any subalgebra containing the values
> of both families: the action is a finite sum of products of components.

```lean
lemma actionFam_apply_mem {act : 𝔤 →ₗ[ℝ] V →ₗ[ℂ] V} {P : Subalgebra ℂ B}
    {f : Module.Dual ℝ 𝔤 →ₗ[ℝ] B} {g : Module.Dual ℂ V →ₗ[ℂ] B}
    (hf : ∀ ψ, f ψ ∈ P) (hg : ∀ χ, g χ ∈ P) (φ : Module.Dual ℂ V) :
    actionFam act f g φ ∈ P
```

**`GaugeAlgebraRealization.covDerivIter_sub_mem`**, a lemma, [line 521](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L521).

> **Unitriangularity of the covariant matter tower**: the covariant and plain
> derivative symbols of a matter family differ by an element of the subalgebra
> generated by the gauge-field symbols and the strictly lower-order matter symbols.
> Stated at every derivative multiset `s`, as needed for the induction.

```lean
lemma covDerivIter_sub_mem (act : 𝔤 →ₗ[ℝ] V →ₗ[ℂ] V)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ V) :
    covDerivIter A act F n l s φ - F (List.ofFn l + s) φ ∈
      Algebra.adjoin ℂ
        ({b : B | ∃ (u : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
            (ψ : Module.Dual ℝ 𝔤), b = A u μ ψ} ∪
          {b : B | ∃ (t : Multiset (Fin 1 ⊕ Fin 3)) (χ : Module.Dual ℂ V),
            t.card < n + s.card ∧ b = F t χ})
```

**`GaugeAlgebraRealization.covDerivIter_mem_adjoin_symbols`**, a lemma, [line 598](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L598).

> Every derivative symbol of the covariant tower is a polynomial in the gauge-field
> symbols and the matter symbols.

```lean
lemma covDerivIter_mem_adjoin_symbols (act : 𝔤 →ₗ[ℝ] V →ₗ[ℂ] V)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ V) :
    covDerivIter A act F n l s φ ∈ Algebra.adjoin ℂ
      ({b : B | ∃ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
          (ψ : Module.Dual ℝ 𝔤), b = A s μ ψ} ∪
        {b : B | ∃ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V),
          b = F s φ})
```

**`GaugeAlgebraRealization.adjoin_symbols_eq_adjoin_covDerivIter`**, a lemma, [line 624](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L624).

> **The span lemma**: the algebra of symbols generated by the gauge field together
> with a matter family's *derivative* symbols equals the one generated by the gauge
> field together with the matter family's *covariant* derivative tower. The
> correction `∇_ρ − ∂_ρ` is the derived action of the gauge field — a sum of products
> of symbols, absorbed by the algebra structure.

```lean
lemma adjoin_symbols_eq_adjoin_covDerivIter (act : 𝔤 →ₗ[ℝ] V →ₗ[ℂ] V)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B) :
    Algebra.adjoin ℂ
      ({b : B | ∃ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
          (ψ : Module.Dual ℝ 𝔤), b = A s μ ψ} ∪
        {b : B | ∃ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V),
          b = F s φ}) =
    Algebra.adjoin ℂ
      ({b : B | ∃ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
          (ψ : Module.Dual ℝ 𝔤), b = A s μ ψ} ∪
        {b : B | ∃ (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V),
          b = covDerivIter A act F n l 0 φ})
```

## D. Naturality in the algebra

> The matter analogue of `bracketFam_map` and `iteratedCovDerivAdjoint_map`: a
> multiplicative linear map into another algebra carries the derived action, and hence
> the whole covariant matter tower, to the tower of the image families. The derived
> action is a finite sum of products of components, so only multiplicativity is needed;
> no derivative operator on the target is involved.

**`GaugeAlgebraRealization.actionFam_map`**, a lemma, [line 695](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L695).

> The action of an adjoint-indexed family on a matter family is natural in the
> algebra.

```lean
lemma actionFam_map (act : 𝔤 →ₗ[ℝ] V →ₗ[ℂ] V) (f : Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (g : Module.Dual ℂ V →ₗ[ℂ] B) :
    actionFam act (Φ.restrictScalars ℝ ∘ₗ f) (Φ ∘ₗ g) = Φ ∘ₗ actionFam act f g
```

**`GaugeAlgebraRealization.actionFamConv_map`**, a lemma, [line 708](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L708).

> The derived action family is natural in the algebra.

```lean
lemma actionFamConv_map
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (act : 𝔤 →ₗ[ℝ] V →ₗ[ℂ] V) (ρ : Fin 1 ⊕ Fin 3)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (s : Multiset (Fin 1 ⊕ Fin 3)) :
    actionFamConv (fun p σ => Φ.restrictScalars ℝ ∘ₗ A p σ) act ρ (fun p => Φ ∘ₗ F p) s
      = Φ ∘ₗ actionFamConv A act ρ F s
```

**`GaugeAlgebraRealization.covDerivAction_map`**, a lemma, [line 725](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L725).

> The covariant derivative of a matter family is natural in the algebra.

```lean
lemma covDerivAction_map
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (act : 𝔤 →ₗ[ℝ] V →ₗ[ℂ] V)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (ρ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    covDerivAction (fun p σ => Φ.restrictScalars ℝ ∘ₗ A p σ) act (fun p => Φ ∘ₗ F p) ρ s
      = Φ ∘ₗ covDerivAction A act F ρ s
```

**`GaugeAlgebraRealization.covDerivIter_map`**, a lemma, [line 737](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean#L737).

> The iterated covariant derivative of a matter family is natural in the algebra: the
> image of the tower is the tower of the image families, at every ordered tuple of
> directions and every derivative multiset.

```lean
lemma covDerivIter_map
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (act : 𝔤 →ₗ[ℝ] V →ₗ[ℂ] V)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B)
    (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    covDerivIter (fun p σ => Φ.restrictScalars ℝ ∘ₗ A p σ) act (fun p => Φ ∘ₗ F p) n l
      = fun s => Φ ∘ₗ covDerivIter A act F n l s
```

## Depends on

- [The gauge law on brackets and iterated derivatives](../part-01/gaugeboson-realization-gaugelaw.md)
- [`V`-valued jets](../part-03/localfield-jet.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/CovariantDeriv.lean)
