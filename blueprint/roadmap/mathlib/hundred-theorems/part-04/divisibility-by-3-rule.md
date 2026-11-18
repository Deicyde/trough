# Divisibility by 3 Rule

**Divisibility by 3 Rule**

```lean
Nat.three_dvd_iff (n : ℕ) : 3 ∣ n ↔ 3 ∣ (Nat.digits 10 n).sum
```

## Depends on

- [List](../../overview/data-structures/list-like-structures/list.md)
- [Natural number](../../overview/general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Nat.three_dvd_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Digits/Div.html#Nat.three_dvd_iff)
- [Source of `Nat.three_dvd_iff` in Mathlib/Data/Nat/Digits/Div.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Data/Nat/Digits/Div.lean#L43)
- [Freek Wiedijk's 100 theorems, no. 85](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/100.yaml#L435)
