---
declaration: theorem
origin: cited
lean: TauCeti.IsAffinoidAlgebra.isRestricted_subring
statement: formalized
proof: formalized
---

# Restricted series over an affinoid algebra form an affinoid algebra

For an affinoid
algebra `A` with a complete ultrametric algebra norm, the Gauss-normed algebra `A⟨X₁, …, Xₘ⟩` of
unit-radius restricted series is affinoid: a Tate presentation `K⟨Y₁, …, Yₙ⟩ → A` induces a
presentation `K⟨X₁, …, Xₘ, Y₁, …, Yₙ⟩ → A⟨X₁, …, Xₘ⟩`.

```lean
TauCeti.IsAffinoidAlgebra.isRestricted_subring.{u_1, u_2, u_3} {K : Type u_1}
  [NontriviallyNormedField K] [IsUltrametricDist K] [CompleteSpace K] {A : Type u_2}
  [NormedCommRing A] [NormedAlgebra K A] [IsUltrametricDist A] [CompleteSpace A] {τ : Type u_3}
  [Finite τ] (hA : TauCeti.IsAffinoidAlgebra K A) :
  TauCeti.IsAffinoidAlgebra K ↥(MvPowerSeries.IsRestricted.subring fun x => 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.IsAffinoidAlgebra.continuous\_algHom](tauceti-isaffinoidalgebra-continuous-alghom.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAffinoidAlgebra.isRestricted_subring`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/Restricted.html#TauCeti.IsAffinoidAlgebra.isRestricted_subring).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAffinoidAlgebra.isRestricted_subring`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/Restricted.html#TauCeti.IsAffinoidAlgebra.isRestricted_subring)
- [Source of `TauCeti.IsAffinoidAlgebra.isRestricted_subring` in TauCeti/RingTheory/Affinoid/Restricted.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Affinoid/Restricted.lean#L69)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
