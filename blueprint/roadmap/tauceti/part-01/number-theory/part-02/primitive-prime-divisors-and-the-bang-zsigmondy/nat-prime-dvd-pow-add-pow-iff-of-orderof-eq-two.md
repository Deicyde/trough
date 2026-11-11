---
declaration: theorem
origin: cited
lean: Nat.Prime.dvd_pow_add_pow_iff_of_orderOf_eq_two_mul
statement: formalized
proof: formalized
---

# Nat.Prime.dvd_pow_add_pow_iff_of_orderOf_eq_two_mul

Suppose that `a / b` has order `2 * m` modulo a prime `p`, with `m ≠ 0`. Then `p` divides
`a ^ k + b ^ k` exactly for the odd multiples `k` of `m`. The inverse is that of `ZMod p`, which is
the field inverse since `p` is prime; the hypothesis on the order forces `p ∤ b`.

```lean
Nat.Prime.dvd_pow_add_pow_iff_of_orderOf_eq_two_mul {p a b m : ℕ} (hp : Nat.Prime p)
  (h : orderOf (↑a * (↑b)⁻¹) = 2 * m) (hm : m ≠ 0) (k : ℕ) : p ∣ a ^ k + b ^ k ↔ m ∣ k ∧ ¬2 * m ∣ k
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Nat.Prime.dvd_pow_add_pow_iff_of_orderOf_eq_two_mul`](https://taucetiproject.org/docs/TauCeti/Data/ZMod/OrderOf.html#Nat.Prime.dvd_pow_add_pow_iff_of_orderOf_eq_two_mul).

## Sources

- [Tau Ceti documentation: `Nat.Prime.dvd_pow_add_pow_iff_of_orderOf_eq_two_mul`](https://taucetiproject.org/docs/TauCeti/Data/ZMod/OrderOf.html#Nat.Prime.dvd_pow_add_pow_iff_of_orderOf_eq_two_mul)
- [Source of `Nat.Prime.dvd_pow_add_pow_iff_of_orderOf_eq_two_mul` in TauCeti/Data/ZMod/OrderOf.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Data/ZMod/OrderOf.lean#L226)
- [Tau Ceti roadmap status: Primitive prime divisors and the Bang–Zsigmondy theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PrimitivePrimeDivisors/STATUS.md)
