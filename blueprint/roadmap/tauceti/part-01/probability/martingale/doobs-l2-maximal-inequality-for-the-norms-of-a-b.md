---
declaration: theorem
origin: cited
lean: MeasureTheory.Martingale.integral_sq_partialSups_norm_le, MeasureTheory.Submartingale.integral_sq_partialSups_le
statement: formalized
proof: formalized
---

# Doob's L² maximal inequality for the norms of a Banach-valued martingale

The second moment of the finite running maximum is bounded by four times the terminal
second moment.

```lean
MeasureTheory.Martingale.integral_sq_partialSups_norm_le.{u_1, u_2} {Ω : Type u_1}
  {mΩ : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsFiniteMeasure μ]
  {ℱ : MeasureTheory.Filtration ℕ mΩ} {E : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [CompleteSpace E] {X : ℕ → Ω → E} (hX : MeasureTheory.Martingale X ℱ μ) (n : ℕ)
  (hn : MeasureTheory.MemLp (X n) 2 μ) :
  ∫ (ω : Ω), (partialSups fun k ω => ‖X k ω‖) n ω ^ 2 ∂μ ≤ 4 * ∫ (ω : Ω), ‖X n ω‖ ^ 2 ∂μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Martingale.integral_sq_partialSups_norm_le`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/L2.html#MeasureTheory.Martingale.integral_sq_partialSups_norm_le).

## Other forms

**Doob's L² maximal inequality for a nonnegative submartingale on a finite time grid.** Formalized in Tau Ceti as [`MeasureTheory.Submartingale.integral_sq_partialSups_le`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/L2.html#MeasureTheory.Submartingale.integral_sq_partialSups_le).

```lean
MeasureTheory.Submartingale.integral_sq_partialSups_le.{u_1} {Ω : Type u_1} {mΩ : MeasurableSpace Ω}
  {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsFiniteMeasure μ]
  {ℱ : MeasureTheory.Filtration ℕ mΩ} {f : ℕ → Ω → ℝ} (hf : MeasureTheory.Submartingale f ℱ μ)
  (hpos : ∀ (k : ℕ), 0 ≤ᵐ[μ] f k) (n : ℕ) (hn : MeasureTheory.MemLp (f n) 2 μ) :
  ∫ (ω : Ω), (partialSups f) n ω ^ 2 ∂μ ≤ 4 * ∫ (ω : Ω), f n ω ^ 2 ∂μ
```

## Sources

- [Tau Ceti documentation: `MeasureTheory.Martingale.integral_sq_partialSups_norm_le`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/MaximalInequality/L2.html#MeasureTheory.Martingale.integral_sq_partialSups_norm_le)
- [Source of `MeasureTheory.Martingale.integral_sq_partialSups_norm_le` in TauCeti/Probability/Martingale/MaximalInequality/L2.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Martingale/MaximalInequality/L2.lean#L122)
