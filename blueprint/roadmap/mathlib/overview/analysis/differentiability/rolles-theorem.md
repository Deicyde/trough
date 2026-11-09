# Rolle's theorem

**Rolle's Theorem** `deriv` version

```lean
exists_deriv_eq_zero {f : ℝ → ℝ} {a b : ℝ} (hab : a < b) (hfc : ContinuousOn f (Set.Icc a b))
  (hfI : f a = f b) : ∃ c ∈ Set.Ioo a b, deriv f c = 0
```

## Depends on

- [Differentials (linear tangent functions)](../../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)

## Proof depends on

- [Extreme value theorem](../../topology/topological-algebra/extreme-value-theorem.md)
- [Fermat's theorem (stationary points)](../../../thousand-plus/analysis/26-real-functions/part-01/fermats-theorem-stationary-points.md)
- [Field $\R$ of real numbers](../../../undergraduate/ring-theory/field-theory/field-r-of-real-numbers.md)

## Sources

- [Mathlib documentation: `exists_deriv_eq_zero`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/LocalExtr/Rolle.html#exists_deriv_eq_zero)
- [Source of `exists_deriv_eq_zero` in Mathlib/Analysis/Calculus/LocalExtr/Rolle.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Calculus/LocalExtr/Rolle.lean#L59)
- [Mathlib overview: Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L310)
- [Mathlib undergraduate list: Single Variable Real Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L318)
- [1000+ theorems list: Q193286](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L165)
- [1000+ theorems project: Q193286](https://1000-plus.github.io/all.html?length=-1#Q193286)
- [Wikipedia: Rolle's theorem](https://en.wikipedia.org/wiki/Rolle's_theorem)
- [Wikidata: Q193286](https://www.wikidata.org/wiki/Q193286)
