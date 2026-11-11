---
declaration: theorem
origin: cited
lean: TauCeti.Int.Matrix.not_forall_exists_ne_zero_int_vec_norm_le
statement: formalized
proof: formalized
---

# The exponent in Siegel's lemma is optimal

For an `m × (m + 1)` integer system, Siegel's
lemma `Int.Matrix.exists_ne_zero_int_vec_norm_le` gives a nonzero integer solution of sup norm at
most `((m + 1) · max 1 ‖A‖) ^ m`. For `0 < m` no exponent `e < m` works, with any constant `C`:
the system `b xᵢ = xᵢ₊₁` with `b` large has no nonzero integer solution of sup norm at most
`C · max 1 ‖A‖ ^ e`.

```lean
TauCeti.Int.Matrix.not_forall_exists_ne_zero_int_vec_norm_le {m : ℕ} (hm : 0 < m) {e : ℝ}
  (he : e < ↑m) (C : ℝ) :
  ¬∀ (A : Matrix (Fin m) (Fin (m + 1)) ℤ), ∃ x, x ≠ 0 ∧ A.mulVec x = 0 ∧ ‖x‖ ≤ C * max 1 ‖A‖ ^ e
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Int.Matrix.not_forall_exists_ne_zero_int_vec_norm_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/SiegelsLemma.html#TauCeti.Int.Matrix.not_forall_exists_ne_zero_int_vec_norm_le).

## Sources

- [Tau Ceti documentation: `TauCeti.Int.Matrix.not_forall_exists_ne_zero_int_vec_norm_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/SiegelsLemma.html#TauCeti.Int.Matrix.not_forall_exists_ne_zero_int_vec_norm_le)
- [Source of `TauCeti.Int.Matrix.not_forall_exists_ne_zero_int_vec_norm_le` in TauCeti/NumberTheory/SiegelsLemma.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/SiegelsLemma.lean#L169)
