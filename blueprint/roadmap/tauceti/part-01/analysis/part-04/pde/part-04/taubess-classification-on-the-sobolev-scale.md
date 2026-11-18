---
declaration: theorem
origin: cited
lean: TauCeti.Vortex.sobolevVortexDivisor_eq_sobolevVortexDivisor_iff
statement: formalized
proof: formalized
---

# Taubes's classification on the Sobolev scale

Two `C²` vortices of `A_m^k` have the same
divisor exactly when they lie in one orbit of the action of `G_(k+1)` on `A_m^k`.

```lean
TauCeti.Vortex.sobolevVortexDivisor_eq_sobolevVortexDivisor_iff {f : ContDiffBump 0} {m k : ℕ}
  [Fact (1 < k)] {hs : 1 < ↑k + 1} {x y : ↑(TauCeti.Vortex.sobolevVortices f m k)} :
  TauCeti.Vortex.sobolevVortexDivisor x = TauCeti.Vortex.sobolevVortexDivisor y ↔ ∃ u, u • ↑y = ↑x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Cauchy–Pompeiu formula with a cutoff](../../../part-03/complex/part-01/the-cauchy-pompeiu-formula-with-a-cutoff.md)
- [The convolution theorem for the inverse Fourier transform](../../../part-03/fourier/part-01/the-convolution-theorem-for-the-inverse-fourier.md)
- [Liouville's theorem (`InnerProductSpace.HarmonicOnNhd.apply_eq_apply_of_bounded`)](../../../part-03/inner-product-space/part-02/liouvilles-theorem-innerproductspace-harmoniconn.md)
- [The Mihlin–Hörmander multiplier theorem on `Lᵖ`](../../../part-02/partial-differential-equations/the-mihlin-hormander-multiplier-theorem-on-lp.md)
- [Peetre's inequality (`TauCeti.one_add_norm_add_sq_rpow_le_mul`)](../../special-functions/peetres-inequality-tauceti-one-add-norm-add-sq-r.md)
- [Young's convolution inequality](../../../part-03/convolution/youngs-convolution-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Vortex.sobolevVortexDivisor_eq_sobolevVortexDivisor_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/FramedGauge/Divisor.html#TauCeti.Vortex.sobolevVortexDivisor_eq_sobolevVortexDivisor_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.Vortex.sobolevVortexDivisor_eq_sobolevVortexDivisor_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/FramedGauge/Divisor.html#TauCeti.Vortex.sobolevVortexDivisor_eq_sobolevVortexDivisor_iff)
- [Source of `TauCeti.Vortex.sobolevVortexDivisor_eq_sobolevVortexDivisor_iff` in TauCeti/Analysis/PDE/Vortex/FramedGauge/Divisor.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Vortex/FramedGauge/Divisor.lean#L167)
