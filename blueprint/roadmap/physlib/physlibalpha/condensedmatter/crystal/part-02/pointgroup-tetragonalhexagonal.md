---
declaration: module
origin: cited
lean: CondensedMatter.Crystal.PeriodicGraph.toAdd_pow_apply, CondensedMatter.Crystal.PeriodicGraph.toVec3_act_iterate, CondensedMatter.Crystal.PeriodicGraph.basis3, CondensedMatter.Crystal.PeriodicGraph.toVec3_single_mem_basis3, CondensedMatter.Crystal.PeriodicGraph.powFixesBasisB, CondensedMatter.Crystal.PeriodicGraph.iterate_act_single_eq_of_powFixesBasisB, CondensedMatter.Crystal.PeriodicGraph.pow_eq_one_of_admissible, CondensedMatter.Crystal.tetragonalNeighbors
statement: formalized
proof: formalized
---

# The point groups of the tetragonal and hexagonal lattices

The module `PhyslibAlpha.CondensedMatter.Crystal.PointGroup.TetragonalHexagonal`, [PhyslibAlpha/CondensedMatter/Crystal/PointGroup/TetragonalHexagonal.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/TetragonalHexagonal.lean): 17 declarations, 15 with a docstring.

> The point groups of the primitive and body-centred tetragonal lattices have order sixteen, and
> the point group of the primitive hexagonal lattice has order twenty-four.

## i. Overview

> The orders are counted as for the cubic lattices, by `PeriodicGraph.card_pointGroup` and the
> reflection of admissibility into a Boolean test on lists of triples of integers. They are those of
> the holohedries `4/mmm` and `6/mmm`. With the bonds of the first shell only, the primitive
> tetragonal graph is the simple cubic graph, and its point group has order `48`.
>
> The exponent of each group is computed in the same way: an element of the point stabilizer is
> determined by the images of the three basis vectors, so it is enough to check its powers on the
> basis, for each admissible triple, which is again a Boolean test on the list of admissible
> triples. Every element of the primitive tetragonal point group satisfies `A ^ 4 = 1`, and every
> element of the hexagonal point group satisfies `A ^ 6 = 1`. So the primitive tetragonal group has
> no rotation of order three, and the hexagonal group none of order four.

## ii. Key results

> - `tetragonal_card_pointGroup`, `bodyCentredTetragonal_card_pointGroup` : order `16`.
> - `hexagonal_card_pointGroup` : order `24`.
> - `tetragonal_pow_four` : `A ^ 4 = 1` on the point stabilizer.
> - `hexagonal_pow_six` : `A ^ 6 = 1` on the point stabilizer.

## iv. References

> * N. Ashcroft & N. D. Mermin, Solid State Physics, Chapter 7.

## A. Powers from admissible triples

**`CondensedMatter.Crystal.PeriodicGraph.toAdd_pow_apply`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/TetragonalHexagonal.lean#L59).

```lean
lemma toAdd_pow_apply {G : Type*} [AddCommGroup G] (A : Multiplicative (AddAut G)) (n : ℕ)
    (x : G) : (Multiplicative.toAdd (A ^ n) : AddAut G) x =
      (Multiplicative.toAdd A : AddAut G)^[n] x
```

**`CondensedMatter.Crystal.PeriodicGraph.toVec3_act_iterate`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/TetragonalHexagonal.lean#L69).

> The powers of the map determined by a tuple of columns, in components.

```lean
lemma toVec3_act_iterate (v : Fin 3 → Fin 3 → ℤ) (n : ℕ) (d : Fin 3 → ℤ) :
    toVec3 ((act v)^[n] d) =
      (act3 (toVec3 (v 0)) (toVec3 (v 1)) (toVec3 (v 2)))^[n] (toVec3 d)
```

**`CondensedMatter.Crystal.PeriodicGraph.basis3`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/TetragonalHexagonal.lean#L77).

> The three basis vectors, as triples.

```lean
def basis3 : List Vec3
```

**`CondensedMatter.Crystal.PeriodicGraph.toVec3_single_mem_basis3`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/TetragonalHexagonal.lean#L79).

```lean
lemma toVec3_single_mem_basis3 (j : Fin 3) : toVec3 (Pi.single j 1) ∈ basis3
```

**`CondensedMatter.Crystal.PeriodicGraph.powFixesBasisB`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/TetragonalHexagonal.lean#L84).

> Whether the `n`-th power of every admissible triple of the neighbour list `l` fixes the
> three basis vectors.

```lean
def powFixesBasisB (l : List Vec3) (n : ℕ) : Bool
```

**`CondensedMatter.Crystal.PeriodicGraph.iterate_act_single_eq_of_powFixesBasisB`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/TetragonalHexagonal.lean#L88).

> If the Boolean test passes, the `n`-th power of every admissible tuple fixes the basis.

