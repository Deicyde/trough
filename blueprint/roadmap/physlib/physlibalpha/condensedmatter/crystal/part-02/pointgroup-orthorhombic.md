---
declaration: module
origin: cited
lean: CondensedMatter.Crystal.PeriodicGraph.PassesTests, CondensedMatter.Crystal.PeriodicGraph.admissible_iff_of_tests, CondensedMatter.Crystal.PeriodicGraph.card_pointGroup_ofBonds, CondensedMatter.Crystal.orthorhombicPointTriples, CondensedMatter.Crystal.orthorhombic_admissible_iff, CondensedMatter.Crystal.baseCentredOrthorhombicPointTriples, CondensedMatter.Crystal.baseCentredOrthorhombic_admissible_iff, CondensedMatter.Crystal.bodyCentredOrthorhombicPointTriples
statement: formalized
proof: formalized
---

# The point groups of the orthorhombic lattices

The module `PhyslibAlpha.CondensedMatter.Crystal.PointGroup.Orthorhombic`, [PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Orthorhombic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Orthorhombic.lean): 16 declarations (1 instance with no name), 15 with a docstring.

> The point groups of the four orthorhombic lattices have order eight: they are the reflections in
> the three coordinate planes and their products, the holohedry `mmm`.

## i. Overview

> An element of the point group is determined by the images of the three basis vectors, an
> admissible triple. Instead of checking all triples of neighbour displacements, each basis vector
> is located by a few tests: a displacement `d` is a neighbour exactly when its image is. For the
> primitive lattice:
>
> - `x` is the only neighbour, up to sign, whose double is a neighbour, so it goes to `±x`;
> - `y` is the only neighbour on both diagonals `x ± y` through `x`, so it goes to `±y`;
> - `z` is on no diagonal through `x`, so it goes to `±z`.
>
> The centred lattices are located in the same way by sums of two and three basis vectors. Each
> lattice then has exactly eight admissible triples, listed explicitly in the basis of its graph.

## ii. Key results

> - `PeriodicGraph.admissible_iff_of_tests` : the admissible triples are a given set, if only its
>   triples pass the tests.
> - `orthorhombic_admissible_iff`, `baseCentredOrthorhombic_admissible_iff`,
>   `bodyCentredOrthorhombic_admissible_iff`, `faceCentredOrthorhombic_admissible_iff` : the eight
>   admissible triples of each lattice.
> - `orthorhombic_card_pointGroup`, `baseCentredOrthorhombic_card_pointGroup`,
>   `bodyCentredOrthorhombic_card_pointGroup`, `faceCentredOrthorhombic_card_pointGroup` :
>   order `8`.

## iv. References

> * N. Ashcroft & N. D. Mermin, Solid State Physics, Chapter 7.

## A. Tests on admissible triples

**`CondensedMatter.Crystal.PeriodicGraph.PassesTests`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Orthorhombic.lean#L67).

> The triple `(a, b, c)` passes the tests `D₀`, `D₁`, `D₂` on its first, first two and three
> vectors: each test `d` and its image under the triple are neighbours together.

```lean
def PassesTests (N : Finset (Fin 3 → ℤ)) (D₀ : List ℤ) (D₁ : List (ℤ × ℤ))
    (D₂ : List (Fin 3 → ℤ)) (a b c : Fin 3 → ℤ) : Prop
```

**An instance with no name**, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Orthorhombic.lean#L73).

```lean
instance (N : Finset (Fin 3 → ℤ)) (D₀ : List ℤ) (D₁ : List (ℤ × ℤ)) (D₂ : List (Fin 3 → ℤ))
    (a b c : Fin 3 → ℤ) : Decidable (PassesTests N D₀ D₁ D₂ a b c)
```

**`CondensedMatter.Crystal.PeriodicGraph.admissible_iff_of_tests`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Orthorhombic.lean#L80).

> The admissible triples are the triples of `S`, if every triple of `S` is admissible and only
> the triples of `S` pass the tests.

```lean
lemma admissible_iff_of_tests (hN : ∀ j, (Pi.single j 1 : Fin 3 → ℤ) ∈ N)
    {S : Finset (Fin 3 → Fin 3 → ℤ)} (D₀ : List ℤ) (D₁ : List (ℤ × ℤ))
    (D₂ : List (Fin 3 → ℤ)) (hS : ∀ v ∈ S, Admissible N v)
    (hD : ∀ a ∈ N, ∀ b ∈ N, ∀ c ∈ N, PassesTests N D₀ D₁ D₂ a b c → ![a, b, c] ∈ S)
    (v : Fin 3 → Fin 3 → ℤ) : Admissible N v ↔ v ∈ S
```

**`CondensedMatter.Crystal.PeriodicGraph.card_pointGroup_ofBonds`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Orthorhombic.lean#L95).

> The order of the point group is the number of admissible triples, once they are known.

```lean
lemma card_pointGroup_ofBonds (bonds : List (Bond (Fin 3 → ℤ) Unit))
    (hN : ∀ j, (Pi.single j 1 : Fin 3 → ℤ) ∈ bondNeighbors bonds)
    {S : Finset (Fin 3 → Fin 3 → ℤ)} (h : ∀ v, Admissible (bondNeighbors bonds) v ↔ v ∈ S) :
    Nat.card (ofBonds bonds).pointGroup = S.card
```

