---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.IsRowCompact.encard_setOf_mem_spectrum_mapCoeffs_le, ContinuousLinearMap.IsRowCompact.encard_setOf_mem_spectrum_le
statement: formalized
proof: formalized
---

# Strassmann's bound for the spectrum

Let `u` be a row-compact endomorphism of `C₀(I, K)`,
and let its Fredholm series `H_u` be distinguished of degree `s` at the radius `ε⁻¹`. Then the
extension of `u` to `C₀(I, L)`, for a complete normed field extension `L` of `K`, has at most `s`
spectral values of norm at least `ε`.

```lean
ContinuousLinearMap.IsRowCompact.encard_setOf_mem_spectrum_mapCoeffs_le.{u_1, u_2, u_3}
  {I : Type u_1} [TopologicalSpace I] [DiscreteTopology I] [DecidableEq I] {K : Type u_2}
  {L : Type u_3} [NontriviallyNormedField K] [IsUltrametricDist K] [CompleteSpace K]
  [NontriviallyNormedField L] [NormedAlgebra K L] [IsUltrametricDist L] [CompleteSpace L]
  {u : ZeroAtInftyContinuousMap I K →L[K] ZeroAtInftyContinuousMap I K} (hu : u.IsRowCompact)
  {ε : ℝ} (hε : 0 < ε) {s : ℕ}
  (hs : TauCeti.PowerSeries.IsDistinguished ε⁻¹ s u.matrixCoeff.charPowerSeries) :
  {μ | μ ∈ spectrum L (u.mapCoeffs (algebraMap K L) ⋯) ∧ ε ≤ ‖μ‖}.encard ≤ ↑s
```

## Depends on

- [ContinuousLinearMap.IsRowCompact](continuouslinearmap-isrowcompact.md)

## Proof depends on

- [The Fredholm determinant is entire](the-fredholm-determinant-is-entire.md)
- [The nonzero spectrum of a row-compact operator](the-nonzero-spectrum-of-a-row-compact-operator.md)
- [Strassmann's theorem](../../../ring-theory/p-adic-measures-completed-group-algebras-and-cha/part-01/strassmanns-theorem.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.IsRowCompact.encard_setOf_mem_spectrum_mapCoeffs_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/Spectrum.html#ContinuousLinearMap.IsRowCompact.encard_setOf_mem_spectrum_mapCoeffs_le).

## Other forms

**Strassmann's bound for the spectrum over the coefficient field.** Formalized in Tau Ceti as [`ContinuousLinearMap.IsRowCompact.encard_setOf_mem_spectrum_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/Spectrum.html#ContinuousLinearMap.IsRowCompact.encard_setOf_mem_spectrum_le).

```lean
ContinuousLinearMap.IsRowCompact.encard_setOf_mem_spectrum_le.{u_1, u_2} {I : Type u_1}
  [TopologicalSpace I] [DiscreteTopology I] [DecidableEq I] {K : Type u_2}
  [NontriviallyNormedField K] [IsUltrametricDist K] [CompleteSpace K]
  {u : ZeroAtInftyContinuousMap I K →L[K] ZeroAtInftyContinuousMap I K} (hu : u.IsRowCompact)
  {ε : ℝ} (hε : 0 < ε) {s : ℕ}
  (hs : TauCeti.PowerSeries.IsDistinguished ε⁻¹ s u.matrixCoeff.charPowerSeries) :
  {μ | μ ∈ spectrum K u ∧ ε ≤ ‖μ‖}.encard ≤ ↑s
```

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.IsRowCompact.encard_setOf_mem_spectrum_mapCoeffs_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/Spectrum.html#ContinuousLinearMap.IsRowCompact.encard_setOf_mem_spectrum_mapCoeffs_le)
- [Source of `ContinuousLinearMap.IsRowCompact.encard_setOf_mem_spectrum_mapCoeffs_le` in TauCeti/Analysis/Normed/Operator/Nonarchimedean/Spectrum.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/Nonarchimedean/Spectrum.lean#L149)
