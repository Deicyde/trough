---
declaration: module
origin: cited
lean: JetComponentSpace.symbolAction, JetComponentSpace.symbolAction_tmul, JetComponentSpace.symbolAction_one_tmul, JetComponentSpace.repDual, JetComponentSpace.repDual_one_tmul, JetComponentSpace.repJet, JetComponentSpace.repJet_fst, JetComponentSpace.repJet_snd
statement: formalized
proof: formalized
---

# The gauge action on the jet component space

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.JetComponent.GaugeAction`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/GaugeAction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/GaugeAction.lean): 12 declarations, 9 with a docstring.

## i. Overview

> For a matter field valued in `V` with an action of a group `GJ` on its jets
> `SpaceTimeAlgebra ⊗[ℂ] V`, this file constructs the induced action of `GJ` on the jet component
> space. Here `GJ` is any group — for the Standard Model it is the jet gauge group
> `JetGaugeGroupI`, but nothing here depends on that.
>
> The construction needs two hypotheses on the jet action `rep`:
>
> * `hlin` — that `rep` is *fibrewise*, `rep U (χ • z) = χ • rep U z`, the statement that a
>   gauge transformation acts on the values of the field over the identity on spacetime.
>   This is what makes the induced action local (a finite Leibniz convolution) and what
>   makes `rep` determined by its restriction to constant jets.
> * finite dimensionality of `V`, which makes that restriction a *matrix of power series*,
>   an element of `SpaceTimeAlgebra ⊗ End V`.
>
>
> - `JetComponentSpace.jetCoeff` : the coefficient of a fibrewise action, in `SpaceTimeAlgebra ⊗ End
>   V`.
> - `JetComponentSpace.coeff_mul_of_smul_comm` : the coefficient is multiplicative.
> - `JetComponentSpace.symbolAction`, `symbolAction_mul` : its action on symbols, an
>   anti-homomorphism.
> - `JetComponentSpace.repDual` : the induced action on the unconjugated symbols.
> - `JetComponentSpace.repConj`, `repConj_smul_comm` : the action on the jets of the
>   conjugate field.
> - `JetComponentSpace.repJet` : the action on the full component space.
> - `JetComponentSpace.comap_comp_repDual`, `JetComponentSpace.comap_comp_repJet` : both are
>   natural in the value space.

## ii. Key results

> - `symbolAction` : the action of a coefficient on the symbols
> - `symbolAction_tmul`
> - `symbolAction_one_tmul` : a coefficient acts on the undifferentiated symbol through its value at
>   the base point
> - `repDual` : the gauge action on the symbols

## iv. References

> * None.

**`JetComponentSpace.symbolAction`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/GaugeAction.lean#L81).

> **The action of a coefficient on the symbols.** A coefficient `g ⊗ T` acts by
> `jetRingAction g` on the derivative label — the Leibniz convolution redistributing
> derivatives between the gauge transformation and the field — and by the transpose `Tᵀ` on
> the target index.
>
> A coefficient is allowed to change the value space, so that the symbol action of an
> endomorphism and the pullback along a map of value spaces are the same construction; at
> `W = V` this is the action on `Module.End ℂ (SpaceTimeDerivAlgebraℂ ⊗ Module.Dual ℂ V)` that
> `repDual` uses.

```lean
noncomputable def symbolAction :
    (SpaceTimeAlgebra ⊗[ℂ] (V →ₗ[ℂ] W)) →ₗ[ℂ]
      ((SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ W) →ₗ[ℂ]
        (SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ V))
```

**`JetComponentSpace.symbolAction_tmul`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/GaugeAction.lean#L109).

```lean
lemma symbolAction_tmul (g : SpaceTimeAlgebra) (T : V →ₗ[ℂ] W) :
    symbolAction (g ⊗ₜ[ℂ] T)
      = TensorProduct.map (SpaceTimeDerivAlgebraℂ.jetRingAction g) (Module.Dual.transpose T)
```

**`JetComponentSpace.symbolAction_one_tmul`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/GaugeAction.lean#L118).

> **A coefficient acts on the undifferentiated symbol through its value at the base
> point.** On `1 ⊗ φ` — the symbol `ψ_φ` carrying no derivatives — only the constant term of
> the power-series coefficient survives, so the result is again undifferentiated and the
> target index is acted on by the transpose of the base-point value.

```lean
lemma symbolAction_one_tmul (c : SpaceTimeAlgebra ⊗[ℂ] Module.End ℂ V) (φ : Module.Dual ℂ V) :
    symbolAction c ((1 : SpaceTimeDerivAlgebraℂ) ⊗ₜ[ℂ] φ)
      = (1 : SpaceTimeDerivAlgebraℂ) ⊗ₜ[ℂ]
        Module.Dual.transpose (jetEval ∘ₗ TensorProduct.lift
          ((LinearMap.llcomp ℂ V V (SpaceTimeAlgebra ⊗[ℂ] V)).comp
            (TensorProduct.mk ℂ SpaceTimeAlgebra V)) c) φ
