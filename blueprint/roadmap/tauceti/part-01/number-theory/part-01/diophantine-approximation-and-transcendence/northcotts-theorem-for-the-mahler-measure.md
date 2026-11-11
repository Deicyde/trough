---
declaration: theorem
origin: cited
lean: TauCeti.finite_setOf_mahlerMeasure_le, Submodule.finite_subspaceHeight_le, TauCeti.finite_setOf_absMulHeight₁_le, TauCeti.finite_setOf_naiveHeight_le
statement: formalized
proof: formalized
---

# Northcott's theorem for the Mahler measure

In a field of characteristic zero, there are
only finitely many algebraic elements of degree at most `d` and Mahler measure at most `B`.

```lean
TauCeti.finite_setOf_mahlerMeasure_le.{u_1} {F : Type u_1} [Field F] [CharZero F] (d : ℕ) (B : ℝ) :
  {z | IsAlgebraic ℚ z ∧ (minpoly ℚ z).natDegree ≤ d ∧ TauCeti.mahlerMeasure z ≤ B}.Finite
```

## Depends on

- [TauCeti.mahlerMeasure](tauceti-mahlermeasure.md)

## Proof depends on

- [Gauss's lemma at a nonarchimedean absolute value](../../../ring-theory/part-01/polynomial/gausss-lemma-at-a-nonarchimedean-absolute-value.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.finite_setOf_mahlerMeasure_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/MahlerMeasure.html#TauCeti.finite_setOf_mahlerMeasure_le).

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

**Northcott's theorem for the naive height, with Evertse's count.** Formalized in Tau Ceti as [`TauCeti.finite_setOf_naiveHeight_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Counting.html#TauCeti.finite_setOf_naiveHeight_le).

```lean
TauCeti.finite_setOf_naiveHeight_le.{u_1} {F : Type u_1} [Field F] [CharZero F] (d : ℕ) (B : ℝ) :
  {z | IsAlgebraic ℚ z ∧ (minpoly ℚ z).natDegree ≤ d ∧ TauCeti.naiveHeight z ≤ B}.Finite ∧
    {z | IsAlgebraic ℚ z ∧ (minpoly ℚ z).natDegree ≤ d ∧ TauCeti.naiveHeight z ≤ B}.ncard ≤
      d * (2 * ⌊B⌋₊ + 1) ^ (d + 1)
```

## Sources

- [Tau Ceti documentation: `TauCeti.finite_setOf_mahlerMeasure_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/MahlerMeasure.html#TauCeti.finite_setOf_mahlerMeasure_le)
- [Source of `TauCeti.finite_setOf_mahlerMeasure_le` in TauCeti/NumberTheory/Height/MahlerMeasure.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Height/MahlerMeasure.lean#L186)
