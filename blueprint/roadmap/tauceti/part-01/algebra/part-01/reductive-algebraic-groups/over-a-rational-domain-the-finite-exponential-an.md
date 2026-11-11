---
declaration: def
origin: cited
lean: TauCeti.GeneralLinear.expEquivHopfIdealPoints
statement: formalized
---

# Over a rational domain, the finite exponential and logarithm identify the nilpotent elements of the Lie algebra of a closed subgroup of `GLₙ` with its unipotent points

This is an
equivalence of sets, not of groups.

```lean
TauCeti.GeneralLinear.expEquivHopfIdealPoints.{u} {R : Type u} [CommRing R] (n : ℕ) [Algebra ℚ R]
  [IsDomain R] (I : TauCeti.HopfIdeal R ↑(TauCeti.GeneralLinear.coordinateHopfAlgebra R n)) :
  { X //
      X ∈
          LieSubalgebra.map (TauCeti.GeneralLinear.tangentLieEquivMatrix n).toLieHom
            I.lieSubalgebra ∧
        IsNilpotent X } ≃
    { g // g ∈ TauCeti.GeneralLinear.hopfIdealPointsSubgroup n I R ∧ IsNilpotent (↑g - 1) }
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GeneralLinear.expEquivHopfIdealPoints`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Unipotent/Exponential.html#TauCeti.GeneralLinear.expEquivHopfIdealPoints).

## Sources

- [Tau Ceti documentation: `TauCeti.GeneralLinear.expEquivHopfIdealPoints`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Unipotent/Exponential.html#TauCeti.GeneralLinear.expEquivHopfIdealPoints)
- [Source of `TauCeti.GeneralLinear.expEquivHopfIdealPoints` in TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Unipotent/Exponential.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Unipotent/Exponential.lean#L183)
- [Tau Ceti roadmap status: Reductive algebraic groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ReductiveGroups/STATUS.md)
