---
declaration: module
origin: cited
lean: CondensedMatter.Crystal.PeriodicGraph.act, CondensedMatter.Crystal.PeriodicGraph.act_apply, CondensedMatter.Crystal.PeriodicGraph.act_single, CondensedMatter.Crystal.PeriodicGraph.apply_eq_act, CondensedMatter.Crystal.PeriodicGraph.Admissible, CondensedMatter.Crystal.PeriodicGraph.Admissible.image_eq, CondensedMatter.Crystal.PeriodicGraph.Admissible.surjective, CondensedMatter.Crystal.PeriodicGraph.Admissible.injective
statement: formalized
proof: formalized
---

# Counting the point group of a Bravais lattice

The module `PhyslibAlpha.CondensedMatter.Crystal.PointGroup.Count`, [PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Count.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Count.lean): 13 declarations, 10 with a docstring.

> The point group of an `n`-dimensional lattice with a finite set `N` of neighbour displacements
> is counted by the possible images of the `n` basis vectors.

## i. Overview

> An automorphism of `ℤⁿ` that preserves the set `N` of bonded displacements is determined by the
> images of the basis vectors, which are neighbour displacements when the basis vectors are
> themselves bonded. A tuple of neighbour displacements, one for each basis vector, defines such
> an automorphism exactly when the linear map it determines maps `N` into itself, and is injective
> on `N`. Injectivity on the finite set `N` makes the map a bijection of `N`, so its image contains
> the basis, and a surjective endomorphism of `ℤⁿ` is an automorphism. The point group is therefore
> in bijection with the set of such tuples, a finite set that is counted by a direct computation.

## ii. Key results

> - `PeriodicGraph.pointStabilizerEquiv` : the point group is in bijection with the admissible
>   tuples of neighbour displacements.
> - `PeriodicGraph.card_pointGroup` : its cardinality is the number of admissible tuples.

## iv. References

> * N. Ashcroft & N. D. Mermin, Solid State Physics, Chapter 7.

## A. Linear maps determined by the images of the basis

**`CondensedMatter.Crystal.PeriodicGraph.act`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Count.lean#L59).

> The linear map of `ℤⁿ` taking the basis vectors to the given vectors.

```lean
def act (v : Fin n → Fin n → ℤ) : (Fin n → ℤ) →ₗ[ℤ] (Fin n → ℤ)
```

**`CondensedMatter.Crystal.PeriodicGraph.act_apply`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Count.lean#L62).

```lean
lemma act_apply (v : Fin n → Fin n → ℤ) (d : Fin n → ℤ) : act v d = ∑ j, d j • v j
```

**`CondensedMatter.Crystal.PeriodicGraph.act_single`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Count.lean#L65).

```lean
lemma act_single (v : Fin n → Fin n → ℤ) (j : Fin n) : act v (Pi.single j 1) = v j
```

**`CondensedMatter.Crystal.PeriodicGraph.apply_eq_act`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Count.lean#L69).

> A lattice automorphism is determined by the images of the basis vectors.

```lean
lemma apply_eq_act (A : AddAut (Fin n → ℤ)) (d : Fin n → ℤ) :
    A d = act (fun j => A (Pi.single j 1)) d
```

## B. Admissible tuples

**`CondensedMatter.Crystal.PeriodicGraph.Admissible`**, a structure, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Count.lean#L84).

> A tuple of neighbour displacements is admissible when its linear map takes the set of
> neighbour displacements into itself, injectively.

```lean
structure Admissible (N : Finset (Fin n → ℤ)) (v : Fin n → Fin n → ℤ) : Prop where
  mem : ∀ j, v j ∈ N
  mapsTo : ∀ d ∈ N, act v d ∈ N
  injOn : Set.InjOn (act v) N
```

**`CondensedMatter.Crystal.PeriodicGraph.Admissible.image_eq`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Count.lean#L94).

> An admissible tuple maps the set of neighbour displacements onto itself.

```lean
lemma Admissible.image_eq {v : Fin n → Fin n → ℤ} (hv : Admissible N v) :
    N.image (act v) = N
```

**`CondensedMatter.Crystal.PeriodicGraph.Admissible.surjective`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Count.lean#L104).

> An admissible tuple gives a surjective linear map.

```lean
lemma Admissible.surjective {v : Fin n → Fin n → ℤ} (hv : Admissible N v) :
    Function.Surjective (act v)
```

**`CondensedMatter.Crystal.PeriodicGraph.Admissible.injective`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Count.lean#L122).

> An admissible tuple gives an injective linear map.

```lean
lemma Admissible.injective {v : Fin n → Fin n → ℤ} (hv : Admissible N v) :
    Function.Injective (act v)
```

**`CondensedMatter.Crystal.PeriodicGraph.Admissible.act_mem_iff`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Count.lean#L128).

> A displacement is a neighbour exactly when its image under an admissible tuple is.

```lean
lemma Admissible.act_mem_iff {v : Fin n → Fin n → ℤ} (hv : Admissible N v) (d : Fin n → ℤ) :
    act v d ∈ N ↔ d ∈ N
```

**`CondensedMatter.Crystal.PeriodicGraph.Admissible.equiv`**, a def, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Count.lean#L138).

> The lattice automorphism of an admissible tuple.

```lean
noncomputable def Admissible.equiv {v : Fin n → Fin n → ℤ} (hv : Admissible N v) :
    AddAut (Fin n → ℤ)
```

**`CondensedMatter.Crystal.PeriodicGraph.Admissible.equiv_apply`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Count.lean#L142).

```lean
lemma Admissible.equiv_apply {v : Fin n → Fin n → ℤ} (hv : Admissible N v) (d : Fin n → ℤ) :
    hv.equiv hN d = act v d
```

## C. The count

**`CondensedMatter.Crystal.PeriodicGraph.pointStabilizerEquiv`**, a def, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Count.lean#L153).

> **The point group of a Bravais lattice is in bijection with the admissible tuples of
> neighbour displacements.**

```lean
noncomputable def pointStabilizerEquiv : g.pointStabilizer ≃ {v // Admissible N v}
```

**`CondensedMatter.Crystal.PeriodicGraph.card_pointGroup`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Count.lean#L175).

> **The order of the point group** is the number of admissible tuples of neighbour
> displacements.

```lean
lemma card_pointGroup : Nat.card g.pointGroup = Nat.card {v // Admissible N v}
```

## Depends on

- [Point groups of Bravais lattices](pointgroup-basic.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Count.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Count.lean)
