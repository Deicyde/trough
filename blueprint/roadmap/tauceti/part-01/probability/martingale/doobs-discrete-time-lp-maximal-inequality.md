---
declaration: theorem
origin: cited
lean: MeasureTheory.Submartingale.eLpNorm_partialSups_le, MeasureTheory.Submartingale.integral_rpow_partialSups_le, MeasureTheory.Submartingale.integral_rpow_partialSups_posPart_le, MeasureTheory.Submartingale.eLpNorm_partialSups_posPart_le, MeasureTheory.Martingale.eLpNorm_partialSups_norm_le, MeasureTheory.Martingale.integral_rpow_partialSups_norm_le
statement: formalized
proof: formalized
---

# Doob's discrete-time `Lᵖ` maximal inequality

Requires nonnegativity only at the terminal
index `n` (`0 ≤ᵐ[μ] f n`) and no `MemLp` hypothesis.

```lean
MeasureTheory.Submartingale.eLpNorm_partialSups_le.{u_1, u_2} {Ω : Type u_1} {ι : Type u_2}
  {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [LinearOrder ι] [LocallyFiniteOrderBot ι]
  [MeasureTheory.IsFiniteMeasure μ] {ℱ : MeasureTheory.Filtration ι m0} {f : ι → Ω → ℝ}
  (hf : MeasureTheory.Submartingale f ℱ μ) {n : ι} (hposn : 0 ≤ᵐ[μ] f n) {p : ENNReal} (hp : 1 < p)
  (hp_top : p ≠ ⊤) :
  MeasureTheory.eLpNorm ((partialSups f) n) p μ ≤ p / (p - 1) * MeasureTheory.eLpNorm (f n) p μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Doob's `Lᵖ` maximal inequality on a countable set](doobs-lp-maximal-inequality-on-a-countable-set.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Submartingale.eLpNorm_partialSups_le`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Lp.html#MeasureTheory.Submartingale.eLpNorm_partialSups_le).

## Other forms

**Doob's discrete-time `Lᵖ` maximal inequality (Bochner moment form).** Formalized in Tau Ceti as [`MeasureTheory.Submartingale.integral_rpow_partialSups_le`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Lp.html#MeasureTheory.Submartingale.integral_rpow_partialSups_le).

```lean
MeasureTheory.Submartingale.integral_rpow_partialSups_le.{u_1, u_2} {Ω : Type u_1} {ι : Type u_2}
  {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [LinearOrder ι] [LocallyFiniteOrderBot ι]
  [MeasureTheory.IsFiniteMeasure μ] {ℱ : MeasureTheory.Filtration ι m0} {f : ι → Ω → ℝ}
  (hf : MeasureTheory.Submartingale f ℱ μ) {n : ι} (hposn : 0 ≤ᵐ[μ] f n) {p : ℝ} (hp : 1 < p)
  (hn : MeasureTheory.MemLp (f n) (ENNReal.ofReal p) μ) :
  ∫ (ω : Ω), (partialSups f) n ω ^ p ∂μ ≤ (p / (p - 1)) ^ p * ∫ (ω : Ω), f n ω ^ p ∂μ
```

**Doob's discrete-time `Lᵖ` maximal inequality (positive-part Bochner moment form).** Formalized in Tau Ceti as [`MeasureTheory.Submartingale.integral_rpow_partialSups_posPart_le`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Lp.html#MeasureTheory.Submartingale.integral_rpow_partialSups_posPart_le).

```lean
MeasureTheory.Submartingale.integral_rpow_partialSups_posPart_le.{u_1, u_2} {Ω : Type u_1}
  {ι : Type u_2} {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [LinearOrder ι]
  [LocallyFiniteOrderBot ι] [MeasureTheory.IsFiniteMeasure μ] {ℱ : MeasureTheory.Filtration ι m0}
  {f : ι → Ω → ℝ} (hf : MeasureTheory.Submartingale f ℱ μ) (n : ι) {p : ℝ} (hp : 1 < p)
  (hn : MeasureTheory.MemLp (f⁺ n) (ENNReal.ofReal p) μ) :
  ∫ (ω : Ω), (partialSups f⁺) n ω ^ p ∂μ ≤ (p / (p - 1)) ^ p * ∫ (ω : Ω), f⁺ n ω ^ p ∂μ
```

