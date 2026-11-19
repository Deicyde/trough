---
declaration: theorem
origin: cited
lean: ConvexOn.expect_map_norm_sum_smul_le
statement: formalized
proof: formalized
---

# Convex Rademacher contraction principle

For any convex nondecreasing function `Φ` on
`[0, ∞)` and real coefficients satisfying `∀ i, |α i| ≤ M`, the average of
`Φ ‖∑ i, εᵢ (αᵢ xᵢ)‖` is at most that of `Φ (M * ‖∑ i, εᵢ xᵢ‖)`.

```lean
ConvexOn.expect_map_norm_sum_smul_le.{u_1, u_2} {ι : Type u_1} {E : Type u_2} [Fintype ι]
  [DecidableEq ι] [SeminormedAddCommGroup E] [NormedSpace ℝ E] {Φ : ℝ → ℝ}
  (hΦ_conv : ConvexOn ℝ (Set.Ici 0) Φ) (hΦ_mono : MonotoneOn Φ (Set.Ici 0)) {α : ι → ℝ} {M : ℝ}
  (hα : ∀ (i : ι), |α i| ≤ M) (x : ι → E) :
  (Finset.univ.expect fun ε => Φ ‖∑ i, ε i • α i • x i‖) ≤
    Finset.univ.expect fun ε => Φ (M * ‖∑ i, ε i • x i‖)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ConvexOn.expect_map_norm_sum_smul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/RademacherSum/Contraction.html#ConvexOn.expect_map_norm_sum_smul_le).

## Sources

- [Tau Ceti documentation: `ConvexOn.expect_map_norm_sum_smul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/RademacherSum/Contraction.html#ConvexOn.expect_map_norm_sum_smul_le)
- [Source of `ConvexOn.expect_map_norm_sum_smul_le` in TauCeti/Analysis/Normed/Module/RademacherSum/Contraction.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Module/RademacherSum/Contraction.lean#L139)
