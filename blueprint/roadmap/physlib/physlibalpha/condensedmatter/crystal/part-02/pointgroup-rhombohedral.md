---
declaration: module
origin: cited
lean: CondensedMatter.Crystal.rhombohedralPointTriples, CondensedMatter.Crystal.rhombohedral_admissible_iff, CondensedMatter.Crystal.rhombohedral_card_pointGroup
statement: formalized
proof: formalized
---

# The point group of the rhombohedral lattice

The module `PhyslibAlpha.CondensedMatter.Crystal.PointGroup.Rhombohedral`, [PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Rhombohedral.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Rhombohedral.lean): 3 declarations, 3 with a docstring.

> The point group of the rhombohedral lattice has order twelve: it permutes the three primitive
> vectors and may reverse all of them, the holohedry `-3m`.

## i. Overview

> The admissible triples are located by tests, as for the orthorhombic lattices. A neighbour `a`
> goes to a neighbour, and the sums `a + b`, `a + c`, `b + c` and `2a + 2b + c` decide which
> triples of neighbours are images of the basis. Exactly twelve triples pass: the six permutations
> of the primitive vectors, and the same with all signs reversed. The permutations are the
> rotations about the threefold axis `a₁ + a₂ + a₃` and the reflections in the planes through it;
> the sign reversal is the inversion.

## ii. Key results

> - `rhombohedral_admissible_iff` : the twelve admissible triples.
> - `rhombohedral_card_pointGroup` : order `12`.

## iv. References

> * N. Ashcroft & N. D. Mermin, Solid State Physics, Chapter 7.

## A. The admissible triples

**`CondensedMatter.Crystal.rhombohedralPointTriples`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Rhombohedral.lean#L53).

> The images of the basis vectors under the twelve point operations of the rhombohedral
> lattice: the permutations of the primitive vectors, with or without the inversion.

```lean
def rhombohedralPointTriples : Finset (Fin 3 → Fin 3 → ℤ)
```

**`CondensedMatter.Crystal.rhombohedral_admissible_iff`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Rhombohedral.lean#L63).

> The point operations of the rhombohedral lattice are the twelve of
> `rhombohedralPointTriples`.

```lean
lemma rhombohedral_admissible_iff (v : Fin 3 → Fin 3 → ℤ) :
    Admissible (bondNeighbors rhombohedralBonds) v ↔ v ∈ rhombohedralPointTriples
```

## B. The order

**`CondensedMatter.Crystal.rhombohedral_card_pointGroup`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Rhombohedral.lean#L71).

> **The point group of the rhombohedral lattice has order `12`.**

```lean
lemma rhombohedral_card_pointGroup : Nat.card rhombohedralGraph.pointGroup = 12
```

## Depends on

- [The rhombohedral lattice](../part-01/examples-rhombohedral.md)
- [The point groups of the face-centred and body-centred cubic lattices](pointgroup-cubic.md)

## Proof depends on

- [The point groups of the orthorhombic lattices](pointgroup-orthorhombic.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Rhombohedral.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Rhombohedral.lean)
