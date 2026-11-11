---
declaration: theorem
origin: cited
lean: TauCeti.exists_prime_dvd_sub_iff
statement: formalized
proof: formalized
---

# TauCeti.exists_prime_dvd_sub_iff

Exponent one: for `b < a`, the number `a - b` has a primitive prime divisor (the condition on
the exponents `0 < k < 1` being vacuous) if and only if `1 < a - b`.

```lean
TauCeti.exists_prime_dvd_sub_iff {a b : ℕ} (hba : b < a) :
  (∃ p, Nat.Prime p ∧ p ∣ a - b ∧ ∀ (k : ℕ), 0 < k → k < 1 → ¬p ∣ a ^ k - b ^ k) ↔ 1 < a - b
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_prime_dvd_sub_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/PrimitivePrimeDivisors/SmallExponents.html#TauCeti.exists_prime_dvd_sub_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_prime_dvd_sub_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/PrimitivePrimeDivisors/SmallExponents.html#TauCeti.exists_prime_dvd_sub_iff)
- [Source of `TauCeti.exists_prime_dvd_sub_iff` in TauCeti/NumberTheory/PrimitivePrimeDivisors/SmallExponents.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/PrimitivePrimeDivisors/SmallExponents.lean#L70)
- [Tau Ceti roadmap status: Primitive prime divisors and the Bang–Zsigmondy theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PrimitivePrimeDivisors/STATUS.md)
