---
declaration: def
origin: cited
lean: TauCeti.PositiveDegrees.completionLieEquivPi
statement: formalized
---

# TauCeti.PositiveDegrees.completionLieEquivPi

Homogeneous coefficients identify the completed Lie algebra with the convolution
Lie algebra on the product of its homogeneous pieces.

```lean
TauCeti.PositiveDegrees.completionLieEquivPi.{u_1, u_2, u_3} {N : Type u_1} {R : Type u_2}
  {L : Type u_3} [AddCommMonoid N] [CommRing R] [LieRing L] [LieAlgebra R L]
  (d : TauCeti.PositiveDegrees N) (ℒ : N → Submodule R L) [DecidableEq N] [GradedLieAlgebra ℒ]
  [TauCeti.IsPositiveGrading d ℒ] : ↥(d.completedLie ℒ) ≃ₗ⁅R⁆ (n : N) → ↥(ℒ n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PositiveDegrees.completionLieEquivPi`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Graded/Completion.html#TauCeti.PositiveDegrees.completionLieEquivPi).

## Sources

- [Tau Ceti documentation: `TauCeti.PositiveDegrees.completionLieEquivPi`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Graded/Completion.html#TauCeti.PositiveDegrees.completionLieEquivPi)
- [Source of `TauCeti.PositiveDegrees.completionLieEquivPi` in TauCeti/Algebra/Lie/Graded/Completion.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Lie/Graded/Completion.lean#L180)
- [Tau Ceti roadmap status: Scattering diagrams, wall crossing and theta functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ScatteringDiagrams/STATUS.md)