## B. The admissible triples

**`CondensedMatter.Crystal.orthorhombicPointTriples`**, a def, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Orthorhombic.lean#L111).

> The images of the basis vectors under the eight point operations of the primitive orthorhombic
> lattice, the sign changes of the three basis vectors.

```lean
def orthorhombicPointTriples : Finset (Fin 3 → Fin 3 → ℤ)
```

**`CondensedMatter.Crystal.orthorhombic_admissible_iff`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Orthorhombic.lean#L119).

> The point operations of the primitive orthorhombic lattice are the eight of
> `orthorhombicPointTriples`.

```lean
lemma orthorhombic_admissible_iff (v : Fin 3 → Fin 3 → ℤ) :
    Admissible (bondNeighbors orthorhombicBonds) v ↔ v ∈ orthorhombicPointTriples
```

**`CondensedMatter.Crystal.baseCentredOrthorhombicPointTriples`**, a def, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Orthorhombic.lean#L126).

> The images of the basis vectors under the eight point operations of the base-centred
> orthorhombic lattice, in the basis `baseCentredVectors a b c`.

```lean
def baseCentredOrthorhombicPointTriples : Finset (Fin 3 → Fin 3 → ℤ)
```

**`CondensedMatter.Crystal.baseCentredOrthorhombic_admissible_iff`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Orthorhombic.lean#L134).

> The point operations of the base-centred orthorhombic lattice are the eight of
> `baseCentredOrthorhombicPointTriples`.

```lean
lemma baseCentredOrthorhombic_admissible_iff (v : Fin 3 → Fin 3 → ℤ) :
    Admissible (bondNeighbors baseCentredOrthorhombicBonds) v ↔
      v ∈ baseCentredOrthorhombicPointTriples
```

**`CondensedMatter.Crystal.bodyCentredOrthorhombicPointTriples`**, a def, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Orthorhombic.lean#L142).

> The images of the basis vectors under the eight point operations of the body-centred
> orthorhombic lattice, in the basis `bccVectors a b c`.

```lean
def bodyCentredOrthorhombicPointTriples : Finset (Fin 3 → Fin 3 → ℤ)
```

**`CondensedMatter.Crystal.bodyCentredOrthorhombic_admissible_iff`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Orthorhombic.lean#L150).

> The point operations of the body-centred orthorhombic lattice are the eight of
> `bodyCentredOrthorhombicPointTriples`.

```lean
lemma bodyCentredOrthorhombic_admissible_iff (v : Fin 3 → Fin 3 → ℤ) :
    Admissible (bondNeighbors bodyCentredOrthorhombicBonds) v ↔
      v ∈ bodyCentredOrthorhombicPointTriples
```

**`CondensedMatter.Crystal.faceCentredOrthorhombicPointTriples`**, a def, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Orthorhombic.lean#L158).

> The images of the basis vectors under the eight point operations of the face-centred
> orthorhombic lattice, in the basis `fccVectors a b c`.

```lean
def faceCentredOrthorhombicPointTriples : Finset (Fin 3 → Fin 3 → ℤ)
```

**`CondensedMatter.Crystal.faceCentredOrthorhombic_admissible_iff`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Orthorhombic.lean#L166).

> The point operations of the face-centred orthorhombic lattice are the eight of
> `faceCentredOrthorhombicPointTriples`.

```lean
lemma faceCentredOrthorhombic_admissible_iff (v : Fin 3 → Fin 3 → ℤ) :
    Admissible (bondNeighbors faceCentredOrthorhombicBonds) v ↔
      v ∈ faceCentredOrthorhombicPointTriples
```

## C. The orders

**`CondensedMatter.Crystal.orthorhombic_card_pointGroup`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Orthorhombic.lean#L176).

> **The point group of the primitive orthorhombic lattice has order `8`.**

```lean
lemma orthorhombic_card_pointGroup : Nat.card orthorhombicGraph.pointGroup = 8
```

**`CondensedMatter.Crystal.baseCentredOrthorhombic_card_pointGroup`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Orthorhombic.lean#L181).

> **The point group of the base-centred orthorhombic lattice has order `8`.**

```lean
lemma baseCentredOrthorhombic_card_pointGroup :
    Nat.card baseCentredOrthorhombicGraph.pointGroup = 8
```

**`CondensedMatter.Crystal.bodyCentredOrthorhombic_card_pointGroup`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Orthorhombic.lean#L187).

> **The point group of the body-centred orthorhombic lattice has order `8`.**

```lean
lemma bodyCentredOrthorhombic_card_pointGroup :
    Nat.card bodyCentredOrthorhombicGraph.pointGroup = 8
```

**`CondensedMatter.Crystal.faceCentredOrthorhombic_card_pointGroup`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Orthorhombic.lean#L193).

> **The point group of the face-centred orthorhombic lattice has order `8`.**

```lean
lemma faceCentredOrthorhombic_card_pointGroup :
    Nat.card faceCentredOrthorhombicGraph.pointGroup = 8
```

## Depends on

- [Orthorhombic lattices](../part-01/examples-orthorhombic.md)
- [The point groups of the face-centred and body-centred cubic lattices](pointgroup-cubic.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Orthorhombic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Orthorhombic.lean)
