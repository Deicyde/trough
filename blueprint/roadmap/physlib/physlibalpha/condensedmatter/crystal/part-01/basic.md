---
declaration: module
origin: cited
lean: CondensedMatter.Crystal, CondensedMatter.Crystal.CellSite, CondensedMatter.Crystal.ofUnitCell
statement: formalized
proof: formalized
---

# Crystals, cells and sites

The module `PhyslibAlpha.CondensedMatter.Crystal.Basic`, [PhyslibAlpha/CondensedMatter/Crystal/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Basic.lean): 6 declarations (3 instances with no name), 6 with a docstring.

## i. Overview

> A crystal is a perfect periodic arrangement obtained by repeating a unit cell. The unit
> cell contains finitely many sites, which may carry atoms, spins or orbitals. A cell is one
> translated copy of the unit cell. A label identifies which site within that copy: for
> example, A or B in a cell containing two sites. A cell index and a site label together
> identify one site in the full crystal.
>
> The translation group `G` determines how the cells repeat. The usual choice is `ℤᵈ`, giving
> an infinite discrete crystal. Choosing `(ℤ/mℤ)ᵈ` with positive `m` gives a finite periodic
> array with opposite boundaries identified. The definition also permits `ℝᵈ`, describing
> continuously translated arrangements.
>
> `Crystal.ofUnitCell G F` constructs the crystal from its translation group `G` and the
> finite set `F` of site labels in the unit cell. Taking `F = Fin 2` gives two sites per cell,
> labelled `0` and `1`. With `G = Fin 2 → ℤ`, the cells form an infinite two-dimensional
> array. With `G = Fin 2 → ZMod 4`, there are four cells in each direction with periodic
> identification.
>
> For a crystal `C` built this way, `C.Site` is the type of its sites. The site `⟨n, i⟩` has
> cell index `n` and label `i`. Translation by `a`, written `a +ᵥ x`, changes its cell index
> to `a + n` and preserves its label. These indices specify site addresses; a geometric
> realization supplies physical positions.

## ii. Key results

> - `Crystal` : a perfectly repeating arrangement of sites under a translation group.
> - `Crystal.ofUnitCell` : the crystal obtained by repeating a unit cell with finitely many labels.
> - `CellSite` : the address of a site, a cell index together with a label.

## iv. References

> * N. Ashcroft & N. D. Mermin, Solid State Physics, Chapter 4.

**`CondensedMatter.Crystal`**, a structure, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Basic.lean#L65).

> A perfectly repeating arrangement of sites under the translation group `G`.
> Every site belongs to one of finitely many families of translated copies.

```lean
structure Crystal (G : Type u) [AddGroup G] where
  /-- The sites of the crystal. -/
  Site : Type v
  /-- Translation by `a : G` takes each site to its corresponding translated copy. -/
  [translations : AddAction G Site]
  /-- Different translations of a site give different sites. -/
  [free : IsCancelVAdd G Site]
  /-- A unit cell requires only finitely many site labels. -/
  [finiteSiteOrbits : Finite (AddAction.orbitRel.Quotient G Site)]
```

## A. Constructing a crystal from a unit cell

> Choose site labels `F` for a reference cell. Repeating this cell under translations by `G`
> gives one site for each cell index `n : G` and label `i : F`.

**`CondensedMatter.Crystal.CellSite`**, a structure, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Basic.lean#L86).

> The address `⟨n, i⟩` of site `i` in the cell indexed by `n`.

```lean
@[ext] structure CellSite (G : Type u) (F : Type v) where
  /-- Translation from the reference cell to this cell. -/
  cell : G
  /-- Which site of the unit cell is being copied. -/
  label : F
  deriving DecidableEq, Fintype
```

**An instance with no name**, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Basic.lean#L94).

> Translate a site by changing its cell index and preserving its label.

```lean
instance {G F : Type*} [AddGroup G] : AddAction G (CellSite G F)
```

**An instance with no name**, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Basic.lean#L102).

> Different cell translations give different copies of a site.

```lean
instance {G F : Type*} [AddGroup G] : IsCancelVAdd G (CellSite G F)
```

**`CondensedMatter.Crystal.ofUnitCell`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Basic.lean#L110).

> Construct a crystal by repeating a unit cell containing one site for each label in `F`.
> The group `G` indexes translated cells. A site of the resulting crystal has address
> `⟨n, i⟩`, where `n : G` specifies its cell and `i : F` identifies the site within that cell.

```lean
def ofUnitCell (G : Type u) (F : Type v) [AddGroup G] [Finite F] : Crystal G
```

**An instance with no name**, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Basic.lean#L129).

> A finite translation group gives a finite crystal.

```lean
instance {G : Type*} [AddGroup G] [Finite G] (C : Crystal G) : Finite C.Site
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Basic.lean)
