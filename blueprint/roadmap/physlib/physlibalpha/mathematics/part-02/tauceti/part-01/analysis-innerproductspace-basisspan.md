---
declaration: module
origin: cited
lean: OrthonormalBasis.spanIndices, OrthonormalBasis.spanIndices_eq_span, OrthonormalBasis.spanIndices_mono, OrthonormalBasis.mem_spanIndices_of_mem, OrthonormalBasis.repr_eq_zero_of_mem_spanIndices, OrthonormalBasis.mem_spanIndices_iff, OrthonormalBasis.finrank_spanIndices, OrthonormalBasis.finrank_spanIndices_set
statement: formalized
proof: formalized
---

# Spans of orthonormal subfamilies

The module `PhyslibAlpha.Mathematics.TauCeti.Analysis.InnerProductSpace.BasisSpan`, [PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/BasisSpan.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/BasisSpan.lean): 9 declarations, 9 with a docstring.

> For a finite-index orthonormal basis and a set of indices, `spanIndices` is the subspace spanned by
> the corresponding basis vectors.

## i. Overview

> For a finite-index orthonormal basis and a set of indices, `spanIndices` is the
> subspace spanned by the corresponding basis vectors.

## ii. Key results

> * `OrthonormalBasis.spanIndices_eq_span`: the explicit span characterization.
> * `OrthonormalBasis.spanIndices_mono`: monotonicity under index-set inclusion.
> * `OrthonormalBasis.mem_spanIndices_of_mem`: selected basis vectors belong to the span.
> * `OrthonormalBasis.mem_spanIndices_iff`: membership means coordinates vanish
>   outside the selected indices.
> * `OrthonormalBasis.finrank_spanIndices`: the dimension of a selected finite span.
> * `OrthonormalBasis.finrank_spanIndices_set`: dimension as set cardinality.
> * `OrthonormalBasis.orthogonal_spanIndices`: orthogonal complement by index complement.

## iv. References

> Source: Adapted from `ForTauCeti/Analysis/InnerProductSpace/BasisSpan.lean` in the
> [AIQ-Kitware DKPS formalization](https://github.com/AIQ-Kitware/aiq-dkps-formalization)
> (Kitware, Inc.; Apache-2.0). The selected-span construction originates in the
> Courant--Fischer development.

## A. Development

**`OrthonormalBasis.spanIndices`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/BasisSpan.lean#L58).

> The subspace spanned by the orthonormal basis vectors `b i` for indices
> `i ∈ s`.

```lean
noncomputable def spanIndices (b : OrthonormalBasis ι 𝕜 E) (s : Set ι) :
    Submodule 𝕜 E
```

**`OrthonormalBasis.spanIndices_eq_span`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/BasisSpan.lean#L64).

> The selected subspace is the span of its basis vectors.
> Use this identity to apply `Submodule.span`'s induction or universal property.

```lean
lemma spanIndices_eq_span (b : OrthonormalBasis ι 𝕜 E) (s : Set ι) :
    b.spanIndices s = Submodule.span 𝕜 (b '' s)
```

**`OrthonormalBasis.spanIndices_mono`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/BasisSpan.lean#L68).

> Selecting more indices spans more.

```lean
lemma spanIndices_mono (b : OrthonormalBasis ι 𝕜 E) {s t : Set ι} (h : s ⊆ t) :
    b.spanIndices s ≤ b.spanIndices t
```

**`OrthonormalBasis.mem_spanIndices_of_mem`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/BasisSpan.lean#L74).

> A selected basis vector lies in the span of its index set.

```lean
lemma mem_spanIndices_of_mem (b : OrthonormalBasis ι 𝕜 E) {s : Set ι} {i : ι}
    (hi : i ∈ s) : b i ∈ b.spanIndices s
```

**`OrthonormalBasis.repr_eq_zero_of_mem_spanIndices`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/BasisSpan.lean#L81).

> A vector in the span of a selected subfamily has zero coordinate at any
> index outside the selection.

```lean
lemma repr_eq_zero_of_mem_spanIndices (b : OrthonormalBasis ι 𝕜 E)
    {s : Set ι} {x : E} (hx : x ∈ b.spanIndices s) {i : ι} (hi : i ∉ s) :
    b.repr x i = 0
```

**`OrthonormalBasis.mem_spanIndices_iff`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/BasisSpan.lean#L101).

> Membership in the span of a selected subfamily is exactly the vanishing of
> the coordinates outside the selection.

```lean
lemma mem_spanIndices_iff (b : OrthonormalBasis ι 𝕜 E)
    {s : Set ι} {x : E} :
    x ∈ b.spanIndices s ↔ ∀ i ∉ s, b.repr x i = 0
```

**`OrthonormalBasis.finrank_spanIndices`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/BasisSpan.lean#L115).

> The span of a selected subfamily has dimension the number of selected
> indices.

```lean
lemma finrank_spanIndices (b : OrthonormalBasis ι 𝕜 E) (s : Finset ι) :
    finrank 𝕜 (b.spanIndices ↑s) = s.card
```

**`OrthonormalBasis.finrank_spanIndices_set`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/BasisSpan.lean#L126).

> The span of a selected set of basis vectors has dimension equal to the
> number of selected indices.

```lean
lemma finrank_spanIndices_set (b : OrthonormalBasis ι 𝕜 E) (s : Set ι) :
    finrank 𝕜 (b.spanIndices s) = s.ncard
```

**`OrthonormalBasis.orthogonal_spanIndices`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/BasisSpan.lean#L134).

> The orthogonal complement of the span of a selected subfamily is the span
> of the complementary subfamily.

```lean
lemma orthogonal_spanIndices (b : OrthonormalBasis ι 𝕜 E) (s : Set ι) :
    (b.spanIndices s)ᗮ = b.spanIndices sᶜ
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/BasisSpan.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/BasisSpan.lean)
