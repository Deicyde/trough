---
declaration: theorem
origin: cited
lean: LinearMap.IsSymmetric.abs_eigenvalue_sub_eigenvalue_le, LinearMap.IsSymmetric.abs_eigenvalue_sub_eigenvalue_le_norm
statement: formalized
proof: formalized
---

# Weyl's inequality

**Weyl's inequality** for symmetric operators on a finite-dimensional inner
product space over `𝕜 = ℝ, ℂ`: the `k`-th (decreasingly sorted) eigenvalues of
`T` and `S` differ by at most the operator norm of `T − S`.

At `LinearMap` level there is no operator norm, so the bound is supplied as the
pointwise hypothesis `∀ x, ‖(T − S) x‖ ≤ ε * ‖x‖`; see
`LinearMap.IsSymmetric.abs_eigenvalue_sub_eigenvalue_le_norm` for the continuous-linear-map
operator-norm form.

Horn & Johnson, *Matrix Analysis* 2nd ed., Theorem 4.3.1; Bhatia,
*Matrix Analysis*, Corollary III.2.6.

```lean
LinearMap.IsSymmetric.abs_eigenvalue_sub_eigenvalue_le.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2}
  [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] {n : ℕ} [FiniteDimensional 𝕜 E]
  {T S : E →ₗ[𝕜] E} (hT : T.IsSymmetric) (hS : S.IsSymmetric) (hn : Module.finrank 𝕜 E = n) {ε : ℝ}
  (hε : ∀ (x : E), ‖(T - S) x‖ ≤ ε * ‖x‖) (k : Fin n) :
  |hT.eigenvalues hn k - hS.eigenvalues hn k| ≤ ε
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Courant–Fischer, lower direction](../part-01/courant-fischer-lower-direction.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.IsSymmetric.abs_eigenvalue_sub_eigenvalue_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/CourantFischer.html#LinearMap.IsSymmetric.abs_eigenvalue_sub_eigenvalue_le).

## Other forms

**Weyl's inequality.** Formalized in Tau Ceti as [`LinearMap.IsSymmetric.abs_eigenvalue_sub_eigenvalue_le_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/CourantFischer.html#LinearMap.IsSymmetric.abs_eigenvalue_sub_eigenvalue_le_norm).

```lean
LinearMap.IsSymmetric.abs_eigenvalue_sub_eigenvalue_le_norm.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2}
  [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] {n : ℕ} [FiniteDimensional 𝕜 E]
  {T S : E →L[𝕜] E} (hT : (↑T).IsSymmetric) (hS : (↑S).IsSymmetric) (hn : Module.finrank 𝕜 E = n)
  (k : Fin n) : |hT.eigenvalues hn k - hS.eigenvalues hn k| ≤ ‖T - S‖
```

## Sources

- [Tau Ceti documentation: `LinearMap.IsSymmetric.abs_eigenvalue_sub_eigenvalue_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/CourantFischer.html#LinearMap.IsSymmetric.abs_eigenvalue_sub_eigenvalue_le)
- [Source of `LinearMap.IsSymmetric.abs_eigenvalue_sub_eigenvalue_le` in TauCeti/Analysis/InnerProductSpace/CourantFischer.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L438)
