---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Differentiable.apply_eq_apply_of_bounded
mathlib_file: Mathlib/Analysis/Complex/Liouville.lean
---

# Liouville theorem

**Liouville's theorem**: a complex differentiable bounded function `f : E → F` is a constant.

```lean
Differentiable.apply_eq_apply_of_bounded.{u, v} {E : Type u} [NormedAddCommGroup E]
  [NormedSpace ℂ E] {F : Type v} [NormedAddCommGroup F] [NormedSpace ℂ F] {f : E → F}
  (hf : Differentiable ℂ f) (hb : Bornology.IsBounded (Set.range f)) (z w : E) : f z = f w
```

## Depends on

- [Differentiable functions](../../../undergraduate/multivariable-calculus/differential-calculus/differentiable-functions.md)
- [Field $\C$ of complex numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-of-complex-numbers.md)
- [Normed vector space over a normed field](../normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Proof depends on

- [Cauchy formulas](../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/cauchy-formulas.md)
- [Dual vector space](../../linear-algebra/duality/dual-vector-space.md)
- [Higher-order derivatives of functions](../../../undergraduate/single-variable-real-analysis/differentiability/higher-order-derivatives-of-functions.md)

## Sources

- [Mathlib documentation: `Differentiable.apply_eq_apply_of_bounded`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Liouville.html#Differentiable.apply_eq_apply_of_bounded)
- [Source of `Differentiable.apply_eq_apply_of_bounded` in Mathlib/Analysis/Complex/Liouville.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Complex/Liouville.lean#L116)
- [Mathlib overview: Analysis › Complex analysis](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L367)
- [1000+ theorems list: Q576478](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L576)
- [1000+ theorems project: Q576478](https://1000-plus.github.io/?length=-1#Q576478)
- [Wikipedia: Liouville's theorem (complex analysis)](https://en.wikipedia.org/wiki/Liouville's_theorem_%28complex_analysis%29)
- [Wikidata: Q576478](https://www.wikidata.org/wiki/Q576478)
