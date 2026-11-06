# Optional stopping theorem

**The optional stopping theorem** (fair game theorem): a strongly adapted integrable process `f`
is a submartingale if and only if for all bounded stopping times `τ` and `π` such that `τ ≤ π`, the
stopped value of `f` at `τ` has expectation smaller than its stopped value at `π`.

```lean
MeasureTheory.submartingale_iff_expected_stoppedValue_mono.{u_1} {Ω : Type u_1}
  {m0 : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} {𝒢 : MeasureTheory.Filtration ℕ m0}
  {f : ℕ → Ω → ℝ} [MeasureTheory.SigmaFiniteFiltration μ 𝒢]
  (hadp : MeasureTheory.StronglyAdapted 𝒢 f) (hint : ∀ (i : ℕ), MeasureTheory.Integrable (f i) μ) :
  MeasureTheory.Submartingale f 𝒢 μ ↔
    ∀ (τ π : Ω → WithTop ℕ),
      MeasureTheory.IsStoppingTime 𝒢 τ →
        MeasureTheory.IsStoppingTime 𝒢 π →
          τ ≤ π →
            (∃ N, ∀ (x : Ω), π x ≤ ↑N) →
              ∫ (x : Ω), MeasureTheory.stoppedValue f τ x ∂μ ≤
                ∫ (x : Ω), MeasureTheory.stoppedValue f π x ∂μ
```

## Depends on

- [Bochner integral](../../analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Conditional expectation](../definitions-in-probability-theory/conditional-expectation.md)
- [Stopping time](stopping-time.md)

## Sources

- [Mathlib documentation: `MeasureTheory.submartingale_iff_expected_stoppedValue_mono`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Martingale/OptionalStopping.html#MeasureTheory.submartingale_iff_expected_stoppedValue_mono)
- [Source of `MeasureTheory.submartingale_iff_expected_stoppedValue_mono` in Mathlib/Probability/Martingale/OptionalStopping.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Probability/Martingale/OptionalStopping.lean#L84)
- [Mathlib overview: Probability Theory › Stochastic Processes](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L424)
- [Freek Wiedijk's 100 theorems, no. 62](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L315)
- [1000+ theorems list: Q2027347](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1986)
- [1000+ theorems project: Q2027347](https://1000-plus.github.io/all.html?length=-1#Q2027347)
- [Wikipedia: Optional stopping theorem](https://en.wikipedia.org/wiki/Optional_stopping_theorem)
- [Wikidata: Q2027347](https://www.wikidata.org/wiki/Q2027347)
