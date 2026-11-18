---
declaration: module
origin: cited
lean: LorentzGroup.IsOrthochronous, LorentzGroup.isOrthochronous_iff_toVector_timeComponet_nonneg, LorentzGroup.isOrthochronous_iff_transpose, LorentzGroup.isOrthochronous_inv_iff, LorentzGroup.isOrthochronous_iff_ge_one, LorentzGroup.orthochronoustoVelocity, LorentzGroup.not_isOrthochronous_iff_le_neg_one, LorentzGroup.isOrthochronous_iff_not_neg
statement: formalized
proof: formalized
---

# The Orthochronous Lorentz Group

The module `Physlib.Relativity.LorentzGroup.Orthochronous.Basic`, [Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean): 29 declarations, 24 with a docstring.

> We define the give a series of lemmas related to the orthochronous property of lorentz
> matrices.

**`LorentzGroup.IsOrthochronous`**, a def, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L35).

> A Lorentz transformation is `orthochronous` if its `0 0` element is non-negative.

```lean
def IsOrthochronous : Prop
```

**`LorentzGroup.isOrthochronous_iff_toVector_timeComponet_nonneg`**, a lemma, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L39).

> A Lorentz transformation is `orthochronous` if and only if its first column is
> future pointing.

```lean
lemma isOrthochronous_iff_toVector_timeComponet_nonneg :
    IsOrthochronous Λ ↔ 0 ≤ (toVector Λ).timeComponent
```

**`LorentzGroup.isOrthochronous_iff_transpose`**, a lemma, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L44).

> A Lorentz transformation is orthochronous if and only if its transpose is orthochronous.

```lean
lemma isOrthochronous_iff_transpose :
    IsOrthochronous Λ ↔ IsOrthochronous (transpose Λ)
```

**`LorentzGroup.isOrthochronous_inv_iff`**, a lemma, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L48).

```lean
lemma isOrthochronous_inv_iff {Λ : LorentzGroup d} :
    IsOrthochronous Λ⁻¹ ↔ IsOrthochronous Λ
```

**`LorentzGroup.isOrthochronous_iff_ge_one`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L54).

> A Lorentz transformation is orthochronous if and only if its `0 0` element is greater
> or equal to one.

```lean
lemma isOrthochronous_iff_ge_one :
    IsOrthochronous Λ ↔ 1 ≤ Λ.1 (Sum.inl 0) (Sum.inl 0)
```

**`LorentzGroup.orthochronoustoVelocity`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L63).

> The `Lorentz.Velocity` from `Lorentz.toVector` of a orthochronous lorentz
> transformation.

```lean
def orthochronoustoVelocity {Λ : LorentzGroup d} (h : IsOrthochronous Λ) :
    Lorentz.Velocity d
```

**`LorentzGroup.not_isOrthochronous_iff_le_neg_one`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L71).

> A Lorentz transformation is not orthochronous if and only if its `0 0` element is less than
> or equal to minus one.

```lean
lemma not_isOrthochronous_iff_le_neg_one :
    ¬ IsOrthochronous Λ ↔ Λ.1 (Sum.inl 0) (Sum.inl 0) ≤ -1
```

**`LorentzGroup.isOrthochronous_iff_not_neg`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L78).

```lean
lemma isOrthochronous_iff_not_neg :
    IsOrthochronous Λ ↔ ¬ IsOrthochronous (- Λ)
```

**`LorentzGroup.neg_isOrthochronous_iff_not`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L83).

```lean
lemma neg_isOrthochronous_iff_not {Λ : LorentzGroup d} :
    IsOrthochronous (- Λ) ↔ ¬ IsOrthochronous Λ
```

**`LorentzGroup.not_isOrthochronous_iff_le_zero`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L90).

> A Lorentz transformation is not orthochronous if and only if its `0 0` element is
> non-positive.

```lean
lemma not_isOrthochronous_iff_le_zero : ¬ IsOrthochronous Λ ↔ Λ.1 (Sum.inl 0) (Sum.inl 0) ≤ 0
```

**`LorentzGroup.not_isOrthochronous_iff_toVector_timeComponet_nonpos`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L96).

```lean
lemma not_isOrthochronous_iff_toVector_timeComponet_nonpos :
    ¬ IsOrthochronous Λ ↔ (toVector Λ).timeComponent ≤ 0
```

**`LorentzGroup.id_isOrthochronous`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L102).

> The identity Lorentz transformation is orthochronous.

```lean
lemma id_isOrthochronous : @IsOrthochronous d 1
```

**`LorentzGroup.timeCompCont`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L106).

> The continuous map taking a Lorentz transformation to its `0 0` element.

```lean
def timeCompCont : C(LorentzGroup d, ℝ)
```

**`LorentzGroup.stepFunction`**, a def, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L112).

> An auxiliary function used in the definition of `orthchroMapReal`.
> This function takes all elements of `ℝ` less than `-1` to `-1`,
> all elements of `R` greater than `1` to `1` and preserves all other elements.

```lean
def stepFunction : ℝ → ℝ
```

**`LorentzGroup.stepFunction_continuous`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L117).

> The `stepFunction` is continuous.

```lean
lemma stepFunction_continuous : Continuous stepFunction
```

**`LorentzGroup.orthchroMapReal`**, a def, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L127).

