---
declaration: theorem
origin: cited
lean: TauCeti.four_mul_ncard_three_pow_mul_lt_norm_sum_div_le
statement: formalized
proof: formalized
---

# Iterated doubly-exponential Rademacher tail bound

for every `k : ℕ`,
`4 * P(3 ^ k * t < ‖S‖) ≤ (4 * P(t < ‖S‖)) ^ (2 ^ k)`.

```lean
TauCeti.four_mul_ncard_three_pow_mul_lt_norm_sum_div_le.{u_1, u_2} {ι : Type u_1} {E : Type u_2}
  [Fintype ι] [SeminormedAddCommGroup E] [NormedSpace ℝ E] (x : ι → E) (t : ℝ) (k : ℕ) :
  4 * (↑{ε | 3 ^ k * t < ‖∑ i, ε i • x i‖}.ncard / 2 ^ Fintype.card ι) ≤
    (4 * (↑{ε | t < ‖∑ i, ε i • x i‖}.ncard / 2 ^ Fintype.card ι)) ^ 2 ^ k
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Lévy's reflection inequality on the sign cube (counting form)](levys-reflection-inequality-on-the-sign-cube-cou.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.four_mul_ncard_three_pow_mul_lt_norm_sum_div_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/RademacherSum/Levy.html#TauCeti.four_mul_ncard_three_pow_mul_lt_norm_sum_div_le).

## Sources

- [Tau Ceti documentation: `TauCeti.four_mul_ncard_three_pow_mul_lt_norm_sum_div_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/RademacherSum/Levy.html#TauCeti.four_mul_ncard_three_pow_mul_lt_norm_sum_div_le)
- [Source of `TauCeti.four_mul_ncard_three_pow_mul_lt_norm_sum_div_le` in TauCeti/Analysis/Normed/Module/RademacherSum/Levy.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Module/RademacherSum/Levy.lean#L427)
