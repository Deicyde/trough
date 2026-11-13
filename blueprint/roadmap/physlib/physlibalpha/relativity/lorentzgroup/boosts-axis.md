---
declaration: module
origin: cited
lean: Lorentz.SL2C.star_boostAxis_apply
statement: formalized
proof: formalized
---

# Entries of an axis boost

The module `PhyslibAlpha.Relativity.LorentzGroup.Boosts.Axis`, [PhyslibAlpha/Relativity/LorentzGroup/Boosts/Axis.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Boosts/Axis.lean): 1 declaration, 1 with a docstring.

> The Hermiticity of a coordinate-axis boost in `SL(2, ℂ)`, read on its entries.

## i. Overview

> A boost along a coordinate axis, `boostAxis i t ht`, is a Hermitian element of `SL(2, ℂ)`:
> `Physlib.Relativity.LorentzGroup.Boosts.Axis` states this as the matrix equation
> `(boostAxis i t ht).1ᴴ = (boostAxis i t ht).1`. Contracting an axis boost against a family
> of tensor components needs that equation one entry at a time, which is what
> `star_boostAxis_apply` provides: conjugating an entry transposes it.

## ii. Key results

> - `Lorentz.SL2C.star_boostAxis_apply` : conjugating an entry of an axis boost transposes it.

## iv. References

> The matrix form of the axis boosts is fixed in `Physlib.Relativity.LorentzGroup.Boosts.Axis`.

## A. Hermiticity on the entries

**`Lorentz.SL2C.star_boostAxis_apply`**, a lemma, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Boosts/Axis.lean#L49).

> Hermiticity read on the entries: conjugating an entry of an axis boost transposes it.

```lean
lemma star_boostAxis_apply (i : Fin 3) (t : ℝ) (ht : t ≠ 0) (β α : Fin 2) :
    star ((boostAxis i t ht).1 β α) = (boostAxis i t ht).1 α β
```

## Depends on

- [Coordinate-axis boosts in `SL(2,ℂ)` and the Lorentz group](../../../physlib/relativity/lorentzgroup/boosts-axis.md)

## Sources

- [PhyslibAlpha/Relativity/LorentzGroup/Boosts/Axis.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Boosts/Axis.lean)
