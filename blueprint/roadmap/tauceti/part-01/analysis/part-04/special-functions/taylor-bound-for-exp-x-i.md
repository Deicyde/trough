---
declaration: theorem
origin: cited
lean: TauCeti.norm_exp_ofReal_mul_I_sub_sum_le
statement: formalized
proof: formalized
---

# Taylor bound for `exp (x * I)`

For every real `x` and every `n`, the Taylor polynomial
of degree `n - 1` approximates `exp (x * I)` to within `|x| ^ n / n !`.

```lean
TauCeti.norm_exp_ofReal_mul_I_sub_sum_le (n : ℕ) (x : ℝ) :
  ‖Complex.exp (↑x * Complex.I) - ∑ k ∈ Finset.range n, (↑x * Complex.I) ^ k / ↑k.factorial‖ ≤
    |x| ^ n / ↑n.factorial
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.norm_exp_ofReal_mul_I_sub_sum_le`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Exp/ImaginaryTaylor.html#TauCeti.norm_exp_ofReal_mul_I_sub_sum_le).

## Sources

- [Tau Ceti documentation: `TauCeti.norm_exp_ofReal_mul_I_sub_sum_le`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Exp/ImaginaryTaylor.html#TauCeti.norm_exp_ofReal_mul_I_sub_sum_le)
- [Source of `TauCeti.norm_exp_ofReal_mul_I_sub_sum_le` in TauCeti/Analysis/SpecialFunctions/Exp/ImaginaryTaylor.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Exp/ImaginaryTaylor.lean#L64)
