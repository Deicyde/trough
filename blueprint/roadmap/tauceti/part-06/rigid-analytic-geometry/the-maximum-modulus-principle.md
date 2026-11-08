---
declaration: theorem
origin: cited
lean: TauCeti.IsAffinoidAlgebra.exists_pointNorm_eq_supSeminorm
statement: formalized
proof: formalized
---

# The maximum modulus principle

On a nonzero affinoid algebra the supremum seminorm is
attained at a classical point: for every `f : A` there is a maximal ideal `x` of `A` with
`|f(x)| = |f|sup`.

```lean
TauCeti.IsAffinoidAlgebra.exists_pointNorm_eq_supSeminorm.{u_1, u_2} {K : Type u_1}
  [NontriviallyNormedField K] [IsUltrametricDist K] [CompleteSpace K] {A : Type u_2} [CommRing A]
  [Algebra K A] [Nontrivial A] (hA : TauCeti.IsAffinoidAlgebra K A) (f : A) :
  ∃ x, TauCeti.pointNorm K x f = TauCeti.supSeminorm K f
```

## Depends on

- [TauCeti.supSeminorm](tauceti-supseminorm.md)

## Proof depends on

- [Affinoid Noether normalisation](affinoid-noether-normalisation.md)
- [The supremum seminorm is the spectral value of the minimal polynomial](the-supremum-seminorm-is-the-spectral-value-of-t.md)
- [TauCeti.IsAffinoidAlgebra.continuous_algHom](tauceti-isaffinoidalgebra-continuous-alghom.md)
- [TauCeti.MvPowerSeries.supSeminorm_eq_norm](tauceti-mvpowerseries-supseminorm-eq-norm.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAffinoidAlgebra.exists_pointNorm_eq_supSeminorm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/MaximumModulus.html#TauCeti.IsAffinoidAlgebra.exists_pointNorm_eq_supSeminorm).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAffinoidAlgebra.exists_pointNorm_eq_supSeminorm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/MaximumModulus.html#TauCeti.IsAffinoidAlgebra.exists_pointNorm_eq_supSeminorm)
- [Source of `TauCeti.IsAffinoidAlgebra.exists_pointNorm_eq_supSeminorm` in TauCeti/RingTheory/Affinoid/MaximumModulus.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Affinoid/MaximumModulus.lean#L153)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
