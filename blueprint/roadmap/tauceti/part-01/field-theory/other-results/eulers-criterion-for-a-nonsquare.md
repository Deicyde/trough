---
declaration: theorem
origin: cited
lean: TauCeti.FiniteField.pow_card_div_two_eq_neg_one, TauCeti.FiniteField.exists_pow_eq_iff_pow_card_sub_one_div_eq_one
statement: formalized
proof: formalized
---

# Euler's criterion for a nonsquare

In a finite field `F`, a nonsquare `r` satisfies
`r ^ (#F / 2) = -1`.

```lean
TauCeti.FiniteField.pow_card_div_two_eq_neg_one.{u_1} {F : Type u_1} [Field F] [Finite F] {r : F}
  (hr : ¬IsSquare r) : r ^ (Nat.card F / 2) = -1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteField.pow_card_div_two_eq_neg_one`](https://taucetiproject.org/docs/TauCeti/FieldTheory/Finite/EulerCriterion.html#TauCeti.FiniteField.pow_card_div_two_eq_neg_one).

## Other forms

**Euler's criterion in a finite field.** Formalized in Tau Ceti as [`TauCeti.FiniteField.exists_pow_eq_iff_pow_card_sub_one_div_eq_one`](https://taucetiproject.org/docs/TauCeti/FieldTheory/Finite/EulerCriterion.html#TauCeti.FiniteField.exists_pow_eq_iff_pow_card_sub_one_div_eq_one).

```lean
TauCeti.FiniteField.exists_pow_eq_iff_pow_card_sub_one_div_eq_one.{u_1} {F : Type u_1} [Field F]
  [Finite F] {n : ℕ} (hn : n ∣ Nat.card F - 1) {a : F} (ha : a ≠ 0) :
  (∃ b, b ^ n = a) ↔ a ^ ((Nat.card F - 1) / n) = 1
```

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteField.pow_card_div_two_eq_neg_one`](https://taucetiproject.org/docs/TauCeti/FieldTheory/Finite/EulerCriterion.html#TauCeti.FiniteField.pow_card_div_two_eq_neg_one)
- [Source of `TauCeti.FiniteField.pow_card_div_two_eq_neg_one` in TauCeti/FieldTheory/Finite/EulerCriterion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/FieldTheory/Finite/EulerCriterion.lean#L59)
