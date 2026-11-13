---
declaration: module
origin: cited
lean: Physlib.CondensedMatter.Crystal, Physlib.CondensedMatter.Crystal.ofUnitCell, Physlib.CondensedMatter.Crystal.Site, Physlib.CondensedMatter.Crystal.Site.ref, Physlib.CondensedMatter.Crystal.Site.cell_ref, Physlib.CondensedMatter.Crystal.Site.label_ref, Physlib.CondensedMatter.Crystal.siteEquiv, Physlib.CondensedMatter.Crystal.Site.vadd_def
statement: formalized
proof: formalized
---

# Crystals, cells and sites (Physlib)

The module `Physlib.CondensedMatter.Crystal.Basic`, [Physlib/CondensedMatter/Crystal/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Basic.lean): 18 declarations (6 instances with no name), 18 with a docstring.

> A crystal is a finite unit cell repeated periodically.

## i. Overview

> The goal is to construct crystals such as the square, hexagonal, fcc, bcc and hcp lattices. The
> standard starting point is a unit cell repeated by translations; see the reference below. We
> start combinatorially, with a unit cell that repeats many times over. This periodicity is modeled
> by a finitely generated abelian group `G`, written additively, with `ℤᵈ` as the prototypical
> example. Each unit cell consists of finitely many things, such as atoms, spins or orbitals, which
> are labeled by a type `F`. Repeating the cell gives one site `⟨n, i⟩` for every cell `n : G` and
> label `i : F`. Translation acts only on the cell:
>
> `a +ᵥ ⟨n, i⟩ = ⟨a + n, i⟩`.
>
> A crystal with one site per cell has a single label, while the honeycomb and hcp lattices have two.
> A species assignment gives each label a species, for example a chemical element.
>
> For `ℤᵈ` the sites form an infinite array, and for `(ℤ/mℤ)ᵈ` a finite array with periodic
> boundary conditions. Coordinates in space, and with them distances and angles, are not part of this
> description and is added in other files.

## ii. Key results

> - `Crystal` : a finitely generated abelian translation group with a finite, nonempty unit cell.
> - `Crystal.ofUnitCell` : the crystal obtained by repeating a labeled unit cell.
> - `Crystal.Site` : a site given by its cell and unit-cell label.
> - `Crystal.Site.ref` : the site with a given label in the reference cell.
> - `Crystal.Species` : a species assignment, one species for each unit-cell label.
> - `Crystal.Site.mem_orbit_iff_label_eq` : the translates of a site are exactly the sites with the
>   same label.

## iv. References

> * F. Göhmann, *Introduction to Solid State Physics*, lecture L3, Section 3.1, for the standard
>   description of a crystal as translated copies of a unit cell. [ref: goehmann\_solid\_state\_2021]

## A. The unit cell

**`Physlib.CondensedMatter.Crystal`**, a structure, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Basic.lean#L68).

> A crystal with finitely generated abelian translation group `G` and a finite, nonempty unit
> cell. The sites are one copy of each unit-cell label in every translated cell.

```lean
structure Crystal (G : Type*) [AddCommGroup G] [AddGroup.FG G] where
  /-- The labels of the things in one unit cell, such as atoms, spins or orbitals. -/
  UnitCell : Type*
  /-- The unit cell has finitely many labels. -/
  [finiteUnitCell : Finite UnitCell]
  /-- The unit cell has at least one label. -/
  [nonemptyUnitCell : Nonempty UnitCell]
```

## B. Constructing a crystal from a unit cell

**`Physlib.CondensedMatter.Crystal.ofUnitCell`**, an abbrev, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Basic.lean#L84).

> Construct a crystal by repeating a unit cell with labels `F`.
> The group `G` indexes translated cells; `⟨n, i⟩` is the site with label `i` in cell `n`.

```lean
abbrev ofUnitCell (G : Type*) (F : Type*) [AddCommGroup G] [AddGroup.FG G]
    [Finite F] [Nonempty F] : Crystal G
```

## C. Sites and their finiteness

**`Physlib.CondensedMatter.Crystal.Site`**, a structure, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Basic.lean#L93).

> A site of `C`, with label `i` in cell `n`.

