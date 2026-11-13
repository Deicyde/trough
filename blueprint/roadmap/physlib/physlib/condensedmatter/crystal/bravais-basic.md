---
declaration: module
origin: cited
lean: Physlib.CondensedMatter.Crystal.bravais, Physlib.CondensedMatter.Crystal.Embedding.ofVectors, Physlib.CondensedMatter.Crystal.Embedding.position_ofVectors, Physlib.CondensedMatter.Crystal.Embedding.isSpaceFilling_ofVectors_iff, Physlib.CondensedMatter.Crystal.Embedding.position_ofVectors_injective, Physlib.CondensedMatter.Crystal.Embedding.finrank_eq_of_ofVectors
statement: formalized
proof: formalized
---

# Bravais lattices

The module `Physlib.CondensedMatter.Crystal.Bravais.Basic`, [Physlib/CondensedMatter/Crystal/Bravais/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Bravais/Basic.lean): 6 declarations, 6 with a docstring.

> A Bravais lattice with one site per cell, repeated by `d` independent translations, and its
> embedding given by `d` primitive vectors.

## i. Overview

> A Bravais lattice of dimension `d` is the crystal with translation group `ℤᵈ` and a unit cell with
> a single site. Its embedding in a normed space `E` is fixed by the `d` primitive vectors, one for
> each generator of `ℤᵈ`: the cell `n` goes to the integer combination of these vectors with
> coefficients `n j`, and the single site sits at the origin of its cell. The different lattice types
> differ only in these vectors, so the general facts are proved here once.

## ii. Key results

> - `Crystal.bravais` : the crystal with translation group `ℤᵈ` and one site per cell.
> - `Crystal.Embedding.ofVectors` : the embedding of `Crystal.bravais d` given by `d` primitive
>   vectors.
> - `Crystal.Embedding.position_ofVectors` : the position of a site is the integer combination of
>   the primitive vectors given by its cell.
> - `Crystal.Embedding.isSpaceFilling_ofVectors_iff` : the embedding is space filling exactly when the
>   primitive vectors span the space.
> - `Crystal.Embedding.position_ofVectors_injective` : linearly independent primitive vectors give
>   distinct positions to distinct sites.
> - `Crystal.Embedding.finrank_eq_of_ofVectors` : a space-filling embedding with linearly
>   independent primitive vectors lives in a space of dimension `d`.

## iv. References

> * None.

## A. The crystal

**`Physlib.CondensedMatter.Crystal.bravais`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Bravais/Basic.lean#L58).

> The Bravais lattice of dimension `d`: the translation group is `ℤᵈ` and the unit cell has a
> single site.

```lean
def bravais (d : ℕ) : Crystal (Fin d → ℤ)
```

## B. The embedding

**`Physlib.CondensedMatter.Crystal.Embedding.ofVectors`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Bravais/Basic.lean#L67).

> The embedding of the Bravais lattice of dimension `d` given by `d` primitive vectors.

```lean
def ofVectors (v : Fin d → E) : Embedding (bravais d) E
```

**`Physlib.CondensedMatter.Crystal.Embedding.position_ofVectors`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Bravais/Basic.lean#L76).

> The position of a site is the integer combination of the primitive vectors given by its
> cell.

```lean
lemma position_ofVectors (v : Fin d → E) (x : (bravais d).Site) :
    (ofVectors v).position x = ∑ j, x.cell j • v j
```

## C. Spanning and independence

**`Physlib.CondensedMatter.Crystal.Embedding.isSpaceFilling_ofVectors_iff`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Bravais/Basic.lean#L86).

> The embedding of a Bravais lattice is space filling exactly when the primitive vectors span
> the space.

```lean
lemma isSpaceFilling_ofVectors_iff (v : Fin d → E) :
    (ofVectors v).IsSpaceFilling ↔ Submodule.span ℝ (Set.range v) = ⊤
```

**`Physlib.CondensedMatter.Crystal.Embedding.position_ofVectors_injective`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Bravais/Basic.lean#L96).

> Linearly independent primitive vectors give distinct positions to distinct sites.

```lean
lemma position_ofVectors_injective {v : Fin d → E} (hv : LinearIndependent ℝ v) :
    Function.Injective (ofVectors v).position
```

**`Physlib.CondensedMatter.Crystal.Embedding.finrank_eq_of_ofVectors`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Bravais/Basic.lean#L110).

> A space-filling embedding of a Bravais lattice with linearly independent primitive vectors
> lives in a space of dimension `d`.

```lean
lemma finrank_eq_of_ofVectors {v : Fin d → E} (hv : LinearIndependent ℝ v)
    (h : (ofVectors v).IsSpaceFilling) : Module.finrank ℝ E = d
```

## Depends on

- [A crystal in space](embedding.md)

## Sources

- [Physlib/CondensedMatter/Crystal/Bravais/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/CondensedMatter/Crystal/Bravais/Basic.lean)
