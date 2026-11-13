---
declaration: module
origin: cited
lean: CondensedMatter.Crystal.l1, CondensedMatter.Crystal.l1_neg, CondensedMatter.Crystal.l1_single, CondensedMatter.Crystal.hypercubic_bonded_iff_exists, CondensedMatter.Crystal.hypercubic_bonded_iff, CondensedMatter.Crystal.signOf, CondensedMatter.Crystal.signOf_mul_self, CondensedMatter.Crystal.abs_signOf
statement: formalized
proof: formalized
---

# The point group of the hypercubic lattice in every dimension

The module `PhyslibAlpha.CondensedMatter.Crystal.PointGroup.Hypercubic`, [PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Hypercubic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Hypercubic.lean): 19 declarations, 10 with a docstring.

> The point group of the hypercubic lattice in `d` dimensions consists of the signed permutations
> of the axes and has order `2 ^ d * d !`.

## i. Overview

> The nearest neighbours of a site of the hypercubic lattice `ℤ^d` are the displacements `±e_j`,
> which are the integer vectors whose coordinates have absolute values summing to one. A lattice
> automorphism preserves the set of these displacements exactly when it maps each basis vector to
> `±e_k` for a distinct axis `k`: it is a permutation of the axes together with a choice of sign
> for each axis. All of these signed permutations preserve the bonds. The point group is therefore
> the hyperoctahedral group, the symmetry group of the `d`-dimensional cube, which has `2 ^ d`
> sign choices and `d !` permutations. For `d = 2` it is the dihedral group of order eight and for
> `d = 3` the octahedral group of order forty-eight.

## ii. Key results

> - `signedPerm` : the lattice automorphism given by a permutation of the axes and signs.
> - `mem_pointStabilizer_hypercubic_iff` : a lattice automorphism preserves the bonds of the
>   hypercubic lattice exactly when it is a signed permutation.
> - `card_pointGroup_hypercubic` : the point group has order `2 ^ d * d !`.

## iv. References

> * N. Ashcroft & N. D. Mermin, Solid State Physics, Chapter 7.

## A. Bonds of the hypercubic lattice

**`CondensedMatter.Crystal.l1`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Hypercubic.lean#L60).

> The sum of the absolute values of the coordinates.

```lean
def l1 (r : Fin d → ℤ) : ℤ
```

**`CondensedMatter.Crystal.l1_neg`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Hypercubic.lean#L62).

```lean
lemma l1_neg (r : Fin d → ℤ) : l1 (-r) = l1 r
```

**`CondensedMatter.Crystal.l1_single`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Hypercubic.lean#L64).

```lean
lemma l1_single (j : Fin d) : l1 (Pi.single j (1 : ℤ) : Fin d → ℤ) = 1
```

**`CondensedMatter.Crystal.hypercubic_bonded_iff_exists`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Hypercubic.lean#L71).

> The bonded displacements of the hypercubic lattice are the vectors `±e_j`.

```lean
lemma hypercubic_bonded_iff_exists (r : Fin d → ℤ) :
    (hypercubicGraph d).Bonded () () r ↔ ∃ j, r = Pi.single j 1 ∨ r = -Pi.single j 1
```

**`CondensedMatter.Crystal.hypercubic_bonded_iff`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Hypercubic.lean#L94).

> **Two sites of the hypercubic lattice are bonded exactly when their cells differ by a vector
> whose coordinates have absolute values summing to one.**

```lean
lemma hypercubic_bonded_iff (r : Fin d → ℤ) :
    (hypercubicGraph d).Bonded () () r ↔ l1 r = 1
```

## B. Signed permutations

**`CondensedMatter.Crystal.signOf`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Hypercubic.lean#L128).

> The sign `+1` for `true` and `-1` for `false`.

```lean
def signOf (b : Bool) : ℤ
```

**`CondensedMatter.Crystal.signOf_mul_self`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Hypercubic.lean#L130).

```lean
lemma signOf_mul_self (b : Bool) : signOf b * signOf b = 1
```

**`CondensedMatter.Crystal.abs_signOf`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Hypercubic.lean#L132).

```lean
lemma abs_signOf (b : Bool) : |signOf b| = 1
```

**`CondensedMatter.Crystal.signOf_ne_zero`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Hypercubic.lean#L134).

