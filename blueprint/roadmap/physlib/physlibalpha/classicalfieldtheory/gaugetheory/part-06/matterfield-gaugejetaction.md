---
declaration: module
origin: cited
lean: GlobalGaugeGroup.MatterField.toLinearMapAlgHom, GlobalGaugeGroup.MatterField.jetAction, GlobalGaugeGroup.MatterField.jetAction_tmul_tmul, GlobalGaugeGroup.MatterField.jetAction_smul, GlobalGaugeGroup.MatterField.jetEval_jetIteratedDeriv_jetAction, GlobalGaugeGroup.MatterField.repAlgebra, GlobalGaugeGroup.MatterField.repAlgebra_apply, GlobalGaugeGroup.MatterField.repJet
statement: formalized
proof: formalized
---

# The jet action of a matter field

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.GaugeJetAction`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/GaugeJetAction.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/GaugeJetAction.lean): 16 declarations, 13 with a docstring.

> The action of gauge jets and of the Lie algebra on the jets of a matter field.

## i. Overview

> A matter field `M` of a global gauge group `G` has a continuous representation
> `ρ : G → GL(V)` on its target space `V`. The jets of the field are `SpaceTimeAlgebra ⊗[ℂ] V`,
> on which the jets of linear maps `SpaceTimeAlgebra ⊗[ℂ] (V →L[ℂ] V)` act fibrewise, `f ⊗ a`
> sending `g ⊗ v` to `f g ⊗ a v`. A gauge jet `U` acts through its jet representation `ρ(U)`, of
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.JetRep`, and the
> Lie algebra through `dρ`.
>
> The physicists' `∂_x ρ(U)|₀` is the base-point Taylor coefficient `M.repCoeff U x` of the jet
> action, the base-point derivative of `ρ(U)`. It obeys two laws, which make `dρ` the
> infinitesimal action underlying the jet action. The Leibniz law `repCoeff_cons` is the
> derivative identity `∂_μ ρ(U) = dρ(ω_μ) ρ(U)` at the base point. The intertwining law
> `repCoeff_act` is the equivariance `ρ(U) dρ(c) = dρ(U c U⁻¹) ρ(U)` at the base
> point, in terms of the adjoint Taylor coefficients `G.adjointCoeff`.

## ii. Key results

> - `GlobalGaugeGroup.MatterField.jetAction` : the action of jets of linear maps on the
>   jets of the field.
> - `GlobalGaugeGroup.MatterField.repJet` : the action of the gauge jets.
> - `GlobalGaugeGroup.MatterField.repAlgebra` : the action of the Lie algebra, `dρ`.
> - `GlobalGaugeGroup.MatterField.repCoeff` : the base-point Taylor coefficients
>   `∂_x ρ(U)|₀`, with the laws `repCoeff_cons` and `repCoeff_act`.

## iv. References

> * None.

## A. The action of jets of linear maps on jets of the field

**`GlobalGaugeGroup.MatterField.toLinearMapAlgHom`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/GaugeJetAction.lean#L76).

> The continuous linear maps on the target space, as linear maps.

```lean
noncomputable def toLinearMapAlgHom : (M.V →L[ℂ] M.V) →ₐ[ℂ] Module.End ℂ M.V
```

**`GlobalGaugeGroup.MatterField.jetAction`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/GaugeJetAction.lean#L81).

> The action of jets of linear maps on the jets of the field, where `f ⊗ a` sends `g ⊗ v` to
> `f g ⊗ a v`.

```lean
noncomputable def jetAction : M.EndJet →ₐ[ℂ] Module.End ℂ (SpaceTimeAlgebra ⊗[ℂ] M.V)
```

**`GlobalGaugeGroup.MatterField.jetAction_tmul_tmul`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/GaugeJetAction.lean#L86).

```lean
lemma jetAction_tmul_tmul (f g : SpaceTimeAlgebra) (a : M.V →L[ℂ] M.V) (v : M.V) :
    jetAction M (f ⊗ₜ[ℂ] a) (g ⊗ₜ[ℂ] v) = (f * g) ⊗ₜ[ℂ] a v
```

**`GlobalGaugeGroup.MatterField.jetAction_smul`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/GaugeJetAction.lean#L90).

> The action is fibrewise, so it commutes with multiplication by scalar jets.

```lean
lemma jetAction_smul (T : M.EndJet) (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] M.V) :
    jetAction M T (χ • z) = χ • jetAction M T z
```

**`GlobalGaugeGroup.MatterField.jetEval_jetIteratedDeriv_jetAction`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/GaugeJetAction.lean#L103).

> The base-point Taylor coefficient along `x` of the action of a jet `T` on a constant is the
> base-point derivative of `T` along `x`.

```lean
lemma jetEval_jetIteratedDeriv_jetAction (T : M.EndJet) (x : Multiset (Fin 1 ⊕ Fin 3))
    (v : M.V) :
    jetEval (jetIteratedDeriv x (jetAction M T (jetOfConstant v))) = jetDerivValue x T v
```

## B. The jet action of the gauge jets

