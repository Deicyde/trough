---
declaration: theorem
origin: cited
lean: TauCeti.exists_prime_dvd_pow_sub_pow
statement: formalized
proof: formalized
---

# The Bang–Zsigmondy theorem

For coprime natural numbers `a > b > 0` and `n ≥ 2`, there is a
prime dividing `a ^ n - b ^ n` and none of `a ^ k - b ^ k` for `0 < k < n`, unless `n = 2` and
`a + b` is a power of two, or `(a, b, n) = (2, 1, 6)`. All standing hypotheses are sharp:
`(a, b, n) = (1, 0, 3)`, `(1, 1, 3)`, `(4, 2, 6)` and `(2, 1, 1)` have no primitive prime
divisor.

```lean
TauCeti.exists_prime_dvd_pow_sub_pow {a b n : ℕ} (hb : 0 < b) (hba : b < a) (hab : a.Coprime b)
  (hn : 2 ≤ n) (h₂ : n = 2 → ¬∃ k, a + b = 2 ^ k) (h₆ : n = 6 → a ≠ 2 ∨ b ≠ 1) :
  ∃ p, Nat.Prime p ∧ p ∣ a ^ n - b ^ n ∧ ∀ (k : ℕ), 0 < k → k < n → ¬p ∣ a ^ k - b ^ k
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Lifting the exponent from an intermediate exponent `d`](../../part-02/primitive-prime-divisors-and-the-bang-zsigmondy/lifting-the-exponent-from-an-intermediate-expone.md)
- [TauCeti.exists_prime_dvd_sq_sub_sq_iff](../../part-02/primitive-prime-divisors-and-the-bang-zsigmondy/tauceti-exists-prime-dvd-sq-sub-sq-iff.md)
- [TauCeti.lt_pow_sub_pow_div_add_pow](../../part-02/primitive-prime-divisors-and-the-bang-zsigmondy/tauceti-lt-pow-sub-pow-div-add-pow.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_prime_dvd_pow_sub_pow`](https://taucetiproject.org/docs/TauCeti/NumberTheory/PrimitivePrimeDivisors/Zsigmondy.html#TauCeti.exists_prime_dvd_pow_sub_pow).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_prime_dvd_pow_sub_pow`](https://taucetiproject.org/docs/TauCeti/NumberTheory/PrimitivePrimeDivisors/Zsigmondy.html#TauCeti.exists_prime_dvd_pow_sub_pow)
- [Source of `TauCeti.exists_prime_dvd_pow_sub_pow` in TauCeti/NumberTheory/PrimitivePrimeDivisors/Zsigmondy.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/PrimitivePrimeDivisors/Zsigmondy.lean#L77)
