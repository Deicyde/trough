---
declaration: module
origin: cited
lean: PoincareGroup, PoincareGroup.translation_mul, PoincareGroup.lorentz_mul, PoincareGroup.translation_inv, PoincareGroup.lorentz_inv, PoincareGroup.smul_def, PoincareGroup.toHomeomorph, PoincareGroup.toHomeomorph_apply
statement: formalized
proof: formalized
---

# The Poincaré group

The module `PhyslibAlpha.Relativity.Poincare.Basic`, [PhyslibAlpha/Relativity/Poincare/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean): 27 declarations (2 instances with no name), 26 with a docstring.

> The Poincaré group acts on spacetime by Lorentz transformations and translations.

## i. Overview

> An element of the Poincaré group is a pair of a translation `a` and a Lorentz transformation `Λ`.
> It acts on a point `x` by `x ↦ Λ x + a`. The group is built from the existing `LorentzGroup d`
> and the vector group of `SpaceTime d`. The file also defines the action on functions of
> spacetime by `(g • u) x = u (g⁻¹ x)`. A group element is orthochronous when its Lorentz part is.
> The action on functions sends the support of a function to the image of the support.

## ii. Key results

> - `PoincareGroup` : the group of translations and Lorentz transformations.
> - `PoincareGroup.IsOrthochronous` : the Lorentz part preserves the direction of time.
> - `PoincareGroup.act` : the action on functions of spacetime.
> - `PoincareGroup.tsupport_act` : the support of `g • u` is the image of the support of `u`.

## iv. References

> None.

## A. The group

> - `PoincareGroup` : the group of translations and Lorentz transformations.

## B. The action on spacetime

> - `PoincareGroup.toHomeomorph` : each element is a homeomorphism of spacetime.

## C. Orthochronous elements

> - `PoincareGroup.IsOrthochronous` : the Lorentz part preserves the direction of time.

## D. Point reflections

> - `PoincareGroup.pointReflection` : the point reflection `x ↦ p - x`.
> - `PoincareGroup.not_isOrthochronous_pointReflection` : it is not orthochronous.

## E. The action on functions

> - `PoincareGroup.act` : the action `(g • u) x = u (g⁻¹ x)` on functions of spacetime.

**`PoincareGroup`**, a structure, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L74).

> The Poincaré group of `SpaceTime d`. An element `⟨a, Λ⟩` acts by `x ↦ Λ x + a`.

```lean
structure PoincareGroup (d : ℕ) where
  /-- The translation part. -/
  translation : SpaceTime d
  /-- The Lorentz part. -/
  lorentz : LorentzGroup d
```

**An instance with no name**, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L86).

```lean
instance : Group (PoincareGroup d)
```

**`PoincareGroup.translation_mul`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L113).

> The translation part of a product.

```lean
lemma translation_mul (g h : PoincareGroup d) :
    (g * h).translation = g.translation + g.lorentz • h.translation
```

**`PoincareGroup.lorentz_mul`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L117).

> The Lorentz part of a product.

```lean
lemma lorentz_mul (g h : PoincareGroup d) : (g * h).lorentz = g.lorentz * h.lorentz
```

**`PoincareGroup.translation_inv`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L120).

> The translation part of an inverse.

```lean
lemma translation_inv (g : PoincareGroup d) :
    g⁻¹.translation = -(g.lorentz⁻¹ • g.translation)
```

**`PoincareGroup.lorentz_inv`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L124).

> The Lorentz part of an inverse.

```lean
lemma lorentz_inv (g : PoincareGroup d) : g⁻¹.lorentz = g.lorentz⁻¹
```

**An instance with no name**, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L131).

> The Poincaré group acts on spacetime by `x ↦ Λ x + a`.

```lean
instance : MulAction (PoincareGroup d) (SpaceTime d)
```

**`PoincareGroup.smul_def`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L143).

> The action on a point.

```lean
lemma smul_def (g : PoincareGroup d) (x : SpaceTime d) :
    g • x = g.lorentz • x + g.translation
```

**`PoincareGroup.toHomeomorph`**, a def, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L147).

> Each element is a homeomorphism of spacetime.

```lean
def toHomeomorph (g : PoincareGroup d) : SpaceTime d ≃ₜ SpaceTime d
```

**`PoincareGroup.toHomeomorph_apply`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L160).

> The homeomorphism acts as the point action.

```lean
lemma toHomeomorph_apply (g : PoincareGroup d) (x : SpaceTime d) : g.toHomeomorph x = g • x
```