**`GlobalGaugeGroup.MatterField.repAlgebra`**, a def, [line 120](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/GaugeJetAction.lean#L120).

> The action of the gauge algebra, `dρ` as linear maps on the target space.

```lean
noncomputable def repAlgebra : G.lieSubalgebra →ₗ[ℝ] M.V →ₗ[ℂ] M.V
```

**`GlobalGaugeGroup.MatterField.repAlgebra_apply`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/GaugeJetAction.lean#L124).

```lean
lemma repAlgebra_apply (a : G.lieSubalgebra) :
    repAlgebra M a = ((lieAlgebraRep M a : M.V →L[ℂ] M.V) : M.V →ₗ[ℂ] M.V)
```

**`GlobalGaugeGroup.MatterField.repJet`**, a def, [line 129](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/GaugeJetAction.lean#L129).

> The jet action of the jet gauge group, where a gauge jet `U` acts through its jet
> representation `ρ(U)`.

```lean
noncomputable def repJet : Representation ℂ G.gaugeJetGroup (SpaceTimeAlgebra ⊗[ℂ] M.V)
```

**`GlobalGaugeGroup.MatterField.repJet_apply`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/GaugeJetAction.lean#L133).

```lean
lemma repJet_apply (U : G.gaugeJetGroup) : repJet M U = jetAction M (jetRep M U)
```

**`GlobalGaugeGroup.MatterField.repJet_smul`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/GaugeJetAction.lean#L136).

> The jet action is fibrewise, so it commutes with multiplication by scalar jets.

```lean
lemma repJet_smul (U : G.gaugeJetGroup) (χ : SpaceTimeAlgebra)
    (z : SpaceTimeAlgebra ⊗[ℂ] M.V) : repJet M U (χ • z) = χ • repJet M U z
```

### B.1. The base-point Taylor coefficients of the jet action

**`GlobalGaugeGroup.MatterField.repCoeff`**, a def, [line 148](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/GaugeJetAction.lean#L148).

> The physicists' `∂_x ρ(U)|₀`, the base-point Taylor coefficient of the jet action of a
> gauge jet `U` along the multiset of directions `x`, on constant fields.

```lean
noncomputable def repCoeff (U : G.gaugeJetGroup) (x : Multiset (Fin 1 ⊕ Fin 3)) :
    M.V →ₗ[ℂ] M.V
```

**`GlobalGaugeGroup.MatterField.repCoeff_eq`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/GaugeJetAction.lean#L154).

> The base-point Taylor coefficients of the jet action are the base-point derivatives of the
> jet representation.

```lean
lemma repCoeff_eq (U : G.gaugeJetGroup) (x : Multiset (Fin 1 ⊕ Fin 3)) :
    repCoeff M U x = ((jetDerivValue x (jetRep M U) : M.V →L[ℂ] M.V) : M.V →ₗ[ℂ] M.V)
```

**`GlobalGaugeGroup.MatterField.repCoeff_zero`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/GaugeJetAction.lean#L159).

> The base-point value of the jet action of a gauge jet is `ρ` of its value.

```lean
lemma repCoeff_zero (U : G.gaugeJetGroup) :
    repCoeff M U 0 =
      ((M.rep (G.evalGaugeJet U) : (M.V →L[ℂ] M.V)ˣ) : M.V →L[ℂ] M.V)
```

**`GlobalGaugeGroup.MatterField.lieAlgebraRep_evalLie_iteratedDeriv`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/GaugeJetAction.lean#L166).

> `dρ` of the base-point derivatives of a Lie algebra jet are the base-point derivatives of
> its jet `dρ(A)`.

```lean
lemma lieAlgebraRep_evalLie_iteratedDeriv (p : Multiset (Fin 1 ⊕ Fin 3))
    (A : G.jetLieSubalgebra) :
    lieAlgebraRep M (G.evalLie (G.iteratedDerivJ p A)) =
      jetDerivValue p (jetLieAlgebraRep M A)
```

### B.2. The infinitesimal action

**`GlobalGaugeGroup.MatterField.repCoeff_cons`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/GaugeJetAction.lean#L181).

> The Leibniz law of the base-point Taylor coefficients, the derivative identity
> `∂_μ ρ(U) = dρ(ω_μ) ρ(U)` at the base point.

```lean
lemma repCoeff_cons (U : G.gaugeJetGroup) (μ : Fin 1 ⊕ Fin 3)
    (x : Multiset (Fin 1 ⊕ Fin 3)) :
    repCoeff M U (μ ::ₘ x) =
      -((x.antidiagonal.map fun p =>
        repAlgebra M (G.evalLie (G.iteratedDerivJ p.1
          (-G.maurerCartan U μ))) ∘ₗ
            repCoeff M U p.2).sum)
```

**`GlobalGaugeGroup.MatterField.repCoeff_act`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/GaugeJetAction.lean#L199).

> The intertwining law of the base-point Taylor coefficients, the equivariance
> `ρ(U) dρ(c) = dρ(U c U⁻¹) ρ(U)` at the base point.

```lean
lemma repCoeff_act (U : G.gaugeJetGroup) (x : Multiset (Fin 1 ⊕ Fin 3))
    (c : G.lieSubalgebra) :
    repCoeff M U x ∘ₗ repAlgebra M c =
      (x.antidiagonal.map fun p =>
        repAlgebra M (G.adjointCoeff U p.1 c) ∘ₗ
          repCoeff M U p.2).sum
```

## Depends on

- [The Taylor coefficients of the adjoint action](../part-02/globalgaugegroup-adjointcoeff.md)
- [The jet representation of a matter field](matterfield-jetrep.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/GaugeJetAction.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/GaugeJetAction.lean)
