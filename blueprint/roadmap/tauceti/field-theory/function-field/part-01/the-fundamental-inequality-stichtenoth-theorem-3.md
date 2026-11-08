---
declaration: theorem
origin: cited
lean: TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_le_finrank
statement: formalized
proof: formalized
---

# The fundamental inequality (Stichtenoth, Theorem 3.1.11)

the ramification indices and
relative degrees of finitely many distinct places of `F' / k'` lying over one place `P` of
`F / k` satisfy `∑ e(P' ∣ P) · f(P' ∣ P) ≤ [F' : F]`.

The reverse inequality — the fundamental *identity* — is not proved here; it is the affine-model
reconciliation with `Ideal.sum_ramification_inertia`.

```lean
TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_le_finrank.{u, u', v, v'} (k : Type u)
  {k' : Type u'} (F : Type v) {F' : Type v'} [Field k] [Field k'] [Field F] [Field F']
  [Algebra k k'] [Algebra k F] [Algebra k' F'] [Algebra F F'] [Algebra k F'] [IsScalarTower k k' F']
  [IsScalarTower k F F'] [FiniteDimensional F F'] (P : TauCeti.Place k F)
  (s : Finset (TauCeti.Place k' F')) (hs : ∀ P' ∈ s, TauCeti.Place.restrict k F P' = P) :
  ∑ P' ∈ s, TauCeti.Place.ramificationIdx F P' * TauCeti.Place.relativeDegree k F P' ≤
    Module.finrank F F'
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The weak approximation theorem](the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_le_finrank`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Fibre.html#TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_le_finrank).

## Sources

- [Tau Ceti documentation: `TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_le_finrank`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Fibre.html#TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_le_finrank)
- [Source of `TauCeti.Place.sum_ramificationIdx_mul_relativeDegree_le_finrank` in TauCeti/FieldTheory/FunctionField/Place/Extension/Fibre.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/Place/Extension/Fibre.lean#L293)
