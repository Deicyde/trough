---
declaration: module
origin: cited
lean: Matrix.PosSemidef.normSq_le, Matrix.PosSemidef.eq_zero_of_apply_self_eq_zero_left, Matrix.PosSemidef.eq_zero_of_apply_self_eq_zero_right, Matrix.PosSemidef.norm_le_one_of_apply_self_eq_one, Matrix.PosSemidef.norm_le_of_norm_apply_self_le, TauCeti.sub_nonneg_of_posSemidef_hankel
statement: formalized
proof: formalized
---

# Analytic bounds for positive-semidefinite matrices

The module `PhyslibAlpha.Mathematics.TauCeti.Analysis.Matrix.PosSemidef`, [PhyslibAlpha/Mathematics/TauCeti/Analysis/Matrix/PosSemidef.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Matrix/PosSemidef.lean): 6 declarations, 6 with a docstring; 2 private, not shown.

> This file supplements the foundational API in `TauCeti.LinearAlgebra.Matrix.PosSemidef` with scalar
> Cauchy--Schwarz and vanishing bounds for `RCLike`-valued positive-semidefinite matrices, together
> with the resulting estimate for *Hankel* matrices: a sequence bounded above whose Hankel matrix `(m,
> n) ↦ a (m + n)` is positive semidefinite cannot increase at the first step.

## i. Overview

> This file supplements the foundational API in `TauCeti.LinearAlgebra.Matrix.PosSemidef` with
> scalar Cauchy--Schwarz and vanishing bounds for `RCLike`-valued positive-semidefinite matrices,
> together with the resulting estimate for *Hankel* matrices: a sequence bounded above whose Hankel
> matrix `(m, n) ↦ a (m + n)` is positive semidefinite cannot increase at the first step.
>
> The results apply in particular to positive-definite kernels, represented directly as matrices,
> but do not depend on Tau Ceti's positive-definite-function theory.
>
> They supply the matrix prerequisites for Part C of the `OneParameterSemigroups` roadmap, including
> the positive-definite-function/kernel correspondence and the GNS/Kolmogorov decomposition. No
> Mathlib code is vendored.

## ii. Key results

> * `Matrix.PosSemidef.normSq_le`: scalar Cauchy--Schwarz.
> * `Matrix.PosSemidef.eq_zero_of_apply_self_eq_zero_left` and
>   `Matrix.PosSemidef.eq_zero_of_apply_self_eq_zero_right`: zero-diagonal vanishing.
> * `Matrix.PosSemidef.norm_le_one_of_apply_self_eq_one`: the normalized scalar bound.
> * `Matrix.PosSemidef.norm_le_of_norm_apply_self_le`: the diagonal bounds every entry.
> * `TauCeti.sub_nonneg_of_posSemidef_hankel`: a positive-semidefinite Hankel sequence bounded above
>   does not increase at the first step.

## iv. References

> * C. Berg, J. P. R. Christensen, P. Ressel, *Harmonic Analysis on Semigroups* (GTM 100, 1984),
>   Chapter 3.

## A. Development

**`Matrix.PosSemidef.normSq_le`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Matrix/PosSemidef.lean#L82).

> Scalar Cauchy--Schwarz for an `RCLike`-valued positive-semidefinite matrix.

```lean
lemma normSq_le {K : α → α → 𝕜}
    (hK : Matrix.PosSemidef K) (a b : α) :
    RCLike.normSq (K a b) ≤ RCLike.re (K a a) * RCLike.re (K b b)
```

**`Matrix.PosSemidef.eq_zero_of_apply_self_eq_zero_left`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Matrix/PosSemidef.lean#L102).

> A zero diagonal entry forces the corresponding row entry to vanish.

```lean
lemma eq_zero_of_apply_self_eq_zero_left {K : α → α → 𝕜}
    (hK : Matrix.PosSemidef K) {a b : α} (ha : K a a = 0) : K a b = 0
```

**`Matrix.PosSemidef.eq_zero_of_apply_self_eq_zero_right`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Matrix/PosSemidef.lean#L111).

> A zero diagonal entry forces the corresponding column entry to vanish.

```lean
lemma eq_zero_of_apply_self_eq_zero_right {K : α → α → 𝕜}
    (hK : Matrix.PosSemidef K) {a b : α} (hb : K b b = 0) : K a b = 0
```

**`Matrix.PosSemidef.norm_le_one_of_apply_self_eq_one`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Matrix/PosSemidef.lean#L122).

> If two diagonal entries are `1`, then the corresponding off-diagonal entry has norm at most
> `1`.

```lean
lemma norm_le_one_of_apply_self_eq_one {K : α → α → 𝕜}
    (hK : Matrix.PosSemidef K) {a b : α} (ha : K a a = 1) (hb : K b b = 1) :
    ‖K a b‖ ≤ 1
```

**`Matrix.PosSemidef.norm_le_of_norm_apply_self_le`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Matrix/PosSemidef.lean#L130).

> **The diagonal of a positive-semidefinite matrix bounds all of its entries.** Cauchy--Schwarz
> turns a uniform bound on the (nonnegative real) diagonal entries into the same bound everywhere.

```lean
lemma norm_le_of_norm_apply_self_le {K : α → α → 𝕜} {C : ℝ}
    (hK : Matrix.PosSemidef K) (hdiag : ∀ i, ‖K i i‖ ≤ C) (a b : α) : ‖K a b‖ ≤ C
```

## B. Bounded positive-semidefinite Hankel sequences

**`TauCeti.sub_nonneg_of_posSemidef_hankel`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Matrix/PosSemidef.lean#L197).

> **A positive-semidefinite Hankel sequence bounded above does not increase at the first step.**
> If `(m, n) ↦ a (m + n)` is positive semidefinite and the real parts of `a` are bounded above by `D`
> — the entries are automatically real — then `a 1 ≤ a 0` in the `RCLike` order. Cauchy--Schwarz
> alone gives `a n ^ 2 ≤ a 0 * a (2 n)`, and the bound rules out a ratio `a 1 / a 0` greater
> than `1`.

```lean
lemma sub_nonneg_of_posSemidef_hankel {a : ℕ → 𝕜} {D : ℝ}
    (ha : Matrix.PosSemidef fun m n : ℕ => a (m + n)) (hbd : ∀ n, RCLike.re (a n) ≤ D) :
    0 ≤ a 0 - a 1
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Analysis/Matrix/PosSemidef.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Matrix/PosSemidef.lean)
