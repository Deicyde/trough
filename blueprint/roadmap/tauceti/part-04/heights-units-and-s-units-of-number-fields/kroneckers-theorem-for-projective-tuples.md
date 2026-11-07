---
declaration: theorem
origin: cited
lean: TauCeti.absoluteProjectiveTupleHeight_eq_one_iff
statement: formalized
proof: formalized
---

# Kronecker's theorem for projective tuples

A tuple with algebraic coordinates has absolute
projective height one if and only if, for every nonzero coordinate `x j`, each ratio `x i / x j`
is zero or of finite multiplicative order. This includes the zero tuple.

```lean
TauCeti.absoluteProjectiveTupleHeight_eq_one_iff.{u_1, u_2} {F : Type u_1} [Field F] [CharZero F]
  {ι : Type u_2} [Finite ι] {x : ι → F} (hx : ∀ (i : ι), IsAlgebraic ℚ (x i)) :
  TauCeti.absoluteProjectiveTupleHeight x = 1 ↔
    ∀ (i j : ι), x j ≠ 0 → x i = 0 ∨ IsOfFinOrder (x i / x j)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.absoluteProjectiveTupleHeight_eq_one_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Kronecker.html#TauCeti.absoluteProjectiveTupleHeight_eq_one_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.absoluteProjectiveTupleHeight_eq_one_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Kronecker.html#TauCeti.absoluteProjectiveTupleHeight_eq_one_iff)
- [Source of `TauCeti.absoluteProjectiveTupleHeight_eq_one_iff` in TauCeti/NumberTheory/Height/Kronecker.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Height/Kronecker.lean#L89)
- [Tau Ceti roadmap status: Heights, units and S-units of number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/HeightsAndUnits/STATUS.md)
