---
declaration: theorem
origin: cited
lean: TauCeti.IsAffinoidAlgebra.height_eq_ringKrullDim_of_isDomain
statement: formalized
proof: formalized
---

# Heights of maximal ideals of affinoid domains

Every maximal ideal of an affinoid domain
`A` has height `dim A`.

```lean
TauCeti.IsAffinoidAlgebra.height_eq_ringKrullDim_of_isDomain.{u_1, u_2} {K : Type u_1}
  [NormedField K] [IsUltrametricDist K] [CompleteSpace K] {A : Type u_2} [CommRing A] [Algebra K A]
  [IsDomain A] (hA : TauCeti.IsAffinoidAlgebra K A) (m : Ideal A) [m.IsMaximal] :
  ↑m.height = ringKrullDim A
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Affinoid Noether normalisation](affinoid-noether-normalisation.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAffinoidAlgebra.height_eq_ringKrullDim_of_isDomain`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/KrullDimension.html#TauCeti.IsAffinoidAlgebra.height_eq_ringKrullDim_of_isDomain).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAffinoidAlgebra.height_eq_ringKrullDim_of_isDomain`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/KrullDimension.html#TauCeti.IsAffinoidAlgebra.height_eq_ringKrullDim_of_isDomain)
- [Source of `TauCeti.IsAffinoidAlgebra.height_eq_ringKrullDim_of_isDomain` in TauCeti/RingTheory/Affinoid/KrullDimension.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Affinoid/KrullDimension.lean#L95)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
