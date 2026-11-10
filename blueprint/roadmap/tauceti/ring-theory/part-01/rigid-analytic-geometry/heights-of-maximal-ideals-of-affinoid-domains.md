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
- [Kedlaya's Hilbert basis theorem for restricted power series](../mv-power-series/kedlayas-hilbert-basis-theorem-for-restricted-po.md)
- [The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2)](../p-adic-measures-completed-group-algebras-and-cha/part-01/the-weierstrass-division-estimate-bosch-guntzer.md)
- [The Weierstrass division identity](../p-adic-measures-completed-group-algebras-and-cha/part-01/the-weierstrass-division-identity.md)
- [Weierstrass preparation](../p-adic-measures-completed-group-algebras-and-cha/part-01/weierstrass-preparation.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAffinoidAlgebra.height_eq_ringKrullDim_of_isDomain`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/KrullDimension.html#TauCeti.IsAffinoidAlgebra.height_eq_ringKrullDim_of_isDomain).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAffinoidAlgebra.height_eq_ringKrullDim_of_isDomain`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/KrullDimension.html#TauCeti.IsAffinoidAlgebra.height_eq_ringKrullDim_of_isDomain)
- [Source of `TauCeti.IsAffinoidAlgebra.height_eq_ringKrullDim_of_isDomain` in TauCeti/RingTheory/Affinoid/KrullDimension.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Affinoid/KrullDimension.lean#L95)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
