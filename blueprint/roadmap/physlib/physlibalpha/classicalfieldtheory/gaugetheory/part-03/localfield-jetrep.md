---
declaration: module
origin: cited
lean: JetComponentSpace.rep_tmul_of_smul_comm, JetComponentSpace.lift_mul_tmul, JetComponentSpace.rep_lift_of_smul_comm, JetComponentSpace.coeff_mul_of_smul_comm, JetComponentSpace.symbolAction_mul, JetComponentSpace.lift_congr_leftComm, JetComponentSpace.repConj, JetComponentSpace.repConj_apply_tmul
statement: formalized
proof: formalized
---

# Fibrewise actions on `V`-valued jets

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalField.JetRep`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/JetRep.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/JetRep.lean): 19 declarations, 19 with a docstring.

## i. Overview

> A gauge transformation acts on the jets `SpaceTimeAlgebra ⊗[ℂ] V` of a `V`-valued field. What makes
> that action local is that it is *fibrewise*: it commutes with multiplication by scalar
> jets, so it acts on the values of the field over the identity on spacetime. This file
> collects what follows from fibrewise-linearity alone, before any component space is built:
>
> * a fibrewise action is determined by its values on constant jets, and for
>   finite-dimensional `V` that restriction is a matrix of power series, its *coefficient*
>   `jetCoeff` in `SpaceTimeAlgebra ⊗ End V`, which is multiplicative;
> * the conjugate action `repConj` on the jets of the conjugate field, again fibrewise;
> * the naturality of both in the value space: a linear map of value spaces intertwining two
>   fibrewise actions intertwines their coefficients, and their conjugate actions.
>
> These are the ingredients from which the action on the jet component space is assembled in
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.JetComponent.GaugeAction`; they
> live here, upstream of `MatterField`, because the infinitesimal-action theory that
> `MatterField` is stated over already needs `repConj`.
>
>
> - `JetComponentSpace.jetCoeff` : the coefficient of a fibrewise action, in `SpaceTimeAlgebra ⊗ End
>   V`.
> - `JetComponentSpace.coeff_mul_of_smul_comm` : the coefficient is multiplicative.
> - `JetComponentSpace.repConj`, `repConj_smul_comm` : the action on the jets of the
>   conjugate field.
> - `JetComponentSpace.jetCoeff_naturality` : the coefficient is natural in the value space.
> - `JetComponentSpace.lTensor_comp_repConj` : so is the conjugate action.

## ii. Key results

> - `repConj` : the conjugate jet action
> - `repConj_smul_comm` : the conjugate jet action is fibrewise-linear whenever the original is
> - `jetCoeff` : the coefficient of a fibrewise gauge action

## iv. References

> * None.

**`JetComponentSpace.rep_tmul_of_smul_comm`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/JetRep.lean#L76).

> **A fibrewise action is determined by its values on constant jets.** If the gauge
> action commutes with multiplication by scalar jets — the statement that it acts on the
> values of the field, over the identity on spacetime — then its value on a general jet
> `f ⊗ₜ v` is the constant-jet value `rep U (1 ⊗ₜ v)` scaled by `f`.

```lean
lemma rep_tmul_of_smul_comm
    {rep : Representation ℂ G (SpaceTimeAlgebra ⊗[ℂ] V)}
    (hlin : ∀ (U : G) (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] V),
      rep U (χ • z) = χ • rep U z)
    (U : G) (f : SpaceTimeAlgebra) (v : V) :
    rep U (f ⊗ₜ[ℂ] v) = f • rep U (jetOfConstant v)
```

**`JetComponentSpace.lift_mul_tmul`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/JetRep.lean#L89).

> **The canonical evaluation is a right module map.** Writing `ev` for the canonical
> `SpaceTimeAlgebra ⊗ End V → (V →ₗ SpaceTimeAlgebra ⊗ V)`, `g ⊗ T ↦ (v ↦ g ⊗ₜ T v)`, multiplying on
> the right by `b ⊗ T` applies `T` to the argument and scales the value by `b`.

