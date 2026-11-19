---
declaration: abbrev
origin: cited
lean: TauCeti.Huber.tateNormedCommRing
statement: formalized
---

# TauCeti.Huber.tateNormedCommRing

The explicitly chosen gauge normed ring, with the original uniformity and topology.
This is an abbreviation so that the inherited ring and uniform space remain definitionally
unchanged for consumers. It is not a global instance: different data can give different norms.

```lean
TauCeti.Huber.tateNormedCommRing.{u_1} {A : Type u_1} [CommRing A] [UniformSpace A]
  [IsUniformAddGroup A] [IsTopologicalRing A] [T2Space A] (d : TauCeti.Huber.TateNormDatum A) :
  NormedCommRing A
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.tateNormedCommRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/TateGauge/Normed.html#TauCeti.Huber.tateNormedCommRing).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.tateNormedCommRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/TateGauge/Normed.html#TauCeti.Huber.tateNormedCommRing)
- [Source of `TauCeti.Huber.tateNormedCommRing` in TauCeti/RingTheory/Huber/TateGauge/Normed.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Huber/TateGauge/Normed.lean#L77)
- [Tau Ceti roadmap status: P-adic functional analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PadicFunctionalAnalysis/STATUS.md)
