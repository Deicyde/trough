---
declaration: theorem
origin: cited
lean: AddSubmonoid.IsNumericalSemigroup.numericalFrobenius_eq_sSup_aperySet_sub
statement: formalized
proof: formalized
---

# Selmer's formula for the Frobenius number

for a numerical semigroup `S` and `n ≠ 0`,
`F(S) = max Ap(S, n) - n`. The usual hypothesis `n ∈ S` is not needed.

```lean
AddSubmonoid.IsNumericalSemigroup.numericalFrobenius_eq_sSup_aperySet_sub {S : AddSubmonoid ℕ}
  {n : ℕ} (h : S.IsNumericalSemigroup) (hpos : n ≠ 0) :
  S.numericalFrobenius = ↑(sSup (S.aperySet n)) - ↑n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AddSubmonoid.IsNumericalSemigroup.numericalFrobenius_eq_sSup_aperySet_sub`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumericalSemigroup/Apery.html#AddSubmonoid.IsNumericalSemigroup.numericalFrobenius_eq_sSup_aperySet_sub).

## Sources

- [Tau Ceti documentation: `AddSubmonoid.IsNumericalSemigroup.numericalFrobenius_eq_sSup_aperySet_sub`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumericalSemigroup/Apery.html#AddSubmonoid.IsNumericalSemigroup.numericalFrobenius_eq_sSup_aperySet_sub)
- [Source of `AddSubmonoid.IsNumericalSemigroup.numericalFrobenius_eq_sSup_aperySet_sub` in TauCeti/NumberTheory/NumericalSemigroup/Apery.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/NumericalSemigroup/Apery.lean#L282)
