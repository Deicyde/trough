# Inner product space $L^2$

Mathlib states this as `MeasureTheory.L2.innerProductSpace`.

```lean
MeasureTheory.L2.innerProductSpace.{u_1, u_2, u_4} {α : Type u_1} {E : Type u_2} {𝕜 : Type u_4}
  [RCLike 𝕜] {m : MeasurableSpace α} {μ : MeasureTheory.Measure α} [NormedAddCommGroup E]
  [InnerProductSpace 𝕜 E] : InnerProductSpace 𝕜 ↥(MeasureTheory.Lp E 2 μ)
```

## Depends on

- [$L^p$ space](../../../overview/analysis/measures-and-integral-calculus/part-01/l-p-space.md)
- [Inner product space, over $R$ or $C$](../../../overview/analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)

## Sources

- [Mathlib documentation: `MeasureTheory.L2.innerProductSpace`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/L2Space.html#MeasureTheory.L2.innerProductSpace)
- [Source of `MeasureTheory.L2.innerProductSpace` in Mathlib/MeasureTheory/Function/L2Space.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/MeasureTheory/Function/L2Space.lean#L191)
- [Mathlib undergraduate list: Topology › Hilbert spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L444)
