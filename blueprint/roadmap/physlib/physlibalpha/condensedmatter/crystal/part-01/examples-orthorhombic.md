---
declaration: module
origin: cited
lean: CondensedMatter.Crystal.orthorhombic, CondensedMatter.Crystal.orthorhombicBonds, CondensedMatter.Crystal.orthorhombicGraph, CondensedMatter.Crystal.baseCentredOrthorhombic, CondensedMatter.Crystal.baseCentredVectors, CondensedMatter.Crystal.baseCentredVectors_independent, CondensedMatter.Crystal.baseCentredOrthorhombicGeometry, CondensedMatter.Crystal.baseCentredOrthorhombicBonds
statement: formalized
proof: formalized
---

# Orthorhombic lattices

The module `PhyslibAlpha.CondensedMatter.Crystal.Examples.Orthorhombic`, [PhyslibAlpha/CondensedMatter/Crystal/Examples/Orthorhombic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Orthorhombic.lean): 19 declarations, 19 with a docstring.

> The primitive, base-centred, body-centred and face-centred orthorhombic lattices, with their
> embeddings and the bonds of their first neighbour shells.

## i. Overview

> An orthorhombic lattice has three different lengths `a`, `b`, `c` along three orthogonal axes.
> The bonds of the first shell alone do not see the three axes as different. For the primitive
> lattice the six bonds `±x, ±y, ±z` are those of the simple cubic lattice. A graph with
> orthorhombic symmetry needs the shells up to the first ones that tell each axis from the other
> two. With the lengths below these are:
>
> - primitive, `(a, b, c) = (3, 4, 7)`: the shells at `3, 4, 5, 6, 7`, twelve neighbours, namely
>   `±a x`, `±b y`, `±c z`, the in-plane diagonals `±a x ± b y` and `±2a x`;
> - base-centred, `(a, b, c) = (3, 6, 5)`: twelve neighbours, namely `(±a / 2, ±b / 2, 0)`,
>   `±a x`, `±c z` and `(±3a / 2, ±b / 2, 0)`;
> - body-centred, `(a, b, c) = (2, 7, 5)`: fourteen neighbours, namely the eight
>   `(±a / 2, ±b / 2, ±c / 2)`, `±a x`, `±2a x` and `±c z`;
> - face-centred, `(a, b, c) = (2, 4, 5)`: eighteen neighbours, namely the twelve face diagonals,
>   `±a x` and `(±3a / 2, ±b / 2, 0)`.
>
> As for the cubic lattices, the graph does not depend on the lengths and the embedding does.

## ii. Key results

> - `orthorhombic`, `baseCentredOrthorhombic`, `bodyCentredOrthorhombic`,
>   `faceCentredOrthorhombic` : the lattices, with one site per cell.
> - `baseCentredVectors` : the primitive vectors of the base-centred lattice.
> - `orthorhombic_neighbors_card`, `baseCentredOrthorhombic_neighbors_card`,
>   `bodyCentredOrthorhombic_neighbors_card`, `faceCentredOrthorhombic_neighbors_card` : the
>   coordination numbers `12`, `12`, `14` and `18`.

## iv. References

> * N. Ashcroft & N. D. Mermin, Solid State Physics, Chapter 7.

## A. Primitive orthorhombic lattice

**`CondensedMatter.Crystal.orthorhombic`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Orthorhombic.lean#L66).

> One site per primitive cell of the primitive orthorhombic lattice.

```lean
def orthorhombic
```

**`CondensedMatter.Crystal.orthorhombicBonds`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Orthorhombic.lean#L70).

> The bonds of the first shells for `(a, b, c) = (3, 4, 7)`, up to sign: the three axes, the
> two in-plane diagonals and twice the shortest axis.

```lean
def orthorhombicBonds : List (Bond (Fin 3 → ℤ) Unit)
```

**`CondensedMatter.Crystal.orthorhombicGraph`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Orthorhombic.lean#L75).

> The twelve-neighbour primitive orthorhombic graph.

```lean
def orthorhombicGraph : PeriodicGraph orthorhombic
```

## B. Base-centred orthorhombic lattice

**`CondensedMatter.Crystal.baseCentredOrthorhombic`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Orthorhombic.lean#L81).

> One site per primitive cell of the base-centred orthorhombic lattice.

```lean
def baseCentredOrthorhombic
```

**`CondensedMatter.Crystal.baseCentredVectors`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Orthorhombic.lean#L85).

> Primitive vectors from a corner to the centres of the two adjacent `a`–`b` faces of a box with
> sides `a`, `b`, `c` that share an edge along `x`, and along the third axis.

```lean
noncomputable def baseCentredVectors (a b c : ℝ) : Fin 3 → EuclideanSpace ℝ (Fin 3)
```

**`CondensedMatter.Crystal.baseCentredVectors_independent`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Orthorhombic.lean#L89).

> The primitive vectors of the base-centred lattice are independent for positive lengths.

```lean
lemma baseCentredVectors_independent {a b c : ℝ} (ha : 0 < a) (hb : 0 < b) (hc : 0 < c) :
    LinearIndependent ℝ (baseCentredVectors a b c)
```

