---
declaration: abbrev
origin: cited
lean: TauCeti.PositiveDegrees.truncatedLie
statement: formalized
---

# TauCeti.PositiveDegrees.truncatedLie

The order-`k` Lie truncation, retaining the homogeneous degrees at most `k`.

```lean
TauCeti.PositiveDegrees.truncatedLie.{u_1, u_2, u_3} {N : Type u_1} [AddCommMonoid N] {R : Type u_2}
  {L : Type u_3} [CommRing R] [LieRing L] [LieAlgebra R L] (d : TauCeti.PositiveDegrees N)
  (ℒ : N → Submodule R L) [DecidableEq N] [GradedLieAlgebra ℒ] [TauCeti.IsPositiveGrading d ℒ]
  (k : ℕ) : Type u_3
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PositiveDegrees.truncatedLie`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Graded/Truncation.html#TauCeti.PositiveDegrees.truncatedLie).

## Sources

- [Tau Ceti documentation: `TauCeti.PositiveDegrees.truncatedLie`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Graded/Truncation.html#TauCeti.PositiveDegrees.truncatedLie)
- [Source of `TauCeti.PositiveDegrees.truncatedLie` in TauCeti/Algebra/Lie/Graded/Truncation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Lie/Graded/Truncation.lean#L134)
- [Tau Ceti roadmap status: Scattering diagrams, wall crossing and theta functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ScatteringDiagrams/STATUS.md)
