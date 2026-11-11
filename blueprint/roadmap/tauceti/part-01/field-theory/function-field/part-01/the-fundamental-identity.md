---
declaration: theorem
origin: cited
lean: TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank, TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank_of_isFunctionField, TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank_of_isSeparable
statement: formalized
proof: formalized
---

# The fundamental identity

**The fundamental identity** (Stichtenoth, Theorem 3.1.11) at a place of the finite chart of a
model: the ramification indices and relative degrees of the places of `F' / k'` lying over the
place of a height one prime `𝔭` of `R` satisfy `∑ e(P' ∣ P) · f(P' ∣ P) = [F' : F]`. Together with
`TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_le_finrank` this settles the fibre over every
place that lies on some affine model.

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

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Krull–Akizuki for Mathlib's `integralClosure`](../../../ring-theory/part-02/other-results/part-02/krull-akizuki-for-mathlibs-integralclosure.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/AffineModel/Extension.html#TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank).

## Other forms

**TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank_of_isFunctionField.** Formalized in Tau Ceti as [`TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank_of_isFunctionField`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Fundamental.html#TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank_of_isFunctionField).

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

**The fundamental identity.** Formalized in Tau Ceti as [`TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank_of_isSeparable`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Fundamental.html#TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank_of_isSeparable).

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

- [Tau Ceti documentation: `TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/AffineModel/Extension.html#TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank)
- [Source of `TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_eq_finrank` in TauCeti/FieldTheory/FunctionField/AffineModel/Extension.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/FieldTheory/FunctionField/AffineModel/Extension.lean#L302)
