---
declaration: module
origin: cited
lean: GaugeBoson.FieldDerivSpace.repLorentzGroup, SpaceTimeDerivAlgebraℝ.repLorentzGroup_basis_singleton, GaugeBoson.FieldDerivSpace.repLorentzGroup_jetDeriv, LocalGaugeFieldAlgebra.repLorentzGroup, LocalGaugeFieldAlgebra.repLorentzGroup_apply, LocalGaugeFieldAlgebra.repLorentzGroup_apply_one, LocalGaugeFieldAlgebra.repLorentzGroup_apply_mul, LocalGaugeFieldAlgebra.repLorentzGroup_ι
statement: formalized
proof: formalized
---

# The Lorentz action on the gauge-boson jet algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeBoson.LocalGaugeFieldAlgebra.LorentzAction`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/LorentzAction.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/LorentzAction.lean): 19 declarations, 12 with a docstring.

> The action of `SL(2,ℂ)` on the gauge-boson jet algebra, for which the total derivative is a
> Lorentz vector.

## i. Overview

> The Lorentz group acts on the jet algebra of the gauge bosons by the symmetric-algebra
> functor applied to its action on the field-derivative space. The derivative labels transform
> in `SpaceTimeDerivAlgebraℝ` and the target index contragrediently through the covector action on
> `GaugeBoson`. The formal total derivative is a Lorentz vector for this action. On the
> complexification this is packaged as a `Lorentz.IsLorentzDeriv` instance.

## ii. Key results

> - `GaugeBoson.FieldDerivSpace.repLorentzGroup` : the Lorentz action on the component
>   space.
> - `LocalGaugeFieldAlgebra.repLorentzGroup` : the Lorentz action on the jet algebra.
> - `LocalGaugeFieldAlgebra.repLorentzGroup_jetDeriv` : the total derivative is a Lorentz vector.
> - `LocalGaugeFieldAlgebra.complexRepLorentzGroup` : the action on the complexification.
> - `LocalGaugeFieldAlgebra.instIsLorentzDeriv` : the `Lorentz.IsLorentzDeriv` instance.

## iv. References

> * None.

## A. The Lorentz action on the component space

**`GaugeBoson.FieldDerivSpace.repLorentzGroup`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/LorentzAction.lean#L69).

> The Lorentz action on the field-derivative space of the gauge bosons. The derivative
> label transforms in `SpaceTimeDerivAlgebraℝ` and the target index contragrediently.

```lean
noncomputable def FieldDerivSpace.repLorentzGroup :
    Representation ℝ SL(2,ℂ) (FieldDerivSpace G)
```

### A.1. Covariance of the derivative shift

**`SpaceTimeDerivAlgebraℝ.repLorentzGroup_basis_singleton`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/LorentzAction.lean#L81).

> The Lorentz action on the singleton derivative symbol. The derivative slot transforms
> by the columns of the Lorentz matrix.

```lean
lemma _root_.SpaceTimeDerivAlgebraℝ.repLorentzGroup_basis_singleton
    (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) :
    SpaceTimeDerivAlgebraℝ.repLorentzGroup Λ
        (SpaceTimeDerivAlgebraℝ.basisMultiset ({μ} : Multiset (Fin 1 ⊕ Fin 3))) =
      ∑ a, ((Lorentz.SL2C.toLorentzGroup Λ).1 a μ) •
        SpaceTimeDerivAlgebraℝ.basisMultiset ({a} : Multiset (Fin 1 ⊕ Fin 3))
```

**`GaugeBoson.FieldDerivSpace.repLorentzGroup_jetDeriv`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/LorentzAction.lean#L95).

> The derivative shift is a Lorentz vector on the component space. Appending `∂_μ`
> and then acting is acting and then appending the transformed `∂_μ`.

```lean
lemma FieldDerivSpace.repLorentzGroup_jetDeriv (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3)
    (v : (FieldDerivSpace G)) :
    (FieldDerivSpace.repLorentzGroup G) Λ ((FieldDerivSpace.jetDeriv G) μ v) =
      ∑ a, ((Lorentz.SL2C.toLorentzGroup Λ).1 a μ) •
        (FieldDerivSpace.jetDeriv G) a ((FieldDerivSpace.repLorentzGroup G) Λ v)
```

