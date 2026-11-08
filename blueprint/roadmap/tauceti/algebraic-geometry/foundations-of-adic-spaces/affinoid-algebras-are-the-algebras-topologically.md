---
declaration: theorem
origin: cited
lean: TauCeti.Huber.isTopologicallyFiniteType_algebraMap_iff_isAffinoidAlgebra
statement: formalized
proof: formalized
---

# Affinoid algebras are the algebras topologically of finite type

A complete ultrametric
normed `K`-algebra `B` is topologically of finite type over `K` in Huber's sense (Wedhorn,
Definition 5.57) exactly when it is a quotient of a Tate algebra `K⟨X₁, …, Xₙ⟩` as a
`K`-algebra.

```lean
TauCeti.Huber.isTopologicallyFiniteType_algebraMap_iff_isAffinoidAlgebra.{u_1, u_2} {K : Type u_1}
  [NontriviallyNormedField K] [IsUltrametricDist K] [CompleteSpace K] {B : Type u_2}
  [NormedCommRing B] [NormedAlgebra K B] [IsUltrametricDist B] [CompleteSpace B] :
  TauCeti.Huber.IsTopologicallyFiniteType (algebraMap K B) ↔ TauCeti.IsAffinoidAlgebra K B
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Kedlaya's Hilbert basis theorem for restricted power series](../../ring-theory/part-01/mv-power-series/kedlayas-hilbert-basis-theorem-for-restricted-po.md)
- [The open mapping theorem over a Tate ring](../../ring-theory/part-01/huber/the-open-mapping-theorem-over-a-tate-ring.md)
- [TauCeti.IsAffinoidAlgebra.continuous_algHom](../../ring-theory/part-01/rigid-analytic-geometry/tauceti-isaffinoidalgebra-continuous-alghom.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.isTopologicallyFiniteType_algebraMap_iff_isAffinoidAlgebra`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/TopologicallyFiniteType.html#TauCeti.Huber.isTopologicallyFiniteType_algebraMap_iff_isAffinoidAlgebra).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.isTopologicallyFiniteType_algebraMap_iff_isAffinoidAlgebra`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/TopologicallyFiniteType.html#TauCeti.Huber.isTopologicallyFiniteType_algebraMap_iff_isAffinoidAlgebra)
- [Source of `TauCeti.Huber.isTopologicallyFiniteType_algebraMap_iff_isAffinoidAlgebra` in TauCeti/RingTheory/Affinoid/TopologicallyFiniteType.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Affinoid/TopologicallyFiniteType.lean#L98)
- [Tau Ceti roadmap status: Foundations of adic spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/AdicSpaces/STATUS.md)
