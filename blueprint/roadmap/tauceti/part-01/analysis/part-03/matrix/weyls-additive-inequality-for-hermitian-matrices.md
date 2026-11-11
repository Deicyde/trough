---
declaration: theorem
origin: cited
lean: Matrix.IsHermitian.eigenvalues₀_add_le, Matrix.IsHermitian.le_eigenvalues₀_add
statement: formalized
proof: formalized
---

# Weyl's additive inequality for Hermitian matrices, upper form

if `i + j ≤ k`, then
`λₖ(A + B) ≤ λᵢ(A) + λⱼ(B)` for the decreasing enumerations `eigenvalues₀`. For `k = i + j`
this is the classical `λ_{i+j-1}(A + B) ≤ λᵢ(A) + λⱼ(B)` in one-based indexing.

```lean
Matrix.IsHermitian.eigenvalues₀_add_le.{u_1, u_2} {𝕜 : Type u_1} {ι : Type u_2} [RCLike 𝕜]
  [Fintype ι] [DecidableEq ι] {A B : Matrix ι ι 𝕜} (hA : A.IsHermitian) (hB : B.IsHermitian)
  {i j k : Fin (Fintype.card ι)} (hk : ↑i + ↑j ≤ ↑k) :
  ⋯.eigenvalues₀ k ≤ hA.eigenvalues₀ i + hB.eigenvalues₀ j
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Weyl's additive inequality, upper form](../inner-product-space/part-03/weyls-additive-inequality-upper-form.md)

## Lean

Formalized in Tau Ceti as [`Matrix.IsHermitian.eigenvalues₀_add_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/Eigenvalues/Basic.html#Matrix.IsHermitian.eigenvalues%E2%82%80_add_le).

## Other forms

**Weyl's additive inequality for Hermitian matrices, lower form.** Formalized in Tau Ceti as [`Matrix.IsHermitian.le_eigenvalues₀_add`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/Eigenvalues/Basic.html#Matrix.IsHermitian.le_eigenvalues%E2%82%80_add).

```lean
Matrix.IsHermitian.le_eigenvalues₀_add.{u_1, u_2} {𝕜 : Type u_1} {ι : Type u_2} [RCLike 𝕜]
  [Fintype ι] [DecidableEq ι] {A B : Matrix ι ι 𝕜} (hA : A.IsHermitian) (hB : B.IsHermitian)
  {i j k : Fin (Fintype.card ι)} (hk : ↑k + Fintype.card ι ≤ ↑i + ↑j + 1) :
  hA.eigenvalues₀ i + hB.eigenvalues₀ j ≤ ⋯.eigenvalues₀ k
```

## Sources

- [Tau Ceti documentation: `Matrix.IsHermitian.eigenvalues₀_add_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/Eigenvalues/Basic.html#Matrix.IsHermitian.eigenvalues%E2%82%80_add_le)
- [Source of `Matrix.IsHermitian.eigenvalues₀_add_le` in TauCeti/Analysis/Matrix/Eigenvalues/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Matrix/Eigenvalues/Basic.lean#L204)
