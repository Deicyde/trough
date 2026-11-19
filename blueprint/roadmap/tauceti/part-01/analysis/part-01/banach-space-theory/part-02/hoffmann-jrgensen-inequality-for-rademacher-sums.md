---
declaration: theorem
origin: cited
lean: TauCeti.two_pow_card_mul_ncard_two_mul_add_norm_toLp_top_lt_norm_sum_le, TauCeti.ncard_two_mul_add_norm_toLp_top_lt_norm_sum_div_le
statement: formalized
proof: formalized
---

# Hoffmann–Jørgensen inequality for Rademacher sums (counting form)

on the sign cube
`ι → ℤˣ`, the exceedance count above `2 * t + ‖WithLp.toLp ∞ x‖` is bounded quadratically by the
exceedance count above `t`.

```lean
TauCeti.two_pow_card_mul_ncard_two_mul_add_norm_toLp_top_lt_norm_sum_le.{u_1, u_2} {ι : Type u_1}
  {E : Type u_2} [Fintype ι] [SeminormedAddCommGroup E] [NormedSpace ℝ E] (x : ι → E) (t : ℝ) :
  2 ^ Fintype.card ι * {ε | 2 * t + ‖WithLp.toLp ⊤ x‖ < ‖∑ i, ε i • x i‖}.ncard ≤
    4 * {ε | t < ‖∑ i, ε i • x i‖}.ncard ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Lévy's reflection inequality on the sign cube (counting form)](levys-reflection-inequality-on-the-sign-cube-cou.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.two_pow_card_mul_ncard_two_mul_add_norm_toLp_top_lt_norm_sum_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/RademacherSum/Levy.html#TauCeti.two_pow_card_mul_ncard_two_mul_add_norm_toLp_top_lt_norm_sum_le).

## Other forms

**Hoffmann–Jørgensen inequality for Rademacher sums (probability form).** Formalized in Tau Ceti as [`TauCeti.ncard_two_mul_add_norm_toLp_top_lt_norm_sum_div_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/RademacherSum/Levy.html#TauCeti.ncard_two_mul_add_norm_toLp_top_lt_norm_sum_div_le).

```lean
TauCeti.ncard_two_mul_add_norm_toLp_top_lt_norm_sum_div_le.{u_1, u_2} {ι : Type u_1} {E : Type u_2}
  [Fintype ι] [SeminormedAddCommGroup E] [NormedSpace ℝ E] (x : ι → E) (t : ℝ) :
  ↑{ε | 2 * t + ‖WithLp.toLp ⊤ x‖ < ‖∑ i, ε i • x i‖}.ncard / 2 ^ Fintype.card ι ≤
    4 * (↑{ε | t < ‖∑ i, ε i • x i‖}.ncard / 2 ^ Fintype.card ι) ^ 2
```

## Sources

- [Tau Ceti documentation: `TauCeti.two_pow_card_mul_ncard_two_mul_add_norm_toLp_top_lt_norm_sum_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/RademacherSum/Levy.html#TauCeti.two_pow_card_mul_ncard_two_mul_add_norm_toLp_top_lt_norm_sum_le)
- [Source of `TauCeti.two_pow_card_mul_ncard_two_mul_add_norm_toLp_top_lt_norm_sum_le` in TauCeti/Analysis/Normed/Module/RademacherSum/Levy.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Module/RademacherSum/Levy.lean#L371)
