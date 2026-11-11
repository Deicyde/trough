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

- [Kedlaya's Hilbert basis theorem for restricted power series](../restricted-power-series-and-tate-algebras/part-01/kedlayas-hilbert-basis-theorem-for-restricted-po.md)
- [TauCeti.IsAffinoidAlgebra.continuous_algHom](tauceti-isaffinoidalgebra-continuous-alghom.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](../restricted-power-series-and-tate-algebras/part-01/tauceti-mvpowerseries-isrestrictedfamily.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAffinoidAlgebra.isRestricted_subring`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/Restricted.html#TauCeti.IsAffinoidAlgebra.isRestricted_subring).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAffinoidAlgebra.isRestricted_subring`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/Restricted.html#TauCeti.IsAffinoidAlgebra.isRestricted_subring)
- [Source of `TauCeti.IsAffinoidAlgebra.isRestricted_subring` in TauCeti/RingTheory/Affinoid/Restricted.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Affinoid/Restricted.lean#L69)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