```lean
lemma lift_mul_tmul (x : SpaceTimeAlgebra ⊗[ℂ] Module.End ℂ V)
    (b : SpaceTimeAlgebra) (T : Module.End ℂ V) (v : V) :
    TensorProduct.lift ((LinearMap.llcomp ℂ V V (SpaceTimeAlgebra ⊗[ℂ] V)).comp
        (TensorProduct.mk ℂ SpaceTimeAlgebra V)) (x * (b ⊗ₜ[ℂ] T)) v
      = b • TensorProduct.lift ((LinearMap.llcomp ℂ V V (SpaceTimeAlgebra ⊗[ℂ] V)).comp
        (TensorProduct.mk ℂ SpaceTimeAlgebra V)) x (T v)
```

**`JetComponentSpace.rep_lift_of_smul_comm`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/JetRep.lean#L109).

> **A fibrewise action is the `SpaceTimeAlgebra`-linear extension of its coefficient.** If the
> element `x` of `SpaceTimeAlgebra ⊗ End V` records `rep U` on constant jets, then `rep U` agrees
> with left multiplication by `x` on every coefficient `y`.

```lean
lemma rep_lift_of_smul_comm
    {rep : Representation ℂ G (SpaceTimeAlgebra ⊗[ℂ] V)}
    (hlin : ∀ (U : G) (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] V),
      rep U (χ • z) = χ • rep U z)
    (U : G) (x : SpaceTimeAlgebra ⊗[ℂ] Module.End ℂ V)
    (hx : ∀ v : V, TensorProduct.lift ((LinearMap.llcomp ℂ V V (SpaceTimeAlgebra ⊗[ℂ] V)).comp
      (TensorProduct.mk ℂ SpaceTimeAlgebra V)) x v = rep U (jetOfConstant v))
    (y : SpaceTimeAlgebra ⊗[ℂ] Module.End ℂ V) (v : V) :
    rep U (TensorProduct.lift ((LinearMap.llcomp ℂ V V (SpaceTimeAlgebra ⊗[ℂ] V)).comp
        (TensorProduct.mk ℂ SpaceTimeAlgebra V)) y v)
      = TensorProduct.lift ((LinearMap.llcomp ℂ V V (SpaceTimeAlgebra ⊗[ℂ] V)).comp
        (TensorProduct.mk ℂ SpaceTimeAlgebra V)) (x * y) v
```

**`JetComponentSpace.coeff_mul_of_smul_comm`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/JetRep.lean#L136).

> **The coefficient of a fibrewise action is multiplicative.** Recording `rep` on
> constant jets as a family `c` in `SpaceTimeAlgebra ⊗ End V`, group multiplication becomes
> multiplication in that algebra. This is the identity that makes the induced action on
> the symbols a representation, and it needs no basis.

```lean
lemma coeff_mul_of_smul_comm
    {rep : Representation ℂ G (SpaceTimeAlgebra ⊗[ℂ] V)}
    (hlin : ∀ (U : G) (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] V),
      rep U (χ • z) = χ • rep U z)
    (c : G → SpaceTimeAlgebra ⊗[ℂ] Module.End ℂ V)
    (hc : ∀ (U : G) (v : V),
      TensorProduct.lift ((LinearMap.llcomp ℂ V V (SpaceTimeAlgebra ⊗[ℂ] V)).comp
        (TensorProduct.mk ℂ SpaceTimeAlgebra V)) (c U) v = rep U (jetOfConstant v))
    (U W : G) (v : V) :
    TensorProduct.lift ((LinearMap.llcomp ℂ V V (SpaceTimeAlgebra ⊗[ℂ] V)).comp
        (TensorProduct.mk ℂ SpaceTimeAlgebra V)) (c U * c W) v
      = rep (U * W) (jetOfConstant v)
```

**`JetComponentSpace.symbolAction_mul`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/JetRep.lean#L158).

> **The symbol action of a coefficient is an anti-homomorphism.** Let `Θ` send a
> coefficient `g ⊗ T` in `SpaceTimeAlgebra ⊗ End V` to the endomorphism `jetRingAction g ⊗ Tᵀ` of
> the symbol space `SpaceTimeDerivAlgebraℂ ⊗ Dual V`. Then `Θ` reverses products: the jet-ring
> factor is multiplicative (`jetRingAction_mul`, and `SpaceTimeAlgebra` is commutative) while the
> target factor is contravariant (`Module.Dual.transpose_comp`). Composed with `U ↦ U⁻¹`
> this is exactly what makes the induced action a representation, with no induction over
> the antidiagonal.

