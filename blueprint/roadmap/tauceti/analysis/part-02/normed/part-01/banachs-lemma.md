---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.exists_preimage_norm_le_of_mem_closure
statement: formalized
proof: formalized
---

# Banach's lemma

If every `y` lies in the closure of the image of the closed ball of radius
`C * ‖y‖`, then every `y` has a preimage of norm at most `2 * C * ‖y‖`. In particular, the
map is surjective.

```lean
ContinuousLinearMap.exists_preimage_norm_le_of_mem_closure.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1}
  {𝕜' : Type u_2} [Semiring 𝕜] [Semiring 𝕜'] {σ : 𝕜 →+* 𝕜'} {E : Type u_3}
  [SeminormedAddCommGroup E] [_root_.Module 𝕜 E] [CompleteSpace E] {F : Type u_4}
  [NormedAddCommGroup F] [_root_.Module 𝕜' F] (f : E →SL[σ] F) {C : ℝ}
  (hC : ∀ (y : F), y ∈ closure (⇑f '' Metric.closedBall 0 (C * ‖y‖))) (y : F) :
  ∃ x, f x = y ∧ ‖x‖ ≤ 2 * C * ‖y‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.exists_preimage_norm_le_of_mem_closure`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Banach.html#ContinuousLinearMap.exists_preimage_norm_le_of_mem_closure).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.exists_preimage_norm_le_of_mem_closure`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Banach.html#ContinuousLinearMap.exists_preimage_norm_le_of_mem_closure)
- [Source of `ContinuousLinearMap.exists_preimage_norm_le_of_mem_closure` in TauCeti/Analysis/Normed/Operator/Banach.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/Banach.lean#L116)