```lean
lemma signOf_ne_zero (b : Bool) : signOf b ≠ 0
```

**`CondensedMatter.Crystal.signOf_injective`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Hypercubic.lean#L136).

```lean
lemma signOf_injective : Function.Injective signOf
```

**`CondensedMatter.Crystal.signedPerm`**, a def, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Hypercubic.lean#L141).

> The lattice automorphism that permutes the axes by `π` and multiplies the `i`-th coordinate
> by the sign `ε i`.

```lean
def signedPerm (π : Equiv.Perm (Fin d)) (ε : Fin d → Bool) : (Fin d → ℤ) ≃+ (Fin d → ℤ)
```

**`CondensedMatter.Crystal.signedPerm_apply`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Hypercubic.lean#L156).

```lean
lemma signedPerm_apply (π : Equiv.Perm (Fin d)) (ε : Fin d → Bool) (r : Fin d → ℤ) (i : Fin d) :
    signedPerm π ε r i = signOf (ε i) * r (π.symm i)
```

**`CondensedMatter.Crystal.l1_signedPerm`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Hypercubic.lean#L160).

> A signed permutation preserves the sum of the absolute values of the coordinates.

```lean
lemma l1_signedPerm (π : Equiv.Perm (Fin d)) (ε : Fin d → Bool) (r : Fin d → ℤ) :
    l1 (signedPerm π ε r) = l1 r
```

**`CondensedMatter.Crystal.signedPerm_single`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Hypercubic.lean#L166).

```lean
lemma signedPerm_single (π : Equiv.Perm (Fin d)) (ε : Fin d → Bool) (j : Fin d) :
    signedPerm π ε (Pi.single j 1) = Pi.single (π j) (signOf (ε (π j)))
```

**`CondensedMatter.Crystal.signedPerm_injective`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Hypercubic.lean#L174).

```lean
lemma signedPerm_injective :
    Function.Injective fun p : Equiv.Perm (Fin d) × (Fin d → Bool) => signedPerm p.1 p.2
```

## C. The point group

**`CondensedMatter.Crystal.signedPerm_mem_pointStabilizer`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Hypercubic.lean#L197).

> **A signed permutation preserves the bonds of the hypercubic lattice.**

```lean
lemma signedPerm_mem_pointStabilizer (π : Equiv.Perm (Fin d)) (ε : Fin d → Bool) :
    Multiplicative.ofAdd (signedPerm π ε) ∈ (hypercubicGraph d).pointStabilizer
```

**`CondensedMatter.Crystal.mem_pointStabilizer_hypercubic_iff`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Hypercubic.lean#L205).

> **The lattice automorphisms preserving the bonds of the hypercubic lattice are exactly the
> signed permutations.**

```lean
lemma mem_pointStabilizer_hypercubic_iff (A : Multiplicative (AddAut (Fin d → ℤ))) :
    A ∈ (hypercubicGraph d).pointStabilizer ↔
      ∃ (π : Equiv.Perm (Fin d)) (ε : Fin d → Bool), Multiplicative.toAdd A = signedPerm π ε
```

**`CondensedMatter.Crystal.pointStabilizerEquivSignedPerm`**, a def, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Hypercubic.lean#L253).

> **The point group of the hypercubic lattice is the group of signed permutations of the
> axes**: it is in bijection with the pairs of a permutation and a choice of signs.

```lean
noncomputable def pointStabilizerEquivSignedPerm :
    (Equiv.Perm (Fin d) × (Fin d → Bool)) ≃ (hypercubicGraph d).pointStabilizer
```

**`CondensedMatter.Crystal.card_pointGroup_hypercubic`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Hypercubic.lean#L263).

> **The point group of the hypercubic lattice in `d` dimensions has order `2 ^ d * d !`.**

```lean
lemma card_pointGroup_hypercubic (d : ℕ) :
    Nat.card (hypercubicGraph d).pointGroup = 2 ^ d * d.factorial
```

## Depends on

- [Standard crystals](../part-01/examples-basic.md)
- [Point groups of Bravais lattices](pointgroup-basic.md)

## Proof depends on

- [Coordinates on the Brillouin zone and the action of the symmetries](../part-01/brillouincoordinates.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Hypercubic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Hypercubic.lean)