```lean
lemma symbolAction_mul
    (Θ : (SpaceTimeAlgebra ⊗[ℂ] Module.End ℂ V) →ₗ[ℂ]
      Module.End ℂ (SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ V))
    (hΘ : ∀ (g : SpaceTimeAlgebra) (T : Module.End ℂ V),
      Θ (g ⊗ₜ[ℂ] T) = TensorProduct.map (SpaceTimeDerivAlgebraℂ.jetRingAction g)
        (Module.Dual.transpose T))
    (x y : SpaceTimeAlgebra ⊗[ℂ] Module.End ℂ V) :
    Θ (x * y) = Θ y ∘ₗ Θ x
```

**`JetComponentSpace.lift_congr_leftComm`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/JetRep.lean#L187).

> **The coefficient of a linear map, canonically.** For finite-dimensional `V` the canonical
> `SpaceTimeAlgebra ⊗ (V →ₗ W) → (V →ₗ SpaceTimeAlgebra ⊗ W)` is inverted by reassociating the
> contraction `Dual V ⊗ (SpaceTimeAlgebra ⊗ W) ≃ SpaceTimeAlgebra ⊗ (Dual V ⊗ W) ≃ SpaceTimeAlgebra ⊗
> (V →ₗ W)`. This is the finite-rank input, obtained from `dualTensorHomEquiv` rather than from a
> basis. Only the source `V` has to be finite-dimensional; the target is arbitrary, which is what lets
> the naturality statements below compare two different value spaces.

```lean
lemma lift_congr_leftComm [Module.Free ℂ V] [Module.Finite ℂ V]
    (G : Module.Dual ℂ V ⊗[ℂ] (SpaceTimeAlgebra ⊗[ℂ] W)) (v : V) :
    TensorProduct.lift ((LinearMap.llcomp ℂ V W (SpaceTimeAlgebra ⊗[ℂ] W)).comp
        (TensorProduct.mk ℂ SpaceTimeAlgebra W))
        ((TensorProduct.congr (LinearEquiv.refl ℂ SpaceTimeAlgebra) (dualTensorHomEquiv ℂ V W))
          (TensorProduct.leftComm ℂ (Module.Dual ℂ V) SpaceTimeAlgebra W G)) v
      = dualTensorHom ℂ V (SpaceTimeAlgebra ⊗[ℂ] W) G v
```

**`JetComponentSpace.repConj`**, a def, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/JetRep.lean#L226).

> **The conjugate jet action.** Given a gauge action on the jets of a `V`-valued field,
> this is the induced action on the jets of the *conjugate* field.
>
> It is `Representation.conj rep` — the same underlying maps, read on `ConjModule` — carried
> across the identification
>
>   `ConjModule (SpaceTimeAlgebra ⊗[ℂ] V) ≃ₗ[ℂ] SpaceTimeAlgebra ⊗[ℂ] ConjModule V`
>
> which is `ConjModule.tensorEquiv` (conjugation is monoidal) followed by
> `SpaceTimeAlgebra.starConjEquiv` on the jet-ring factor (the real structure of the jet ring). On
> pure tensors the composite is `f ⊗ₜ v ↦ star f ⊗ₜ v`, so `repConj` carries the conjugate
> gauge matrix — the physicists' `ψ̄ ↦ ψ̄ U†`.
>
> Being a representation is free: `LinearEquiv.conjRingEquiv` is a ring equivalence of
> endomorphism rings, hence multiplicative.

```lean
noncomputable def repConj (rep : Representation ℂ G (SpaceTimeAlgebra ⊗[ℂ] V)) :
    Representation ℂ G (SpaceTimeAlgebra ⊗[ℂ] ConjModule V)
```

**`JetComponentSpace.repConj_apply_tmul`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/JetRep.lean#L238).

> On pure tensors the conjugate jet action conjugates the jet factor: it is `rep`
> evaluated at `star f ⊗ₜ v`, read back through the same identification.

```lean
lemma repConj_apply_tmul (rep : Representation ℂ G (SpaceTimeAlgebra ⊗[ℂ] V))
    (U : G) (f : SpaceTimeAlgebra) (v : V) :
    repConj rep U (f ⊗ₜ[ℂ] conjEquiv (k := ℂ) (M := V) v)
      = ((ConjModule.tensorEquiv (k := ℂ) (M := SpaceTimeAlgebra) (N := V)).symm.trans
          (TensorProduct.congr SpaceTimeAlgebra.starConjEquiv (LinearEquiv.refl ℂ (ConjModule V))))
        (conjEquiv (k := ℂ) (M := SpaceTimeAlgebra ⊗[ℂ] V) (rep U (star f ⊗ₜ[ℂ] v)))
```

