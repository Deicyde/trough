---
declaration: theorem
origin: cited
lean: Matrix.IsHermitian.abs_eigenvalues₀_sub_le_norm
statement: formalized
proof: formalized
---

# Weyl's perturbation bound for ordered eigenvalues of Hermitian matrices

corresponding
eigenvalues differ by at most the Euclidean operator norm of the matrix difference.

```lean
Matrix.IsHermitian.abs_eigenvalues₀_sub_le_norm.{u_1, u_2} {𝕜 : Type u_1} {ι : Type u_2} [RCLike 𝕜]
  [Fintype ι] [DecidableEq ι] {A B : Matrix ι ι 𝕜} (hA : A.IsHermitian) (hB : B.IsHermitian)
  (i : Fin (Fintype.card ι)) : |hA.eigenvalues₀ i - hB.eigenvalues₀ i| ≤ ‖A - B‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Weyl's inequality](../inner-product-space/part-03/weyls-inequality.md)

## Lean

Formalized in Tau Ceti as [`Matrix.IsHermitian.abs_eigenvalues₀_sub_le_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/Eigenvalues/Basic.html#Matrix.IsHermitian.abs_eigenvalues%E2%82%80_sub_le_norm).

## Sources

- [Tau Ceti documentation: `Matrix.IsHermitian.abs_eigenvalues₀_sub_le_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/Eigenvalues/Basic.html#Matrix.IsHermitian.abs_eigenvalues%E2%82%80_sub_le_norm)
- [Source of `Matrix.IsHermitian.abs_eigenvalues₀_sub_le_norm` in TauCeti/Analysis/Matrix/Eigenvalues/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Matrix/Eigenvalues/Basic.lean#L102)
