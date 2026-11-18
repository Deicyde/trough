---
declaration: module
origin: cited
lean: Representation.prodMap, Representation.prodMap_apply
statement: formalized
proof: formalized
---

# The componentwise representation of a product group

The module `PhyslibAlpha.Mathematics.RepresentationProdMap`, [PhyslibAlpha/Mathematics/RepresentationProdMap.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationProdMap.lean): 2 declarations, 1 with a docstring.

## i. Overview

> Representations `ρ₁` of `G₁` on `V₁` and `ρ₂` of `G₂` on `V₂` give a representation of
> `G₁ × G₂` on `V₁ × V₂`, acting componentwise. Mathlib's `Representation.prod` is the
> diagonal action of a single group; this is the external product.

## ii. Key results

> - `Representation.prodMap` : the componentwise representation.

## iv. References

> * None.

## A. The componentwise representation

**`Representation.prodMap`**, a def, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationProdMap.lean#L41).

> The componentwise representation of a product group on a product space.

```lean
noncomputable def Representation.prodMap {k G₁ G₂ V₁ V₂ : Type*} [CommSemiring k]
    [Monoid G₁] [Monoid G₂] [AddCommMonoid V₁] [Module k V₁] [AddCommMonoid V₂] [Module k V₂]
    (ρ₁ : Representation k G₁ V₁) (ρ₂ : Representation k G₂ V₂) :
    Representation k (G₁ × G₂) (V₁ × V₂)
```

**`Representation.prodMap_apply`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationProdMap.lean#L54).

```lean
lemma Representation.prodMap_apply {k G₁ G₂ V₁ V₂ : Type*} [CommSemiring k]
    [Monoid G₁] [Monoid G₂] [AddCommMonoid V₁] [Module k V₁] [AddCommMonoid V₂] [Module k V₂]
    (ρ₁ : Representation k G₁ V₁) (ρ₂ : Representation k G₂ V₂) (p : G₁ × G₂) (v : V₁ × V₂) :
    Representation.prodMap ρ₁ ρ₂ p v = (ρ₁ p.1 v.1, ρ₂ p.2 v.2)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/RepresentationProdMap.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationProdMap.lean)
