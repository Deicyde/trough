---
declaration: theorem
origin: cited
lean: TauCeti.Symbol.HasCompactSpatialSupport.exists_eLpNorm_smul_fourier_quantizeSchwartzValue_le
statement: formalized
proof: formalized
---

# The Sobolev estimate on Schwartz functions

For a symbol `a` of order `m` with compact
spatial support and every real `s`, there is a constant `C` with
`‖⟨ξ⟩ ^ (s - m) 𝓕 (Op(a) u)‖_{L²} ≤ C ‖⟨ξ⟩ ^ s 𝓕 u‖_{L²}` for every Schwartz function `u`, that
is, `‖Op(a) u‖_{H^{s-m}} ≤ C ‖u‖_{H^s}`.

```lean
TauCeti.Symbol.HasCompactSpatialSupport.exists_eLpNorm_smul_fourier_quantizeSchwartzValue_le.{u_1,
    u_2}
  {n : ℕ} {m : ℝ} {V : Type u_1} {W : Type u_2} [NormedAddCommGroup V] [NormedSpace ℂ V]
  [NormedAddCommGroup W] [NormedSpace ℂ W] {a : TauCeti.Symbol n V W m}
  (ha : a.HasCompactSpatialSupport) (s : ℝ) :
  ∃ C,
    0 ≤ C ∧
      ∀ (u : SchwartzMap (TauCeti.CoordinateSpace n) V),
        MeasureTheory.eLpNorm
            (fun ξ =>
              ↑((1 + ‖ξ‖ ^ 2) ^ ((s - m) / 2)) •
                FourierTransform.fourier (TauCeti.quantizeSchwartzValue a.coefficient u) ξ)
            2 MeasureTheory.volume ≤
          ENNReal.ofReal C *
            MeasureTheory.eLpNorm
              (fun ξ => ↑((1 + ‖ξ‖ ^ 2) ^ (s / 2)) • (FourierTransform.fourier u) ξ) 2
              MeasureTheory.volume
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Peetre's inequality (`TauCeti.one_add_norm_add_sq_rpow_le_mul`)](../../part-03/special-functions/peetres-inequality-tauceti-one-add-norm-add-sq-r.md)
- [Young's inequality for integral kernels](../../../measure-theory/integral/part-02/youngs-inequality-for-integral-kernels.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Symbol.HasCompactSpatialSupport.exists_eLpNorm_smul_fourier_quantizeSchwartzValue_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/Sobolev.html#TauCeti.Symbol.HasCompactSpatialSupport.exists_eLpNorm_smul_fourier_quantizeSchwartzValue_le).

## Sources

- [Tau Ceti documentation: `TauCeti.Symbol.HasCompactSpatialSupport.exists_eLpNorm_smul_fourier_quantizeSchwartzValue_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/Sobolev.html#TauCeti.Symbol.HasCompactSpatialSupport.exists_eLpNorm_smul_fourier_quantizeSchwartzValue_le)
- [Source of `TauCeti.Symbol.HasCompactSpatialSupport.exists_eLpNorm_smul_fourier_quantizeSchwartzValue_le` in TauCeti/Analysis/Pseudodifferential/Sobolev.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Pseudodifferential/Sobolev.lean#L613)
