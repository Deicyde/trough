---
declaration: theorem
origin: cited
lean: Matrix.sum_sq_singularValues_toEuclideanLin_sub_le_frobenius_norm_sub_sq
statement: formalized
proof: formalized
---

# The singular-value Hoffman–Wielandt inequality for same-shaped rectangular matrices

the squared distance between their ordered singular values, summed up to the smaller dimension,
is bounded by the squared Frobenius norm of their difference.

```lean
Matrix.sum_sq_singularValues_toEuclideanLin_sub_le_frobenius_norm_sub_sq.{u_3, u_4, u_5}
  {m : Type u_3} {n : Type u_4} [Fintype m] [Fintype n] [DecidableEq n] {𝕜 : Type u_5} [RCLike 𝕜]
  (A B : Matrix m n 𝕜) :
  ∑ i,
      ((Matrix.toEuclideanLin A).singularValues ↑i - (Matrix.toEuclideanLin B).singularValues ↑i) ^
        2 ≤
    ‖A - B‖ ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The singular-value Hoffman–Wielandt inequality](../inner-product-space/part-03/the-singular-value-hoffman-wielandt-inequality.md)

## Lean

Formalized in Tau Ceti as [`Matrix.sum_sq_singularValues_toEuclideanLin_sub_le_frobenius_norm_sub_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/HoffmanWielandt.html#Matrix.sum_sq_singularValues_toEuclideanLin_sub_le_frobenius_norm_sub_sq).

## Sources

- [Tau Ceti documentation: `Matrix.sum_sq_singularValues_toEuclideanLin_sub_le_frobenius_norm_sub_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/HoffmanWielandt.html#Matrix.sum_sq_singularValues_toEuclideanLin_sub_le_frobenius_norm_sub_sq)
- [Source of `Matrix.sum_sq_singularValues_toEuclideanLin_sub_le_frobenius_norm_sub_sq` in TauCeti/Analysis/Matrix/HoffmanWielandt.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Matrix/HoffmanWielandt.lean#L64)
