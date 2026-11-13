---
declaration: module
origin: cited
lean: Physlib.CondensedMatter.Crystal.Embedding, Physlib.CondensedMatter.Crystal.Embedding.position, Physlib.CondensedMatter.Crystal.Embedding.position_vadd, Physlib.CondensedMatter.Crystal.Embedding.action, Physlib.CondensedMatter.Crystal.Embedding.positionHom, Physlib.CondensedMatter.Crystal.Embedding.dist_position_vadd, Physlib.CondensedMatter.Crystal.Embedding.IsSpaceFilling, Physlib.CondensedMatter.Crystal.Embedding.isSpaceFilling_iff
statement: formalized
proof: formalized
---

# A crystal in space

The module `Physlib.CondensedMatter.Crystal.Embedding`, [Physlib/CondensedMatter/Crystal/Embedding.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Embedding.lean): 10 declarations, 10 with a docstring.

> Embedding of a crystal into a space.

## i. Overview

> Given a normed additive commutative group `E`, an embedding sends each translation of the crystal to
> a vector in `E` and each site of the reference cell to a point in `E`. The site `(n, i)` is then
> placed at the vector of `n` plus the point of `i`. The embedding is space filling if the vectors of
> the translations span `E`.

## ii. Key results

> - `Crystal.Embedding` : the vectors `ρ` of the translations and the positions `p` of the
>   sites of the reference cell, in a normed group.
> - `Crystal.Embedding.positionHom` : the positions commute with the translations, as an equivariant
>   map of the sites.
> - `Crystal.Embedding.position_vadd` : translating a site translates its position.
> - `Crystal.Embedding.dist_position_vadd` : translating two sites does not change the
>   distance between their positions.
> - `Crystal.Embedding.IsSpaceFilling` : the vectors of the translations span the space.
> - `Crystal.Embedding.isSpaceFilling_iff` : space filling can be checked on a generating set.
> - `Crystal.Embedding.IsSpaceFilling.finiteDimensional` : a space-filling embedding lies in a
>   finite-dimensional space.
> - `Crystal.Embedding.IsSpaceFilling.finrank_eq_rank` : the dimension of the space equals the rank
>   of the translation group when the vectors of a basis of the group are linearly independent.

## iv. References

> * None.

## A. Vectors and positions

**`Physlib.CondensedMatter.Crystal.Embedding`**, a structure, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Embedding.lean#L63).

> An embedding of a crystal in a normed group `E`. It assigns a vector to each translation and a
> position to each site of the reference cell.

```lean
structure Embedding (C : Crystal G) (E : Type*) [NormedAddCommGroup E] where
  /-- The vector of a translation. -/
  vector : G →+ E
  /-- The position of the site with a given label in the reference cell. -/
  basis : C.UnitCell → E
```

**`Physlib.CondensedMatter.Crystal.Embedding.position`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Embedding.lean#L74).

> The site `(n, i)` sits at the vector of `n` plus the position of the label `i`.

```lean
def position (x : C.Site) : E
```

**`Physlib.CondensedMatter.Crystal.Embedding.position_vadd`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Embedding.lean#L77).

> Translating a site by `a` translates its position by the vector of `a`.

```lean
lemma position_vadd (a : G) (x : C.Site) : R.position (a +ᵥ x) = R.vector a + R.position x
```

**`Physlib.CondensedMatter.Crystal.Embedding.action`**, an abbrev, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Embedding.lean#L81).

> The translation group acts on the space by its vectors.

```lean
abbrev action : AddAction G E
```

**`Physlib.CondensedMatter.Crystal.Embedding.positionHom`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Embedding.lean#L84).

> The positions commute with the translations.

```lean
def positionHom : letI := R.action; AddActionHom (id : G → G) C.Site E
```

**`Physlib.CondensedMatter.Crystal.Embedding.dist_position_vadd`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Embedding.lean#L90).

> Translating two sites does not change the distance between their positions.

```lean
lemma dist_position_vadd (a : G) (x y : C.Site) :
    Dist.dist (R.position (a +ᵥ x)) (R.position (a +ᵥ y)) =
      Dist.dist (R.position x) (R.position y)
```

## B. Filling the space

**`Physlib.CondensedMatter.Crystal.Embedding.IsSpaceFilling`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Embedding.lean#L101).

> The embedding is space filling if the vectors of the translations span the space, so that the
> crystal repeats in every direction.

```lean
def IsSpaceFilling : Prop
```

**`Physlib.CondensedMatter.Crystal.Embedding.isSpaceFilling_iff`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Embedding.lean#L105).

> An embedding fills the space exactly when the vectors of a generating set of the translation
> group span it.

```lean
lemma isSpaceFilling_iff {S : Set G} (hS : AddSubgroup.closure S = ⊤) :
    R.IsSpaceFilling ↔ Submodule.span ℝ (R.vector '' S) = ⊤
```

**`Physlib.CondensedMatter.Crystal.Embedding.IsSpaceFilling.finiteDimensional`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Embedding.lean#L118).

> A space-filling embedding is in a finite-dimensional space.

```lean
lemma IsSpaceFilling.finiteDimensional (h : R.IsSpaceFilling) : FiniteDimensional ℝ E
```

**`Physlib.CondensedMatter.Crystal.Embedding.IsSpaceFilling.finrank_eq_rank`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Embedding.lean#L124).

> The dimension equals the rank of the translation group when the vectors of a basis of the
> group are linearly independent over `ℝ`.

```lean
lemma IsSpaceFilling.finrank_eq_rank (h : R.IsSpaceFilling) {ι : Type*} [Fintype ι]
    (B : Module.Basis ι ℤ G) (hB : LinearIndependent ℝ (R.vector ∘ B)) :
    Module.finrank ℝ E = Module.finrank ℤ G
```

## Depends on

- [Crystals, cells and sites](basic.md)

## Sources

- [Physlib/CondensedMatter/Crystal/Embedding.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Embedding.lean)
