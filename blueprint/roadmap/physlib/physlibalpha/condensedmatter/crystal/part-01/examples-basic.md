---
declaration: module
origin: cited
lean: CondensedMatter.Crystal.hypercubic, CondensedMatter.Crystal.hypercubicDisplacement, CondensedMatter.Crystal.hypercubicGeometry, CondensedMatter.Crystal.hypercubicBonds, CondensedMatter.Crystal.hypercubicGraph, CondensedMatter.Crystal.chain, CondensedMatter.Crystal.chainGeometry, CondensedMatter.Crystal.chainGraph
statement: formalized
proof: formalized
---

# Standard crystals

The module `PhyslibAlpha.CondensedMatter.Crystal.Examples.Basic`, [PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean): 50 declarations (2 instances with no name), 48 with a docstring.

## i. Overview

> These examples specify the same three ingredients: a repeated unit cell, its physical
> positions and its bonds. The crystal, geometry and graph remain separately accessible.
>
> The hypercubic lattice has one site per cell in any dimension. The chain and square
> lattice are its one- and two-dimensional cases. The triangular lattice has six neighbors
> per site. The honeycomb lattice has two sites per cell, each with three neighbors.
> Their Euclidean geometries use unit nearest-neighbor spacing.
>
> The finite periodic chain places equally spaced sites on a circle of circumference one.
> Its bonds connect consecutive cells modulo the period.

## ii. Key results

> - `hypercubic`, `square`, `chain` : one site per cell.
> - `triangular`, `honeycomb`, `diamond` : standard lattices with their geometries and bond graphs.
> - `periodicChain` : a finite periodic chain.
> - `honeycomb_neighbors_card`, `diamond_neighbors_card` : coordination numbers.

## iv. References

> * N. Ashcroft & N. D. Mermin, Solid State Physics, Chapter 4.

## A. Hypercubic lattices

**`CondensedMatter.Crystal.hypercubic`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L58).

> One site per integer-indexed cell in `d` dimensions.

```lean
def hypercubic (d : ℕ)
```

**`CondensedMatter.Crystal.hypercubicDisplacement`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L61).

> Unit orthogonal cell displacements in Cartesian coordinates.

```lean
noncomputable def hypercubicDisplacement (d : ℕ) :
    (Fin d → ℤ) →+ EuclideanSpace ℝ (Fin d)
```

**`CondensedMatter.Crystal.hypercubicGeometry`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L66).

> The hypercubic lattice embedded with unit spacing along each Cartesian axis.

```lean
noncomputable def hypercubicGeometry (d : ℕ) : Geometry (hypercubic d) (EuclideanSpace ℝ (Fin d))
```

**`CondensedMatter.Crystal.hypercubicBonds`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L71).

> One positive-axis bond for each direction generates all hypercubic connections.

```lean
def hypercubicBonds (d : ℕ) : List (Bond (Fin d → ℤ) Unit)
```

**`CondensedMatter.Crystal.hypercubicGraph`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L75).

> The graph connecting each site to its neighboring cells along the coordinate axes.

```lean
def hypercubicGraph (d : ℕ) : PeriodicGraph (hypercubic d)
```

**`CondensedMatter.Crystal.chain`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L80).

> The infinite chain with one site per cell.

```lean
def chain
```

**`CondensedMatter.Crystal.chainGeometry`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L83).

> Unit-spaced positions of the infinite chain.

```lean
noncomputable def chainGeometry
```

**`CondensedMatter.Crystal.chainGraph`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L86).

> Consecutive sites of the infinite chain are connected.

```lean
def chainGraph
```

**`CondensedMatter.Crystal.square`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L90).

> The square lattice with one site per cell.

```lean
def square
```

**`CondensedMatter.Crystal.squareGeometry`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L93).

> Cartesian positions of the unit-spaced square lattice.

```lean
noncomputable def squareGeometry
```

**`CondensedMatter.Crystal.squareGraph`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L96).

> The four-neighbor square-lattice graph.

```lean
def squareGraph
```

## B. Triangular lattice

**`CondensedMatter.Crystal.triangular`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L102).

> One site per cell of the triangular lattice.

```lean
def triangular
```

**`CondensedMatter.Crystal.triangularVectors`**, a def, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L105).

> Unit primitive vectors meeting at an angle of sixty degrees.

```lean
noncomputable def triangularVectors : Fin 2 → EuclideanSpace ℝ (Fin 2)
```

**`CondensedMatter.Crystal.triangularVectors_independent`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L109).

> The two primitive translations of the triangular lattice are independent.

```lean
lemma triangularVectors_independent : LinearIndependent ℝ triangularVectors
```

**`CondensedMatter.Crystal.triangularGeometry`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L118).

> The triangular lattice embedded with unit bond lengths.

