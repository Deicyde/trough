---
declaration: abbrev
origin: cited
lean: TauCeti.classifyingSpaceLocalSystem
statement: formalized
---

# TauCeti.classifyingSpaceLocalSystem

The local coefficient system on Milnor's classifying space associated to a representation `A`
of `G`: its fibre over `x` is `(A ⊗ k[π⁻¹ x])_G`, where `π` is the orbit map of the countable join,
and transport along a path is induced by lifting it to the countable join.

```lean
TauCeti.classifyingSpaceLocalSystem.{u} (k : Type u) [CommRing k] {G : Type u} [Group G]
  (A : Rep.{u, u, u} k G) : TauCeti.LocalCoefficientSystem k ↧(TauCeti.classifyingSpace G)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.classifyingSpaceLocalSystem`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/LocalCoefficients.html#TauCeti.classifyingSpaceLocalSystem).

## Sources

- [Tau Ceti documentation: `TauCeti.classifyingSpaceLocalSystem`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/LocalCoefficients.html#TauCeti.classifyingSpaceLocalSystem)
- [Source of `TauCeti.classifyingSpaceLocalSystem` in TauCeti/AlgebraicTopology/ClassifyingSpace/LocalCoefficients.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/ClassifyingSpace/LocalCoefficients.lean#L212)
- [Tau Ceti roadmap status: Classifying spaces of discrete groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ClassifyingSpaces/STATUS.md)
