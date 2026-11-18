---
declaration: module
origin: cited
lean: TauCeti.posSemidef_rankOne, TauCeti.posSemidef_const_one, TauCeti.posSemidef_const_of_nonneg, TauCeti.posSemidef_iff_finite_sum, TauCeti.posSemidef_schur_finset_prod, TauCeti.posSemidef_prod_union, Matrix.PosSemidef.hadamard_pow
statement: formalized
proof: formalized
---

# Positive-semidefinite matrix algebra

The module `PhyslibAlpha.Mathematics.TauCeti.LinearAlgebra.Matrix.PosSemidef`, [PhyslibAlpha/Mathematics/TauCeti/LinearAlgebra/Matrix/PosSemidef.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/LinearAlgebra/Matrix/PosSemidef.lean): 7 declarations, 7 with a docstring; 1 private, not shown.

> This file supplements Mathlib's `Matrix.PosSemidef` API for matrices indexed by arbitrary types.

## i. Overview

> This file supplements Mathlib's `Matrix.PosSemidef` API for matrices indexed by arbitrary types.
> It provides rank-one and constant matrices, finite Schur products, Schur powers,
> products of weights over unions of finite sets, and the quadratic-form characterization.
>
> The results apply in particular to positive-definite kernels, represented directly as matrices,
> but do not depend on Tau Ceti's positive-definite-function theory.

## ii. Key results

> * `TauCeti.posSemidef_rankOne`: rank-one positive-semidefinite matrices.
> * `TauCeti.posSemidef_const_one` and `TauCeti.posSemidef_const_of_nonneg`: constant matrices.
> * `TauCeti.posSemidef_iff_finite_sum`: the quadratic-form characterization.
> * `TauCeti.posSemidef_schur_finset_prod` and `Matrix.PosSemidef.hadamard_pow`: finite Schur
>   products and Schur powers.
> * `TauCeti.posSemidef_prod_union`: the matrix `(i, j) ↦ ∏_{a ∈ L i ∪ L j} w a` for weights in
>   `[0, 1]`.

## iv. References

> * C. Berg, J. P. R. Christensen, P. Ressel, *Harmonic Analysis on Semigroups* (GTM 100, 1984),
>   Chapter 3.

## A. Development

**`TauCeti.posSemidef_rankOne`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/LinearAlgebra/Matrix/PosSemidef.lean#L84).

> The rank-one matrix `(a, b) ↦ star (g a) · g b` is positive semidefinite for an arbitrary
> index type. Such matrices are elementary building blocks for positive-semidefinite matrices;
> taking `g ≡ 1` gives the constant matrix `1`.

```lean
lemma posSemidef_rankOne {R : Type u}
    [Ring R] [PartialOrder R] [StarRing R] [StarOrderedRing R] (g : α → R) :
    Matrix.PosSemidef (fun a b => star (g a) * g b)
```

**`TauCeti.posSemidef_const_one`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/LinearAlgebra/Matrix/PosSemidef.lean#L94).

> The constant matrix with value `1` is positive semidefinite.

```lean
lemma posSemidef_const_one {R : Type u}
    [Ring R] [PartialOrder R] [StarRing R] [StarOrderedRing R] :
    Matrix.PosSemidef (fun _ _ : α => (1 : R))
```

**`TauCeti.posSemidef_const_of_nonneg`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/LinearAlgebra/Matrix/PosSemidef.lean#L100).

> A nonnegative constant gives a positive-semidefinite constant matrix.

```lean
lemma posSemidef_const_of_nonneg {R : Type u}
    [Ring R] [PartialOrder R] [StarRing R] [StarOrderedRing R]
    {c : R} (hc : 0 ≤ c) : Matrix.PosSemidef (fun _ _ : α => c)
```

**`TauCeti.posSemidef_iff_finite_sum`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/LinearAlgebra/Matrix/PosSemidef.lean#L110).

> The quadratic-form characterization of an arbitrary-index positive-semidefinite matrix:
> conjugate symmetry and nonnegativity on every finite family, allowing repeated indices.

```lean
lemma posSemidef_iff_finite_sum {R : Type u} [Ring R] [PartialOrder R] [StarRing R]
    {K : α → α → R} :
    Matrix.PosSemidef K ↔
      (∀ a b, star (K a b) = K b a) ∧
        ∀ {ι : Type*} [Fintype ι] (v : ι → α) (x : ι → R),
          0 ≤ ∑ i, ∑ j, star (x i) * K (v i) (v j) * x j
```

**`TauCeti.posSemidef_schur_finset_prod`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/LinearAlgebra/Matrix/PosSemidef.lean#L147).

> Finite pointwise Schur products of positive-semidefinite matrices are positive semidefinite.

```lean
lemma posSemidef_schur_finset_prod {ι : Type w} {s : Finset ι}
    {K : ι → α → α → 𝕜} (hK : ∀ i ∈ s, Matrix.PosSemidef (K i)) :
    Matrix.PosSemidef (fun a b => ∏ i ∈ s, K i a b)
```

**`TauCeti.posSemidef_prod_union`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/LinearAlgebra/Matrix/PosSemidef.lean#L157).

> For weights `w` in `[0, 1]` and finite sets `L i`, the matrix
> `(i, j) ↦ ∏_{a ∈ L i ∪ L j} w a` is positive semidefinite.

```lean
lemma posSemidef_prod_union {ι : Type w} [DecidableEq α] (L : ι → Finset α)
    {w : α → ℝ} (hw₀ : ∀ a, 0 ≤ w a) (hw₁ : ∀ a, w a ≤ 1) :
    Matrix.PosSemidef (fun i j => ∏ a ∈ L i ∪ L j, w a)
```

**`Matrix.PosSemidef.hadamard_pow`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/LinearAlgebra/Matrix/PosSemidef.lean#L192).

> Schur powers of a positive-semidefinite matrix are positive semidefinite.

```lean
lemma Matrix.PosSemidef.hadamard_pow {α 𝕜 : Type*} [RCLike 𝕜] {K : α → α → 𝕜}
    (hK : Matrix.PosSemidef K) (n : ℕ) :
    Matrix.PosSemidef (fun a b => K a b ^ n)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/LinearAlgebra/Matrix/PosSemidef.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/LinearAlgebra/Matrix/PosSemidef.lean)
