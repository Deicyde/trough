---
declaration: theorem
origin: cited
lean: Nat.sub_one_mul_sum_div_pow_succ_eq_sub_sum_digits
statement: formalized
proof: formalized
---

# Legendre's identity over a fixed range

For `a < b ^ f`,
`(b - 1) ∑_{i < f} ⌊a / b ^ (i + 1)⌋ = a - s(a)`, where `s(a)` is the base-`b` digit sum of `a`.
This is `Nat.sub_one_mul_sum_log_div_pow_eq_sub_sum_digits` with the sum extended by zero terms
from `log b a + 1` to `f`.

```lean
Nat.sub_one_mul_sum_div_pow_succ_eq_sub_sum_digits {b f a : ℕ} (ha : a < b ^ f) :
  (b - 1) * ∑ i ∈ Finset.range f, a / b ^ (i + 1) = a - (b.digits a).sum
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Nat.sub_one_mul_sum_div_pow_succ_eq_sub_sum_digits`](https://taucetiproject.org/docs/TauCeti/Data/Nat/Digits.html#Nat.sub_one_mul_sum_div_pow_succ_eq_sub_sum_digits).

## Sources

- [Tau Ceti documentation: `Nat.sub_one_mul_sum_div_pow_succ_eq_sub_sum_digits`](https://taucetiproject.org/docs/TauCeti/Data/Nat/Digits.html#Nat.sub_one_mul_sum_div_pow_succ_eq_sub_sum_digits)
- [Source of `Nat.sub_one_mul_sum_div_pow_succ_eq_sub_sum_digits` in TauCeti/Data/Nat/Digits.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Data/Nat/Digits.lean#L135)
