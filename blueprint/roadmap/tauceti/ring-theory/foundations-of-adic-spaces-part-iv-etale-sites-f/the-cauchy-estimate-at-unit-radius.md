---
declaration: theorem
origin: cited
lean: TauCeti.Dagger.washnitzerAlgebra.norm_toTate_hasseDeriv_le, TauCeti.MvPowerSeries.norm_restrictedPDeriv_le, MvPowerSeries.norm_restrictedHasseDeriv_le
statement: formalized
proof: formalized
---

# The Cauchy estimate at unit radius

Hasse derivatives do not increase the Gauss norm of an
overconvergent series.

```lean
TauCeti.Dagger.washnitzerAlgebra.norm_toTate_hasseDeriv_le.{u_1, u_2} {σ : Type u_1} {R : Type u_2}
  [NormedCommRing R] [IsUltrametricDist R] (d : σ →₀ ℕ)
  (f : ↥(TauCeti.Dagger.washnitzerAlgebra σ R)) :
  ‖(TauCeti.Dagger.washnitzerAlgebra.toTate σ R)
        ((TauCeti.Dagger.washnitzerAlgebra.hasseDeriv σ R d) f)‖ ≤
    ‖(TauCeti.Dagger.washnitzerAlgebra.toTate σ R) f‖
```

## Depends on

- [TauCeti.Dagger.washnitzerAlgebra](tauceti-dagger-washnitzeralgebra.md)
- [TauCeti.Dagger.washnitzerAlgebra.toTate](tauceti-dagger-washnitzeralgebra-totate.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.washnitzerAlgebra.norm_toTate_hasseDeriv_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/Derivative.html#TauCeti.Dagger.washnitzerAlgebra.norm_toTate_hasseDeriv_le).

## Other forms

**The Cauchy estimate for partial derivatives.** Formalized in Tau Ceti as [`TauCeti.MvPowerSeries.norm_restrictedPDeriv_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Derivative.html#TauCeti.MvPowerSeries.norm_restrictedPDeriv_le).

```lean
TauCeti.MvPowerSeries.norm_restrictedPDeriv_le.{u_1, u_2} {σ : Type u_1} {R : Type u_2}
  [NormedCommRing R] [IsUltrametricDist R] {c : σ → ℝ} [∀ (i : σ), Fact (0 < c i)] (i : σ)
  (f : ↥(MvPowerSeries.IsRestricted.subring c)) :
  ‖(TauCeti.MvPowerSeries.restrictedPDeriv i) f‖ ≤ (c i)⁻¹ * ‖f‖
```

**The Cauchy estimate on the restricted-series ring.** Formalized in Tau Ceti as [`MvPowerSeries.norm_restrictedHasseDeriv_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/HasseDeriv/GaussNorm.html#MvPowerSeries.norm_restrictedHasseDeriv_le).

```lean
MvPowerSeries.norm_restrictedHasseDeriv_le.{u_1, u_2} {σ : Type u_1} {R : Type u_2} [NormedRing R]
  [IsUltrametricDist R] {c : σ → ℝ} [∀ (i : σ), Fact (0 < c i)] (d : σ →₀ ℕ)
  (f : ↥(MvPowerSeries.IsRestricted.subring c)) :
  ‖(MvPowerSeries.restrictedHasseDeriv d) f‖ ≤ (d.prod fun x1 x2 => c x1 ^ x2)⁻¹ * ‖f‖
```

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.washnitzerAlgebra.norm_toTate_hasseDeriv_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/Derivative.html#TauCeti.Dagger.washnitzerAlgebra.norm_toTate_hasseDeriv_le)
- [Source of `TauCeti.Dagger.washnitzerAlgebra.norm_toTate_hasseDeriv_le` in TauCeti/RingTheory/Dagger/Derivative.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Dagger/Derivative.lean#L247)
