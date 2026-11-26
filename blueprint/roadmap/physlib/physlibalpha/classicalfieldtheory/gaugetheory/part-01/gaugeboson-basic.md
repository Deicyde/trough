---
declaration: module
origin: cited
lean: GaugeBoson, GaugeBoson.valEquiv, GaugeBoson.valLinEquiv, GaugeBoson.valLinEquiv_apply, GaugeBoson.valLinEquiv_symm_apply, GaugeBoson.val_add, GaugeBoson.val_smul, GaugeBoson.repLorentzGroup
statement: formalized
proof: formalized
---

# The gauge-boson field of a gauge theory

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeBoson.Basic`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean): 16 declarations (3 instances with no name), 8 with a docstring.

> The target space of the gauge bosons, a spacetime covector with values in the gauge algebra.

## i. Overview

> The gauge bosons of a gauge theory with Lie algebra `G.lieSubalgebra` are jointly one bosonic field
> valued in `Lorentz.CoVector ⊗[ℝ] G.lieSubalgebra`, a spacetime covector with values in the gauge
> algebra. Its components are the fields `A_μ^a`, but no basis of the gauge algebra is
> chosen. The adjoint index is carried by an abstract covector `φ : Module.Dual ℝ G.lieSubalgebra`
> throughout.
>
> This file is the target space alone, with its linear structure, the Lorentz action, the
> global gauge action, and the field-derivative space spanned by the component functions
> `∂_s A_μ^φ`. The jet algebra built on it, and the actions and gradings it carries, are in the
> directory
> `PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra`. For the Standard
> Model, `G.lieSubalgebra` is `StandardModel.GaugeAlgebra`.

## ii. Key results

> - `GaugeBoson` : the target space of the gauge-boson field.
> - `GaugeBoson.repLorentzGroup` : the Lorentz action on the target space.
> - `GaugeBoson.repValue` : the global gauge action on the target space, from a
>   representation of the value group.
> - `GaugeBoson.FieldDerivSpace` : the span of the component functions `∂_s A_μ^φ`.
> - `GaugeBoson.componentDual` : the covector picking out a spacetime and an adjoint index.
> - `GaugeBoson.dual_eq_sum_componentDual` : every covector on the target space is a sum of
>   component covectors.

## iv. References

> * None.

## A. The target space of the gauge-boson field

**`GaugeBoson`**, a structure, [line 75](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L75).

> The target vector space of the gauge-boson field, a spacetime covector
> with values in the gauge algebra. Its components are the fields `A_μ^a`, and here the
> adjoint index is kept abstract, as the gauge-algebra factor.

```lean
structure GaugeBoson where
  /-- The underlying covector-valued gauge algebra element. -/
  val : Lorentz.CoVector ⊗[ℝ] G.lieSubalgebra
```

### A.1. Linear structure

**`GaugeBoson.valEquiv`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L89).

> Identifies a gauge boson with its underlying tensor-product value.

```lean
def valEquiv : (GaugeBoson G) ≃ Lorentz.CoVector ⊗[ℝ] G.lieSubalgebra
```

**An instance with no name**, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L93).

```lean
noncomputable instance : AddCommGroup (GaugeBoson G)
```

**An instance with no name**, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L95).

```lean
noncomputable instance : Module ℝ (GaugeBoson G)
```

**`GaugeBoson.valLinEquiv`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L100).

> The linear identification with the underlying tensor product.

```lean
def valLinEquiv : (GaugeBoson G) ≃ₗ[ℝ] Lorentz.CoVector ⊗[ℝ] G.lieSubalgebra
```

**`GaugeBoson.valLinEquiv_apply`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L107).

```lean
lemma valLinEquiv_apply (v : (GaugeBoson G)) : (valLinEquiv G) v = v.val
```

**`GaugeBoson.valLinEquiv_symm_apply`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L109).

```lean
lemma valLinEquiv_symm_apply (m : Lorentz.CoVector ⊗[ℝ] G.lieSubalgebra) :
    (valLinEquiv G).symm m = ⟨m⟩