**`JetComponentSpace.tensorEquiv_congr_conjEquiv_smul`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/JetRep.lean#L248).

> **The identification conjugates the jet-ring action.** Carrying a `V`-valued jet over
> to the conjugate side turns multiplication by `star χ` into multiplication by `χ`: the
> `star` on the jet-ring factor is exactly what absorbs the conjugation.

```lean
lemma tensorEquiv_congr_conjEquiv_smul (χ : SpaceTimeAlgebra) (y : SpaceTimeAlgebra ⊗[ℂ] V) :
    ((ConjModule.tensorEquiv (k := ℂ) (M := SpaceTimeAlgebra) (N := V)).symm.trans
        (TensorProduct.congr SpaceTimeAlgebra.starConjEquiv (LinearEquiv.refl ℂ (ConjModule V))))
          (conjEquiv (k := ℂ) (M := SpaceTimeAlgebra ⊗[ℂ] V) (star χ • y))
      = χ • ((ConjModule.tensorEquiv (k := ℂ) (M := SpaceTimeAlgebra) (N := V)).symm.trans
        (TensorProduct.congr SpaceTimeAlgebra.starConjEquiv (LinearEquiv.refl ℂ (ConjModule V))))
          (conjEquiv (k := ℂ) (M := SpaceTimeAlgebra ⊗[ℂ] V) y)
```

**`JetComponentSpace.repConj_apply_conjEquiv`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/JetRep.lean#L269).

> The conjugate jet action is the original one, read through the identification. On
> a jet carried over to the conjugate side, `repConj rep U` is `rep U` applied on the
> original side and carried over again. Everything about `repConj` beyond its definition
> follows from this.

```lean
lemma repConj_apply_conjEquiv (rep : Representation ℂ G (SpaceTimeAlgebra ⊗[ℂ] V)) (U : G)
    (y : SpaceTimeAlgebra ⊗[ℂ] V) :
    repConj rep U (((ConjModule.tensorEquiv (k := ℂ) (M := SpaceTimeAlgebra) (N := V)).symm.trans
        (TensorProduct.congr SpaceTimeAlgebra.starConjEquiv (LinearEquiv.refl ℂ (ConjModule V))))
        (conjEquiv (k := ℂ) (M := SpaceTimeAlgebra ⊗[ℂ] V) y))
      = ((ConjModule.tensorEquiv (k := ℂ) (M := SpaceTimeAlgebra) (N := V)).symm.trans
          (TensorProduct.congr SpaceTimeAlgebra.starConjEquiv (LinearEquiv.refl ℂ (ConjModule V))))
        (conjEquiv (k := ℂ) (M := SpaceTimeAlgebra ⊗[ℂ] V) (rep U y))
```

**`JetComponentSpace.repConj_smul_comm`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/JetRep.lean#L292).

> **The conjugate jet action is fibrewise-linear whenever the original is.** This is
> what lets the coefficient machinery of `coeff_mul_of_smul_comm` be instantiated at
> `ConjModule V`, giving the conjugate half of the symbol action.

```lean
lemma repConj_smul_comm
    {rep : Representation ℂ G (SpaceTimeAlgebra ⊗[ℂ] V)}
    (hlin : ∀ (U : G) (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] V),
      rep U (χ • z) = χ • rep U z)
    (U : G) (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] ConjModule V) :
    repConj rep U (χ • z) = χ • repConj rep U z
```

