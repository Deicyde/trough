---
declaration: theorem
origin: cited
lean: TauCeti.finite_setOf_naiveHeight_le, Submodule.finite_subspaceHeight_le, TauCeti.finite_setOf_absMulHeight₁_le, TauCeti.finite_setOf_mahlerMeasure_le
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

- [TauCeti.mahlerMeasure](../diophantine-approximation-and-transcendence/tauceti-mahlermeasure.md)

## Proof depends on

- [Gauss's lemma at a nonarchimedean absolute value](../../../ring-theory/part-01/polynomial/gausss-lemma-at-a-nonarchimedean-absolute-value.md)
- [TauCeti.Polynomial.ncard_biUnion_roots_natDegree_le_abs_intCoeff_le](tauceti-polynomial-ncard-biunion-roots-natdegree.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.finite_setOf_naiveHeight_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Counting.html#TauCeti.finite_setOf_naiveHeight_le).

## Other forms

**Northcott's theorem for subspaces (Schmidt).** Formalized in Tau Ceti as [`Submodule.finite_subspaceHeight_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Arakelov/Subspace/Basic.html#Submodule.finite_subspaceHeight_le).

```lean
Submodule.finite_subspaceHeight_le.{u_1, u_2} {ι : Type u_1} {K : Type u_2} [LinearOrder ι]
  [Finite ι] [Field K] [NumberField K] (B : ℝ) : {U | U.subspaceHeight ≤ B}.Finite
```

**Northcott's theorem for the absolute height.** Formalized in Tau Ceti as [`TauCeti.finite_setOf_absMulHeight₁_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Absolute.html#TauCeti.finite_setOf_absMulHeight%E2%82%81_le).

```lean
TauCeti.finite_setOf_absMulHeight₁_le.{u_1} {F : Type u_1} [Field F] [CharZero F] (d : ℕ) (B : ℝ) :
  {x | IsAlgebraic ℚ x ∧ (minpoly ℚ x).natDegree ≤ d ∧ NumberField.absMulHeight₁ x ≤ B}.Finite
```

**Northcott's theorem for the Mahler measure.** Formalized in Tau Ceti as [`TauCeti.finite_setOf_mahlerMeasure_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/MahlerMeasure.html#TauCeti.finite_setOf_mahlerMeasure_le).

```lean
TauCeti.finite_setOf_mahlerMeasure_le.{u_1} {F : Type u_1} [Field F] [CharZero F] (d : ℕ) (B : ℝ) :
  {z | IsAlgebraic ℚ z ∧ (minpoly ℚ z).natDegree ≤ d ∧ TauCeti.mahlerMeasure z ≤ B}.Finite
```

## Sources

- [Tau Ceti documentation: `TauCeti.finite_setOf_naiveHeight_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Counting.html#TauCeti.finite_setOf_naiveHeight_le)
- [Source of `TauCeti.finite_setOf_naiveHeight_le` in TauCeti/NumberTheory/Height/Counting.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Height/Counting.lean#L49)
- [Tau Ceti roadmap status: Effective arithmetic bounds and geometry of numbers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/EffectiveBounds/STATUS.md)
