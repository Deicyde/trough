---
declaration: theorem
origin: cited
lean: IsCompact.exists_pos_forall_norm_sub_le_mul, IsCompact.exists_pos_forall_norm_sub_le_mul_norm_sub
statement: formalized
proof: formalized
---

# Uniform Lipschitz bound at a compact family of base points

Let `F : P → E → G` be jointly
`C¹` at the points `(p, x p)`, where `x : P → E` is continuous on a compact set `K` and `p ∈ K`.
Then there are `δ > 0` and `L` such that `‖F p y - F p (x p)‖ ≤ L ‖y - x p‖` for every `p ∈ K`
and every `y` with `‖y - x p‖ ≤ δ`.

```lean
IsCompact.exists_pos_forall_norm_sub_le_mul.{u_1, u_2, u_3} {P : Type u_1} {E : Type u_2}
  {G : Type u_3} [NormedAddCommGroup P] [NormedSpace ℝ P] [NormedAddCommGroup E] [NormedSpace ℝ E]
  [NormedAddCommGroup G] [NormedSpace ℝ G] {F : P → E → G} {K : Set P} {x : P → E}
  (hK : IsCompact K) (hF : ∀ p ∈ K, ContDiffAt ℝ 1 (Function.uncurry F) (p, x p))
  (hx : ContinuousOn x K) :
  ∃ δ > 0, ∃ L, ∀ p ∈ K, ∀ (y : E), ‖y - x p‖ ≤ δ → ‖F p y - F p (x p)‖ ≤ L * ‖y - x p‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsCompact.exists_pos_forall_norm_sub_le_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/FDeriv/Remainder.html#IsCompact.exists_pos_forall_norm_sub_le_mul).

## Other forms

**Uniform Lipschitz bound on balls about a compact family of base points.** Formalized in Tau Ceti as [`IsCompact.exists_pos_forall_norm_sub_le_mul_norm_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/FDeriv/Remainder.html#IsCompact.exists_pos_forall_norm_sub_le_mul_norm_sub).

```lean
IsCompact.exists_pos_forall_norm_sub_le_mul_norm_sub.{u_1, u_2, u_3} {P : Type u_1} {E : Type u_2}
  {G : Type u_3} [NormedAddCommGroup P] [NormedSpace ℝ P] [NormedAddCommGroup E] [NormedSpace ℝ E]
  [NormedAddCommGroup G] [NormedSpace ℝ G] {F : P → E → G} {K : Set P} {x : P → E}
  (hK : IsCompact K) (hF : ∀ p ∈ K, ContDiffAt ℝ 1 (Function.uncurry F) (p, x p))
  (hx : ContinuousOn x K) :
  ∃ δ > 0,
    ∃ L, ∀ p ∈ K, ∀ (a b : E), ‖a‖ ≤ δ → ‖b‖ ≤ δ → ‖F p (x p + a) - F p (x p + b)‖ ≤ L * ‖a - b‖
```

## Sources

- [Tau Ceti documentation: `IsCompact.exists_pos_forall_norm_sub_le_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/FDeriv/Remainder.html#IsCompact.exists_pos_forall_norm_sub_le_mul)
- [Source of `IsCompact.exists_pos_forall_norm_sub_le_mul` in TauCeti/Analysis/Calculus/FDeriv/Remainder.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Calculus/FDeriv/Remainder.lean#L182)
