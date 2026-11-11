---
declaration: theorem
origin: cited
lean: TauCeti.exists_prime_dvd_sq_sub_sq_iff
statement: formalized
proof: formalized
---

# TauCeti.exists_prime_dvd_sq_sub_sq_iff

Exponent two: for coprime `b ≤ a`, the number `a ^ 2 - b ^ 2` has a primitive prime divisor
if and only if `a + b` is not a power of two. This is the Bang–Zsigmondy theorem at `n = 2`
together with its exceptional case.

```lean
TauCeti.exists_prime_dvd_sq_sub_sq_iff {a b : ℕ} (hba : b ≤ a) (hab : a.Coprime b) :
  (∃ p, Nat.Prime p ∧ p ∣ a ^ 2 - b ^ 2 ∧ ∀ (k : ℕ), 0 < k → k < 2 → ¬p ∣ a ^ k - b ^ k) ↔
    ¬∃ k, a + b = 2 ^ k
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_prime_dvd_sq_sub_sq_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/PrimitivePrimeDivisors/SmallExponents.html#TauCeti.exists_prime_dvd_sq_sub_sq_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_prime_dvd_sq_sub_sq_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/PrimitivePrimeDivisors/SmallExponents.html#TauCeti.exists_prime_dvd_sq_sub_sq_iff)
- [Source of `TauCeti.exists_prime_dvd_sq_sub_sq_iff` in TauCeti/NumberTheory/PrimitivePrimeDivisors/SmallExponents.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/PrimitivePrimeDivisors/SmallExponents.lean#L108)
- [Tau Ceti roadmap status: Primitive prime divisors and the Bang–Zsigmondy theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PrimitivePrimeDivisors/STATUS.md)
