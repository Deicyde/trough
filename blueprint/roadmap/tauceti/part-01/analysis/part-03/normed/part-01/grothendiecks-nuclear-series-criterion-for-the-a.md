---
declaration: theorem
origin: cited
lean: TauCeti.hasApproximationProperty_iff_tsum_apply_eq_zero
statement: formalized
proof: formalized
---

# Grothendieck's nuclear-series criterion for the approximation property

A Banach space `E`
over `ℝ` or `ℂ` has the approximation property iff for every sequence of functionals
`f : ℕ → StrongDual 𝕜 E` and vectors `x : ℕ → E` with `∑ n, ‖f n‖ * ‖x n‖ < ∞` such that
`∑' n, f n v • x n = 0` for every `v : E`, one has `∑' n, f n (x n) = 0`.

```lean
TauCeti.hasApproximationProperty_iff_tsum_apply_eq_zero.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2}
  [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] [CompleteSpace E] :
  TauCeti.HasApproximationProperty 𝕜 E ↔
    ∀ (f : ℕ → StrongDual 𝕜 E) (x : ℕ → E),
      (Summable fun n => ‖f n‖ * ‖x n‖) →
        (∀ (v : E), ∑' (n : ℕ), (f n) v • x n = 0) → ∑' (n : ℕ), (f n) (x n) = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Grothendieck's trace criterion for the approximation property](grothendiecks-trace-criterion-for-the-approximat.md)
- [TauCeti.CompletedInjectiveTensor](../../../part-01/banach-space-theory/part-01/tauceti-completedinjectivetensor.md)
- [TauCeti.CompletedProjectiveTensor](../../../part-01/banach-space-theory/part-01/tauceti-completedprojectivetensor.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hasApproximationProperty_iff_tsum_apply_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/ApproximationProperty/TensorProduct.html#TauCeti.hasApproximationProperty_iff_tsum_apply_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.hasApproximationProperty_iff_tsum_apply_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/ApproximationProperty/TensorProduct.html#TauCeti.hasApproximationProperty_iff_tsum_apply_eq_zero)
- [Source of `TauCeti.hasApproximationProperty_iff_tsum_apply_eq_zero` in TauCeti/Analysis/Normed/Module/ApproximationProperty/TensorProduct.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Module/ApproximationProperty/TensorProduct.lean#L416)
