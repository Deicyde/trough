---
declaration: theorem
origin: cited
lean: TauCeti.ncard_exists_lt_norm_sum_Iic_le, TauCeti.ncard_exists_lt_norm_sum_Iic_div_le
statement: formalized
proof: formalized
---

# Lévy's reflection inequality on the sign cube (counting form)

the number of sign patterns
for which some partial sum `∑ j ≤ k, εⱼ xⱼ` exceeds `t` in norm is at most twice the number of sign
patterns for which the full sum exceeds `t` in norm.

```lean
TauCeti.ncard_exists_lt_norm_sum_Iic_le.{u_1} {n : ℕ} {E : Type u_1} [SeminormedAddCommGroup E]
  [NormedSpace ℝ E] (x : Fin n → E) (t : ℝ) :
  {ε | ∃ k, t < ‖∑ j ≤ k, ε j • x j‖}.ncard ≤ 2 * {ε | t < ‖∑ j, ε j • x j‖}.ncard
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ncard_exists_lt_norm_sum_Iic_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/RademacherSum/Levy.html#TauCeti.ncard_exists_lt_norm_sum_Iic_le).

## Other forms

**Lévy's reflection inequality on the sign cube (probability form).** Formalized in Tau Ceti as [`TauCeti.ncard_exists_lt_norm_sum_Iic_div_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/RademacherSum/Levy.html#TauCeti.ncard_exists_lt_norm_sum_Iic_div_le).

```lean
TauCeti.ncard_exists_lt_norm_sum_Iic_div_le.{u_1} {n : ℕ} {E : Type u_1} [SeminormedAddCommGroup E]
  [NormedSpace ℝ E] (x : Fin n → E) (t : ℝ) :
  ↑{ε | ∃ k, t < ‖∑ j ≤ k, ε j • x j‖}.ncard / 2 ^ n ≤
    2 * (↑{ε | t < ‖∑ j, ε j • x j‖}.ncard / 2 ^ n)
```

## Sources

- [Tau Ceti documentation: `TauCeti.ncard_exists_lt_norm_sum_Iic_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/RademacherSum/Levy.html#TauCeti.ncard_exists_lt_norm_sum_Iic_le)
- [Source of `TauCeti.ncard_exists_lt_norm_sum_Iic_le` in TauCeti/Analysis/Normed/Module/RademacherSum/Levy.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Module/RademacherSum/Levy.lean#L184)
