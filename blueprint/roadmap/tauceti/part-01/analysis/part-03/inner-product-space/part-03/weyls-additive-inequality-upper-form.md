---
declaration: theorem
origin: cited
lean: LinearMap.IsSymmetric.eigenvalues_add_le, LinearMap.IsSymmetric.le_eigenvalues_add
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

## Sources

- [Tau Ceti documentation: `LinearMap.IsSymmetric.eigenvalues_add_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/CourantFischer.html#LinearMap.IsSymmetric.eigenvalues_add_le)
- [Source of `LinearMap.IsSymmetric.eigenvalues_add_le` in TauCeti/Analysis/InnerProductSpace/CourantFischer.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L519)
