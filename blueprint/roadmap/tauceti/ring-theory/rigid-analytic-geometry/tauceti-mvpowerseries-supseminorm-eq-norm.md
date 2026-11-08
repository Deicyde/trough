---
declaration: theorem
origin: cited
lean: TauCeti.MvPowerSeries.supSeminorm_eq_norm
statement: formalized
proof: formalized
---

# TauCeti.MvPowerSeries.supSeminorm_eq_norm

On a Tate algebra the supremum seminorm is the Gauss norm: `|f|sup = ‖f‖`.

```lean
TauCeti.MvPowerSeries.supSeminorm_eq_norm.{u_1} {K : Type u_1} [NontriviallyNormedField K]
  [IsUltrametricDist K] [CompleteSpace K] {n : ℕ}
  (f : ↥(MvPowerSeries.IsRestricted.subring fun x => 1)) : TauCeti.supSeminorm K f = ‖f‖
```

## Depends on

- [TauCeti.supSeminorm](tauceti-supseminorm.md)

## Proof depends on

- [Kedlaya's Hilbert basis theorem for `A^r` (Kedlaya, Theorem 3.2)](../mv-power-series/kedlayas-hilbert-basis-theorem-for-a-r-kedlaya-t.md)
- [TauCeti.IsAffinoidAlgebra.continuous_algHom](tauceti-isaffinoidalgebra-continuous-alghom.md)
- [The Weierstrass division estimate in several variables](../mv-power-series/the-weierstrass-division-estimate-in-several-var.md)
- [The Weierstrass division identity](../p-adic-measures-completed-group-algebras-and-cha/part-01/the-weierstrass-division-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.MvPowerSeries.supSeminorm_eq_norm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/MaximumModulus.html#TauCeti.MvPowerSeries.supSeminorm_eq_norm).

## Sources

- [Tau Ceti documentation: `TauCeti.MvPowerSeries.supSeminorm_eq_norm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/MaximumModulus.html#TauCeti.MvPowerSeries.supSeminorm_eq_norm)
- [Source of `TauCeti.MvPowerSeries.supSeminorm_eq_norm` in TauCeti/RingTheory/Affinoid/MaximumModulus.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Affinoid/MaximumModulus.lean#L112)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
