---
declaration: theorem
origin: cited
lean: TauCeti.Huber.henselianRing_powerBoundedSubring
statement: formalized
proof: formalized
---

# TauCeti.Huber.henselianRing_powerBoundedSubring

The power-bounded elements of a complete Hausdorff Tate ring are henselian along a
pseudouniformizer, even when they are not adically separated.

```lean
TauCeti.Huber.henselianRing_powerBoundedSubring.{u_1} {A : Type u_1} [CommRing A] [UniformSpace A]
  [IsUniformAddGroup A] [IsTopologicalRing A] [TauCeti.Huber.IsHuberRing A] [CompleteSpace A]
  [T0Space A] (ϖ : ↥(TauCeti.Huber.powerBoundedSubring A))
  (hϖ : TauCeti.Huber.IsPseudoUniformizer ↑ϖ) :
  HenselianRing (↥(TauCeti.Huber.powerBoundedSubring A)) (Ideal.span {ϖ})
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.henselianRing_powerBoundedSubring`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/Henselian.html#TauCeti.Huber.henselianRing_powerBoundedSubring).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.henselianRing_powerBoundedSubring`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/Henselian.html#TauCeti.Huber.henselianRing_powerBoundedSubring)
- [Source of `TauCeti.Huber.henselianRing_powerBoundedSubring` in TauCeti/RingTheory/Huber/Henselian.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Huber/Henselian.lean#L107)
- [Tau Ceti roadmap status: Analytic adic geometry for diamonds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicEtaleGeometry/STATUS.md)
