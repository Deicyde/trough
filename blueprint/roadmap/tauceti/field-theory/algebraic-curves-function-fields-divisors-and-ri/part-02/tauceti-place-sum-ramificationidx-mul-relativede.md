---
declaration: theorem
origin: cited
lean: TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank_of_isFunctionField, TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank, TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank_of_isSeparable
statement: formalized
proof: formalized
---

# TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank_of_isFunctionField

**The fundamental identity** (Stichtenoth, Theorem 3.1.11) at an arbitrary place `P` of an
algebraic function field `F / k`, for an extension `F' / k'` whose extension of function fields
`F' / F` is finite, **with no separability hypothesis**: the ramification indices and relative
degrees of the places of `F' / k'` lying over `P` satisfy
`∑_{P' ∣ P} e(P' ∣ P) · f(P' ∣ P) = [F' : F]`.

The finite set `s` is the fibre of `TauCeti.Place.restrict` over `P`, which is finite by
`TauCeti.Place.finite_setOf_restrict_eq`.

For a separable `F' / F` the identity holds without assuming that `F / k` is a function field;
that is `TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank_of_isSeparable`.

```lean
TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank_of_isFunctionField.{u, u', v, v'}
  (k : Type u) {k' : Type u'} (F : Type v) {F' : Type v'} [Field k] [Field k'] [Field F] [Field F']
  [Algebra k k'] [Algebra k F] [Algebra k' F'] [Algebra F F'] [Algebra k F'] [IsScalarTower k k' F']
  [IsScalarTower k F F'] [FiniteDimensional F F'] [Algebra.IsIntegral k k']
  (hF : TauCeti.IsFunctionField k F) (P : TauCeti.Place k F) {s : Finset (TauCeti.Place k' F')}
  (hs : ∀ (P' : TauCeti.Place k' F'), P' ∈ s ↔ TauCeti.Place.restrict k F P' = P) :
  ∑ P' ∈ s, TauCeti.Place.ramificationIdx F P' * TauCeti.Place.relativeDegree k F P' =
    Module.finrank F F'
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Krull–Akizuki's length bound](../../../ring-theory/other-results/part-01/krull-akizukis-length-bound.md)
- [TauCeti.Ring.IsJapanese](../../../ring-theory/scheme-stack-cohomology-and-intersection-foundat/tauceti-ring-isjapanese.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank_of_isFunctionField`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Fundamental.html#TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank_of_isFunctionField).

## Other forms

**The fundamental identity (Stichtenoth, Theorem 3.1.11) at a place of the finite chart of a model.** Formalized in Tau Ceti as [`TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/AffineModel/Extension.html#TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank).

```lean
TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank.{u, u', v, v', w, w'} (k : Type u)
  {k' : Type u'} (F : Type v) {F' : Type v'} [Field k] [Field k'] [Field F] [Field F']
  [Algebra k k'] [Algebra k F] [Algebra k' F'] [Algebra F F'] [Algebra k F'] [IsScalarTower k k' F']
  [IsScalarTower k F F'] {R : Type w} [CommRing R] [Algebra R F] (S : Type w') [CommRing S]
  [Algebra S F'] [Algebra R S] [Algebra R F'] [IsScalarTower R S F'] [IsScalarTower R F F']
  [Algebra.IsIntegral F F'] [IsDedekindDomain R] [IsDedekindDomain S] [IsFractionRing R F]
  [IsFractionRing S F'] [Algebra k' S] [IsScalarTower k' S F'] [Algebra k R] [IsScalarTower k R F]
  (𝔭 : IsDedekindDomain.HeightOneSpectrum R) [Module.Finite R S] {s : Finset (TauCeti.Place k' F')}
  (hs :
    ∀ (P' : TauCeti.Place k' F'),
      P' ∈ s ↔ TauCeti.Place.restrict k F P' = TauCeti.Place.ofPrime k F 𝔭) :
  ∑ P' ∈ s, TauCeti.Place.ramificationIdx F P' * TauCeti.Place.relativeDegree k F P' =
    Module.finrank F F'
```

**The fundamental identity (Stichtenoth, Theorem 3.1.11) at an arbitrary place `P` of `F / k`, for an extension `F' / k'` whose extension of function fields `F' / F` is finite and **separable**.** Formalized in Tau Ceti as [`TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank_of_isSeparable`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Fundamental.html#TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank_of_isSeparable).

```lean
TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank_of_isSeparable.{u, u', v, v'}
  (k : Type u) {k' : Type u'} (F : Type v) {F' : Type v'} [Field k] [Field k'] [Field F] [Field F']
  [Algebra k k'] [Algebra k F] [Algebra k' F'] [Algebra F F'] [Algebra k F'] [IsScalarTower k k' F']
  [IsScalarTower k F F'] [FiniteDimensional F F'] [Algebra.IsIntegral k k']
  [Algebra.IsSeparable F F'] (P : TauCeti.Place k F) {s : Finset (TauCeti.Place k' F')}
  (hs : ∀ (P' : TauCeti.Place k' F'), P' ∈ s ↔ TauCeti.Place.restrict k F P' = P) :
  ∑ P' ∈ s, TauCeti.Place.ramificationIdx F P' * TauCeti.Place.relativeDegree k F P' =
    Module.finrank F F'
```

## Sources

- [Tau Ceti documentation: `TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank_of_isFunctionField`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Fundamental.html#TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank_of_isFunctionField)
- [Source of `TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank_of_isFunctionField` in TauCeti/FieldTheory/FunctionField/Place/Extension/Fundamental.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/Place/Extension/Fundamental.lean#L122)