**Doob's discrete-time `Lᵖ` maximal inequality (positive-part form).** Formalized in Tau Ceti as [`MeasureTheory.Submartingale.eLpNorm_partialSups_posPart_le`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Lp.html#MeasureTheory.Submartingale.eLpNorm_partialSups_posPart_le).

```lean
MeasureTheory.Submartingale.eLpNorm_partialSups_posPart_le.{u_1, u_2} {Ω : Type u_1} {ι : Type u_2}
  {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [LinearOrder ι] [LocallyFiniteOrderBot ι]
  [MeasureTheory.IsFiniteMeasure μ] {ℱ : MeasureTheory.Filtration ι m0} {f : ι → Ω → ℝ}
  (hf : MeasureTheory.Submartingale f ℱ μ) (n : ι) {p : ENNReal} (hp : 1 < p) (hp_top : p ≠ ⊤) :
  MeasureTheory.eLpNorm ((partialSups f⁺) n) p μ ≤ p / (p - 1) * MeasureTheory.eLpNorm (f⁺ n) p μ
```

**Doob's discrete-time `Lᵖ` maximal inequality for Banach-valued martingales (`eLpNorm` form).** Formalized in Tau Ceti as [`MeasureTheory.Martingale.eLpNorm_partialSups_norm_le`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Lp.html#MeasureTheory.Martingale.eLpNorm_partialSups_norm_le).

```lean
MeasureTheory.Martingale.eLpNorm_partialSups_norm_le.{u_1, u_2, u_3} {Ω : Type u_1} {E : Type u_2}
  {ι : Type u_3} {mΩ : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [CompleteSpace E] [LinearOrder ι] [LocallyFiniteOrderBot ι]
  [MeasureTheory.IsFiniteMeasure μ] {ℱ : MeasureTheory.Filtration ι mΩ} {X : ι → Ω → E}
  (hX : MeasureTheory.Martingale X ℱ μ) (n : ι) {p : ENNReal} (hp : 1 < p) (hp_top : p ≠ ⊤) :
  MeasureTheory.eLpNorm ((partialSups fun k ω => ‖X k ω‖) n) p μ ≤
    p / (p - 1) * MeasureTheory.eLpNorm (X n) p μ
```

**Doob's discrete-time `Lᵖ` maximal inequality for Banach-valued martingales (Bochner moment form).** Formalized in Tau Ceti as [`MeasureTheory.Martingale.integral_rpow_partialSups_norm_le`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Lp.html#MeasureTheory.Martingale.integral_rpow_partialSups_norm_le).

```lean
MeasureTheory.Martingale.integral_rpow_partialSups_norm_le.{u_1, u_2, u_3} {Ω : Type u_1}
  {E : Type u_2} {ι : Type u_3} {mΩ : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E] [LinearOrder ι]
  [LocallyFiniteOrderBot ι] [MeasureTheory.IsFiniteMeasure μ] {ℱ : MeasureTheory.Filtration ι mΩ}
  {X : ι → Ω → E} (hX : MeasureTheory.Martingale X ℱ μ) (n : ι) {p : ℝ} (hp : 1 < p)
  (hn : MeasureTheory.MemLp (X n) (ENNReal.ofReal p) μ) :
  ∫ (ω : Ω), (partialSups fun k ω => ‖X k ω‖) n ω ^ p ∂μ ≤
    (p / (p - 1)) ^ p * ∫ (ω : Ω), ‖X n ω‖ ^ p ∂μ
```

## Sources

- [Tau Ceti documentation: `MeasureTheory.Submartingale.eLpNorm_partialSups_le`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/Lp.html#MeasureTheory.Submartingale.eLpNorm_partialSups_le)
- [Source of `MeasureTheory.Submartingale.eLpNorm_partialSups_le` in TauCeti/Probability/Martingale/MaximalInequality/Lp.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Martingale/MaximalInequality/Lp.lean#L376)
