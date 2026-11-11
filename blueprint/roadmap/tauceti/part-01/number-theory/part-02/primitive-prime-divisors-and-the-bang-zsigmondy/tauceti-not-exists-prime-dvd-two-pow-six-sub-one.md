---
declaration: theorem
origin: cited
lean: TauCeti.not_exists_prime_dvd_two_pow_six_sub_one_pow_six
statement: formalized
proof: formalized
---

# TauCeti.not_exists_prime_dvd_two_pow_six_sub_one_pow_six

The exceptional case `(a, b, n) = (2, 1, 6)` of the Bang–Zsigmondy theorem: every prime
divisor of `2 ^ 6 - 1 ^ 6 = 63 = 3 ^ 2 * 7` divides an earlier `2 ^ k - 1 ^ k`, namely
`3 ∣ 2 ^ 2 - 1` and `7 ∣ 2 ^ 3 - 1`.

```lean
TauCeti.not_exists_prime_dvd_two_pow_six_sub_one_pow_six :
  ¬∃ p, Nat.Prime p ∧ p ∣ 2 ^ 6 - 1 ^ 6 ∧ ∀ (k : ℕ), 0 < k → k < 6 → ¬p ∣ 2 ^ k - 1 ^ k
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.not_exists_prime_dvd_two_pow_six_sub_one_pow_six`](https://taucetiproject.org/docs/TauCeti/NumberTheory/PrimitivePrimeDivisors/SmallExponents.html#TauCeti.not_exists_prime_dvd_two_pow_six_sub_one_pow_six).

## Sources

- [Tau Ceti documentation: `TauCeti.not_exists_prime_dvd_two_pow_six_sub_one_pow_six`](https://taucetiproject.org/docs/TauCeti/NumberTheory/PrimitivePrimeDivisors/SmallExponents.html#TauCeti.not_exists_prime_dvd_two_pow_six_sub_one_pow_six)
- [Source of `TauCeti.not_exists_prime_dvd_two_pow_six_sub_one_pow_six` in TauCeti/NumberTheory/PrimitivePrimeDivisors/SmallExponents.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/PrimitivePrimeDivisors/SmallExponents.lean#L122)
- [Tau Ceti roadmap status: Primitive prime divisors and the Bang–Zsigmondy theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PrimitivePrimeDivisors/STATUS.md)