```lean
noncomputable def triangularGeometry : Geometry triangular (EuclideanSpace ℝ (Fin 2))
```

**`CondensedMatter.Crystal.triangularBonds`**, a def, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L123).

> Three cell displacements generate the six triangular-lattice neighbors.

```lean
def triangularBonds : List (Bond (Fin 2 → ℤ) Unit)
```

**`CondensedMatter.Crystal.triangularGraph`**, a def, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L127).

> The six-neighbor triangular-lattice graph.

```lean
def triangularGraph : PeriodicGraph triangular
```

## C. Honeycomb lattice

**`CondensedMatter.Crystal.HoneycombLabel`**, an inductive, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L132).

> The two sites in a honeycomb unit cell.

```lean
inductive HoneycombLabel
  /-- The site at the reference-cell origin. -/
  | A
  /-- The site one unit above the reference-cell origin. -/
  | B
  deriving DecidableEq, Repr
```

**An instance with no name**, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L139).

```lean
instance : Fintype HoneycombLabel
```

**`CondensedMatter.Crystal.honeycomb`**, a def, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L145).

> A honeycomb crystal has two sites per integer-indexed cell.

```lean
def honeycomb
```

**`CondensedMatter.Crystal.honeycombVectors`**, a def, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L148).

> Primitive cell translations for a honeycomb lattice with unit bond lengths.

```lean
noncomputable def honeycombVectors : Fin 2 → EuclideanSpace ℝ (Fin 2)
```

**`CondensedMatter.Crystal.honeycombVectors_independent`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L152).

> The primitive cell translations of the honeycomb lattice are independent.

```lean
lemma honeycombVectors_independent : LinearIndependent ℝ honeycombVectors
```

**`CondensedMatter.Crystal.honeycombBasis`**, a def, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L164).

> Physical positions of A and B within the reference honeycomb cell.

```lean
noncomputable def honeycombBasis : HoneycombLabel → EuclideanSpace ℝ (Fin 2)
```

**`CondensedMatter.Crystal.honeycomb_positions_injective`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L169).

> The honeycomb reference positions and their translated copies are all distinct.

```lean
lemma honeycomb_positions_injective : Function.Injective
    (fun x : CellSite (Fin 2 → ℤ) HoneycombLabel =>
      latticeMap honeycombVectors x.cell + honeycombBasis x.label)
```

**`CondensedMatter.Crystal.honeycombGeometry`**, a def, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L195).

> The honeycomb crystal embedded with distinct A and B sites and unit bond spacing.

```lean
noncomputable def honeycombGeometry : Geometry honeycomb (EuclideanSpace ℝ (Fin 2))
```

**`CondensedMatter.Crystal.honeycombBonds`**, a def, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L200).

> Each A site connects to B in its own cell and in two adjacent cells.

```lean
def honeycombBonds : List (Bond (Fin 2 → ℤ) HoneycombLabel)
```

**`CondensedMatter.Crystal.honeycombGraph`**, a def, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L204).

> The three-neighbor honeycomb graph.

```lean
def honeycombGraph : PeriodicGraph honeycomb
```

## D. Diamond lattice

**`CondensedMatter.Crystal.DiamondLabel`**, an inductive, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L209).

> The two atoms in a diamond unit cell.

```lean
inductive DiamondLabel
  /-- The atom at the reference-cell origin. -/
  | A
  /-- The atom displaced by a quarter of the body diagonal of the cubic cell. -/
  | B
  deriving DecidableEq, Repr
```

**An instance with no name**, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L216).

```lean
instance : Fintype DiamondLabel
```

**`CondensedMatter.Crystal.diamond`**, a def, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L222).

> A diamond crystal has two atoms per integer-indexed cell of its face-centered cubic lattice.

```lean
def diamond
```

**`CondensedMatter.Crystal.diamondVectors`**, a def, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L226).

> Primitive translations of the face-centered cubic lattice, in units of the cubic lattice
> constant.

```lean
noncomputable def diamondVectors : Fin 3 → EuclideanSpace ℝ (Fin 3)
```

**`CondensedMatter.Crystal.diamondVectors_independent`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L230).

> The primitive translations of the face-centered cubic lattice are independent.

```lean
lemma diamondVectors_independent : LinearIndependent ℝ diamondVectors
```

**`CondensedMatter.Crystal.diamondBasis`**, a def, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L240).

> Physical positions of the two atoms within the reference diamond cell.

```lean
noncomputable def diamondBasis : DiamondLabel → EuclideanSpace ℝ (Fin 3)
```

**`CondensedMatter.Crystal.diamond_positions_injective`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L245).

> The positions of the two diamond sublattices are distinct, and so are all translated copies.

