---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.weightSpace, PhyslibAlpha.Sl2.e_mapsTo_weightSpace, PhyslibAlpha.Sl2.f_mapsTo_weightSpace, PhyslibAlpha.Sl2.repr_apply_diag, PhyslibAlpha.Sl2.string_coord_eq_zero, PhyslibAlpha.Sl2.weightSpace_eq_bot_of_ne, PhyslibAlpha.Sl2.weightSpace_finrank_le_one_of_eq, PhyslibAlpha.Sl2.weightSpace_finrank_le_one
statement: formalized
proof: formalized
---

# Weight spaces for sl₂ modules

The module `PhyslibAlpha.Mathematics.RepresentationTheory.Sl2.Weights`, [PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Weights.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Weights.lean): 11 declarations, 11 with a docstring.

> Restates the rank-one weight-space results using endomorphism eigenspaces.

## i. Overview

> The eigenspaces of the Cartan operator are weight spaces. The raising and lowering
> operators map them to neighboring weights. In a finite-dimensional irreducible module the
> weights in a primitive string occur with multiplicity one, and the highest weight is unique.

## ii. Key results

> - `weightSpace` defines the Cartan eigenspace.
> - `e_mapsTo_weightSpace` and `f_mapsTo_weightSpace` shift weights by two.
> - `weightSpace_finrank_le_one` and `weightSpace_highest_unique` express multiplicity one
>   and uniqueness of the highest weight.

## iv. References

> - Mathlib, `Mathlib.Algebra.Lie.Sl2`.

## A. Weight spaces

**`PhyslibAlpha.Sl2.weightSpace`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Weights.lean#L49).

> The eigenspace of the Cartan operator `h` with eigenvalue `n`.

```lean
def weightSpace (_t : IsSl2Triple h e f) (n : K) : Submodule K M
```

**`PhyslibAlpha.Sl2.e_mapsTo_weightSpace`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Weights.lean#L53).

> The raising operator maps weight `n` into weight `n + 2`.

```lean
lemma e_mapsTo_weightSpace (t : IsSl2Triple h e f) (n : K) :
    ∀ v ∈ weightSpace (M := M) t n, LieModule.toEnd K L M e v ∈ weightSpace t (n + 2)
```

**`PhyslibAlpha.Sl2.f_mapsTo_weightSpace`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Weights.lean#L61).

> `f` lowers the weight by `2`. Dual to `e_mapsTo_weightSpace`.

```lean
lemma f_mapsTo_weightSpace (t : IsSl2Triple h e f) (n : K) :
    ∀ v ∈ weightSpace (M := M) t n, LieModule.toEnd K L M f v ∈ weightSpace t (n - 2)
```

**`PhyslibAlpha.Sl2.repr_apply_diag`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Weights.lean#L70).

> If a basis diagonalises `T`, then `T` multiplies the `i`-th coordinate by `μ i`.

```lean
lemma repr_apply_diag {ι : Type*} (b : Module.Basis ι K M) (T : Module.End K M)
    (μ : ι → K) (hT : ∀ j, T (b j) = μ j • b j) (i : ι) (w : M) :
    b.repr (T w) i = μ i * b.repr w i
```

**`PhyslibAlpha.Sl2.string_coord_eq_zero`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Weights.lean#L88).

> A weight vector has vanishing string coordinates at every other weight.

```lean
lemma string_coord_eq_zero {n : K} {w : M} (hw : w ∈ weightSpace (M := M) t n)
    (i : Fin (N + 1)) (hi : (N : K) - 2 * (i : ℕ) ≠ n) : (stringBasis P).repr w i = 0
```

**`PhyslibAlpha.Sl2.weightSpace_eq_bot_of_ne`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Weights.lean#L100).

> The weight space is trivial at a value that is not a weight of the string.

```lean
lemma weightSpace_eq_bot_of_ne {n : K} (hn : ∀ i : Fin (N + 1), (N : K) - 2 * (i : ℕ) ≠ n) :
    weightSpace (M := M) t n = ⊥
```

**`PhyslibAlpha.Sl2.weightSpace_finrank_le_one_of_eq`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Weights.lean#L108).

> The weight space of a weight of the string has dimension at most one.

```lean
lemma weightSpace_finrank_le_one_of_eq {n : K} (i₀ : Fin (N + 1))
    (hi₀ : (N : K) - 2 * (i₀ : ℕ) = n) : Module.finrank K (weightSpace (M := M) t n) ≤ 1
```

**`PhyslibAlpha.Sl2.weightSpace_finrank_le_one`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Weights.lean#L125).

> Every Cartan weight space of a finite-dimensional irreducible `sl₂` module has
> dimension at most one. The lowering-string basis has pairwise distinct weights.

```lean
lemma weightSpace_finrank_le_one [IsAlgClosed K] [CharZero K] [FiniteDimensional K M]
    (t : IsSl2Triple h e f) [LieModule.IsIrreducible K ↥(t.toLieSubalgebra (R := K)) M]
    (n : K) : Module.finrank K (weightSpace (M := M) t n) ≤ 1
```

**`PhyslibAlpha.Sl2.lie_e_eq_zero_of_top_weight`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Weights.lean#L139).

> A vector at a weight with empty weight space two steps above is killed by `e`.

```lean
lemma lie_e_eq_zero_of_top_weight {n : K} {v : M} (t : IsSl2Triple h e f)
    (hv : v ∈ weightSpace (M := M) t n) (hn : weightSpace (M := M) t (n + 2) = ⊥) :
    ⁅e, v⁆ = 0
```

**`PhyslibAlpha.Sl2.finrank_of_top_weight`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Weights.lean#L147).

> A top weight `p` of a finite-dimensional irreducible module fixes the dimension.

```lean
lemma finrank_of_top_weight [CharZero K] [FiniteDimensional K M]
    (t : IsSl2Triple h e f) [LieModule.IsIrreducible K ↥(t.toLieSubalgebra (R := K)) M]
    {p : ℕ} (hp : weightSpace (M := M) t (p : K) ≠ ⊥)
    (hp' : weightSpace (M := M) t ((p : K) + 2) = ⊥) : Module.finrank K M = p + 1
```

**`PhyslibAlpha.Sl2.weightSpace_highest_unique`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Weights.lean#L159).

> A nonzero weight space with no weight space two steps above it determines the
> highest weight of a finite-dimensional irreducible module.

```lean
lemma weightSpace_highest_unique [CharZero K] [FiniteDimensional K M]
    (t : IsSl2Triple h e f) [LieModule.IsIrreducible K ↥(t.toLieSubalgebra (R := K)) M]
    {m n : ℕ} (hm : weightSpace (M := M) t (m : K) ≠ ⊥)
    (hm' : weightSpace (M := M) t ((m : K) + 2) = ⊥)
    (hn : weightSpace (M := M) t (n : K) ≠ ⊥)
    (hn' : weightSpace (M := M) t ((n : K) + 2) = ⊥) : m = n
```

## Depends on

- [Classification of irreducible sl₂ modules](sl2-classification.md)

## Sources

- [PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Weights.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Weights.lean)
