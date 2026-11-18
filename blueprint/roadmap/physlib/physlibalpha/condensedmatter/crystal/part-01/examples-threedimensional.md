---
declaration: module
origin: cited
lean: CondensedMatter.Crystal.orthorhombicVectors, CondensedMatter.Crystal.orthorhombicVectors_independent, CondensedMatter.Crystal.orthorhombicGeometry, CondensedMatter.Crystal.fcc, CondensedMatter.Crystal.fccVectors, CondensedMatter.Crystal.fccVectors_independent, CondensedMatter.Crystal.fccGeometry, CondensedMatter.Crystal.fccBonds
statement: formalized
proof: formalized
---

# Orthorhombic, cubic and hexagonal close-packed crystals

The module `PhyslibAlpha.CondensedMatter.Crystal.Examples.ThreeDimensional`, [PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean): 31 declarations (1 instance with no name), 30 with a docstring; 1 private, not shown.

> The orthorhombic lattice and the face-centred cubic, body-centred cubic and hexagonal
> close-packed crystals, with embeddings that allow different lengths along the coordinate axes.

## i. Overview

> A cubic lattice has one length, the lattice constant. Stretching the three axes independently
> gives the orthorhombic lattice with lengths `a`, `b`, `c`. The face-centred cubic (fcc) lattice
> has one site per primitive cell, with primitive vectors from a corner of the conventional cell to
> the centres of the three adjacent faces. Each site has twelve nearest neighbours. The body-centred
> cubic (bcc) lattice has one site per primitive cell, with primitive vectors from a corner to the
> centres of three conventional cells, and eight nearest neighbours. The hexagonal close-packed
> (hcp) crystal has two sites per primitive cell, on two interpenetrating hexagonal lattices, and
> twelve nearest neighbours for the ideal ratio `c / a = √(8 / 3)`.
>
> Each crystal is a graph, given by the bonds of its nearest neighbours, together with an embedding
> in three-dimensional space. The graph does not depend on the lengths. The embedding depends on
> `a`, `b` and `c` in the cubic cases, and on `a` and `c` for hcp, and any positive values give an
> embedding in which distinct sites have distinct positions. Only for the cubic values `a = b = c`
> and the ideal ratio do all bonds of the graph have equal length, so that the graph is the
> nearest-neighbour graph of the embedding.

## ii. Key results

> - `orthorhombicGeometry` : the hypercubic crystal with a separate length for each axis.
> - `fcc`, `bcc`, `hcp` : the crystals, with `fccGraph`, `bccGraph`, `hcpGraph` their bond graphs.
> - `fccGeometry`, `bccGeometry`, `hcpGeometry` : their embeddings with free lengths.
> - `fcc_neighbors_card`, `bcc_neighbors_card`, `hcp_neighbors_card` : the coordination numbers
>   `12`, `8` and `12`.
> - `fcc_bond_length`, `bcc_bond_length`, `hcp_bond_length` : bond lengths of the cubic and ideal
>   lattices.

## iv. References

> * N. Ashcroft & N. D. Mermin, Solid State Physics, Chapter 4.

## A. Orthorhombic lattices

**`CondensedMatter.Crystal.orthorhombicVectors`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L67).

> The primitive vectors of an orthorhombic lattice: `l i` along the `i`-th coordinate axis.

```lean
noncomputable def orthorhombicVectors {d : ℕ} (l : Fin d → ℝ) : Fin d → EuclideanSpace ℝ (Fin d)
```

**`CondensedMatter.Crystal.orthorhombicVectors_independent`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L71).

> The primitive vectors of an orthorhombic lattice are independent when no length vanishes.

```lean
lemma orthorhombicVectors_independent {d : ℕ} {l : Fin d → ℝ} (hl : ∀ i, 0 < l i) :
    LinearIndependent ℝ (orthorhombicVectors l)
```

**`CondensedMatter.Crystal.orthorhombicGeometry`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L80).

> The hypercubic crystal embedded with the length `l i` along the `i`-th axis.

```lean
noncomputable def orthorhombicGeometry {d : ℕ} (l : Fin d → ℝ) (hl : ∀ i, 0 < l i) :
    Geometry (hypercubic d) (EuclideanSpace ℝ (Fin d))
```

## B. Face-centred cubic lattice