**`CondensedMatter.Crystal.baseCentredOrthorhombicGeometry`**, a def, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Orthorhombic.lean#L105).

> The base-centred orthorhombic lattice embedded with a box of sides `a`, `b`, `c`.

```lean
noncomputable def baseCentredOrthorhombicGeometry (a b c : ℝ) (ha : 0 < a) (hb : 0 < b)
    (hc : 0 < c) : Geometry baseCentredOrthorhombic (EuclideanSpace ℝ (Fin 3))
```

**`CondensedMatter.Crystal.baseCentredOrthorhombicBonds`**, a def, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Orthorhombic.lean#L112).

> The bonds of the first shells for `(a, b, c) = (3, 6, 5)`, up to sign: the two primitive
> vectors in the plane, the third axis, their sum `a x` and the two vectors `(3a / 2, ±b / 2, 0)`.

```lean
def baseCentredOrthorhombicBonds : List (Bond (Fin 3 → ℤ) Unit)
```

**`CondensedMatter.Crystal.baseCentredOrthorhombicGraph`**, a def, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Orthorhombic.lean#L117).

> The twelve-neighbour base-centred orthorhombic graph.

```lean
def baseCentredOrthorhombicGraph : PeriodicGraph baseCentredOrthorhombic
```

## C. Body-centred and face-centred orthorhombic lattices

**`CondensedMatter.Crystal.bodyCentredOrthorhombic`**, a def, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Orthorhombic.lean#L124).

> One site per primitive cell of the body-centred orthorhombic lattice.

```lean
def bodyCentredOrthorhombic
```

**`CondensedMatter.Crystal.bodyCentredOrthorhombicBonds`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Orthorhombic.lean#L128).

> The bonds of the first shells for `(a, b, c) = (2, 7, 5)` in the basis `bccVectors a b c`,
> up to sign: the four body diagonals, `a x`, `2a x` and `c z`.

```lean
def bodyCentredOrthorhombicBonds : List (Bond (Fin 3 → ℤ) Unit)
```

**`CondensedMatter.Crystal.bodyCentredOrthorhombicGraph`**, a def, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Orthorhombic.lean#L133).

> The fourteen-neighbour body-centred orthorhombic graph, embedded by `bccGeometry a b c`.

```lean
def bodyCentredOrthorhombicGraph : PeriodicGraph bodyCentredOrthorhombic
```

**`CondensedMatter.Crystal.faceCentredOrthorhombic`**, a def, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Orthorhombic.lean#L138).

> One site per primitive cell of the face-centred orthorhombic lattice.

```lean
def faceCentredOrthorhombic
```

**`CondensedMatter.Crystal.faceCentredOrthorhombicBonds`**, a def, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Orthorhombic.lean#L142).

> The bonds of the first shells for `(a, b, c) = (2, 4, 5)` in the basis `fccVectors a b c`,
> up to sign: the six face diagonals, `a x` and the two vectors `(3a / 2, ±b / 2, 0)`.

```lean
def faceCentredOrthorhombicBonds : List (Bond (Fin 3 → ℤ) Unit)
```

**`CondensedMatter.Crystal.faceCentredOrthorhombicGraph`**, a def, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Orthorhombic.lean#L148).

> The eighteen-neighbour face-centred orthorhombic graph, embedded by `fccGeometry a b c`.

```lean
def faceCentredOrthorhombicGraph : PeriodicGraph faceCentredOrthorhombic
```

## D. Coordination numbers

**`CondensedMatter.Crystal.orthorhombic_neighbors_card`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Orthorhombic.lean#L154).

> Each site of the primitive orthorhombic lattice has twelve neighbours.

```lean
lemma orthorhombic_neighbors_card (x : orthorhombic.Site) :
    (orthorhombicGraph.neighbors x).card = 12
```

**`CondensedMatter.Crystal.baseCentredOrthorhombic_neighbors_card`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Orthorhombic.lean#L162).

> Each site of the base-centred orthorhombic lattice has twelve neighbours.

```lean
lemma baseCentredOrthorhombic_neighbors_card (x : baseCentredOrthorhombic.Site) :
    (baseCentredOrthorhombicGraph.neighbors x).card = 12
```

**`CondensedMatter.Crystal.bodyCentredOrthorhombic_neighbors_card`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Orthorhombic.lean#L170).

> Each site of the body-centred orthorhombic lattice has fourteen neighbours.

```lean
lemma bodyCentredOrthorhombic_neighbors_card (x : bodyCentredOrthorhombic.Site) :
    (bodyCentredOrthorhombicGraph.neighbors x).card = 14
```

**`CondensedMatter.Crystal.faceCentredOrthorhombic_neighbors_card`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Orthorhombic.lean#L178).

> Each site of the face-centred orthorhombic lattice has eighteen neighbours.

```lean
lemma faceCentredOrthorhombic_neighbors_card (x : faceCentredOrthorhombic.Site) :
    (faceCentredOrthorhombicGraph.neighbors x).card = 18
```

## Depends on

- [Crystal geometry](geometry.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/Examples/Orthorhombic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Orthorhombic.lean)
