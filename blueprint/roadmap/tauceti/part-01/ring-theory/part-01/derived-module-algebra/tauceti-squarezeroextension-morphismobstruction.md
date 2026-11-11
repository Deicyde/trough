---
declaration: theorem
origin: cited
lean: TauCeti.SquareZeroExtension.morphismObstruction_eq_zero_iff
statement: formalized
proof: formalized
---

# TauCeti.SquareZeroExtension.morphismObstruction_eq_zero_iff

The obstruction vanishes exactly when the algebra map `T → B` lifts through `E → B`.

```lean
TauCeti.SquareZeroExtension.morphismObstruction_eq_zero_iff.{u, v, t} {A : Type u} {B : Type v}
  (T : Type v) {M : Type t} [CommRing A] [CommRing B] [Algebra A B] [AddCommGroup M]
  [_root_.Module B M] [CommRing T] [Algebra A T] [Algebra T B] [IsScalarTower A T B]
  [_root_.Module T M] [IsScalarTower T B M] [_root_.Module Tᵐᵒᵖ M] [IsCentralScalar T M]
  [_root_.Module A M] [IsScalarTower A T M] [IsScalarTower A Tᵐᵒᵖ M]
  (E : TauCeti.SquareZeroExtension A B M) :
  E.morphismObstruction T = 0 ↔ ∃ g, E.π.comp g = IsScalarTower.toAlgHom A T B
```

## Depends on

- [TauCeti.Exal](tauceti-exal.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SquareZeroExtension.morphismObstruction_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/Extension/SquareZero/Pullback.html#TauCeti.SquareZeroExtension.morphismObstruction_eq_zero_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.SquareZeroExtension.morphismObstruction_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/Extension/SquareZero/Pullback.html#TauCeti.SquareZeroExtension.morphismObstruction_eq_zero_iff)
- [Source of `TauCeti.SquareZeroExtension.morphismObstruction_eq_zero_iff` in TauCeti/RingTheory/Extension/SquareZero/Pullback.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Extension/SquareZero/Pullback.lean#L260)
- [Tau Ceti roadmap status: Derived module algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DerivedModuleAlgebra/STATUS.md)