```lean
lemma diamond_positions_injective : Function.Injective
    (fun x : CellSite (Fin 3 → ℤ) DiamondLabel =>
      latticeMap diamondVectors x.cell + diamondBasis x.label)
```

**`CondensedMatter.Crystal.diamondGeometry`**, a def, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L264).

> The diamond crystal embedded with distinct atoms in three-dimensional space.

```lean
noncomputable def diamondGeometry : Geometry diamond (EuclideanSpace ℝ (Fin 3))
```

**`CondensedMatter.Crystal.diamondBonds`**, a def, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L269).

> Each A atom connects to the B atom of its own cell and of the three cells reached by
> subtracting one primitive translation: its four tetrahedral neighbors.

```lean
def diamondBonds : List (Bond (Fin 3 → ℤ) DiamondLabel)
```

**`CondensedMatter.Crystal.diamondGraph`**, a def, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L273).

> The four-neighbor tetrahedral diamond graph.

```lean
def diamondGraph : PeriodicGraph diamond
```

## E. Finite periodic chain

**`CondensedMatter.Crystal.periodicChain`**, a def, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L279).

> A finite chain whose cell indices are taken modulo `m`.

```lean
def periodicChain (m : ℕ)
```

**`CondensedMatter.Crystal.periodicChainGeometry`**, a def, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L282).

> Equally spaced sites on a circle of circumference one.

```lean
noncomputable def periodicChainGeometry (m : ℕ) [NeZero m] :
    Geometry (periodicChain m) UnitAddCircle
```

**`CondensedMatter.Crystal.periodicChainBonds`**, a def, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L287).

> Connect consecutive cells around the periodic chain.

```lean
def periodicChainBonds (m : ℕ) : List (Bond (ZMod m) Unit)
```

**`CondensedMatter.Crystal.periodicChainGraph`**, a def, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L290).

> The undirected graph of consecutive cells modulo `m`.

```lean
def periodicChainGraph (m : ℕ) : PeriodicGraph (periodicChain m)
```

## F. Coordination numbers

**`CondensedMatter.Crystal.chain_neighbors_card`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L296).

> Each site of the infinite chain has two neighbors.

```lean
lemma chain_neighbors_card (x : chain.Site) : (chainGraph.neighbors x).card = 2
```

**`CondensedMatter.Crystal.square_neighbors_card`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L303).

> Each site of the square lattice has four neighbors.

```lean
lemma square_neighbors_card (x : square.Site) : (squareGraph.neighbors x).card = 4
```

**`CondensedMatter.Crystal.triangular_neighbors_card`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L310).

> Each site of the triangular lattice has six neighbors.

```lean
lemma triangular_neighbors_card (x : triangular.Site) : (triangularGraph.neighbors x).card = 6
```

**`CondensedMatter.Crystal.honeycomb_neighbors_card`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L317).

> Both honeycomb site labels have three neighbors in every cell.

```lean
lemma honeycomb_neighbors_card (x : honeycomb.Site) : (honeycombGraph.neighbors x).card = 3
```

**`CondensedMatter.Crystal.diamond_neighbors_card`**, a lemma, [line 323](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L323).

> Both diamond site labels have four neighbors in every cell.

```lean
lemma diamond_neighbors_card (x : diamond.Site) : (diamondGraph.neighbors x).card = 4
```

## G. Bond lengths

**`CondensedMatter.Crystal.hypercubic_bond_length`**, a lemma, [line 331](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L331).

> Every hypercubic graph edge has unit physical length, in any dimension.

```lean
lemma hypercubic_bond_length (d : ℕ) {x y : (hypercubic d).Site}
    (h : (hypercubicGraph d).toSimpleGraph.Adj x y) :
    (hypercubicGeometry d).distance x y = 1
```

**`CondensedMatter.Crystal.square_bond_length`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L342).

> All square-lattice graph edges have unit physical length.

```lean
lemma square_bond_length {x y : square.Site} (h : squareGraph.toSimpleGraph.Adj x y) :
    squareGeometry.distance x y = 1
```

**`CondensedMatter.Crystal.triangular_bond_length`**, a lemma, [line 346](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L346).

> All triangular-lattice graph edges have unit physical length.

```lean
lemma triangular_bond_length {x y : triangular.Site}
    (h : triangularGraph.toSimpleGraph.Adj x y) : triangularGeometry.distance x y = 1
```

**`CondensedMatter.Crystal.honeycomb_bond_length`**, a lemma, [line 357](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean#L357).

> All honeycomb graph edges have unit physical length.

```lean
lemma honeycomb_bond_length {x y : honeycomb.Site}
    (h : honeycombGraph.toSimpleGraph.Adj x y) : honeycombGeometry.distance x y = 1
```

## Depends on

- [Crystal geometry](geometry.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Basic.lean)