> The continuous map from `lorentzGroup` to `ℝ` wh
> taking Orthochronous elements to `1` and non-orthochronous to `-1`.

```lean
def orthchroMapReal : C(LorentzGroup d, ℝ)
```

**`LorentzGroup.orthchroMapReal_on_IsOrthochronous`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L131).

> A Lorentz transformation which is orthochronous maps under `orthchroMapReal` to `1`.

```lean
lemma orthchroMapReal_on_IsOrthochronous {Λ : LorentzGroup d} (h : IsOrthochronous Λ) :
    orthchroMapReal Λ = 1
```

**`LorentzGroup.orthchroMapReal_on_not_IsOrthochronous`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L138).

> A Lorentz transformation which is not-orthochronous maps under `orthchroMapReal` to `- 1`.

```lean
lemma orthchroMapReal_on_not_IsOrthochronous {Λ : LorentzGroup d} (h : ¬ IsOrthochronous Λ) :
    orthchroMapReal Λ = - 1
```

**`LorentzGroup.orthchroMapReal_minus_one_or_one`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L145).

> Every Lorentz transformation maps under `orthchroMapReal` to either `1` or `-1`.

```lean
lemma orthchroMapReal_minus_one_or_one (Λ : LorentzGroup d) :
    orthchroMapReal Λ = -1 ∨ orthchroMapReal Λ = 1
```

**`LorentzGroup.orthchroMap`**, a def, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L154).

> A continuous map from `lorentzGroup` to `ℤ₂` whose kernel are the Orthochronous elements.

```lean
def orthchroMap : C(LorentzGroup d, ℤ₂)
```

**`LorentzGroup.orthchroMap_IsOrthochronous`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L161).

> A Lorentz transformation which is orthochronous maps under `orthchroMap` to `1`
> in `ℤ₂` (the identity element).

```lean
lemma orthchroMap_IsOrthochronous {Λ : LorentzGroup d} (h : IsOrthochronous Λ) :
    orthchroMap Λ = 1
```

**`LorentzGroup.orthchroMap_not_IsOrthochronous`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L167).

> A Lorentz transformation which is not-orthochronous maps under `orthchroMap` to
> the non-identity element of `ℤ₂`.

```lean
lemma orthchroMap_not_IsOrthochronous {Λ : LorentzGroup d} (h : ¬ IsOrthochronous Λ) :
    orthchroMap Λ = Additive.toMul (1 : ZMod 2)
```

**`LorentzGroup.isOrthochronous_mul`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L175).

> The product of two orthochronous Lorentz transformations is orthochronous.

```lean
lemma isOrthochronous_mul {Λ Λ' : LorentzGroup d} (h : IsOrthochronous Λ)
    (h' : IsOrthochronous Λ') : IsOrthochronous (Λ * Λ')
```

**`LorentzGroup.isOrthochronous_mul_iff`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L183).

```lean
lemma isOrthochronous_mul_iff {Λ Λ' : LorentzGroup d} :
    IsOrthochronous (Λ * Λ') ↔ (IsOrthochronous Λ = IsOrthochronous Λ')
```

**`LorentzGroup.orthchroRep`**, a def, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L200).

> The homomorphism from `LorentzGroup` to `ℤ₂`.

```lean
def orthchroRep : LorentzGroup d →* ℤ₂
```

**`LorentzGroup.IsOrthochronous.iff_in_orthchroRep_ker`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L212).

> The orthochronous Lorentz transformations form the kernel of the homomorphism from
> `LorentzGroup` to `ℤ₂`.

```lean
lemma IsOrthochronous.iff_in_orthchroRep_ker : IsOrthochronous Λ ↔ Λ ∈ orthchroRep.ker
```

**`LorentzGroup.orthchroRep_inv_eq_self`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L224).

> The homomorphism from `LorentzGroup` to `ℤ₂` assigns the same value to any Lorentz
> transformation and its inverse.

```lean
lemma orthchroRep_inv_eq_self (Λ : LorentzGroup d) : orthchroRep Λ = orthchroRep Λ⁻¹
```

**`LorentzGroup.isOrthochronous_iff_of_orthchroMap_eq`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L232).

> Two Lorentz transformations are both orthochronous or both not orthochronous if they are mapped
> to the same element via the homomorphism from `LorentzGroup` to `ℤ₂`.

```lean
lemma isOrthochronous_iff_of_orthchroMap_eq {Λ Λ' : LorentzGroup d}
    (h : orthchroMap Λ = orthchroMap Λ') : IsOrthochronous Λ ↔ IsOrthochronous Λ'
```

**`LorentzGroup.isOrthochronous_on_connected_component`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean#L241).

> Two Lorentz transformations which are in the same connected component are either both
> orthochronous or both not orthochronous.

```lean
lemma isOrthochronous_on_connected_component {Λ Λ' : LorentzGroup d}
    (h : Λ' ∈ connectedComponent Λ) : IsOrthochronous Λ ↔ IsOrthochronous Λ'
```

## Depends on

- [The Proper Lorentz Group](proper.md)
- [Vectors from Lorentz group elements](tovector.md)
- [Lorentz Velocities](../tensors/part-04/realtensor-velocity-basic.md)

## Sources

- [Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous/Basic.lean)