```

**`GaugeBoson.val_add`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L113).

```lean
lemma val_add (v₁ v₂ : (GaugeBoson G)) : (v₁ + v₂).val = v₁.val + v₂.val
```

**`GaugeBoson.val_smul`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L116).

```lean
lemma val_smul (r : ℝ) (v : (GaugeBoson G)) : (r • v).val = r • v.val
```

**An instance with no name**, [line 118](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L118).

```lean
instance : Module.Finite ℝ (GaugeBoson G)
```

### A.2. The Lorentz action on the target space

**`GaugeBoson.repLorentzGroup`**, a def, [line 132](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L132).

> The Lorentz action on the gauge-boson target space, the covector action on the
> spacetime index and the trivial action on the gauge-algebra factor.

```lean
noncomputable def repLorentzGroup : Representation ℝ SL(2,ℂ) (GaugeBoson G)
```

### A.3. The global gauge action on the target space

**`GaugeBoson.repValue`**, a def, [line 155](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L155).

> The global gauge action on the gauge-boson target space, the given action on the
> gauge-algebra factor and the trivial action on the spacetime index.

```lean
noncomputable def repValue {G₀ : Type} [Monoid G₀] (ρ : Representation ℝ G₀ G.lieSubalgebra) :
    Representation ℝ G₀ (GaugeBoson G)
```

## B. The field-derivative space

**`GaugeBoson.FieldDerivSpace`**, an abbrev, [line 183](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L183).

> The field-derivative space of the gauge-boson field, the span of the component functions
> `∂_s A_μ^φ`. The `SpaceTimeDerivAlgebraℝ` factor carries the derivative label `s`, and the
> dual factor the spacetime and adjoint indices, the latter as an abstract covector on
> the gauge algebra with no basis chosen. Unlike a matter field, the gauge boson is real,
> so there is no conjugate half.

```lean
abbrev FieldDerivSpace : Type
```

### B.1. The component covectors

**`GaugeBoson.componentDual`**, a def, [line 195](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L195).

> The covector on the gauge-boson target space pairing the spacetime index against a
> covector `ω` and the adjoint index against `φ`.

```lean
noncomputable def componentDual :
    Module.Dual ℝ Lorentz.CoVector →ₗ[ℝ]
      Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] Module.Dual ℝ (GaugeBoson G)
```

**`GaugeBoson.componentDual_apply_val_tmul`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L211).

```lean
lemma componentDual_apply_val_tmul (ω : Module.Dual ℝ Lorentz.CoVector)
    (φ : Module.Dual ℝ G.lieSubalgebra) (v : Lorentz.CoVector) (a : G.lieSubalgebra) :
    (componentDual G) ω φ ⟨v ⊗ₜ[ℝ] a⟩ = ω v * φ a
```

**`GaugeBoson.dual_eq_sum_componentDual`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L219).

> Every covector on the gauge-boson target space decomposes along the Lorentz coordinate
> directions into component covectors. The spacetime index is expanded in the coordinate
> basis, while the adjoint index stays abstract.

```lean
lemma dual_eq_sum_componentDual
    (ψ : Module.Dual ℝ (GaugeBoson G)) :
    ψ = ∑ μ, (GaugeBoson.componentDual G) (Lorentz.CoVector.basis.dualBasis μ)
      (ψ ∘ₗ (GaugeBoson.valLinEquiv G).symm.toLinearMap ∘ₗ
        TensorProduct.mk ℝ Lorentz.CoVector G.lieSubalgebra (Lorentz.CoVector.basis μ))
```

## Depends on

- [The Lie algebra of a global gauge group](../part-02/globalgaugegroup-liealgebra-basic.md)
- [Derivative algebras](../../../spaceandtime/spacetime/spacetimederivalgebra.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean)
