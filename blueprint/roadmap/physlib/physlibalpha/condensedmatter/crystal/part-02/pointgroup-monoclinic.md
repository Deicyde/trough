---
declaration: module
origin: cited
lean: CondensedMatter.Crystal.monoclinicPointTriples, CondensedMatter.Crystal.monoclinic_admissible_iff, CondensedMatter.Crystal.baseCentredMonoclinicPointTriples, CondensedMatter.Crystal.baseCentredMonoclinic_admissible_iff, CondensedMatter.Crystal.triclinicPointTriples, CondensedMatter.Crystal.triclinic_admissible_iff, CondensedMatter.Crystal.monoclinic_card_pointGroup, CondensedMatter.Crystal.baseCentredMonoclinic_card_pointGroup
statement: formalized
proof: formalized
---

# The point groups of the monoclinic and triclinic lattices

The module `PhyslibAlpha.CondensedMatter.Crystal.PointGroup.Monoclinic`, [PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Monoclinic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Monoclinic.lean): 9 declarations, 9 with a docstring.

> The point groups of the two monoclinic lattices have order four, the holohedry `2/m`, and the
> point group of the triclinic lattice has order two, the holohedry `-1`.

## i. Overview

> The admissible triples are located by tests, as for the orthorhombic lattices. For the primitive
> monoclinic lattice the four point operations are the identity, the reflection `b ↦ -b` in the
> plane of `a` and `c`, the rotation by `π` about `b`, and the inversion. For the base-centred
> lattice the reflection exchanges the two primitive vectors in the `a`–`b` plane. The triclinic
> lattice keeps only the identity and the inversion, the symmetry of every lattice.

## ii. Key results

> - `monoclinic_admissible_iff`, `baseCentredMonoclinic_admissible_iff`,
>   `triclinic_admissible_iff` : the admissible triples.
> - `monoclinic_card_pointGroup`, `baseCentredMonoclinic_card_pointGroup` : order `4`.
> - `triclinic_card_pointGroup` : order `2`.

## iv. References

> * N. Ashcroft & N. D. Mermin, Solid State Physics, Chapter 7.

## A. The admissible triples

**`CondensedMatter.Crystal.monoclinicPointTriples`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Monoclinic.lean#L54).

> The four point operations of the primitive monoclinic lattice: the identity, the reflection
> `b ↦ -b`, the rotation by `π` about `b` and the inversion.

```lean
def monoclinicPointTriples : Finset (Fin 3 → Fin 3 → ℤ)
```

**`CondensedMatter.Crystal.monoclinic_admissible_iff`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Monoclinic.lean#L60).

> The point operations of the primitive monoclinic lattice are the four of
> `monoclinicPointTriples`.

```lean
lemma monoclinic_admissible_iff (v : Fin 3 → Fin 3 → ℤ) :
    Admissible (bondNeighbors monoclinicBonds) v ↔ v ∈ monoclinicPointTriples
```

**`CondensedMatter.Crystal.baseCentredMonoclinicPointTriples`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Monoclinic.lean#L67).

> The four point operations of the base-centred monoclinic lattice, in the basis
> `baseCentredMonoclinicVectors`.

```lean
def baseCentredMonoclinicPointTriples : Finset (Fin 3 → Fin 3 → ℤ)
```

**`CondensedMatter.Crystal.baseCentredMonoclinic_admissible_iff`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Monoclinic.lean#L73).

> The point operations of the base-centred monoclinic lattice are the four of
> `baseCentredMonoclinicPointTriples`.

```lean
lemma baseCentredMonoclinic_admissible_iff (v : Fin 3 → Fin 3 → ℤ) :
    Admissible (bondNeighbors baseCentredMonoclinicBonds) v ↔
      v ∈ baseCentredMonoclinicPointTriples
```

**`CondensedMatter.Crystal.triclinicPointTriples`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Monoclinic.lean#L80).

> The two point operations of the triclinic lattice: the identity and the inversion.

```lean
def triclinicPointTriples : Finset (Fin 3 → Fin 3 → ℤ)
```

**`CondensedMatter.Crystal.triclinic_admissible_iff`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Monoclinic.lean#L84).

> The point operations of the triclinic lattice are the identity and the inversion.

```lean
lemma triclinic_admissible_iff (v : Fin 3 → Fin 3 → ℤ) :
    Admissible (bondNeighbors triclinicBonds) v ↔ v ∈ triclinicPointTriples
```

## B. The orders

**`CondensedMatter.Crystal.monoclinic_card_pointGroup`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Monoclinic.lean#L93).

> **The point group of the primitive monoclinic lattice has order `4`.**

```lean
lemma monoclinic_card_pointGroup : Nat.card monoclinicGraph.pointGroup = 4
```

**`CondensedMatter.Crystal.baseCentredMonoclinic_card_pointGroup`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Monoclinic.lean#L98).

> **The point group of the base-centred monoclinic lattice has order `4`.**

```lean
lemma baseCentredMonoclinic_card_pointGroup :
    Nat.card baseCentredMonoclinicGraph.pointGroup = 4
```

**`CondensedMatter.Crystal.triclinic_card_pointGroup`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Monoclinic.lean#L104).

> **The point group of the triclinic lattice has order `2`.**

```lean
lemma triclinic_card_pointGroup : Nat.card triclinicGraph.pointGroup = 2
```

## Depends on

- [Monoclinic and triclinic lattices](../part-01/examples-monoclinic.md)
- [The point groups of the face-centred and body-centred cubic lattices](pointgroup-cubic.md)

## Proof depends on

- [The point groups of the orthorhombic lattices](pointgroup-orthorhombic.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Monoclinic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Monoclinic.lean)