**`CondensedMatter.Crystal.fcc`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L89).

> One site per primitive cell of the face-centred cubic lattice.

```lean
def fcc
```

**`CondensedMatter.Crystal.fccVectors`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L93).

> Primitive vectors from a corner to the centres of the three adjacent faces of a box with
> sides `a`, `b`, `c`.

```lean
noncomputable def fccVectors (a b c : ℝ) : Fin 3 → EuclideanSpace ℝ (Fin 3)
```

**`CondensedMatter.Crystal.fccVectors_independent`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L97).

> The primitive vectors of the face-centred lattice are independent for positive lengths.

```lean
lemma fccVectors_independent {a b c : ℝ} (ha : 0 < a) (hb : 0 < b) (hc : 0 < c) :
    LinearIndependent ℝ (fccVectors a b c)
```

**`CondensedMatter.Crystal.fccGeometry`**, a def, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L114).

> The face-centred cubic lattice embedded with a box of sides `a`, `b`, `c`.

```lean
noncomputable def fccGeometry (a b c : ℝ) (ha : 0 < a) (hb : 0 < b) (hc : 0 < c) :
    Geometry fcc (EuclideanSpace ℝ (Fin 3))
```

**`CondensedMatter.Crystal.fccBonds`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L121).

> The twelve nearest neighbours, up to sign: along the three primitive vectors and along their
> differences.

```lean
def fccBonds : List (Bond (Fin 3 → ℤ) Unit)
```

**`CondensedMatter.Crystal.fccGraph`**, a def, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L126).

> The twelve-neighbour face-centred cubic graph.

```lean
def fccGraph : PeriodicGraph fcc
```

## C. Body-centred cubic lattice

**`CondensedMatter.Crystal.bcc`**, a def, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L132).

> One site per primitive cell of the body-centred cubic lattice.

```lean
def bcc
```

**`CondensedMatter.Crystal.bccVectors`**, a def, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L136).

> Primitive vectors from a corner to the centres of three adjacent boxes of sides `a`, `b`,
> `c`.

```lean
noncomputable def bccVectors (a b c : ℝ) : Fin 3 → EuclideanSpace ℝ (Fin 3)
```

**`CondensedMatter.Crystal.bccVectors_independent`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L140).

> The primitive vectors of the body-centred lattice are independent for positive lengths.

```lean
lemma bccVectors_independent {a b c : ℝ} (ha : 0 < a) (hb : 0 < b) (hc : 0 < c) :
    LinearIndependent ℝ (bccVectors a b c)
```

**`CondensedMatter.Crystal.bccGeometry`**, a def, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L157).

> The body-centred cubic lattice embedded with a box of sides `a`, `b`, `c`.

```lean
noncomputable def bccGeometry (a b c : ℝ) (ha : 0 < a) (hb : 0 < b) (hc : 0 < c) :
    Geometry bcc (EuclideanSpace ℝ (Fin 3))
```

**`CondensedMatter.Crystal.bccBonds`**, a def, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L164).

> The eight nearest neighbours, up to sign: along the three primitive vectors and along their
> sum, the body diagonal of the box.

```lean
def bccBonds : List (Bond (Fin 3 → ℤ) Unit)
```

**`CondensedMatter.Crystal.bccGraph`**, a def, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L168).

> The eight-neighbour body-centred cubic graph.

```lean
def bccGraph : PeriodicGraph bcc
```

## D. Hexagonal close-packed crystal

**`CondensedMatter.Crystal.HcpLabel`**, an inductive, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L174).

> The two layers of an hcp crystal: the sites of the second layer are shifted within the plane
> and raised by half a period.

```lean
inductive HcpLabel
  /-- The site at the origin of the cell. -/
  | A
  /-- The site of the other layer. -/
  | B
  deriving DecidableEq, Repr
```

**An instance with no name**, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L181).

```lean
instance : Fintype HcpLabel
```

**`CondensedMatter.Crystal.hcp`**, a def, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L187).

> Two sites per primitive cell of the hexagonal close-packed crystal.

```lean
def hcp
```

**`CondensedMatter.Crystal.hcpVectors`**, a def, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L190).

> Primitive vectors of the hexagonal lattice with in-plane length `a` and period `c`.

```lean
noncomputable def hcpVectors (a c : ℝ) : Fin 3 → EuclideanSpace ℝ (Fin 3)
```

