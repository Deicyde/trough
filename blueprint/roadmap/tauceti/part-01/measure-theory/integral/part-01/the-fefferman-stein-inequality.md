---
declaration: theorem
origin: cited
lean: TauCeti.eLpNorm_le_eLpNorm_sharpMaximalFunction, TauCeti.lintegral_enorm_rpow_le_lintegral_sharpMaximalFunction_rpow, TauCeti.exists_eLpNorm_le_mul_eLpNorm_sharpMaximalFunction, TauCeti.exists_lintegral_enorm_rpow_le_mul_lintegral_sharpMaximalFunction_rpow
statement: formalized
proof: formalized
---

# The Fefferman–Stein inequality

For `1 < p < ∞` and `f ∈ L^p₀(ℝⁿ)`, `ℝⁿ = ι → ℝ`, `n ≥ 1`,
for some `1 ≤ p₀ ≤ p`, the `Lᵖ` norm of `f` is controlled by that of its sharp maximal function
`f^#`, with a constant depending only on `n` and `p`:

`‖f‖_p ≤ (2^(p + 1) 2^((p + 2n + 2) p))^(1 / p) ‖f^#‖_p`.

The case `p₀ = 1` is that of an integrable `f`, and `p₀ = p` that of `f ∈ Lᵖ`. Balls are taken in
the sup distance of `ι → ℝ`. The a priori integrability of `f` cannot be dropped altogether, since
`f^#` vanishes for constant `f`; and positive dimension is needed, since in dimension `0` every
ball is the whole space and `f^#` vanishes identically.

```lean
TauCeti.eLpNorm_le_eLpNorm_sharpMaximalFunction.{u_1, u_2} {ι : Type u_1} [Fintype ι] {F : Type u_2}
  [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] [Nonempty ι] {f : (ι → ℝ) → F}
  {p₀ p : ENNReal} (hf : MeasureTheory.MemLp f p₀ MeasureTheory.volume) (hp₀ : 1 ≤ p₀)
  (hp₀p : p₀ ≤ p) (hp : 1 < p) (hp_top : p ≠ ⊤) :
  MeasureTheory.eLpNorm f p MeasureTheory.volume ≤
    ENNReal.ofReal (2 ^ (p.toReal + 1) * 2 ^ ((p.toReal + 2 * ↑(Fintype.card ι) + 2) * p.toReal)) ^
        (1 / p.toReal) *
      MeasureTheory.eLpNorm (TauCeti.sharpMaximalFunction MeasureTheory.volume f) p
        MeasureTheory.volume
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Hardy–Littlewood maximal inequality](the-hardy-littlewood-maximal-inequality.md)
- [Jensen's inequality for the square of a mean](../part-02/jensens-inequality-for-the-square-of-a-mean.md)
- [Lebesgue's differentiation theorem along dyadic cubes](../../measure/lebesgues-differentiation-theorem-along-dyadic-c.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.eLpNorm_le_eLpNorm_sharpMaximalFunction`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/SharpMaximalFunction.html#TauCeti.eLpNorm_le_eLpNorm_sharpMaximalFunction).

## Other forms

**The Fefferman–Stein inequality, as an inequality between the integrals `∫⁻ ‖·‖ₑ ^ p`.** Formalized in Tau Ceti as [`TauCeti.lintegral_enorm_rpow_le_lintegral_sharpMaximalFunction_rpow`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/SharpMaximalFunction.html#TauCeti.lintegral_enorm_rpow_le_lintegral_sharpMaximalFunction_rpow).

```lean
TauCeti.lintegral_enorm_rpow_le_lintegral_sharpMaximalFunction_rpow.{u_1, u_2} {ι : Type u_1}
  [Fintype ι] {F : Type u_2} [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] [Nonempty ι]
  {f : (ι → ℝ) → F} (hf : MeasureTheory.AEStronglyMeasurable f MeasureTheory.volume) {p₀ p : ℝ}
  (hp₀ : 1 ≤ p₀) (hp₀p : p₀ ≤ p) (hp : 1 < p) (hfp₀ : ∫⁻ (x : ι → ℝ), ‖f x‖ₑ ^ p₀ ≠ ⊤) :
  ∫⁻ (x : ι → ℝ), ‖f x‖ₑ ^ p ≤
    ENNReal.ofReal (2 ^ (p + 1) * 2 ^ ((p + 2 * ↑(Fintype.card ι) + 2) * p)) *
      ∫⁻ (x : ι → ℝ), TauCeti.sharpMaximalFunction MeasureTheory.volume f x ^ p
```

**The Fefferman–Stein inequality for Euclidean balls, in terms of `Lᵖ` seminorms.** Formalized in Tau Ceti as [`TauCeti.exists_eLpNorm_le_mul_eLpNorm_sharpMaximalFunction`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/SharpMaximalFunction.html#TauCeti.exists_eLpNorm_le_mul_eLpNorm_sharpMaximalFunction).

```lean
TauCeti.exists_eLpNorm_le_mul_eLpNorm_sharpMaximalFunction.{u_3, u_4} {ι : Type u_3} [Fintype ι]
  [Nonempty ι] {p : ENNReal} (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C,
    ∀ {F : Type u_4} [inst : NormedAddCommGroup F] [inst_1 : NormedSpace ℝ F] [CompleteSpace F]
      (f : EuclideanSpace ℝ ι → F),
      MeasureTheory.Integrable f MeasureTheory.volume →
        MeasureTheory.eLpNorm f p MeasureTheory.volume ≤
          ↑C *
            MeasureTheory.eLpNorm (TauCeti.sharpMaximalFunction MeasureTheory.volume f) p
              MeasureTheory.volume
```

**The Fefferman–Stein inequality for Euclidean balls.** Formalized in Tau Ceti as [`TauCeti.exists_lintegral_enorm_rpow_le_mul_lintegral_sharpMaximalFunction_rpow`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/SharpMaximalFunction.html#TauCeti.exists_lintegral_enorm_rpow_le_mul_lintegral_sharpMaximalFunction_rpow).

```lean
TauCeti.exists_lintegral_enorm_rpow_le_mul_lintegral_sharpMaximalFunction_rpow.{u_3, u_4}
  {ι : Type u_3} [Fintype ι] [Nonempty ι] {p : ℝ} (hp : 1 < p) :
  ∃ C,
    ∀ {F : Type u_4} [inst : NormedAddCommGroup F] [inst_1 : NormedSpace ℝ F] [CompleteSpace F]
      (f : EuclideanSpace ℝ ι → F),
      MeasureTheory.Integrable f MeasureTheory.volume →
        ∫⁻ (x : EuclideanSpace ℝ ι), ‖f x‖ₑ ^ p ≤
          ↑C *
            ∫⁻ (x : EuclideanSpace ℝ ι), TauCeti.sharpMaximalFunction MeasureTheory.volume f x ^ p
```

## Sources

- [Tau Ceti documentation: `TauCeti.eLpNorm_le_eLpNorm_sharpMaximalFunction`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/SharpMaximalFunction.html#TauCeti.eLpNorm_le_eLpNorm_sharpMaximalFunction)
- [Source of `TauCeti.eLpNorm_le_eLpNorm_sharpMaximalFunction` in TauCeti/MeasureTheory/Integral/SharpMaximalFunction.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Integral/SharpMaximalFunction.lean#L655)
