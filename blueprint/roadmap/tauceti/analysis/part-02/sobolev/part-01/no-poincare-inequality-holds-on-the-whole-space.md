---
declaration: theorem
origin: cited
lean: TauCeti.not_exists_eLpNorm_le_const_mul_eLpNorm_fderiv
statement: formalized
proof: formalized
---

# No Poincaré inequality holds on the whole space

There is no constant `C` with
`‖u‖_p ≤ C ‖Du‖_p` for every compactly supported `Cᵏ` function `u`, for any order `k ≤ ∞`
and any `p ≠ 0`, including `p = ∞`. In particular, the inequality fails even when restricted
to smooth test functions.

Compare `MeasureTheory.eLpNorm_le_eLpNorm_fderiv`, which supplies such a constant once every
`u` is supported in one fixed bounded set; the proof here shows that hypothesis cannot be
dropped.

```lean
TauCeti.not_exists_eLpNorm_le_const_mul_eLpNorm_fderiv.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [MeasurableSpace E] [BorelSpace E] [FiniteDimensional ℝ E]
  (μ : MeasureTheory.Measure E) [μ.IsAddHaarMeasure] {p : ENNReal} {k : ℕ∞} (hp₀ : p ≠ 0) :
  ¬∃ C,
      ∀ (u : E → ℝ),
        ContDiff ℝ (↑k) u →
          HasCompactSupport u →
            MeasureTheory.eLpNorm u p μ ≤ ↑C * MeasureTheory.eLpNorm (fderiv ℝ u) p μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.not_exists_eLpNorm_le_const_mul_eLpNorm_fderiv`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/WholeSpace.html#TauCeti.not_exists_eLpNorm_le_const_mul_eLpNorm_fderiv).

## Sources

- [Tau Ceti documentation: `TauCeti.not_exists_eLpNorm_le_const_mul_eLpNorm_fderiv`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/WholeSpace.html#TauCeti.not_exists_eLpNorm_le_const_mul_eLpNorm_fderiv)
- [Source of `TauCeti.not_exists_eLpNorm_le_const_mul_eLpNorm_fderiv` in TauCeti/Analysis/Sobolev/Poincare/WholeSpace.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/Poincare/WholeSpace.lean#L88)
