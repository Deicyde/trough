---
declaration: theorem
origin: cited
lean: TauCeti.house_eq_one_iff, TauCeti.mahlerMeasure_eq_one_iff, TauCeti.absoluteProjectiveTupleHeight_eq_one_iff
statement: formalized
proof: formalized
---

# Kronecker's theorem

An algebraic integer has house `1` exactly when it is a root of
unity.

```lean
TauCeti.house_eq_one_iff.{u_1} {F : Type u_1} [Field F] [CharZero F] {x : F} (hx : IsIntegral ℤ x) :
  TauCeti.house x = 1 ↔ ∃ n, 0 < n ∧ x ^ n = 1
```

## Depends on

- [TauCeti.mahlerMeasure](../../part-01/diophantine-approximation-and-transcendence/tauceti-mahlermeasure.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.house_eq_one_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/House.html#TauCeti.house_eq_one_iff).

## Other forms

**Kronecker's theorem.** Formalized in Tau Ceti as [`TauCeti.mahlerMeasure_eq_one_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/MahlerMeasure.html#TauCeti.mahlerMeasure_eq_one_iff).

```lean
TauCeti.mahlerMeasure_eq_one_iff.{u_1} {F : Type u_1} [Field F] [CharZero F] {x : F}
  (hx : IsAlgebraic ℚ x) : TauCeti.mahlerMeasure x = 1 ↔ x = 0 ∨ ∃ n, 0 < n ∧ x ^ n = 1
```

**Kronecker's theorem for projective tuples.** Formalized in Tau Ceti as [`TauCeti.absoluteProjectiveTupleHeight_eq_one_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Kronecker.html#TauCeti.absoluteProjectiveTupleHeight_eq_one_iff).

```lean
TauCeti.absoluteProjectiveTupleHeight_eq_one_iff.{u_1, u_2} {F : Type u_1} [Field F] [CharZero F]
  {ι : Type u_2} [Finite ι] {x : ι → F} (hx : ∀ (i : ι), IsAlgebraic ℚ (x i)) :
  TauCeti.absoluteProjectiveTupleHeight x = 1 ↔
    ∀ (i j : ι), x j ≠ 0 → x i = 0 ∨ IsOfFinOrder (x i / x j)
```

## Sources

- [Tau Ceti documentation: `TauCeti.house_eq_one_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/House.html#TauCeti.house_eq_one_iff)
- [Source of `TauCeti.house_eq_one_iff` in TauCeti/NumberTheory/Height/House.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Height/House.lean#L294)
