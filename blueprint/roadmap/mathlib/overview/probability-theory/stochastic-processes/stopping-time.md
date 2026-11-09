# Stopping time

A stopping time with respect to some filtration `f` is a function
`τ` such that for all `i`, the preimage of `{j | j ≤ i}` along `τ` is measurable
with respect to `f i`.

Intuitively, the stopping time `τ` describes some stopping rule such that at time
`i`, we may determine it with the information we have at time `i`.

```lean
MeasureTheory.IsStoppingTime.{u_1, u_3} {Ω : Type u_1} {ι : Type u_3} {m : MeasurableSpace Ω}
  [Preorder ι] (f : MeasureTheory.Filtration ι m) (τ : Ω → WithTop ι) : Prop
```

## Depends on

- [Events](../../../undergraduate/probability-theory/definitions-of-a-probability-space/events.md)

## Sources

- [Mathlib documentation: `MeasureTheory.IsStoppingTime`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Process/Stopping.html#MeasureTheory.IsStoppingTime)
- [Source of `MeasureTheory.IsStoppingTime` in Mathlib/Probability/Process/Stopping.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Probability/Process/Stopping.lean#L69)
- [Mathlib overview: Probability Theory › Stochastic Processes](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L425)
