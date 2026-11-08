---
declaration: theorem
origin: cited
lean: TauCeti.absoluteProjectiveTupleHeight_eq_one_iff, TauCeti.house_eq_one_iff, TauCeti.mahlerMeasure_eq_one_iff, TauCeti.denseRange_mul_sub_intCast
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

- [TauCeti.mahlerMeasure](../../diophantine-approximation-and-transcendence/part-01/tauceti-mahlermeasure.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.absoluteProjectiveTupleHeight_eq_one_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Kronecker.html#TauCeti.absoluteProjectiveTupleHeight_eq_one_iff).

## Other forms

**Kronecker's theorem.** Formalized in Tau Ceti as [`TauCeti.house_eq_one_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/House.html#TauCeti.house_eq_one_iff).

```lean
TauCeti.house_eq_one_iff.{u_1} {F : Type u_1} [Field F] [CharZero F] {x : F} (hx : IsIntegral ℤ x) :
  TauCeti.house x = 1 ↔ ∃ n, 0 < n ∧ x ^ n = 1
```

**Kronecker's theorem.** Formalized in Tau Ceti as [`TauCeti.mahlerMeasure_eq_one_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/MahlerMeasure.html#TauCeti.mahlerMeasure_eq_one_iff).

```lean
TauCeti.mahlerMeasure_eq_one_iff.{u_1} {F : Type u_1} [Field F] [CharZero F] {x : F}
  (hx : IsAlgebraic ℚ x) : TauCeti.mahlerMeasure x = 1 ↔ x = 0 ∨ ∃ n, 0 < n ∧ x ^ n = 1
```

**Kronecker's theorem, density form.** Formalized in Tau Ceti as [`TauCeti.denseRange_mul_sub_intCast`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Kronecker.html#TauCeti.denseRange_mul_sub_intCast).

```lean
TauCeti.denseRange_mul_sub_intCast.{u_1} {ι : Type u_1} [Fintype ι] {α : ι → ℝ}
  (hα : ∀ (x : ℤ × (ι → ℤ)), ↑x.1 + ∑ i, ↑(x.2 i) * α i = 0 → x = 0) :
  DenseRange fun p i => α i * ↑p.2 - ↑(p.1 i)
```

## Sources

- [Tau Ceti documentation: `TauCeti.absoluteProjectiveTupleHeight_eq_one_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Kronecker.html#TauCeti.absoluteProjectiveTupleHeight_eq_one_iff)
- [Source of `TauCeti.absoluteProjectiveTupleHeight_eq_one_iff` in TauCeti/NumberTheory/Height/Kronecker.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Height/Kronecker.lean#L89)
- [Tau Ceti roadmap status: Heights, units and S-units of number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/HeightsAndUnits/STATUS.md)
