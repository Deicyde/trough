---
declaration: def
origin: cited
lean: TauCeti.Vortex.sobolevGaugeGroup
statement: formalized
---

# The Sobolev framed gauge group `G_s`, `s > 1`

the continuous circle-valued maps `u` on
the plane with `u - 1 ∈ H^s(ℂ; ℂ)`, that is, with `Re u - 1` and `Im u` in `H^s`.

```lean
TauCeti.Vortex.sobolevGaugeGroup {s : ℝ} (hs : 1 < s) : Subgroup (ℂ → Circle)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The convolution theorem for the inverse Fourier transform](../fourier/the-convolution-theorem-for-the-inverse-fourier.md)
- [Peetre's inequality (`TauCeti.one_add_norm_add_sq_rpow_le_mul`)](../../part-03/special-functions/peetres-inequality-tauceti-one-add-norm-add-sq-r.md)
- [Young's convolution inequality](../convolution/youngs-convolution-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Vortex.sobolevGaugeGroup`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/FramedGauge/Sobolev.html#TauCeti.Vortex.sobolevGaugeGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.Vortex.sobolevGaugeGroup`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/FramedGauge/Sobolev.html#TauCeti.Vortex.sobolevGaugeGroup)
- [Source of `TauCeti.Vortex.sobolevGaugeGroup` in TauCeti/Analysis/PDE/Vortex/FramedGauge/Sobolev.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Vortex/FramedGauge/Sobolev.lean#L99)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TaubesGromov/STATUS.md)
