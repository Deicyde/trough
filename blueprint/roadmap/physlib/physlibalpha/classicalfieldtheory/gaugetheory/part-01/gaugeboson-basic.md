---
declaration: module
origin: cited
lean: GaugeBoson, GaugeBoson.valEquiv, GaugeBoson.valLinEquiv, GaugeBoson.valLinEquiv_apply, GaugeBoson.valLinEquiv_symm_apply, GaugeBoson.val_add, GaugeBoson.val_smul, GaugeBoson.repLorentzGroup
statement: formalized
proof: formalized
---

# The gauge-boson field of a gauge theory

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeBoson.Basic`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean): 15 declarations (3 instances with no name), 7 with a docstring.

## i. Overview

> The gauge bosons of a gauge theory with Lie algebra `𝔤` are jointly one bosonic field
> valued in `Lorentz.CoVector ⊗[ℝ] 𝔤`: a spacetime covector with values in the gauge
> algebra. Its components are the fields `A_μ^a`, but **no basis of the gauge algebra is
> chosen**: the adjoint index is carried by an abstract covector `φ : Module.Dual ℝ 𝔤`
> throughout.
>
> This file is the target space alone — its linear structure, the Lorentz action, the
> global gauge action, and the jet component space spanned by the component functions
> `∂_s A_μ^φ`. The jet algebra built on it, and the actions and gradings it carries, are in
> `Physlib.ClassicalFieldTheory.GaugeTheory.GaugeBoson.LocalGaugeFieldAlgebra`. For the Standard
> Model, `𝔤` is `StandardModel.GaugeAlgebra`.

## ii. Key results

> - `GaugeBoson` : the target space of the gauge-boson field.
> - `GaugeBoson.repLorentzGroup` : the Lorentz action on the target space.
> - `GaugeBoson.repValue` : the global gauge action on the target space, from a
>   representation of the value group.
> - `GaugeBoson.JetComponentSpace` : the span of the component functions `∂_s A_μ^φ`.
> - `GaugeBoson.componentDual` : the covector picking out a spacetime and an adjoint index.

## iv. References

> * None.

## A. The target space of the gauge-boson field

**`GaugeBoson`**, a structure, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L69).

> The target vector space of the gauge-boson field: a spacetime covector
> with values in the gauge algebra. Its components are the fields `A_μ^a`; here the
> adjoint index is kept abstract, as the gauge-algebra factor.

```lean
structure GaugeBoson where
  /-- The underlying covector-valued gauge algebra element. -/
  val : Lorentz.CoVector ⊗[ℝ] 𝔤
```

### A.1. Linear structure

**`GaugeBoson.valEquiv`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L83).

> Identifies a gauge boson with its underlying tensor-product value.

```lean
def valEquiv : (GaugeBoson 𝔤) ≃ Lorentz.CoVector ⊗[ℝ] 𝔤
```

**An instance with no name**, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L87).

```lean
noncomputable instance : AddCommGroup (GaugeBoson 𝔤)
```

**An instance with no name**, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L89).

```lean
noncomputable instance : Module ℝ (GaugeBoson 𝔤)
```

**`GaugeBoson.valLinEquiv`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L94).

> The linear identification with the underlying tensor product.

```lean
def valLinEquiv : (GaugeBoson 𝔤) ≃ₗ[ℝ] Lorentz.CoVector ⊗[ℝ] 𝔤
```

**`GaugeBoson.valLinEquiv_apply`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L102).

```lean
lemma valLinEquiv_apply (v : (GaugeBoson 𝔤)) : (valLinEquiv 𝔤) v = v.val
```

**`GaugeBoson.valLinEquiv_symm_apply`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L105).

```lean
lemma valLinEquiv_symm_apply (m : Lorentz.CoVector ⊗[ℝ] 𝔤) :
    (valLinEquiv 𝔤).symm m = ⟨m⟩
```

**`GaugeBoson.val_add`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L110).

```lean
lemma val_add (v₁ v₂ : (GaugeBoson 𝔤)) : (v₁ + v₂).val = v₁.val + v₂.val
```

**`GaugeBoson.val_smul`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L114).

```lean
lemma val_smul (r : ℝ) (v : (GaugeBoson 𝔤)) : (r • v).val = r • v.val
```

**An instance with no name**, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L116).

```lean
instance : Module.Finite ℝ (GaugeBoson 𝔤)
```

### A.2. The Lorentz action on the target space

**`GaugeBoson.repLorentzGroup`**, a def, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L130).

> The Lorentz action on the gauge-boson target space: the covector action on the
> spacetime index, and the trivial action on the gauge-algebra factor.

```lean
noncomputable def repLorentzGroup : Representation ℝ SL(2,ℂ) (GaugeBoson 𝔤)
```

### A.3. The global gauge action on the target space

**`GaugeBoson.repValue`**, a def, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L153).

> The global gauge action on the gauge-boson target space: the adjoint action on the
> gauge-algebra factor, and the trivial action on the spacetime index.

```lean
noncomputable def repValue {G₀ : Type} [Monoid G₀] (ρ : Representation ℝ G₀ 𝔤) :
    Representation ℝ G₀ (GaugeBoson 𝔤)
```

## B. The jet component space

**`GaugeBoson.JetComponentSpace`**, an abbrev, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L181).

> The jet component space of the gauge-boson field: the span of the component functions
> `∂_s A_μ^φ`. The `SpaceTimeDerivAlgebraℝ` factor carries the derivative label `s`, and the
> dual factor the spacetime and adjoint indices — the latter as an abstract covector on
> the gauge algebra, with no basis chosen. Unlike a matter field, the gauge boson is real,
> so there is no conjugate half.

```lean
abbrev JetComponentSpace : Type
```

### B.1. The component covectors

**`GaugeBoson.componentDual`**, a def, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L193).

> The covector on the gauge-boson target space pairing the spacetime index against a
> covector `ω` and the adjoint index against `φ`.

```lean
noncomputable def componentDual :
    Module.Dual ℝ Lorentz.CoVector →ₗ[ℝ]
      Module.Dual ℝ 𝔤 →ₗ[ℝ] Module.Dual ℝ (GaugeBoson 𝔤)
```

**`GaugeBoson.componentDual_apply_val_tmul`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean#L210).

```lean
lemma componentDual_apply_val_tmul (ω : Module.Dual ℝ Lorentz.CoVector)
    (φ : Module.Dual ℝ 𝔤) (v : Lorentz.CoVector) (a : 𝔤) :
    (componentDual 𝔤) ω φ ⟨v ⊗ₜ[ℝ] a⟩ = ω v * φ a
```

## Depends on

- [Derivative algebras](../../../spaceandtime/spacetime/spacetimederivalgebra.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Basic.lean)
