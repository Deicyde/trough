---
declaration: theorem
origin: cited
lean: TauCeti.Place.ramificationIdx_le_differentExponent_add_one, TauCeti.Divisor.ramificationIdx_le_coeff_different_add_one, TauCeti.Divisor.tameDifferent_le_different, TauCeti.Place.ramificationIdx_eq_differentExponent_add_one_iff
statement: formalized
proof: formalized
---

# Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))

the different
exponent of a place is at least one less than its ramification index.  It is stated as
`e(P' ∣ P) ≤ d(P' ∣ P) + 1` so that no truncated subtraction of natural numbers appears.

Unlike the second part of that theorem — equality exactly in the tame case — this half needs no
hypothesis beyond separability of `F' / F`, and in particular none on the residue extension.

```lean
TauCeti.Place.ramificationIdx_le_differentExponent_add_one.{u, u', v, v'} (k : Type u)
  {k' : Type u'} (F : Type v) {F' : Type v'} [Field k] [Field F] [Field F'] [Algebra k F]
  [Algebra F F'] [Field k'] [Algebra k k'] [Algebra k' F'] [Algebra k F'] [IsScalarTower k k' F']
  [IsScalarTower k F F'] [FiniteDimensional F F'] (P' : TauCeti.Place k' F')
  [Algebra.IsSeparable F F'] :
  TauCeti.Place.ramificationIdx F P' ≤ TauCeti.Place.differentExponent k F P' + 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dedekind's different theorem, the tame case, as an exponent](../../../ring-theory/part-02/other-results/part-01/dedekinds-different-theorem-the-tame-case-as-an.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](the-fundamental-inequality-stichtenoth-theorem-3.md)
- [The weak approximation theorem](../part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Place.ramificationIdx_le_differentExponent_add_one`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Different/Basic.html#TauCeti.Place.ramificationIdx_le_differentExponent_add_one).

## Other forms

**Dedekind's different theorem (Stichtenoth, Theorem 3.5.1(a)) at the level of divisors.** Formalized in Tau Ceti as [`TauCeti.Divisor.ramificationIdx_le_coeff_different_add_one`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Different/Divisor.html#TauCeti.Divisor.ramificationIdx_le_coeff_different_add_one).

```lean
TauCeti.Divisor.ramificationIdx_le_coeff_different_add_one.{u, u', v, v'} {k : Type u}
  (k' : Type u') {F : Type v} (F' : Type v') [Field k] [Field k'] [Field F] [Field F']
  [Algebra k k'] [Algebra k F] [Algebra k' F'] [Algebra F F'] [Algebra k F'] [IsScalarTower k k' F']
  [IsScalarTower k F F'] [FiniteDimensional F F'] [Algebra.IsSeparable F F']
  (hF : TauCeti.IsFunctionField k F) (P' : TauCeti.Place k' F') :
  ↑(TauCeti.Place.ramificationIdx F P') ≤
    TauCeti.AlgebraicGeometry.WeilDivisor.coeff (TauCeti.Divisor.different k' F' hF) P' + 1
```

**Dedekind's different theorem, first part, as an inequality of divisors (Stichtenoth, Theorem 3.5.1(a)).** Formalized in Tau Ceti as [`TauCeti.Divisor.tameDifferent_le_different`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Different/Tame.html#TauCeti.Divisor.tameDifferent_le_different).

```lean
TauCeti.Divisor.tameDifferent_le_different.{u, u', v, v'} {k : Type u} (k' : Type u') {F : Type v}
  (F' : Type v') [Field k] [Field k'] [Field F] [Field F'] [Algebra k F] [Algebra F F']
  [Algebra k k'] [Algebra k' F'] [Algebra k F'] [IsScalarTower k k' F'] [IsScalarTower k F F']
  [FiniteDimensional F F'] [Algebra.IsSeparable F F'] (hF : TauCeti.IsFunctionField k F) :
  TauCeti.Divisor.tameDifferent k' F' hF ≤ TauCeti.Divisor.different k' F' hF
```

**Dedekind's different theorem, second part (Stichtenoth, Theorem 3.5.1(b)).** Formalized in Tau Ceti as [`TauCeti.Place.ramificationIdx_eq_differentExponent_add_one_iff`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Different/Tame.html#TauCeti.Place.ramificationIdx_eq_differentExponent_add_one_iff).

```lean
TauCeti.Place.ramificationIdx_eq_differentExponent_add_one_iff.{u, u', v, v'} (k : Type u)
  {k' : Type u'} (F : Type v) {F' : Type v'} [Field k] [Field k'] [Field F] [Field F'] [Algebra k F]
  [Algebra F F'] [Algebra k k'] [Algebra k' F'] [Algebra k F'] [IsScalarTower k k' F']
  [IsScalarTower k F F'] [FiniteDimensional F F'] [Algebra.IsSeparable F F']
  (P' : TauCeti.Place k' F') :
  TauCeti.Place.ramificationIdx F P' = TauCeti.Place.differentExponent k F P' + 1 ↔
    TauCeti.Place.IsTame k F P'
```

## Sources

- [Tau Ceti documentation: `TauCeti.Place.ramificationIdx_le_differentExponent_add_one`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Different/Basic.html#TauCeti.Place.ramificationIdx_le_differentExponent_add_one)
- [Source of `TauCeti.Place.ramificationIdx_le_differentExponent_add_one` in TauCeti/FieldTheory/FunctionField/Different/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/FieldTheory/FunctionField/Different/Basic.lean#L236)
