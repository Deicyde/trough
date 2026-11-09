# Martingale

A family of functions `f : ι → Ω → E` is a martingale with respect to a filtration `ℱ` if `f`
is strongly adapted with respect to `ℱ` and for all `i ≤ j`, `μ[f j | ℱ i] =ᵐ[μ] f i`.

```lean
MeasureTheory.Martingale.{u_1, u_2, u_3} {Ω : Type u_1} {E : Type u_2} {ι : Type u_3} [Preorder ι]
  {m0 : MeasurableSpace Ω} [NormedAddCommGroup E] [NormedSpace ℝ E] (f : ι → Ω → E)
  (ℱ : MeasureTheory.Filtration ι m0) (μ : MeasureTheory.Measure Ω) : Prop
```

## Depends on

- [Conditional expectation](../definitions-in-probability-theory/conditional-expectation.md)

## Sources

- [Mathlib documentation: `MeasureTheory.Martingale`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Martingale/Basic.html#MeasureTheory.Martingale)
- [Source of `MeasureTheory.Martingale` in Mathlib/Probability/Martingale/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Probability/Martingale/Basic.lean#L51)
- [Mathlib overview: Probability Theory › Stochastic Processes](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L423)
