---
declaration: theorem
origin: cited
lean: TauCeti.FiniteField.exists_pow_eq_iff_pow_card_sub_one_div_eq_one
statement: formalized
proof: formalized
---

# Euler's criterion in a finite field

If `n ∣ #F - 1`, then a nonzero `a ∈ F` is an `n`-th
power exactly when `a ^ ((#F - 1) / n) = 1`.

```lean
TauCeti.FiniteField.exists_pow_eq_iff_pow_card_sub_one_div_eq_one.{u_1} {F : Type u_1} [Field F]
  [Finite F] {n : ℕ} (hn : n ∣ Nat.card F - 1) {a : F} (ha : a ≠ 0) :
  (∃ b, b ^ n = a) ↔ a ^ ((Nat.card F - 1) / n) = 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteField.exists_pow_eq_iff_pow_card_sub_one_div_eq_one`](https://taucetiproject.org/docs/TauCeti/FieldTheory/Finite/EulerCriterion.html#TauCeti.FiniteField.exists_pow_eq_iff_pow_card_sub_one_div_eq_one).

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteField.exists_pow_eq_iff_pow_card_sub_one_div_eq_one`](https://taucetiproject.org/docs/TauCeti/FieldTheory/Finite/EulerCriterion.html#TauCeti.FiniteField.exists_pow_eq_iff_pow_card_sub_one_div_eq_one)
- [Source of `TauCeti.FiniteField.exists_pow_eq_iff_pow_card_sub_one_div_eq_one` in TauCeti/FieldTheory/Finite/EulerCriterion.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/Finite/EulerCriterion.lean#L31)
