# Riemann sums

The integral sum of `f : ℝⁿ → E` over a tagged prepartition `π` w.r.t. box-additive volume `vol`
with codomain `E →L[ℝ] F` is the sum of `vol J (f (π.tag J))` over all boxes of `π`.

```lean
BoxIntegral.integralSum.{u, v, w} {ι : Type u} {E : Type v} {F : Type w} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F] {I : BoxIntegral.Box ι}
  (f : (ι → ℝ) → E) (vol : BoxIntegral.BoxAdditiveMap ι (E →L[ℝ] F) ⊤)
  (π : BoxIntegral.TaggedPrepartition I) : F
```

## Depends on

- [Continuous linear map](../../../overview/topology/topological-algebra/continuous-linear-map.md)
- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Sources

- [Mathlib documentation: `BoxIntegral.integralSum`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/BoxIntegral/Basic.html#BoxIntegral.integralSum)
- [Source of `BoxIntegral.integralSum` in Mathlib/Analysis/BoxIntegral/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/BoxIntegral/Basic.lean#L77)
- [Mathlib undergraduate list: Single Variable Real Analysis › Integration](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L341)
