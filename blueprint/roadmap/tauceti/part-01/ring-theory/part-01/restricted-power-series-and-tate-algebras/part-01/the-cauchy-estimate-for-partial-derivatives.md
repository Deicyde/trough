---
declaration: theorem
origin: cited
lean: TauCeti.MvPowerSeries.norm_restrictedPDeriv_le, MvPowerSeries.norm_restrictedHasseDeriv_le
statement: formalized
proof: formalized
---

# The Cauchy estimate for partial derivatives

`‖∂ᵢ f‖ ≤ cᵢ⁻¹ ‖f‖` for the Gauss norm at
the polyradius `c`.

```lean
TauCeti.MvPowerSeries.norm_restrictedPDeriv_le.{u_1, u_2} {σ : Type u_1} {R : Type u_2}
  [NormedCommRing R] [IsUltrametricDist R] {c : σ → ℝ} [∀ (i : σ), Fact (0 < c i)] (i : σ)
  (f : ↥(MvPowerSeries.IsRestricted.subring c)) :
  ‖(TauCeti.MvPowerSeries.restrictedPDeriv i) f‖ ≤ (c i)⁻¹ * ‖f‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MvPowerSeries.norm_restrictedPDeriv_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Derivative.html#TauCeti.MvPowerSeries.norm_restrictedPDeriv_le).

## Other forms

**The Cauchy estimate on the restricted-series ring.** Formalized in Tau Ceti as [`MvPowerSeries.norm_restrictedHasseDeriv_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/HasseDeriv/GaussNorm.html#MvPowerSeries.norm_restrictedHasseDeriv_le).

```lean
MvPowerSeries.norm_restrictedHasseDeriv_le.{u_1, u_2} {σ : Type u_1} {R : Type u_2} [NormedRing R]
  [IsUltrametricDist R] {c : σ → ℝ} [∀ (i : σ), Fact (0 < c i)] (d : σ →₀ ℕ)
  (f : ↥(MvPowerSeries.IsRestricted.subring c)) :
  ‖(MvPowerSeries.restrictedHasseDeriv d) f‖ ≤ (d.prod fun x1 x2 => c x1 ^ x2)⁻¹ * ‖f‖
```

## Sources

- [Tau Ceti documentation: `TauCeti.MvPowerSeries.norm_restrictedPDeriv_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Derivative.html#TauCeti.MvPowerSeries.norm_restrictedPDeriv_le)
- [Source of `TauCeti.MvPowerSeries.norm_restrictedPDeriv_le` in TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Derivative.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Derivative.lean#L105)
