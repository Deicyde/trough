---
declaration: theorem
origin: cited
lean: LinearMap.IsSymmetric.eigenvalues_add_le, LinearMap.IsSymmetric.le_eigenvalues_add, Matrix.IsHermitian.eigenvalues₀_add_le, Matrix.IsHermitian.le_eigenvalues₀_add
statement: formalized
proof: formalized
---

# Weyl's additive inequality, upper form

for symmetric operators `T` and `S` and indices
with `i + j ≤ k`, the decreasingly sorted eigenvalues satisfy `λₖ(T + S) ≤ λᵢ(T) + λⱼ(S)`.
Indices start at `0`, so for `k = i + j` this is the classical
`λ_{i+j-1}(T + S) ≤ λᵢ(T) + λⱼ(S)` in one-based indexing.

Horn & Johnson, *Matrix Analysis* 2nd ed., Theorem 4.3.1; Bhatia, *Matrix Analysis*,
Theorem III.2.1.

```lean
LinearMap.IsSymmetric.eigenvalues_add_le.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] {n : ℕ} [FiniteDimensional 𝕜 E] {T S : E →ₗ[𝕜] E}
  (hT : T.IsSymmetric) (hS : S.IsSymmetric) (hn : Module.finrank 𝕜 E = n) {i j k : Fin n}
  (hk : ↑i + ↑j ≤ ↑k) : ⋯.eigenvalues hn k ≤ hT.eigenvalues hn i + hS.eigenvalues hn j
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.IsSymmetric.eigenvalues_add_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/CourantFischer.html#LinearMap.IsSymmetric.eigenvalues_add_le).

## Other forms

**Weyl's additive inequality, lower form.** Formalized in Tau Ceti as [`LinearMap.IsSymmetric.le_eigenvalues_add`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/CourantFischer.html#LinearMap.IsSymmetric.le_eigenvalues_add).

```lean
LinearMap.IsSymmetric.le_eigenvalues_add.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] {n : ℕ} [FiniteDimensional 𝕜 E] {T S : E →ₗ[𝕜] E}
  (hT : T.IsSymmetric) (hS : S.IsSymmetric) (hn : Module.finrank 𝕜 E = n) {i j k : Fin n}
  (hk : ↑k + n ≤ ↑i + ↑j + 1) : hT.eigenvalues hn i + hS.eigenvalues hn j ≤ ⋯.eigenvalues hn k
```

**Weyl's additive inequality for Hermitian matrices, upper form.** Formalized in Tau Ceti as [`Matrix.IsHermitian.eigenvalues₀_add_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/Eigenvalues/Basic.html#Matrix.IsHermitian.eigenvalues%E2%82%80_add_le).

```lean
Matrix.IsHermitian.eigenvalues₀_add_le.{u_1, u_2} {𝕜 : Type u_1} {ι : Type u_2} [RCLike 𝕜]
  [Fintype ι] [DecidableEq ι] {A B : Matrix ι ι 𝕜} (hA : A.IsHermitian) (hB : B.IsHermitian)
  {i j k : Fin (Fintype.card ι)} (hk : ↑i + ↑j ≤ ↑k) :
  ⋯.eigenvalues₀ k ≤ hA.eigenvalues₀ i + hB.eigenvalues₀ j
```

**Weyl's additive inequality for Hermitian matrices, lower form.** Formalized in Tau Ceti as [`Matrix.IsHermitian.le_eigenvalues₀_add`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/Eigenvalues/Basic.html#Matrix.IsHermitian.le_eigenvalues%E2%82%80_add).

```lean
Matrix.IsHermitian.le_eigenvalues₀_add.{u_1, u_2} {𝕜 : Type u_1} {ι : Type u_2} [RCLike 𝕜]
  [Fintype ι] [DecidableEq ι] {A B : Matrix ι ι 𝕜} (hA : A.IsHermitian) (hB : B.IsHermitian)
  {i j k : Fin (Fintype.card ι)} (hk : ↑k + Fintype.card ι ≤ ↑i + ↑j + 1) :
  hA.eigenvalues₀ i + hB.eigenvalues₀ j ≤ ⋯.eigenvalues₀ k
```

## Sources

- [Tau Ceti documentation: `LinearMap.IsSymmetric.eigenvalues_add_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/CourantFischer.html#LinearMap.IsSymmetric.eigenvalues_add_le)
- [Source of `LinearMap.IsSymmetric.eigenvalues_add_le` in TauCeti/Analysis/InnerProductSpace/CourantFischer.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L530)
