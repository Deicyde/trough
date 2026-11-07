---
declaration: def
origin: cited
lean: TauCeti.IsAffinoidAlgebra.toContinuousAlgEquiv
statement: formalized
---

# Equivalence of complete affinoid norms

An algebra isomorphism between completely normed
affinoid algebras is a homeomorphism, whatever complete ultrametric algebra norms they carry.
Applied to two such norms on one algebra, this says that they define the same topology.

```lean
TauCeti.IsAffinoidAlgebra.toContinuousAlgEquiv.{u_1, u_2, u_3} {K : Type u_1}
  [NontriviallyNormedField K] [IsUltrametricDist K] [CompleteSpace K] {A : Type u_2}
  [NormedCommRing A] [NormedAlgebra K A] [IsUltrametricDist A] [CompleteSpace A] {B : Type u_3}
  [NormedCommRing B] [NormedAlgebra K B] [IsUltrametricDist B] [CompleteSpace B]
  (hB : TauCeti.IsAffinoidAlgebra K B) (e : A ≃ₐ[K] B) : A ≃A[K] B
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.IsAffinoidAlgebra.continuous\_algHom](tauceti-isaffinoidalgebra-continuous-alghom.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAffinoidAlgebra.toContinuousAlgEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/QuotientNorm.html#TauCeti.IsAffinoidAlgebra.toContinuousAlgEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAffinoidAlgebra.toContinuousAlgEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/QuotientNorm.html#TauCeti.IsAffinoidAlgebra.toContinuousAlgEquiv)
- [Source of `TauCeti.IsAffinoidAlgebra.toContinuousAlgEquiv` in TauCeti/RingTheory/Affinoid/QuotientNorm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Affinoid/QuotientNorm.lean#L95)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
