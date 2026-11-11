---
declaration: theorem
origin: cited
lean: Matrix.re_det_gram_le_prod_norm_sq, Matrix.det_gram_le_prod_norm_sq
statement: formalized
proof: formalized
---

# Hadamard's inequality for Gram determinants, for the real part

the real part of the Gram
determinant of a finite family is at most the product of the squared norms of its vectors.

```lean
Matrix.re_det_gram_le_prod_norm_sq.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2} {ι : Type u_3}
  [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [Fintype ι] [DecidableEq ι]
  (v : ι → E) : RCLike.re (Matrix.gram 𝕜 v).det ≤ ∏ i, ‖v i‖ ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Informally uses

- [Hadamard's inequality](hadamards-inequality.md)

## Lean

Formalized in Tau Ceti as [`Matrix.re_det_gram_le_prod_norm_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Gram/Hadamard.html#Matrix.re_det_gram_le_prod_norm_sq).

## Other forms

**Hadamard's inequality for Gram determinants.** Formalized in Tau Ceti as [`Matrix.det_gram_le_prod_norm_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Gram/Hadamard.html#Matrix.det_gram_le_prod_norm_sq).

```lean
Matrix.det_gram_le_prod_norm_sq.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2} {ι : Type u_3}
  [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [Fintype ι] [DecidableEq ι]
  (v : ι → E) : (Matrix.gram 𝕜 v).det ≤ ∏ i, ↑‖v i‖ ^ 2
```

## Sources

- [Tau Ceti documentation: `Matrix.re_det_gram_le_prod_norm_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Gram/Hadamard.html#Matrix.re_det_gram_le_prod_norm_sq)
- [Source of `Matrix.re_det_gram_le_prod_norm_sq` in TauCeti/Analysis/InnerProductSpace/Gram/Hadamard.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/Gram/Hadamard.lean#L137)
- [Tau Ceti roadmap status: Successive minima and Minkowski's theorems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SuccessiveMinima/STATUS.md)