**`JetComponentSpace.lTensor_conjEquiv_naturality`**, a lemma, [line 313](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/JetRep.lean#L313).

> The identification of the conjugate of the jets with the jets of the conjugate is
> natural in the value space. A linear map of value spaces acts on either side by the same
> underlying map, so carrying a jet over to the conjugate side commutes with it.

```lean
lemma lTensor_conjEquiv_naturality (f : V →ₗ[ℂ] W) (y : SpaceTimeAlgebra ⊗[ℂ] V) :
    (LinearMap.lTensor SpaceTimeAlgebra (ConjModule.map (k := ℂ) f))
        (((ConjModule.tensorEquiv (k := ℂ) (M := SpaceTimeAlgebra) (N := V)).symm.trans
          (TensorProduct.congr SpaceTimeAlgebra.starConjEquiv (LinearEquiv.refl ℂ (ConjModule V))))
          (conjEquiv (k := ℂ) (M := SpaceTimeAlgebra ⊗[ℂ] V) y))
      = ((ConjModule.tensorEquiv (k := ℂ) (M := SpaceTimeAlgebra) (N := W)).symm.trans
          (TensorProduct.congr SpaceTimeAlgebra.starConjEquiv (LinearEquiv.refl ℂ (ConjModule W))))
        (conjEquiv (k := ℂ) (M := SpaceTimeAlgebra ⊗[ℂ] W)
            ((LinearMap.lTensor SpaceTimeAlgebra f) y))
```

**`JetComponentSpace.lTensor_comp_repConj`**, a lemma, [line 335](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/JetRep.lean#L335).

> The conjugate jet action is natural in the value space. A linear map of value
> spaces intertwining two fibrewise jet actions intertwines the actions on the jets of the
> conjugate fields, through the induced map of conjugate modules. This is what supplies the
> conjugate half of the naturality of the gauge action on the jet component space, which
> does not follow from the unconjugated half.

```lean
lemma lTensor_comp_repConj (repV : Representation ℂ G (SpaceTimeAlgebra ⊗[ℂ] V))
    (repW : Representation ℂ G (SpaceTimeAlgebra ⊗[ℂ] W)) (f : V →ₗ[ℂ] W)
    (hf : ∀ U : G, (LinearMap.lTensor SpaceTimeAlgebra f).comp (repV U)
      = (repW U).comp (LinearMap.lTensor SpaceTimeAlgebra f)) (U : G) :
    (LinearMap.lTensor SpaceTimeAlgebra (ConjModule.map (k := ℂ) f)).comp (repConj repV U)
      = (repConj repW U).comp (LinearMap.lTensor SpaceTimeAlgebra (ConjModule.map (k := ℂ) f))
```

**`JetComponentSpace.lift_injective`**, a lemma, [line 357](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/JetRep.lean#L357).

> **The coefficient is determined by its action on constants.** For finite-dimensional `V` the
> canonical evaluation `SpaceTimeAlgebra ⊗ (V →ₗ W) → (V →ₗ SpaceTimeAlgebra ⊗ W)` is injective.

```lean
lemma lift_injective [Module.Free ℂ V] [Module.Finite ℂ V]
    {x y : SpaceTimeAlgebra ⊗[ℂ] (V →ₗ[ℂ] W)}
    (h : ∀ v : V, TensorProduct.lift ((LinearMap.llcomp ℂ V W (SpaceTimeAlgebra ⊗[ℂ] W)).comp
      (TensorProduct.mk ℂ SpaceTimeAlgebra W)) x v = TensorProduct.lift ((LinearMap.llcomp ℂ V W
        (SpaceTimeAlgebra ⊗[ℂ] W)).comp
      (TensorProduct.mk ℂ SpaceTimeAlgebra W)) y v) : x = y
```

**`JetComponentSpace.jetCoeff`**, a def, [line 381](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/JetRep.lean#L381).

> **The coefficient of a fibrewise gauge action.** For finite-dimensional `V`, the
> restriction of `rep U` to constant jets is an element of `SpaceTimeAlgebra ⊗ End V` — a matrix of
> power series, obtained canonically from `dualTensorHomEquiv` rather than from a basis.

```lean
noncomputable def jetCoeff [Module.Free ℂ V] [Module.Finite ℂ V]
    (rep : Representation ℂ G (SpaceTimeAlgebra ⊗[ℂ] V)) (U : G) :
    SpaceTimeAlgebra ⊗[ℂ] Module.End ℂ V
```

**`JetComponentSpace.jetCoeff_spec`**, a lemma, [line 389](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/JetRep.lean#L389).

> The coefficient reproduces `rep U` on constant jets.

```lean
lemma jetCoeff_spec [Module.Free ℂ V] [Module.Finite ℂ V]
    (rep : Representation ℂ G (SpaceTimeAlgebra ⊗[ℂ] V)) (U : G) (v : V) :
    TensorProduct.lift ((LinearMap.llcomp ℂ V V (SpaceTimeAlgebra ⊗[ℂ] V)).comp
      (TensorProduct.mk ℂ SpaceTimeAlgebra V)) (jetCoeff rep U) v = rep U (jetOfConstant v)
```

## A. Naturality of the coefficient in the value space

> A linear map `f : V →ₗ W` of value spaces intertwining two fibrewise jet actions relates their
> coefficients, but not as an equation between elements of two different modules: the comparison takes
> place in `SpaceTimeAlgebra ⊗ (V →ₗ W)`, into which `SpaceTimeAlgebra ⊗ End V` maps by
> postcomposition with `f` and `SpaceTimeAlgebra ⊗ End W` by precomposition. The two images agree, and
> that single identity is what carries the gauge action across a map of value spaces.

**`JetComponentSpace.lift_lTensor_llcomp`**, a lemma, [line 413](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/JetRep.lean#L413).

> Postcomposing a coefficient with `f` evaluates as applying `f` to the value.

```lean
lemma lift_lTensor_llcomp (f : V →ₗ[ℂ] W) (x : SpaceTimeAlgebra ⊗[ℂ] Module.End ℂ V) (v : V) :
    TensorProduct.lift ((LinearMap.llcomp ℂ V W (SpaceTimeAlgebra ⊗[ℂ] W)).comp
        (TensorProduct.mk ℂ SpaceTimeAlgebra W))
        (LinearMap.lTensor SpaceTimeAlgebra (LinearMap.llcomp ℂ V V W f) x) v
      = LinearMap.lTensor SpaceTimeAlgebra f
        (TensorProduct.lift ((LinearMap.llcomp ℂ V V (SpaceTimeAlgebra ⊗[ℂ] V)).comp
          (TensorProduct.mk ℂ SpaceTimeAlgebra V)) x v)
```

**`JetComponentSpace.lift_lTensor_lcomp`**, a lemma, [line 426](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/JetRep.lean#L426).

> Precomposing a coefficient with `f` evaluates as evaluating at the image of the
> argument.

```lean
lemma lift_lTensor_lcomp (f : V →ₗ[ℂ] W) (y : SpaceTimeAlgebra ⊗[ℂ] Module.End ℂ W) (v : V) :
    TensorProduct.lift ((LinearMap.llcomp ℂ V W (SpaceTimeAlgebra ⊗[ℂ] W)).comp
        (TensorProduct.mk ℂ SpaceTimeAlgebra W))
        (LinearMap.lTensor SpaceTimeAlgebra (LinearMap.lcomp ℂ W f) y) v
      = TensorProduct.lift ((LinearMap.llcomp ℂ W W (SpaceTimeAlgebra ⊗[ℂ] W)).comp
        (TensorProduct.mk ℂ SpaceTimeAlgebra W)) y (f v)
```

**`JetComponentSpace.jetCoeff_naturality`**, a lemma, [line 442](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/JetRep.lean#L442).

> The coefficient of a fibrewise action is natural in the value space. If `f` maps
> the values of one field to the values of another and intertwines their jet actions, then
> the coefficient of the first followed by `f` is `f` followed by the coefficient of the
> second, as elements of `SpaceTimeAlgebra ⊗ (V →ₗ W)`. Both value spaces have to be
> finite-dimensional, since both coefficients have to exist; no fibrewise-linearity is used
> here, the coefficient being defined for any action.

```lean
lemma jetCoeff_naturality [Module.Free ℂ V] [Module.Finite ℂ V]
    [Module.Free ℂ W] [Module.Finite ℂ W]
    (repV : Representation ℂ G (SpaceTimeAlgebra ⊗[ℂ] V))
    (repW : Representation ℂ G (SpaceTimeAlgebra ⊗[ℂ] W)) (f : V →ₗ[ℂ] W)
    (hf : ∀ U : G, (LinearMap.lTensor SpaceTimeAlgebra f).comp (repV U)
      = (repW U).comp (LinearMap.lTensor SpaceTimeAlgebra f)) (U : G) :
    LinearMap.lTensor SpaceTimeAlgebra (LinearMap.llcomp ℂ V V W f) (jetCoeff repV U)
      = LinearMap.lTensor SpaceTimeAlgebra (LinearMap.lcomp ℂ W f) (jetCoeff repW U)
```

## Depends on

- [`V`-valued jets](localfield-jet.md)
- [Algebras, duals and representations on a conjugate module](../../../mathematics/part-02/modules/conjmodule.md)
- [Derivative algebras](../../../spaceandtime/spacetime/spacetimederivalgebra.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/JetRep.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/JetRep.lean)
