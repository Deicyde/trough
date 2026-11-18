---
declaration: module
origin: cited
lean: CondensedMatter.Crystal.rhombohedral, CondensedMatter.Crystal.rhombohedralVectors, CondensedMatter.Crystal.rhombohedralVectors_independent, CondensedMatter.Crystal.rhombohedralGeometry, CondensedMatter.Crystal.rhombohedralBonds, CondensedMatter.Crystal.rhombohedralGraph, CondensedMatter.Crystal.rhombohedral_neighbors_card
statement: formalized
proof: formalized
---

# The rhombohedral lattice

The module `PhyslibAlpha.CondensedMatter.Crystal.Examples.Rhombohedral`, [PhyslibAlpha/CondensedMatter/Crystal/Examples/Rhombohedral.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Rhombohedral.lean): 7 declarations, 7 with a docstring.

> The rhombohedral lattice, with its embedding and the bonds of its first two neighbour shells.

## i. Overview

> A rhombohedral lattice has three primitive vectors of the same length with the same angle `α`
> between any two of them. Up to a rotation they are `(p, q, q)`, `(q, p, q)` and `(q, q, p)`,
> with `cos α = (2 p q + q ²) / (p ² + 2 q ²)`. The six bonds `±aᵢ` of the first shell are those of
> the simple cubic lattice, so the first shell alone does not see the threefold axis. When
> `-1 / 4 < cos α < 0` the second shell is made of the six vectors `±(aᵢ + aⱼ)`, and the graph with
> both shells has twelve neighbours. This holds for instance for `(p, q) = (10, -1)`, with
> `cos α = -19 / 102`. The graph is defined by these twelve bonds and does not depend on `p`
> and `q`: that they form the two nearest shells is the statement above, not yet a lemma.

## ii. Key results

> - `rhombohedral` : the lattice, with one site per cell.
> - `rhombohedralVectors` : the primitive vectors `(p, q, q)`, `(q, p, q)`, `(q, q, p)`.
> - `rhombohedralGeometry` : the embedding, for `p ≠ q` and `p + 2 q ≠ 0`.
> - `rhombohedral_neighbors_card` : the coordination number `12`.

## iv. References

> * N. Ashcroft & N. D. Mermin, Solid State Physics, Chapter 7.

## A. The lattice and its embedding

**`CondensedMatter.Crystal.rhombohedral`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Rhombohedral.lean#L53).

> One site per primitive cell of the rhombohedral lattice.

```lean
def rhombohedral
```

**`CondensedMatter.Crystal.rhombohedralVectors`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Rhombohedral.lean#L56).

> The primitive vectors `(p, q, q)`, `(q, p, q)` and `(q, q, p)` of a rhombohedral lattice.

```lean
noncomputable def rhombohedralVectors (p q : ℝ) : Fin 3 → EuclideanSpace ℝ (Fin 3)
```

**`CondensedMatter.Crystal.rhombohedralVectors_independent`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Rhombohedral.lean#L60).

> The primitive vectors are independent when `p ≠ q` and `p + 2 q ≠ 0`.

```lean
lemma rhombohedralVectors_independent {p q : ℝ} (hpq : p ≠ q) (hp : p + 2 * q ≠ 0) :
    LinearIndependent ℝ (rhombohedralVectors p q)
```

**`CondensedMatter.Crystal.rhombohedralGeometry`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Rhombohedral.lean#L78).

> The rhombohedral lattice embedded with the primitive vectors `rhombohedralVectors p q`.

```lean
noncomputable def rhombohedralGeometry (p q : ℝ) (hpq : p ≠ q) (hp : p + 2 * q ≠ 0) :
    Geometry rhombohedral (EuclideanSpace ℝ (Fin 3))
```

## B. Bonds and coordination number

**`CondensedMatter.Crystal.rhombohedralBonds`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Rhombohedral.lean#L87).

> The bonds of the first two shells for `-1 / 4 < cos α < 0`, up to sign: the three primitive
> vectors and their pairwise sums.

```lean
def rhombohedralBonds : List (Bond (Fin 3 → ℤ) Unit)
```

**`CondensedMatter.Crystal.rhombohedralGraph`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Rhombohedral.lean#L92).

> The twelve-neighbour rhombohedral graph.

```lean
def rhombohedralGraph : PeriodicGraph rhombohedral
```

**`CondensedMatter.Crystal.rhombohedral_neighbors_card`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Rhombohedral.lean#L95).

> Each site of the rhombohedral lattice has twelve neighbours.

```lean
lemma rhombohedral_neighbors_card (x : rhombohedral.Site) :
    (rhombohedralGraph.neighbors x).card = 12
```

## Depends on

- [Crystal geometry](geometry.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/Examples/Rhombohedral.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Rhombohedral.lean)