**`PoincareGroup.toHomeomorph_symm_apply`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L163).

> The inverse homeomorphism acts as the inverse point action.

```lean
lemma toHomeomorph_symm_apply (g : PoincareGroup d) (x : SpaceTime d) :
    g.toHomeomorph.symm x = g⁻¹ • x
```

**`PoincareGroup.isCompact_smul`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L167).

> The image of a compact set under a Poincaré transformation is compact.

```lean
lemma isCompact_smul (g : PoincareGroup d) {K : Set (SpaceTime d)} (hK : IsCompact K) :
    IsCompact (g • K)
```

**`PoincareGroup.IsOrthochronous`**, a def, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L178).

> A Poincaré element is orthochronous when its Lorentz part preserves the direction of time.

```lean
def IsOrthochronous (g : PoincareGroup d) : Prop
```

**`PoincareGroup.isOrthochronous_one`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L181).

> The identity is orthochronous.

```lean
lemma isOrthochronous_one : IsOrthochronous (1 : PoincareGroup d)
```

**`PoincareGroup.IsOrthochronous.mul`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L185).

> Products of orthochronous elements are orthochronous.

```lean
lemma IsOrthochronous.mul {g h : PoincareGroup d} (hg : IsOrthochronous g)
    (hh : IsOrthochronous h) : IsOrthochronous (g * h)
```

**`PoincareGroup.IsOrthochronous.inv`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L190).

> Inverses of orthochronous elements are orthochronous.

```lean
lemma IsOrthochronous.inv {g : PoincareGroup d} (hg : IsOrthochronous g) :
    IsOrthochronous g⁻¹
```

**`PoincareGroup.pointReflection`**, a def, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L199).

> The point reflection `x ↦ p - x` as a Poincaré transformation.

```lean
def pointReflection (p : SpaceTime d) : PoincareGroup d
```

**`PoincareGroup.pointReflection_smul`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L202).

> The point reflection sends `x` to `p - x`.

```lean
lemma pointReflection_smul (p x : SpaceTime d) : pointReflection p • x = p - x
```

**`PoincareGroup.not_isOrthochronous_pointReflection`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L209).

> The point reflection is not orthochronous.

```lean
lemma not_isOrthochronous_pointReflection (p : SpaceTime d) :
    ¬ (pointReflection p).IsOrthochronous
```

**`PoincareGroup.act`**, a def, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L223).

> The action on functions of spacetime: `(g • u) x = u (g⁻¹ x)`.

```lean
def act (g : PoincareGroup d) (u : SpaceTime d → V) : SpaceTime d → V
```

**`PoincareGroup.act_apply`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L226).

> The value of the transformed function.

```lean
lemma act_apply (g : PoincareGroup d) (u : SpaceTime d → V) (x : SpaceTime d) :
    act g u x = u (g⁻¹ • x)
```

**`PoincareGroup.act_one`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L230).

> The identity acts trivially.

```lean
lemma act_one (u : SpaceTime d → V) : act (1 : PoincareGroup d) u = u
```

**`PoincareGroup.act_mul`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L235).

> The action is a left action.

```lean
lemma act_mul (g h : PoincareGroup d) (u : SpaceTime d → V) :
    act (g * h) u = act g (act h u)
```

**`PoincareGroup.act_inv_act`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L241).

> The action of an element and its inverse cancel.

```lean
lemma act_inv_act (g : PoincareGroup d) (u : SpaceTime d → V) : act g⁻¹ (act g u) = u
```

**`PoincareGroup.act_add`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L245).

> The action commutes with addition.

```lean
lemma act_add [AddCommGroup V] (g : PoincareGroup d) (u v : SpaceTime d → V) :
    act g (u + v) = act g u + act g v
```

**`PoincareGroup.act_smul`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L249).

> The action commutes with scalar multiplication.

```lean
lemma act_smul {R : Type*} [SMul R V] (g : PoincareGroup d) (c : R) (u : SpaceTime d → V) :
    act g (c • u) = c • act g u
```

**`PoincareGroup.tsupport_act`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean#L256).

> The support of the transformed function is the image of the support.

```lean
lemma tsupport_act [Zero V] (g : PoincareGroup d) (u : SpaceTime d → V) :
    tsupport (act g u) = g • tsupport u
```

## Depends on

- [Spacetime](../../../physlib/spaceandtime/spacetime/basic.md)

## Sources

- [PhyslibAlpha/Relativity/Poincare/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Basic.lean)
