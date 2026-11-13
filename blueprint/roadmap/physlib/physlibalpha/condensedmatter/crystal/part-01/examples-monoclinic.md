---
declaration: module
origin: cited
lean: CondensedMatter.Crystal.monoclinic, CondensedMatter.Crystal.monoclinicVectors, CondensedMatter.Crystal.monoclinicVectors_independent, CondensedMatter.Crystal.monoclinicBonds, CondensedMatter.Crystal.monoclinicGraph, CondensedMatter.Crystal.baseCentredMonoclinic, CondensedMatter.Crystal.baseCentredMonoclinicVectors, CondensedMatter.Crystal.baseCentredMonoclinicVectors_independent
statement: formalized
proof: formalized
---

# Monoclinic and triclinic lattices

The module `PhyslibAlpha.CondensedMatter.Crystal.Examples.Monoclinic`, [PhyslibAlpha/CondensedMatter/Crystal/Examples/Monoclinic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Monoclinic.lean): 18 declarations, 18 with a docstring.

> The primitive and base-centred monoclinic lattices and the triclinic lattice, with their
> embeddings and the bonds of their first neighbour shells.

## i. Overview

> A monoclinic lattice has two axes `a = (a, 0, 0)` and `b = (0, b, 0)` and a third axis
> `c = (c₁, 0, c₃)` in the plane of `a` and perpendicular to `b`, at an angle `β ≠ π / 2` with
> `a`. The base-centred lattice adds the centres of the `a`–`b` faces. A triclinic lattice has
> three axes with no relation between their lengths and angles. Here they are
> `(a, 0, 0)`, `(b₁, b₂, 0)`, `(c₁, c₂, c₃)`. As for the orthorhombic lattices, the first shell
> alone sees more symmetry than the lattice, and the graph keeps the shells up to the first ones
> that pin the point group down. With the lengths below these are:
>
> - primitive monoclinic, `a = 3`, `b = 5`, `c = (1, 0, 3)`: twenty neighbours, the shells at
>   squared lengths `9, 10, 13, 25, 34, 35`;
> - base-centred monoclinic, `a = 4`, `b = 2`, `c = (1, 0, 3)`: sixteen neighbours, the shells at
>   squared lengths `4, 5, 10, 11, 13`;
> - triclinic, `(3, 0, 0)`, `(1, 4, 0)`, `(1, 1, 5)`: sixteen neighbours, the shells at squared
>   lengths `9, 17, 20, 27, 30, 32, 34, 36`.

## ii. Key results

> - `monoclinic`, `baseCentredMonoclinic`, `triclinic` : the lattices, with one site per cell.
> - `monoclinicVectors`, `baseCentredMonoclinicVectors`, `triclinicVectors` : primitive vectors.
> - `monoclinic_neighbors_card`, `baseCentredMonoclinic_neighbors_card`,
>   `triclinic_neighbors_card` : the coordination numbers `20`, `16` and `16`.

## iv. References

> * N. Ashcroft & N. D. Mermin, Solid State Physics, Chapter 7.

## A. Primitive monoclinic lattice

**`CondensedMatter.Crystal.monoclinic`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Monoclinic.lean#L62).

> One site per primitive cell of the primitive monoclinic lattice.

```lean
def monoclinic
```

**`CondensedMatter.Crystal.monoclinicVectors`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Monoclinic.lean#L65).

> The primitive vectors `(a, 0, 0)`, `(0, b, 0)` and `(c₁, 0, c₃)`.

```lean
noncomputable def monoclinicVectors (a b c₁ c₃ : ℝ) : Fin 3 → EuclideanSpace ℝ (Fin 3)
```

**`CondensedMatter.Crystal.monoclinicVectors_independent`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Monoclinic.lean#L69).

> The primitive vectors are independent for nonzero `a`, `b` and `c₃`.

```lean
lemma monoclinicVectors_independent {a b c₁ c₃ : ℝ} (ha : a ≠ 0) (hb : b ≠ 0) (hc : c₃ ≠ 0) :
    LinearIndependent ℝ (monoclinicVectors a b c₁ c₃)
```

**`CondensedMatter.Crystal.monoclinicBonds`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Monoclinic.lean#L85).

> The bonds of the first shells for `a = 3`, `b = 5`, `c = (1, 0, 3)`, up to sign.

```lean
def monoclinicBonds : List (Bond (Fin 3 → ℤ) Unit)
```

**`CondensedMatter.Crystal.monoclinicGraph`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Monoclinic.lean#L92).

> The twenty-neighbour primitive monoclinic graph.

```lean
def monoclinicGraph : PeriodicGraph monoclinic
```

## B. Base-centred monoclinic lattice

