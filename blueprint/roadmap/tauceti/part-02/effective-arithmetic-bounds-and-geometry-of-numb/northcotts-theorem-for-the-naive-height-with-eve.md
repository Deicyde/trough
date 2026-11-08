---
declaration: theorem
origin: cited
lean: TauCeti.finite_setOf_naiveHeight_le
statement: formalized
proof: formalized
---

# Northcott's theorem for the naive height, with Evertse's count

In a field of
characteristic zero, the algebraic elements of degree at most `d` and naive height at most `B`
form a finite set with at most `d (2⌊B⌋ + 1)^(d + 1)` elements.

```lean
TauCeti.finite_setOf_naiveHeight_le.{u_1} {F : Type u_1} [Field F] [CharZero F] (d : ℕ) (B : ℝ) :
  {z | IsAlgebraic ℚ z ∧ (minpoly ℚ z).natDegree ≤ d ∧ TauCeti.naiveHeight z ≤ B}.Finite ∧
    {z | IsAlgebraic ℚ z ∧ (minpoly ℚ z).natDegree ≤ d ∧ TauCeti.naiveHeight z ≤ B}.ncard ≤
      d * (2 * ⌊B⌋₊ + 1) ^ (d + 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.Polynomial.ncard_biUnion_roots_natDegree_le_abs_intCoeff_le](tauceti-polynomial-ncard-biunion-roots-natdegree.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.finite_setOf_naiveHeight_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Counting.html#TauCeti.finite_setOf_naiveHeight_le).

## Sources

- [Tau Ceti documentation: `TauCeti.finite_setOf_naiveHeight_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Counting.html#TauCeti.finite_setOf_naiveHeight_le)
- [Source of `TauCeti.finite_setOf_naiveHeight_le` in TauCeti/NumberTheory/Height/Counting.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Height/Counting.lean#L49)
- [Tau Ceti roadmap status: Effective arithmetic bounds and geometry of numbers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/EffectiveBounds/STATUS.md)
