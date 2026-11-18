---
declaration: module
origin: cited
lean: minkowskiMatrixZ, minkowskiMatrixZ.as_diagonal, minkowskiMatrixZ.inl_0_inl_0, minkowskiMatrixZ.inr_i_inr_i, minkowskiMatrixZ.off_diag_zero, minkowskiMatrixZ.comm, minkowskiMatrixZ.cast_apply
statement: formalized
proof: formalized
---

# The Minkowski matrix over the integers

The module `PhyslibAlpha.Relativity.MinkowskiMatrix`, [PhyslibAlpha/Relativity/MinkowskiMatrix.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/MinkowskiMatrix.lean): 7 declarations, 7 with a docstring.

> The Minkowski matrix with integer entries, so that the kernel can evaluate it.

## i. Overview

> The entries of `minkowskiMatrix` are integers, but it is a matrix over `ℝ`, and the kernel
> cannot evaluate arithmetic in `ℝ`. Statements which a decision procedure has to evaluate are
> therefore stated with `minkowskiMatrixZ`, the same diagonal matrix `diag(1, -1, …, -1)` taken
> over `ℤ`. The bridge back is `minkowskiMatrixZ.cast_apply`, which casts an entry to the
> corresponding entry of `minkowskiMatrix`; the remaining lemmas are the entry values and the
> symmetry, matching the `minkowskiMatrix` API.

## ii. Key results

> - `minkowskiMatrixZ` : the Minkowski matrix over `ℤ`.
> - `minkowskiMatrixZ.cast_apply` : its cast to `ℝ` is `minkowskiMatrix`, entry by entry.
> - `minkowskiMatrixZ.inl_0_inl_0`, `minkowskiMatrixZ.inr_i_inr_i`,
>   `minkowskiMatrixZ.off_diag_zero` : the entries.
> - `minkowskiMatrixZ.comm` : it is symmetric.

## iv. References

> The real Minkowski matrix and its API are in `Physlib.Relativity.MinkowskiMatrix`.

## A. The Minkowski matrix over the integers

**`minkowskiMatrixZ`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/MinkowskiMatrix.lean#L53).

> The Minkowski matrix over the integers, `diag(1, -1, -1, ...)` in `ℤ`. Its cast to `ℝ` is
> `minkowskiMatrix`, by `minkowskiMatrixZ.cast_apply`.

```lean
def minkowskiMatrixZ {d : ℕ} : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℤ
```

**`minkowskiMatrixZ.as_diagonal`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/MinkowskiMatrix.lean#L61).

> The integer Minkowski matrix as a diagonal matrix.

```lean
lemma as_diagonal : @minkowskiMatrixZ d = diagonal (Sum.elim 1 (-1))
```

**`minkowskiMatrixZ.inl_0_inl_0`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/MinkowskiMatrix.lean#L65).

> The time-time component of the integer Minkowski matrix is `1`.

```lean
lemma inl_0_inl_0 : @minkowskiMatrixZ d (Sum.inl 0) (Sum.inl 0) = 1
```

**`minkowskiMatrixZ.inr_i_inr_i`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/MinkowskiMatrix.lean#L70).

> The space diagonal components of the integer Minkowski matrix are `-1`.

```lean
lemma inr_i_inr_i (i : Fin d) : @minkowskiMatrixZ d (Sum.inr i) (Sum.inr i) = -1
```

**`minkowskiMatrixZ.off_diag_zero`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/MinkowskiMatrix.lean#L75).

> The off-diagonal components of the integer Minkowski matrix vanish.

```lean
lemma off_diag_zero {μ ν : Fin 1 ⊕ Fin d} (h : μ ≠ ν) : @minkowskiMatrixZ d μ ν = 0
```

**`minkowskiMatrixZ.comm`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/MinkowskiMatrix.lean#L79).

> The integer Minkowski matrix is symmetric, being diagonal.

```lean
lemma comm (μ ν : Fin 1 ⊕ Fin d) : @minkowskiMatrixZ d μ ν = minkowskiMatrixZ ν μ
```

**`minkowskiMatrixZ.cast_apply`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/MinkowskiMatrix.lean#L85).

> The integer Minkowski matrix casts to the Minkowski matrix, entry by entry.

```lean
lemma cast_apply (μ ν : Fin 1 ⊕ Fin d) :
    ((minkowskiMatrixZ μ ν : ℤ) : ℝ) = minkowskiMatrix μ ν
```

## Depends on

- [The Minkowski matrix](../../physlib/relativity/minkowskimatrix.md)

## Sources

- [PhyslibAlpha/Relativity/MinkowskiMatrix.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/MinkowskiMatrix.lean)
