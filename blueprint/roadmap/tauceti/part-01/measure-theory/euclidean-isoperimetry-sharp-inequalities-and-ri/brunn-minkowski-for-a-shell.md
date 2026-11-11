---
declaration: theorem
origin: cited
lean: TauCeti.finrank_mul_rpow_pow_mul_le_volume_real_sub
statement: formalized
proof: formalized
---

# Brunn–Minkowski for a shell

If the `r`-neighbourhood `G + ball 0 r` of a nonempty
null-measurable set `G` lies in a set `F` of finite volume, then in dimension `n ≥ 1`
`volume F - volume G ≥ n (volume G ^ (1 / n)) ^ (n - 1) r ω_n ^ (1 / n)`.

```lean
TauCeti.finrank_mul_rpow_pow_mul_le_volume_real_sub.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  (hn : Module.finrank ℝ E ≠ 0) {G F : Set E}
  (hG : MeasureTheory.NullMeasurableSet G MeasureTheory.volume) (hG0 : G.Nonempty)
  (hF : MeasureTheory.volume F ≠ ⊤) {r : ℝ} (hr : 0 < r) (hsub : G + Metric.ball 0 r ⊆ F) :
  ↑(Module.finrank ℝ E) *
        (MeasureTheory.volume.real G ^ (↑(Module.finrank ℝ E))⁻¹) ^ (Module.finrank ℝ E - 1) *
      (r * MeasureTheory.volume.real (Metric.ball 0 1) ^ (↑(Module.finrank ℝ E))⁻¹) ≤
    MeasureTheory.volume.real F - MeasureTheory.volume.real G
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Prékopa–Leindler inequality for the minimum on `ℝ`](../integral/part-02/prekopa-leindler-inequality-for-the-minimum-on-r.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.finrank_mul_rpow_pow_mul_le_volume_real_sub`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Basic.html#TauCeti.finrank_mul_rpow_pow_mul_le_volume_real_sub).

## Sources

- [Tau Ceti documentation: `TauCeti.finrank_mul_rpow_pow_mul_le_volume_real_sub`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Basic.html#TauCeti.finrank_mul_rpow_pow_mul_le_volume_real_sub)
- [Source of `TauCeti.finrank_mul_rpow_pow_mul_le_volume_real_sub` in TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Measure/Lebesgue/BrunnMinkowski/Basic.lean#L219)
