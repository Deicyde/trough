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

- [The Tarski–Seidenberg theorem](../../part-01/complex-morse-theory-affine-topology-and-weak-le/the-tarski-seidenberg-theorem.md)

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
- [Source of `TauCeti.isSemialgebraic_iff_definable_ring_real` in TauCeti/Geometry/RealAlgebraic/Semialgebraic/RingLanguage.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/RealAlgebraic/Semialgebraic/RingLanguage.lean#L123)
