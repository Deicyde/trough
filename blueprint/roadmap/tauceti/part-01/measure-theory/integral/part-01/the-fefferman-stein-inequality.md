---
declaration: theorem
origin: cited
lean: TauCeti.eLpNorm_le_eLpNorm_sharpMaximalFunction, TauCeti.lintegral_enorm_rpow_le_lintegral_sharpMaximalFunction_rpow
statement: formalized
proof: formalized
---

# The Fefferman–Stein inequality

For `1 < p < ∞` and integrable `f` on `ℝⁿ = ι → ℝ`,
`n ≥ 1`, the `Lᵖ` norm of `f` is controlled by that of its sharp maximal function `f^#`, with a
constant depending only on `n` and `p`:

`‖f‖_p ≤ (2^(p + 1) 2^((p + 2n + 2) p))^(1 / p) ‖f^#‖_p`.

Balls are taken in the sup distance of `ι → ℝ`. The integrability of `f` cannot be dropped
altogether, since `f^#` vanishes for constant `f`; and positive dimension is needed, since in
dimension `0` every ball is the whole space and `f^#` vanishes identically.

```lean
TauCeti.eLpNorm_le_eLpNorm_sharpMaximalFunction.{u_1, u_2} {ι : Type u_1} [Fintype ι] {F : Type u_2}
  [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] [Nonempty ι] {f : (ι → ℝ) → F}
  (hf : MeasureTheory.Integrable f MeasureTheory.volume) {p : ENNReal} (hp : 1 < p)
  (hp_top : p ≠ ⊤) :
  MeasureTheory.eLpNorm f p MeasureTheory.volume ≤
    ENNReal.ofReal (2 ^ (p.toReal + 1) * 2 ^ ((p.toReal + 2 * ↑(Fintype.card ι) + 2) * p.toReal)) ^
        (1 / p.toReal) *
      MeasureTheory.eLpNorm (TauCeti.sharpMaximalFunction MeasureTheory.volume f) p
        MeasureTheory.volume
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Lebesgue's differentiation theorem along dyadic cubes](../../measure/lebesgues-differentiation-theorem-along-dyadic-c.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.eLpNorm_le_eLpNorm_sharpMaximalFunction`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/SharpMaximalFunction.html#TauCeti.eLpNorm_le_eLpNorm_sharpMaximalFunction).

## Other forms

**The Fefferman–Stein inequality, as an inequality between the integrals `∫⁻ ‖·‖ₑ ^ p`.** Formalized in Tau Ceti as [`TauCeti.lintegral_enorm_rpow_le_lintegral_sharpMaximalFunction_rpow`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/SharpMaximalFunction.html#TauCeti.lintegral_enorm_rpow_le_lintegral_sharpMaximalFunction_rpow).

```lean
TauCeti.lintegral_enorm_rpow_le_lintegral_sharpMaximalFunction_rpow.{u_1, u_2} {ι : Type u_1}
  [Fintype ι] {F : Type u_2} [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] [Nonempty ι]
  {f : (ι → ℝ) → F} (hf : MeasureTheory.Integrable f MeasureTheory.volume) {p : ℝ} (hp : 1 < p) :
  ∫⁻ (x : ι → ℝ), ‖f x‖ₑ ^ p ≤
    ENNReal.ofReal (2 ^ (p + 1) * 2 ^ ((p + 2 * ↑(Fintype.card ι) + 2) * p)) *
      ∫⁻ (x : ι → ℝ), TauCeti.sharpMaximalFunction MeasureTheory.volume f x ^ p
```

## Sources

- [Tau Ceti documentation: `TauCeti.eLpNorm_le_eLpNorm_sharpMaximalFunction`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/SharpMaximalFunction.html#TauCeti.eLpNorm_le_eLpNorm_sharpMaximalFunction)
- [Source of `TauCeti.eLpNorm_le_eLpNorm_sharpMaximalFunction` in TauCeti/MeasureTheory/Integral/SharpMaximalFunction.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Integral/SharpMaximalFunction.lean#L558)
