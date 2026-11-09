---
declaration: theorem
origin: cited
lean: TauCeti.isSemialgebraic_iff_definable_ring_real, TauCeti.isSemialgebraic_iff_definable_ring
statement: formalized
proof: formalized
---

# Tarski's theorem for the real field

A subset of `σ → ℝ` is semialgebraic if and only if
it is definable with parameters in the field `ℝ`, that is, in the language of rings with its usual
interpretation.

```lean
TauCeti.isSemialgebraic_iff_definable_ring_real.{u_2} {σ : Type u_2} {s : Set (σ → ℝ)} :
  TauCeti.IsSemialgebraic s ↔ Set.univ.Definable FirstOrder.Language.ring s
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Tarski–Seidenberg theorem](the-tarski-seidenberg-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isSemialgebraic_iff_definable_ring_real`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Semialgebraic/RingLanguage.html#TauCeti.isSemialgebraic_iff_definable_ring_real).

## Other forms

**Tarski's theorem in the field language.** Formalized in Tau Ceti as [`TauCeti.isSemialgebraic_iff_definable_ring`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Semialgebraic/RingLanguage.html#TauCeti.isSemialgebraic_iff_definable_ring).

```lean
TauCeti.isSemialgebraic_iff_definable_ring.{u_1, u_2} {R : Type u_1} [Field R]
  [FirstOrder.Ring.CompatibleRing R] [LinearOrder R] [IsStrictOrderedRing R] [IsRealClosed R]
  {σ : Type u_2} [TauCeti.HasSemialgebraicProjections R] {s : Set (σ → R)} :
  TauCeti.IsSemialgebraic s ↔ Set.univ.Definable FirstOrder.Language.ring s
```

## Sources

- [Tau Ceti documentation: `TauCeti.isSemialgebraic_iff_definable_ring_real`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Semialgebraic/RingLanguage.html#TauCeti.isSemialgebraic_iff_definable_ring_real)
- [Source of `TauCeti.isSemialgebraic_iff_definable_ring_real` in TauCeti/Geometry/RealAlgebraic/Semialgebraic/RingLanguage.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/RealAlgebraic/Semialgebraic/RingLanguage.lean#L123)
- [Tau Ceti roadmap status: Real algebraic geometry: sign determination and cylindrical decomposition](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/RealAlgebraicGeometry/STATUS.md)
