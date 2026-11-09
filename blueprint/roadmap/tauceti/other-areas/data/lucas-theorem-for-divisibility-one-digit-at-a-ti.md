---
declaration: theorem
origin: cited
lean: Nat.dvd_choose_add_mul_iff
statement: formalized
proof: formalized
---

# Lucas' theorem for divisibility, one digit at a time

For last digits `r, a < p`, the
prime `p` divides `(r + p q) choose (a + p b)` exactly when `r < a` or `p` divides
`q choose b`.

```lean
Nat.dvd_choose_add_mul_iff {p : ℕ} [hp : Fact (Nat.Prime p)] {q r a b : ℕ} (hr : r < p)
  (ha : a < p) : p ∣ (r + p * q).choose (a + p * b) ↔ r < a ∨ p ∣ q.choose b
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Nat.dvd_choose_add_mul_iff`](https://taucetiproject.org/docs/TauCeti/Data/Nat/Choose/Digits.html#Nat.dvd_choose_add_mul_iff).

## Sources

- [Tau Ceti documentation: `Nat.dvd_choose_add_mul_iff`](https://taucetiproject.org/docs/TauCeti/Data/Nat/Choose/Digits.html#Nat.dvd_choose_add_mul_iff)
- [Source of `Nat.dvd_choose_add_mul_iff` in TauCeti/Data/Nat/Choose/Digits.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Data/Nat/Choose/Digits.lean#L55)