**`CondensedMatter.Crystal.hcpVectors_independent`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L194).

> The primitive vectors of the hexagonal lattice are independent for positive lengths.

```lean
lemma hcpVectors_independent {a c : ℝ} (ha : 0 < a) (hc : 0 < c) :
    LinearIndependent ℝ (hcpVectors a c)
```

**`CondensedMatter.Crystal.hcpBasis`**, a def, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L211).

> Positions of the two sites in the reference cell.

```lean
noncomputable def hcpBasis (a c : ℝ) : HcpLabel → EuclideanSpace ℝ (Fin 3)
```

**`CondensedMatter.Crystal.hcp_positions_injective`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L216).

> The two layers occupy distinct positions.

```lean
lemma hcp_positions_injective {a c : ℝ} (ha : 0 < a) (hc : 0 < c) : Function.Injective
    (fun x : CellSite (Fin 3 → ℤ) HcpLabel =>
      latticeMap (hcpVectors a c) x.cell + hcpBasis a c x.label)
```

**`CondensedMatter.Crystal.hcpGeometry`**, a def, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L240).

> The hexagonal close-packed crystal with in-plane length `a` and layer period `c`.

```lean
noncomputable def hcpGeometry (a c : ℝ) (ha : 0 < a) (hc : 0 < c) :
    Geometry hcp (EuclideanSpace ℝ (Fin 3))
```

**`CondensedMatter.Crystal.hcpBonds`**, a def, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L246).

> The nearest neighbours: six in the plane of each layer, and three in each adjacent layer.

```lean
def hcpBonds : List (Bond (Fin 3 → ℤ) HcpLabel)
```

**`CondensedMatter.Crystal.hcpGraph`**, a def, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L253).

> The twelve-neighbour hexagonal close-packed graph.

```lean
def hcpGraph : PeriodicGraph hcp
```

## E. Coordination numbers

**`CondensedMatter.Crystal.fcc_neighbors_card`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L258).

> Each site of the face-centred cubic lattice has twelve neighbours.

```lean
lemma fcc_neighbors_card (x : fcc.Site) : (fccGraph.neighbors x).card = 12
```

**`CondensedMatter.Crystal.bcc_neighbors_card`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L265).

> Each site of the body-centred cubic lattice has eight neighbours.

```lean
lemma bcc_neighbors_card (x : bcc.Site) : (bccGraph.neighbors x).card = 8
```

**`CondensedMatter.Crystal.hcp_neighbors_card`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L272).

> Both sites of the hexagonal close-packed crystal have twelve neighbours.

```lean
lemma hcp_neighbors_card (x : hcp.Site) : (hcpGraph.neighbors x).card = 12
```

## F. Bond lengths

**`CondensedMatter.Crystal.fcc_bond_length`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L287).

> In the face-centred cubic lattice with cube side `a`, every edge has length `a √2 / 2`.

```lean
lemma fcc_bond_length {a : ℝ} (ha : 0 < a) {x y : fcc.Site}
    (h : fccGraph.toSimpleGraph.Adj x y) :
    (fccGeometry a a a ha ha ha).distance x y = a * Real.sqrt 2 / 2
```

**`CondensedMatter.Crystal.bcc_bond_length`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L302).

> In the body-centred cubic lattice with cube side `a`, every edge has length `a √3 / 2`.

```lean
lemma bcc_bond_length {a : ℝ} (ha : 0 < a) {x y : bcc.Site}
    (h : bccGraph.toSimpleGraph.Adj x y) :
    (bccGeometry a a a ha ha ha).distance x y = a * Real.sqrt 3 / 2
```

**`CondensedMatter.Crystal.hcp_bond_length`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean#L318).

> In the ideal hexagonal close-packed crystal, with `c ^ 2 = 8 a ^ 2 / 3`, every edge has
> length `a`.

```lean
lemma hcp_bond_length {a c : ℝ} (ha : 0 < a) (hc : 0 < c) (hideal : c ^ 2 = 8 * a ^ 2 / 3)
    {x y : hcp.Site} (h : hcpGraph.toSimpleGraph.Adj x y) :
    (hcpGeometry a c ha hc).distance x y = a
```

## Depends on

- [Standard crystals](examples-basic.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/ThreeDimensional.lean)
