---
declaration: module
origin: cited
lean: CondensedMatter.Crystal.tetragonal, CondensedMatter.Crystal.tetragonalGeometry, CondensedMatter.Crystal.tetragonalBonds, CondensedMatter.Crystal.tetragonalGraph, CondensedMatter.Crystal.bodyCentredTetragonal, CondensedMatter.Crystal.bodyCentredTetragonalGeometry, CondensedMatter.Crystal.bodyCentredTetragonalBonds, CondensedMatter.Crystal.bodyCentredTetragonalGraph
statement: formalized
proof: formalized
---

# Tetragonal and hexagonal lattices

The module `PhyslibAlpha.CondensedMatter.Crystal.Examples.TetragonalHexagonal`, [PhyslibAlpha/CondensedMatter/Crystal/Examples/TetragonalHexagonal.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/TetragonalHexagonal.lean): 15 declarations, 15 with a docstring.

> The primitive and body-centred tetragonal lattices and the primitive hexagonal lattice, with
> their embeddings and the bonds of their first neighbour shells.

## i. Overview

> A tetragonal lattice is a cubic lattice stretched along one axis: the in-plane length `a` and the
> period `c` differ. The bonds of the first shell alone do not see this. For the primitive lattice
> the six bonds `±x, ±y, ±z` are those of the simple cubic lattice, and for the body-centred
> lattice with `c = a √2` the twelve nearest neighbours are those of the face-centred cubic lattice.
> A graph with tetragonal symmetry needs the shells up to the first one that tells `z` from `x`:
>
> - primitive tetragonal, `a < c < a √2`: the shells at `a`, `c` and `a √2`, ten neighbours;
> - body-centred tetragonal, `a √2 < c < a √6`: the shells at `a`, `√(a² / 2 + c² / 4)` and
>   `a √2`, sixteen neighbours.
>
> The primitive hexagonal lattice has six neighbours at `a` in the plane and two at `c` along the
> axis. For `c < a √3` these are the first shells, whatever the order of `a` and `c`.
>
> As for the cubic lattices, the graph does not depend on the lengths and the embedding does.

## ii. Key results

> - `tetragonal`, `bodyCentredTetragonal`, `hexagonal` : the lattices, with one site per cell.
> - `tetragonalGeometry`, `bodyCentredTetragonalGeometry`, `hexagonalGeometry` : their embeddings.
> - `tetragonalGraph`, `bodyCentredTetragonalGraph`, `hexagonalGraph` : their bond graphs.
> - `tetragonal_neighbors_card`, `bodyCentredTetragonal_neighbors_card`,
>   `hexagonal_neighbors_card` : the coordination numbers `10`, `16` and `8`.

## iv. References

> * N. Ashcroft & N. D. Mermin, Solid State Physics, Chapter 7.

## A. Primitive tetragonal lattice

**`CondensedMatter.Crystal.tetragonal`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/TetragonalHexagonal.lean#L63).

> One site per primitive cell of the primitive tetragonal lattice.

```lean
def tetragonal
```

**`CondensedMatter.Crystal.tetragonalGeometry`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/TetragonalHexagonal.lean#L66).

> The primitive tetragonal lattice embedded with in-plane length `a` and period `c`.

```lean
noncomputable def tetragonalGeometry (a c : ℝ) (ha : 0 < a) (hc : 0 < c) :
    Geometry tetragonal (EuclideanSpace ℝ (Fin 3))
```

**`CondensedMatter.Crystal.tetragonalBonds`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/TetragonalHexagonal.lean#L72).

> The bonds of the first three shells for `a < c < a √2`, up to sign: the two in-plane axes,
> the period, and the two in-plane diagonals.

```lean
def tetragonalBonds : List (Bond (Fin 3 → ℤ) Unit)
```

**`CondensedMatter.Crystal.tetragonalGraph`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/TetragonalHexagonal.lean#L77).

> The ten-neighbour primitive tetragonal graph.

```lean
def tetragonalGraph : PeriodicGraph tetragonal
```

## B. Body-centred tetragonal lattice