```

**`JetComponentSpace.repDual`**, a def, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/GaugeAction.lean#L142).

> **The gauge action on the symbols.** Given a fibrewise gauge action on the jets of a
> `V`-valued field, this is the induced (contragredient) action on the derivative symbols
> `∂_s ψ_α`, which span `SpaceTimeDerivAlgebraℂ ⊗ Module.Dual ℂ V`.
>
> Multiplicativity is bookkeeping: `coeff_mul_of_smul_comm` makes the coefficient
> multiplicative, `symbolAction_mul` makes its action an anti-homomorphism, and the inverse
> flips that back.

```lean
noncomputable def repDual [Module.Free ℂ V] [Module.Finite ℂ V]
    (rep : Representation ℂ GJ (SpaceTimeAlgebra ⊗[ℂ] V))
    (hlin : ∀ (U : GJ) (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] V),
      rep U (χ • z) = χ • rep U z) :
    Representation ℂ GJ (SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ V)
```

**`JetComponentSpace.repDual_one_tmul`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/GaugeAction.lean#L173).

> **The undifferentiated symbol transforms by the value of the gauge transformation at
> the base point.** No derivative of the gauge jet contributes: the symbol `ψ_φ` is acted on
> by the contragredient of `rep U⁻¹` restricted to constant jets and evaluated at the base
> point.

```lean
lemma repDual_one_tmul [Module.Free ℂ V] [Module.Finite ℂ V]
    (rep : Representation ℂ GJ (SpaceTimeAlgebra ⊗[ℂ] V))
    (hlin : ∀ (U : GJ) (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] V),
      rep U (χ • z) = χ • rep U z)
    (U : GJ) (φ : Module.Dual ℂ V) :
    repDual rep hlin U ((1 : SpaceTimeDerivAlgebraℂ) ⊗ₜ[ℂ] φ)
      = (1 : SpaceTimeDerivAlgebraℂ) ⊗ₜ[ℂ]
        Module.Dual.transpose (jetEval ∘ₗ (rep U⁻¹).comp jetOfConstant) φ
```

**`JetComponentSpace.repJet`**, a def, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/GaugeAction.lean#L203).

> **The gauge action on the jet component space.** The induced action of the jets of
> gauge transformations on the full space of component functions of the matter field `M` —
> the symbols `∂_s ψ_α` together with their conjugates `∂_s ψ̄_α`.
>
> The unconjugated half is `repDual M.repJet`, the contragredient action on the symbols. The
> conjugate half is the *same* construction applied to `repConj M.repJet`, the action on the
> jets of the conjugate field; `repConj_smul_comm` supplies the fibrewise-linearity it needs.
> The conjugate half therefore carries `star` of the gauge matrix, which is the physicists'
> `ψ̄ ↦ ψ̄ U†`.
>
> Everything the construction needs is a field of `MatterField`: the jet action `M.repJet`,
> its fibrewise linearity `M.repJet_smul`, and the freeness and finiteness of `M.V`. Taking
> the matter field rather than a bare value space is what removes all three from the
> argument list.

```lean
noncomputable def repJet (M : MatterField jets) :
    Representation ℂ GJ (JetComponentSpace M)
```

**`JetComponentSpace.repJet_fst`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/GaugeAction.lean#L209).

```lean
lemma repJet_fst (M : MatterField jets) (U : GJ) (x : JetComponentSpace M) :
    (repJet M U x).1 = repDual M.repJet M.repJet_smul U x.1
```

**`JetComponentSpace.repJet_snd`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/GaugeAction.lean#L213).

```lean
lemma repJet_snd (M : MatterField jets) (U : GJ) (x : JetComponentSpace M) :
    (repJet M U x).2
      = repDual (repConj M.repJet) (repConj_smul_comm M.repJet_smul) U x.2