**`CondensedMatter.Crystal.baseCentredMonoclinic`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Monoclinic.lean#L98).

> One site per primitive cell of the base-centred monoclinic lattice.

```lean
def baseCentredMonoclinic
```

**`CondensedMatter.Crystal.baseCentredMonoclinicVectors`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Monoclinic.lean#L101).

> The primitive vectors `(a / 2, -b / 2, 0)`, `(a / 2, b / 2, 0)` and `(c₁, 0, c₃)`.

```lean
noncomputable def baseCentredMonoclinicVectors (a b c₁ c₃ : ℝ) :
    Fin 3 → EuclideanSpace ℝ (Fin 3)
```

**`CondensedMatter.Crystal.baseCentredMonoclinicVectors_independent`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Monoclinic.lean#L106).

> The primitive vectors are independent for nonzero `a`, `b` and `c₃`.

```lean
lemma baseCentredMonoclinicVectors_independent {a b c₁ c₃ : ℝ} (ha : a ≠ 0) (hb : b ≠ 0)
    (hc : c₃ ≠ 0) : LinearIndependent ℝ (baseCentredMonoclinicVectors a b c₁ c₃)
```

**`CondensedMatter.Crystal.baseCentredMonoclinicBonds`**, a def, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Monoclinic.lean#L124).

> The bonds of the first shells for `a = 4`, `b = 2`, `c = (1, 0, 3)`, up to sign, in the
> basis `baseCentredMonoclinicVectors`.

```lean
def baseCentredMonoclinicBonds : List (Bond (Fin 3 → ℤ) Unit)
```

**`CondensedMatter.Crystal.baseCentredMonoclinicGraph`**, a def, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Monoclinic.lean#L130).

> The sixteen-neighbour base-centred monoclinic graph.

```lean
def baseCentredMonoclinicGraph : PeriodicGraph baseCentredMonoclinic
```

## C. Triclinic lattice

**`CondensedMatter.Crystal.triclinic`**, a def, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Monoclinic.lean#L137).

> One site per primitive cell of the triclinic lattice.

```lean
def triclinic
```

**`CondensedMatter.Crystal.triclinicVectors`**, a def, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Monoclinic.lean#L140).

> The primitive vectors `(a, 0, 0)`, `(b₁, b₂, 0)` and `(c₁, c₂, c₃)`.

```lean
noncomputable def triclinicVectors (a b₁ b₂ c₁ c₂ c₃ : ℝ) : Fin 3 → EuclideanSpace ℝ (Fin 3)
```

**`CondensedMatter.Crystal.triclinicVectors_independent`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Monoclinic.lean#L144).

> The primitive vectors are independent for nonzero `a`, `b₂` and `c₃`.

```lean
lemma triclinicVectors_independent {a b₁ b₂ c₁ c₂ c₃ : ℝ} (ha : a ≠ 0) (hb : b₂ ≠ 0)
    (hc : c₃ ≠ 0) : LinearIndependent ℝ (triclinicVectors a b₁ b₂ c₁ c₂ c₃)
```

**`CondensedMatter.Crystal.triclinicBonds`**, a def, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Monoclinic.lean#L162).

> The bonds of the first shells for `(3, 0, 0)`, `(1, 4, 0)`, `(1, 1, 5)`, up to sign.

```lean
def triclinicBonds : List (Bond (Fin 3 → ℤ) Unit)
```

**`CondensedMatter.Crystal.triclinicGraph`**, a def, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Monoclinic.lean#L168).

> The sixteen-neighbour triclinic graph.

```lean
def triclinicGraph : PeriodicGraph triclinic
```

## D. Coordination numbers

**`CondensedMatter.Crystal.monoclinic_neighbors_card`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Monoclinic.lean#L173).

> Each site of the primitive monoclinic lattice has twenty neighbours.

```lean
lemma monoclinic_neighbors_card (x : monoclinic.Site) :
    (monoclinicGraph.neighbors x).card = 20
```

**`CondensedMatter.Crystal.baseCentredMonoclinic_neighbors_card`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Monoclinic.lean#L181).

> Each site of the base-centred monoclinic lattice has sixteen neighbours.

```lean
lemma baseCentredMonoclinic_neighbors_card (x : baseCentredMonoclinic.Site) :
    (baseCentredMonoclinicGraph.neighbors x).card = 16
```

**`CondensedMatter.Crystal.triclinic_neighbors_card`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Monoclinic.lean#L189).

> Each site of the triclinic lattice has sixteen neighbours.

```lean
lemma triclinic_neighbors_card (x : triclinic.Site) :
    (triclinicGraph.neighbors x).card = 16
```

## Depends on

- [Crystal bonds and connectivity](graph.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/Examples/Monoclinic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/Monoclinic.lean)