```lean
structure Site (C : Crystal G) where
  /-- The cell containing this site. -/
  cell : G
  /-- The label of this site within its cell. -/
  label : C.UnitCell
```

**`Physlib.CondensedMatter.Crystal.Site.ref`**, an abbrev, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Basic.lean#L100).

> The site with label `i` in the reference cell, the cell `0`.

```lean
abbrev Site.ref {C : Crystal G} (i : C.UnitCell) : C.Site
```

**`Physlib.CondensedMatter.Crystal.Site.cell_ref`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Basic.lean#L103).

> The reference site lies in the cell `0`.

```lean
lemma Site.cell_ref {C : Crystal G} (i : C.UnitCell) : (Site.ref i).cell = 0
```

**`Physlib.CondensedMatter.Crystal.Site.label_ref`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Basic.lean#L106).

> The reference site has the label `i`.

```lean
lemma Site.label_ref {C : Crystal G} (i : C.UnitCell) : (Site.ref i).label = i
```

**`Physlib.CondensedMatter.Crystal.siteEquiv`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Basic.lean#L109).

> A site is a pair of its unit-cell label and its cell.

```lean
def siteEquiv (C : Crystal G) : C.Site ≃ C.UnitCell × G
```

**An instance with no name**, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Basic.lean#L116).

> Sites can be compared when cells and unit-cell labels can be compared.

```lean
instance (C : Crystal G) [DecidableEq G] [DecidableEq C.UnitCell] : DecidableEq C.Site
```

**An instance with no name**, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Basic.lean#L120).

> A finite set of cells and a finite unit cell give a finite set of sites.

```lean
instance (C : Crystal G) [Fintype G] [Fintype C.UnitCell] : Fintype C.Site
```

**An instance with no name**, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Basic.lean#L124).

> A finite translation group, as for periodic boundary conditions, gives a finite crystal.

```lean
instance (C : Crystal G) [Finite G] : Finite C.Site
```

**An instance with no name**, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Basic.lean#L128).

> Every crystal has a site in its reference cell.

```lean
instance (C : Crystal G) : Nonempty C.Site
```

## D. Translation symmetry

**An instance with no name**, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Basic.lean#L135).

> Translate a site to another cell, preserving its unit-cell label.

```lean
instance (C : Crystal G) : AddAction G C.Site
```

**`Physlib.CondensedMatter.Crystal.Site.vadd_def`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Basic.lean#L141).

> Translation changes a site's cell and preserves its label.

```lean
lemma Site.vadd_def {C : Crystal G} (a : G) (x : C.Site) :
    a +ᵥ x = ⟨a + x.cell, x.label⟩
```

**`Physlib.CondensedMatter.Crystal.Site.cell_vadd`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Basic.lean#L145).

> The cell of a translated site is the translated cell.

```lean
lemma Site.cell_vadd {C : Crystal G} (a : G) (x : C.Site) :
    (a +ᵥ x).cell = a + x.cell
```

**`Physlib.CondensedMatter.Crystal.Site.label_vadd`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Basic.lean#L149).

> Translation preserves the label of a site.

```lean
lemma Site.label_vadd {C : Crystal G} (a : G) (x : C.Site) :
    (a +ᵥ x).label = x.label
```

**An instance with no name**, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Basic.lean#L154).

> Translation acts freely: translations are injective on sites, and different translations move
> a site to different sites.

```lean
instance (C : Crystal G) : IsCancelVAdd G C.Site
```

**`Physlib.CondensedMatter.Crystal.Site.mem_orbit_iff_label_eq`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Basic.lean#L159).

> The translates of a site are exactly the sites with the same label.

```lean
lemma Site.mem_orbit_iff_label_eq {C : Crystal G} (x y : C.Site) :
    y ∈ AddAction.orbit G x ↔ x.label = y.label
```

## E. Species

**`Physlib.CondensedMatter.Crystal.Species`**, an abbrev, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Basic.lean#L172).

> A species assignment gives each label of the unit cell a species in `Q`, for example a chemical
> element. The same assignment holds in every cell.

```lean
abbrev Species (C : Crystal G) (Q : Type*)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/CondensedMatter/Crystal/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Basic.lean)
