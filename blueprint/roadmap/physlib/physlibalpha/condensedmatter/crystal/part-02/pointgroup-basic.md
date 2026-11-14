---
declaration: module
origin: cited
lean: CondensedMatter.Crystal.PeriodicGraph.pointStabilizer, CondensedMatter.Crystal.PeriodicGraph.linearHom, CondensedMatter.Crystal.PeriodicGraph.linear_mem_pointStabilizer, CondensedMatter.Crystal.PeriodicGraph.pointHom, CondensedMatter.Crystal.PeriodicGraph.pointHom_surjective, CondensedMatter.Crystal.PeriodicGraph.ker_pointHom, CondensedMatter.Crystal.PeriodicGraph.pointGroupEquiv, CondensedMatter.Crystal.PeriodicGraph.pointLinearHom
statement: formalized
proof: formalized
---

# Point groups of Bravais lattices

The module `PhyslibAlpha.CondensedMatter.Crystal.PointGroup.Basic`, [PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Basic.lean): 8 declarations, 6 with a docstring.

> The point group of a crystal with one site per cell is the group of automorphisms of its
> translation lattice that preserve its bonds.

## i. Overview

> The point group of a crystal is the group of its bond-preserving symmetries modulo translations.
> A symmetry of any crystal acts on the lattice of cell translations by a lattice automorphism, its
> linear part, and this gives a homomorphism `pointLinearHom` from the point group to the lattice
> automorphisms. It is not injective in general: a symmetry may permute the sites within every cell
> and move none of the cells, and such a symmetry is not a translation.
>
> When there is one site per cell, a symmetry is determined, up to a translation, by its linear part.
> An automorphism of the lattice then extends to a bond-preserving symmetry exactly when it maps
> the set of bonded displacements to itself. In this case the point group is isomorphic to the
> group of lattice automorphisms preserving the bonded displacements (`pointGroupEquiv`). This group
> is finite when the graph is connected and has finitely many neighbours; it is the group of
> rotations and reflections of the lattice that leave it invariant. No geometry is involved: a
> square and a rectangular lattice with the same bonds have the same point group as graphs.

## ii. Key results

> - `PeriodicGraph.pointLinearHom` : the action of the point group of any crystal on the lattice.
> - `PeriodicGraph.pointStabilizer` : the lattice automorphisms preserving the bonded displacements.
> - `PeriodicGraph.pointGroupEquiv` : the point group is isomorphic to this group.

## iv. References

> * N. Ashcroft & N. D. Mermin, Solid State Physics, Chapter 7.

## A. Automorphisms preserving the bonds

**`CondensedMatter.Crystal.PeriodicGraph.pointStabilizer`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Basic.lean#L63).

> The lattice automorphisms that map bonded displacements to bonded displacements.

```lean
def pointStabilizer (g : PeriodicGraph (Crystal.ofUnitCell G Unit)) :
    Subgroup (Multiplicative (AddAut G))
```

**`CondensedMatter.Crystal.PeriodicGraph.linearHom`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Basic.lean#L80).

> The linear part of a cell symmetry as a homomorphism to the lattice automorphisms.

```lean
def linearHom (G F : Type*) [AddCommGroup G] : CellSymmetry G F →* Multiplicative (AddAut G)
```

**`CondensedMatter.Crystal.PeriodicGraph.linear_mem_pointStabilizer`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Basic.lean#L86).

> Bond-preserving symmetries have linear parts in the point stabilizer.

```lean
lemma linear_mem_pointStabilizer (g : PeriodicGraph (Crystal.ofUnitCell G Unit))
    {s : CellSymmetry G Unit} (hs : s ∈ g.symmetries) :
    Multiplicative.ofAdd s.linear ∈ g.pointStabilizer
```

## B. The point group of a crystal with one site per cell

**`CondensedMatter.Crystal.PeriodicGraph.pointHom`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Basic.lean#L98).

> The homomorphism from bond-preserving symmetries to the point stabilizer taking a symmetry to
> its action on the lattice.

```lean
def pointHom (g : PeriodicGraph (Crystal.ofUnitCell G Unit)) :
    g.symmetries →* g.pointStabilizer
```

**`CondensedMatter.Crystal.PeriodicGraph.pointHom_surjective`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Basic.lean#L103).

```lean
lemma pointHom_surjective (g : PeriodicGraph (Crystal.ofUnitCell G Unit)) :
    Function.Surjective (pointHom g)
```

**`CondensedMatter.Crystal.PeriodicGraph.ker_pointHom`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Basic.lean#L111).

```lean
lemma ker_pointHom (g : PeriodicGraph (Crystal.ofUnitCell G Unit)) :
    (pointHom g).ker = (CellSymmetry.translations G Unit).subgroupOf g.symmetries
```

**`CondensedMatter.Crystal.PeriodicGraph.pointGroupEquiv`**, a def, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Basic.lean#L132).

> **The point group of a crystal with one site per cell is the group of lattice automorphisms
> preserving the bonded displacements.**

```lean
noncomputable def pointGroupEquiv (g : PeriodicGraph (Crystal.ofUnitCell G Unit)) :
    g.pointGroup ≃* g.pointStabilizer
```

## C. The action on the lattice of any crystal

**`CondensedMatter.Crystal.PeriodicGraph.pointLinearHom`**, a def, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Basic.lean#L141).

> **The point group of any crystal acts on its translation lattice** through the linear parts of
> its symmetries.

```lean
noncomputable def pointLinearHom {F : Type*} [Finite F]
    (g : PeriodicGraph (Crystal.ofUnitCell G F)) : g.pointGroup →* Multiplicative (AddAut G)
```

## Depends on

- [Symmetries of a crystal graph](../part-01/symmetry.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Basic.lean)