```

## A. Naturality in the value space

> A component function is a covector on the value space, so a linear map `f : V →ₗ W` of
> value spaces pulls the symbols of a `W`-valued field back to those of a `V`-valued field.
> If `f` intertwines two fibrewise jet actions then that pullback is equivariant, in the
> opposite direction: this is the gauge counterpart of
> `JetComponentSpace.comap_comp_repLorentzGroup`, and unlike it, it needs the value spaces to
> be finite-dimensional, because the gauge action is defined through the coefficient.
>
> Both halves have to be proved. The unconjugated half is the naturality of `repDual` at
> `f`; the conjugate half is the naturality of `repDual` at `ConjModule.map f`, for the
> conjugate actions, and is supplied by `JetComponentSpace.lTensor_comp_repConj`. A conjugate
> symbol carries `star` of the gauge matrix, so nothing about it follows from the
> unconjugated half.

**`JetComponentSpace.map_transpose_comp_symbolAction`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/GaugeAction.lean#L239).

> Pulling back and then acting is acting and then pulling back, on the symbols of a
> coefficient. Precomposing the symbol action of a coefficient of `W` with the pullback
> along `f` is the symbol action of the coefficient precomposed with `f`.

```lean
lemma map_transpose_comp_symbolAction (f : V →ₗ[ℂ] W) (y : SpaceTimeAlgebra ⊗[ℂ] Module.End ℂ W) :
    (TensorProduct.map LinearMap.id (Module.Dual.transpose f)).comp (symbolAction y)
      = symbolAction (LinearMap.lTensor SpaceTimeAlgebra (LinearMap.lcomp ℂ W f) y)
```

**`JetComponentSpace.symbolAction_comp_map_transpose`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/GaugeAction.lean#L252).

> The companion of `map_transpose_comp_symbolAction` on the other side: postcomposing
> the symbol action of a coefficient of `V` with the pullback along `f` is the symbol
> action of the coefficient postcomposed with `f`.

```lean
lemma symbolAction_comp_map_transpose (f : V →ₗ[ℂ] W) (x : SpaceTimeAlgebra ⊗[ℂ] Module.End ℂ V) :
    (symbolAction x).comp (TensorProduct.map LinearMap.id (Module.Dual.transpose f))
      = symbolAction (LinearMap.lTensor SpaceTimeAlgebra (LinearMap.llcomp ℂ V V W f) x)
```

**`JetComponentSpace.comap_comp_repDual`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/GaugeAction.lean#L268).

> The gauge action on the unconjugated symbols is natural in the value space. A
> linear map of value spaces intertwining two fibrewise jet actions makes the pullback of
> symbols equivariant for the two contragredient actions. The whole content is the naturality
> of the coefficient, `JetComponentSpace.jetCoeff_naturality`, read through the symbol
> action; the group element is inverted on both sides alike, so no convention is disturbed
> by it.

```lean
lemma comap_comp_repDual [Module.Free ℂ V] [Module.Finite ℂ V]
    [Module.Free ℂ W] [Module.Finite ℂ W]
    (repV : Representation ℂ GJ (SpaceTimeAlgebra ⊗[ℂ] V))
    (hV : ∀ (U : GJ) (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] V), repV U
        (χ • z) = χ • repV U z)
    (repW : Representation ℂ GJ (SpaceTimeAlgebra ⊗[ℂ] W))
    (hW : ∀ (U : GJ) (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] W), repW U
        (χ • z) = χ • repW U z)
    (f : V →ₗ[ℂ] W)
    (hf : ∀ U : GJ, (LinearMap.lTensor SpaceTimeAlgebra f).comp (repV U)
      = (repW U).comp (LinearMap.lTensor SpaceTimeAlgebra f)) (U : GJ) :
    (TensorProduct.map LinearMap.id (Module.Dual.transpose f)).comp (repDual repW hW U)
      = (repDual repV hV U).comp
        (TensorProduct.map LinearMap.id (Module.Dual.transpose f))
```

**`JetComponentSpace.comap_comp_repJet`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/GaugeAction.lean#L297).

> The gauge action on the jet component space is natural in the value space. If
> `f : M.V →ₗ N.V` intertwines the two fields' actions on the jets, then the pullback of component
> functions along `f` intertwines the induced actions on the component spaces, in the
> opposite direction — the pullback of a component function of a `W`-valued field being a
> component function of a `V`-valued field.
>
> Both halves are covered and every derivative label is carried: the statement is an equality
> of linear maps on the whole component space, not a statement about undifferentiated
> symbols. The conjugate half is the unconjugated argument applied to `repConj M.repJet` and
> `repConj N.repJet`, whose intertwining is `JetComponentSpace.lTensor_comp_repConj`.

```lean
lemma comap_comp_repJet {M N : MatterField jets} (f : M.V →ₗ[ℂ] N.V)
    (hf : ∀ U : GJ, (LinearMap.lTensor SpaceTimeAlgebra f).comp (M.repJet U)
      = (N.repJet U).comp (LinearMap.lTensor SpaceTimeAlgebra f)) (U : GJ) :
    (comap f).comp (repJet N U) = (repJet M U).comp (comap f)
```

## Depends on

- [The jet component space of a matter field](../part-05/matterfield-jetcomponent-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/GaugeAction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetComponent/GaugeAction.lean)
