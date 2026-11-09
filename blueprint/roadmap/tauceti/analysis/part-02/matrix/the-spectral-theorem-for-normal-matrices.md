---
declaration: theorem
origin: cited
lean: Matrix.exists_mem_unitaryGroup_star_mul_mul_eq_diagonal
statement: formalized
proof: formalized
---

# The spectral theorem for normal matrices

A normal complex matrix is unitarily
diagonalizable: there is a unitary matrix `U` with `star U * A * U` diagonal.

```lean
Matrix.exists_mem_unitaryGroup_star_mul_mul_eq_diagonal.{u_1} {n : Type u_1} [Fintype n]
  [DecidableEq n] (A : Matrix n n ℂ) [IsStarNormal A] :
  ∃ U ∈ Matrix.unitaryGroup n ℂ, ∃ d, star U * A * U = Matrix.diagonal d
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.exists_mem_unitaryGroup_star_mul_mul_eq_diagonal`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/Normal.html#Matrix.exists_mem_unitaryGroup_star_mul_mul_eq_diagonal).

## Sources

- [Tau Ceti documentation: `Matrix.exists_mem_unitaryGroup_star_mul_mul_eq_diagonal`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/Normal.html#Matrix.exists_mem_unitaryGroup_star_mul_mul_eq_diagonal)
- [Source of `Matrix.exists_mem_unitaryGroup_star_mul_mul_eq_diagonal` in TauCeti/Analysis/Matrix/Normal.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Matrix/Normal.lean#L86)
