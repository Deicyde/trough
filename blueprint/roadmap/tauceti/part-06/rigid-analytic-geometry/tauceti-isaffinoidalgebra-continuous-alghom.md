---
declaration: theorem
origin: cited
lean: TauCeti.IsAffinoidAlgebra.continuous_algHom
statement: formalized
proof: formalized
---

# TauCeti.IsAffinoidAlgebra.continuous\_algHom

Every homomorphism from a noetherian ultrametric Banach algebra to a completely normed
affinoid algebra is continuous. The affinoid presentation is purely algebraic.

```lean
TauCeti.IsAffinoidAlgebra.continuous_algHom.{u_1, u_2, u_3} {K : Type u_1}
  [NontriviallyNormedField K] [IsUltrametricDist K] [CompleteSpace K] {A : Type u_2}
  [NormedCommRing A] [NormedAlgebra K A] [IsUltrametricDist A] [CompleteSpace A]
  (hA : TauCeti.IsAffinoidAlgebra K A) {B : Type u_3} [NormedCommRing B] [NormedAlgebra K B]
  [IsUltrametricDist B] [CompleteSpace B] [IsNoetherianRing B] (f : B →ₐ[K] A) : Continuous ⇑f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAffinoidAlgebra.continuous_algHom`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/Continuity.html#TauCeti.IsAffinoidAlgebra.continuous_algHom).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAffinoidAlgebra.continuous_algHom`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/Continuity.html#TauCeti.IsAffinoidAlgebra.continuous_algHom)
- [Source of `TauCeti.IsAffinoidAlgebra.continuous_algHom` in TauCeti/RingTheory/Affinoid/Continuity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Affinoid/Continuity.lean#L44)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