```lean
lemma iterate_act_single_eq_of_powFixesBasisB {N : Finset (Fin 3 → ℤ)} {l : List Vec3}
    (hl : ∀ t, t ∈ l ↔ ofVec3 t ∈ N) {n : ℕ} (h : powFixesBasisB l n = true)
    {v : Fin 3 → Fin 3 → ℤ} (hv : Admissible N v) (j : Fin 3) :
    (act v)^[n] (Pi.single j 1) = Pi.single j 1
```

**`CondensedMatter.Crystal.PeriodicGraph.pow_eq_one_of_admissible`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/TetragonalHexagonal.lean#L108).

> If the `n`-th power of every admissible triple fixes the basis, then every element of the
> point stabilizer satisfies `A ^ n = 1`.

```lean
lemma pow_eq_one_of_admissible (n : ℕ)
    (h : ∀ v, Admissible N v → ∀ j, (act v)^[n] (Pi.single j 1) = Pi.single j 1)
    (A : Multiplicative (AddAut (Fin 3 → ℤ))) (hA : A ∈ g.pointStabilizer) : A ^ n = 1
```

## B. The orders

> The neighbour lists are written out with the neighbours that are not basis vectors first, so
> that the Boolean test fails early on most candidate tuples.

**`CondensedMatter.Crystal.tetragonalNeighbors`**, a def, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/TetragonalHexagonal.lean#L135).

> The ten neighbours of the primitive tetragonal lattice.

```lean
def tetragonalNeighbors : List PeriodicGraph.Vec3
```

**`CondensedMatter.Crystal.tetragonal_card_pointGroup`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/TetragonalHexagonal.lean#L140).

> **The point group of the primitive tetragonal lattice has order `16`.**

```lean
lemma tetragonal_card_pointGroup : Nat.card tetragonalGraph.pointGroup = 16
```

**`CondensedMatter.Crystal.bodyCentredTetragonalNeighbors`**, a def, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/TetragonalHexagonal.lean#L150).

> The sixteen neighbours of the body-centred tetragonal lattice.

```lean
def bodyCentredTetragonalNeighbors : List PeriodicGraph.Vec3
```

**`CondensedMatter.Crystal.bodyCentredTetragonal_card_pointGroup`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/TetragonalHexagonal.lean#L156).

> **The point group of the body-centred tetragonal lattice has order `16`.**

```lean
lemma bodyCentredTetragonal_card_pointGroup :
    Nat.card bodyCentredTetragonalGraph.pointGroup = 16
```

**`CondensedMatter.Crystal.hexagonalNeighbors`**, a def, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/TetragonalHexagonal.lean#L169).

> The eight neighbours of the primitive hexagonal lattice.

```lean
def hexagonalNeighbors : List PeriodicGraph.Vec3
```

**`CondensedMatter.Crystal.hexagonal_card_pointGroup`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/TetragonalHexagonal.lean#L173).

> **The point group of the primitive hexagonal lattice has order `24`.**

```lean
lemma hexagonal_card_pointGroup : Nat.card hexagonalGraph.pointGroup = 24
```

**`CondensedMatter.Crystal.firstShellNeighbors`**, a def, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/TetragonalHexagonal.lean#L183).

> The six neighbours of the first shell, `±x, ±y, ±z`.

```lean
def firstShellNeighbors : List PeriodicGraph.Vec3
```

**`CondensedMatter.Crystal.tetragonal_firstShell_card_pointGroup`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/TetragonalHexagonal.lean#L188).

> With the bonds of the first shell only, `±x, ±y, ±z`, a tetragonal lattice has the point
> group of the simple cubic lattice, of order `48`.

```lean
lemma tetragonal_firstShell_card_pointGroup :
    Nat.card (PeriodicGraph.ofBonds (G := Fin 3 → ℤ) (F := Unit)
      [⟨(), (), ![1, 0, 0]⟩, ⟨(), (), ![0, 1, 0]⟩, ⟨(), (), ![0, 0, 1]⟩]).pointGroup = 48
```

## C. The exponents

**`CondensedMatter.Crystal.tetragonal_pow_four`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/TetragonalHexagonal.lean#L204).

> Every element of the point group of the primitive tetragonal lattice satisfies `A ^ 4 = 1`.

```lean
lemma tetragonal_pow_four (A : Multiplicative (AddAut (Fin 3 → ℤ)))
    (hA : A ∈ tetragonalGraph.pointStabilizer) : A ^ 4 = 1
```

**`CondensedMatter.Crystal.hexagonal_pow_six`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/TetragonalHexagonal.lean#L213).

> Every element of the point group of the primitive hexagonal lattice satisfies `A ^ 6 = 1`.

```lean
lemma hexagonal_pow_six (A : Multiplicative (AddAut (Fin 3 → ℤ)))
    (hA : A ∈ hexagonalGraph.pointStabilizer) : A ^ 6 = 1
```

## Depends on

- [Tetragonal and hexagonal lattices](../part-01/examples-tetragonalhexagonal.md)
- [The point groups of the face-centred and body-centred cubic lattices](pointgroup-cubic.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/PointGroup/TetragonalHexagonal.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/TetragonalHexagonal.lean)
