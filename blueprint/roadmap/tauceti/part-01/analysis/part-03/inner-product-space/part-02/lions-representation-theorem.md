---
declaration: theorem
origin: cited
lean: LinearMap.exists_forall_apply_eq_and_norm_le_of_coercive
statement: formalized
proof: formalized
---

# Lions' representation theorem

Let `H` be a real Hilbert space, `Φ` a real vector space
with a map `j : Φ → H` and a function `p : Φ → ℝ` dominating it, `‖j φ‖ ≤ p φ`, and let `E` assign
to each `φ ∈ Φ` a continuous linear functional on `H` that is coercive on the diagonal,
`c p(φ)² ≤ E φ (j φ)` with `c > 0`. Then every linear functional `ℓ` on `Φ` with
`|ℓ φ| ≤ M p(φ)` is represented by some `u ∈ H`, in the sense that `E φ u = ℓ φ` for every
`φ ∈ Φ`, and `u` can be chosen with `‖u‖ ≤ M / c`.

No continuity of `E` in `φ`, completeness of `Φ` or uniqueness of `u` is claimed; the test space
`Φ` carries no topology at all.

```lean
LinearMap.exists_forall_apply_eq_and_norm_le_of_coercive.{u_1, u_2} {Φ : Type u_1} {H : Type u_2}
  [AddCommGroup Φ] [_root_.Module ℝ Φ] [NormedAddCommGroup H] [InnerProductSpace ℝ H]
  [CompleteSpace H] (E : Φ →ₗ[ℝ] StrongDual ℝ H) (j : Φ → H) (p : Φ → ℝ) (ℓ : Φ →ₗ[ℝ] ℝ) {c M : ℝ}
  (hc : 0 < c) (hM : 0 ≤ M) (hE : ∀ (φ : Φ), c * p φ ^ 2 ≤ (E φ) (j φ))
  (hj : ∀ (φ : Φ), ‖j φ‖ ≤ p φ) (hℓ : ∀ (φ : Φ), |ℓ φ| ≤ M * p φ) :
  ∃ u, (∀ (φ : Φ), (E φ) u = ℓ φ) ∧ ‖u‖ ≤ M / c
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.exists_forall_apply_eq_and_norm_le_of_coercive`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Lions.html#LinearMap.exists_forall_apply_eq_and_norm_le_of_coercive).

## Sources

- [Tau Ceti documentation: `LinearMap.exists_forall_apply_eq_and_norm_le_of_coercive`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Lions.html#LinearMap.exists_forall_apply_eq_and_norm_le_of_coercive)
- [Source of `LinearMap.exists_forall_apply_eq_and_norm_le_of_coercive` in TauCeti/Analysis/InnerProductSpace/Lions.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/Lions.lean#L62)