## B. The Lorentz action on the jet algebra

**`LocalGaugeFieldAlgebra.repLorentzGroup`**, a def, [line 136](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/LorentzAction.lean#L136).

> The Lorentz action on the gauge-boson jet algebra, the symmetric-algebra functor
> applied to the Lorentz action on the field-derivative space.

```lean
noncomputable def repLorentzGroup : Representation ℝ SL(2,ℂ) (LocalGaugeFieldAlgebra G)
```

**`LocalGaugeFieldAlgebra.repLorentzGroup_apply`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/LorentzAction.lean#L145).

```lean
lemma repLorentzGroup_apply (Λ : SL(2,ℂ)) (x : (LocalGaugeFieldAlgebra G)) :
    (repLorentzGroup G) Λ x =
      SymmetricAlgebra.map ((GaugeBoson.FieldDerivSpace.repLorentzGroup G) Λ) x
```

**`LocalGaugeFieldAlgebra.repLorentzGroup_apply_one`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/LorentzAction.lean#L150).

```lean
lemma repLorentzGroup_apply_one (Λ : SL(2,ℂ)) :
    (repLorentzGroup G) Λ (1 : (LocalGaugeFieldAlgebra G)) = 1
```

**`LocalGaugeFieldAlgebra.repLorentzGroup_apply_mul`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/LorentzAction.lean#L154).

```lean
lemma repLorentzGroup_apply_mul (Λ : SL(2,ℂ)) (x y : (LocalGaugeFieldAlgebra G)) :
    (repLorentzGroup G) Λ (x * y) = (repLorentzGroup G) Λ x * (repLorentzGroup G) Λ y
```

**`LocalGaugeFieldAlgebra.repLorentzGroup_ι`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/LorentzAction.lean#L159).

```lean
lemma repLorentzGroup_ι (Λ : SL(2,ℂ)) (v : (GaugeBoson.FieldDerivSpace G)) :
    (repLorentzGroup G) Λ (SymmetricAlgebra.ι ℝ _ v) =
      SymmetricAlgebra.ι ℝ _ ((GaugeBoson.FieldDerivSpace.repLorentzGroup G) Λ v)
```

## C. Lorentz covariance of the total derivative

**`LocalGaugeFieldAlgebra.repLorentzGroup_jetDeriv`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/LorentzAction.lean#L171).

> The total derivative on the gauge-boson jet algebra is a Lorentz vector.

```lean
lemma repLorentzGroup_jetDeriv (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) (x : (LocalGaugeFieldAlgebra G)) :
    (repLorentzGroup G) Λ ((jetDeriv G) μ x) =
      ∑ a, ((Lorentz.SL2C.toLorentzGroup Λ).1 a μ) •
        (jetDeriv G) a ((repLorentzGroup G) Λ x)
```

## D. The complexified action

**`LocalGaugeFieldAlgebra.complexRepLorentzGroup`**, a def, [line 202](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/LorentzAction.lean#L202).

> The Lorentz action on the complexified gauge-boson jet algebra, by base change.

```lean
noncomputable def complexRepLorentzGroup :
    Representation ℂ SL(2,ℂ) (ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra G))
```

**`LocalGaugeFieldAlgebra.complexRepLorentzGroup_tmul`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/LorentzAction.lean#L211).

```lean
lemma complexRepLorentzGroup_tmul (Λ : SL(2,ℂ)) (z : ℂ) (x : (LocalGaugeFieldAlgebra G)) :
    (complexRepLorentzGroup G) Λ (z ⊗ₜ[ℝ] x) = z ⊗ₜ[ℝ] (repLorentzGroup G) Λ x
```

**`LocalGaugeFieldAlgebra.complexRepLorentzGroupAlgHom`**, a def, [line 218](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/LorentzAction.lean#L218).

> The action of a Lorentz transformation on the complexified gauge-boson jet algebra, as
> an algebra endomorphism, the base change of the symmetric-algebra functor applied to the
> action on the field-derivative space.

```lean
noncomputable def complexRepLorentzGroupAlgHom (Λ : SL(2,ℂ)) :
    ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra G) →ₐ[ℂ] ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra G)
```

**`LocalGaugeFieldAlgebra.complexRepLorentzGroup_apply`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/LorentzAction.lean#L223).

```lean
lemma complexRepLorentzGroup_apply (Λ : SL(2,ℂ)) (x : ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra G)) :
    (complexRepLorentzGroup G) Λ x = complexRepLorentzGroupAlgHom G Λ x
```

**`LocalGaugeFieldAlgebra.complexRepLorentzGroup_apply_mul`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/LorentzAction.lean#L229).

```lean
lemma complexRepLorentzGroup_apply_mul (Λ : SL(2,ℂ)) (x y : ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra G)) :
    (complexRepLorentzGroup G) Λ (x * y)
      = (complexRepLorentzGroup G) Λ x * (complexRepLorentzGroup G) Λ y
```

**`LocalGaugeFieldAlgebra.complexRepLorentzGroup_jetDeriv`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/LorentzAction.lean#L243).

> The complexified total derivative is a Lorentz vector.

```lean
lemma complexRepLorentzGroup_jetDeriv (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3)
    (x : ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra G)) :
    (complexRepLorentzGroup G) Λ ((complexJetDeriv G) μ x) =
      ∑ a, (((Lorentz.SL2C.toLorentzGroup Λ).1 a μ : ℝ) : ℂ) •
        (complexJetDeriv G) a ((complexRepLorentzGroup G) Λ x)
```

**`LocalGaugeFieldAlgebra.instIsLorentzDeriv`**, an instance, [line 263](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/LorentzAction.lean#L263).

> The complexified total derivatives form a Lorentz derivative, a family of derivatives
> transforming as a Lorentz vector.

```lean
instance instIsLorentzDeriv :
    Lorentz.IsLorentzDeriv (complexRepLorentzGroup G) (complexJetDeriv G)
```

## E. The Lorentz law of the gauge-field generators

**`GaugeBoson.repLorentzGroup_dual_componentDual`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/LorentzAction.lean#L275).

> The contragredient Lorentz action passes through a component covector to its spacetime
> slot. The adjoint index is Lorentz-inert.

```lean
lemma _root_.GaugeBoson.repLorentzGroup_dual_componentDual (Λ : SL(2,ℂ))
    (ω : Module.Dual ℝ Lorentz.CoVector) (φ : Module.Dual ℝ G.lieSubalgebra) :
    (GaugeBoson.repLorentzGroup G).dual Λ ((GaugeBoson.componentDual G) ω φ)
      = (GaugeBoson.componentDual G) (Lorentz.CoVector.sl2Rep.dual Λ ω) φ
```

**`LocalGaugeFieldAlgebra.repLorentzGroup_ofA`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/LorentzAction.lean#L294).

> The gauge field is a Lorentz covector. The generator `A_μ^φ` mixes into the `A_a^φ`
> by the columns of the Lorentz matrix, with the adjoint index untouched.

```lean
lemma repLorentzGroup_ofA (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    (repLorentzGroup G) Λ ((ofA G) μ φ)
      = ∑ a, ((Lorentz.SL2C.toLorentzGroup Λ).1 a μ) • (ofA G) a φ
```

**`LocalGaugeFieldAlgebra.complexRepLorentzGroup_one_tmul_ofA`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/LorentzAction.lean#L314).

> The Lorentz law of the gauge-field generators on the complexification.

```lean
lemma complexRepLorentzGroup_one_tmul_ofA (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    (complexRepLorentzGroup G) Λ ((1 : ℂ) ⊗ₜ[ℝ] (ofA G) μ φ)
      = ∑ a, (((Lorentz.SL2C.toLorentzGroup Λ).1 a μ : ℝ) : ℂ) •
          ((1 : ℂ) ⊗ₜ[ℝ] (ofA G) a φ)
```

## Depends on

- [The formal total derivative on the gauge-boson jet algebra](gaugeboson-localgaugefieldalgebra-jetderiv.md)
- [Class IsLorentzDeriv](../../../relativity/islorentzderiv.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/LorentzAction.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/LorentzAction.lean)
