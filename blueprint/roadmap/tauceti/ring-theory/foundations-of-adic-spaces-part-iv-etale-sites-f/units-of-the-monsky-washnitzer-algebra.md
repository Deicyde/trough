---
declaration: theorem
origin: cited
lean: TauCeti.Dagger.isUnit_washnitzerAlgebra_iff
statement: formalized
proof: formalized
---

# Units of the Monsky–Washnitzer algebra

Over a complete ultrametric normed field, an
overconvergent series is a unit of `W` iff its constant coefficient is nonzero and strictly
dominates the norm of every other coefficient.

```lean
TauCeti.Dagger.isUnit_washnitzerAlgebra_iff.{u_1, u_2} {σ : Type u_1} {K : Type u_2} [NormedField K]
  [IsUltrametricDist K] [CompleteSpace K] (f : ↥(TauCeti.Dagger.washnitzerAlgebra σ K)) :
  IsUnit f ↔
    MvPowerSeries.constantCoeff ↑f ≠ 0 ∧
      ∀ (t : σ →₀ ℕ), t ≠ 0 → ‖(MvPowerSeries.coeff t) ↑f‖ < ‖MvPowerSeries.constantCoeff ↑f‖
```

## Depends on

- [TauCeti.Dagger.washnitzerAlgebra](tauceti-dagger-washnitzeralgebra.md)

## Proof depends on

- [Neumann series criterion (`MvPowerSeries.isNormMulUnit_of_norm_sub_C_lt`)](../mv-power-series/neumann-series-criterion-mvpowerseries-isnormmul.md)
- [TauCeti.Dagger.washnitzerAlgebra.toTate](tauceti-dagger-washnitzeralgebra-totate.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.isUnit_washnitzerAlgebra_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/WashnitzerAlgebra.html#TauCeti.Dagger.isUnit_washnitzerAlgebra_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.isUnit_washnitzerAlgebra_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/WashnitzerAlgebra.html#TauCeti.Dagger.isUnit_washnitzerAlgebra_iff)
- [Source of `TauCeti.Dagger.isUnit_washnitzerAlgebra_iff` in TauCeti/RingTheory/Dagger/WashnitzerAlgebra.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Dagger/WashnitzerAlgebra.lean#L554)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
