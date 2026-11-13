---
declaration: module
origin: cited
lean: Physlib.CondensedMatter.Crystal.Bond, Physlib.CondensedMatter.Crystal.Bond.Links, Physlib.CondensedMatter.Crystal.Bond.links_reference, Physlib.CondensedMatter.Crystal.Bond.eq_of_links, Physlib.CondensedMatter.Crystal.Bond.links_vadd
statement: formalized
proof: formalized
---

# Bonds in a crystal

The module `Physlib.CondensedMatter.Crystal.Bonds`, [Physlib/CondensedMatter/Crystal/Bonds.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Bonds.lean): 7 declarations (2 instances with no name), 7 with a docstring.

> A bond connects sites in two unit cells of a crystal.

## i. Overview

> A bond `⟨i, j, d⟩` joins the site with label `i` in cell `n` to the site with label `j`
> in cell `n + d`. Translating both endpoints gives another copy of the same bond.

## ii. Key results

> - `Bond` : a source label, a target label and the displacement between their cells.
> - `Bond.Links` : the relation between sites connected by a bond.

## iv. References

> * F. Göhmann, *Introduction to Solid State Physics*, lecture L3, Section 3.1, for the standard
>   description of a crystal. [ref: goehmann\_solid\_state\_2021]

## A. Bonds in a unit cell

**`Physlib.CondensedMatter.Crystal.Bond`**, a structure, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Bonds.lean#L45).

> A bond from `source` in one cell to `target` in the cell displaced by `displacement`.

```lean
structure Bond (C : Crystal G) where
  /-- The site label at the start of the bond. -/
  source : C.UnitCell
  /-- The site label at the end of the bond. -/
  target : C.UnitCell
  /-- Translation from the source cell to the target cell. -/
  displacement : G
```

**An instance with no name**, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Bonds.lean#L54).

> Bonds can be compared when cells and unit-cell labels can be compared.

```lean
instance {C : Crystal G} [DecidableEq G] [DecidableEq C.UnitCell] : DecidableEq (Bond C)
```

**`Physlib.CondensedMatter.Crystal.Bond.Links`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Bonds.lean#L62).

> Site `x` is the source and site `y` is the target of this bond.

```lean
def Links (b : Bond C) (x y : C.Site) : Prop
```

**`Physlib.CondensedMatter.Crystal.Bond.links_reference`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Bonds.lean#L66).

> Every bond links the reference site of its source to the site its displacement points to.

```lean
lemma links_reference (b : Bond C) : b.Links (Site.ref b.source) ⟨b.displacement, b.target⟩
```

**`Physlib.CondensedMatter.Crystal.Bond.eq_of_links`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Bonds.lean#L70).

> Two bonds linking the same pair of sites are equal.

```lean
lemma eq_of_links {b b' : Bond C} {x y : C.Site} (h : b.Links x y) (h' : b'.Links x y) :
    b = b'
```

**`Physlib.CondensedMatter.Crystal.Bond.links_vadd`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Bonds.lean#L79).

> Translating the endpoints gives another copy of the same bond.

```lean
lemma links_vadd (b : Bond C) (a : G) (x y : C.Site) :
    b.Links (a +ᵥ x) (a +ᵥ y) ↔ b.Links x y
```

**An instance with no name**, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Bonds.lean#L84).

> The source and target of a bond can be checked from their site addresses.

```lean
instance [DecidableEq G] [DecidableEq C.UnitCell] (b : Bond C) : DecidableRel b.Links
```

## Depends on

- [Crystals, cells and sites](basic.md)

## Sources

- [Physlib/CondensedMatter/Crystal/Bonds.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Bonds.lean)