**`CondensedMatter.Crystal.bodyCentredTetragonal`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/TetragonalHexagonal.lean#L83).

> One site per primitive cell of the body-centred tetragonal lattice.

```lean
def bodyCentredTetragonal
```

**`CondensedMatter.Crystal.bodyCentredTetragonalGeometry`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/TetragonalHexagonal.lean#L87).

> The body-centred tetragonal lattice embedded with in-plane length `a` and period `c`, with
> the primitive vectors `bccVectors a a c`.

```lean
noncomputable def bodyCentredTetragonalGeometry (a c : ℝ) (ha : 0 < a) (hc : 0 < c) :
    Geometry bodyCentredTetragonal (EuclideanSpace ℝ (Fin 3))
```

**`CondensedMatter.Crystal.bodyCentredTetragonalBonds`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/TetragonalHexagonal.lean#L94).

> The bonds of the first three shells for `a √2 < c < a √6`, up to sign: the four body
> diagonals, the two in-plane axes and the two in-plane diagonals. In the basis `bccVectors a a c`
> the in-plane axes are `![0, 1, 1]` and `![1, 0, 1]`.

```lean
def bodyCentredTetragonalBonds : List (Bond (Fin 3 → ℤ) Unit)
```

**`CondensedMatter.Crystal.bodyCentredTetragonalGraph`**, a def, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/TetragonalHexagonal.lean#L99).

> The sixteen-neighbour body-centred tetragonal graph.

```lean
def bodyCentredTetragonalGraph : PeriodicGraph bodyCentredTetragonal
```

## C. Primitive hexagonal lattice

**`CondensedMatter.Crystal.hexagonal`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/TetragonalHexagonal.lean#L106).

> One site per primitive cell of the primitive hexagonal lattice.

```lean
def hexagonal
```

**`CondensedMatter.Crystal.hexagonalGeometry`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/TetragonalHexagonal.lean#L110).

> The primitive hexagonal lattice embedded with in-plane length `a` and period `c`, with the
> primitive vectors `hcpVectors a c`.

```lean
noncomputable def hexagonalGeometry (a c : ℝ) (ha : 0 < a) (hc : 0 < c) :
    Geometry hexagonal (EuclideanSpace ℝ (Fin 3))
```

**`CondensedMatter.Crystal.hexagonalBonds`**, a def, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/TetragonalHexagonal.lean#L117).

> The bonds of the first shells for `c < a √3`, up to sign: three in the plane, at `120°`
> from each other, and the period.

```lean
def hexagonalBonds : List (Bond (Fin 3 → ℤ) Unit)
```

**`CondensedMatter.Crystal.hexagonalGraph`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/TetragonalHexagonal.lean#L121).

> The eight-neighbour primitive hexagonal graph.

```lean
def hexagonalGraph : PeriodicGraph hexagonal
```

## D. Coordination numbers

**`CondensedMatter.Crystal.tetragonal_neighbors_card`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/TetragonalHexagonal.lean#L126).

> Each site of the primitive tetragonal lattice has ten neighbours.

```lean
lemma tetragonal_neighbors_card (x : tetragonal.Site) :
    (tetragonalGraph.neighbors x).card = 10
```

**`CondensedMatter.Crystal.bodyCentredTetragonal_neighbors_card`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/TetragonalHexagonal.lean#L134).

> Each site of the body-centred tetragonal lattice has sixteen neighbours.

```lean
lemma bodyCentredTetragonal_neighbors_card (x : bodyCentredTetragonal.Site) :
    (bodyCentredTetragonalGraph.neighbors x).card = 16
```

**`CondensedMatter.Crystal.hexagonal_neighbors_card`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/TetragonalHexagonal.lean#L142).

> Each site of the primitive hexagonal lattice has eight neighbours.

```lean
lemma hexagonal_neighbors_card (x : hexagonal.Site) :
    (hexagonalGraph.neighbors x).card = 8
```

## Depends on

- [Orthorhombic, cubic and hexagonal close-packed crystals](examples-threedimensional.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/Examples/TetragonalHexagonal.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/TetragonalHexagonal.lean)
