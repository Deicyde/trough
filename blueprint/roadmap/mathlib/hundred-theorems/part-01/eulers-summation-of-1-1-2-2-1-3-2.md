---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: hasSum_zeta_two
mathlib_file: Mathlib/NumberTheory/ZetaValues.lean
---

# Euler’s Summation of 1 + (1/2)^2 + (1/3)^2 + ….

Mathlib states this as `hasSum_zeta_two`.

```lean
hasSum_zeta_two : HasSum (fun n => 1 / ↑n ^ 2) (Real.pi ^ 2 / 6)
```

## Depends on

- [Bornology](../../overview/analysis/topological-vector-spaces/bornology.md)
- [Cos (extension of trigonometric functions to the complex plane)](../../undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md)
- [Infinite sum](../../overview/topology/topological-algebra/infinite-sum.md)
- [Uniform space](../../overview/topology/uniform-notions/uniform-space.md)

## Proof depends on

- [Absolutely convergent series in Banach spaces](../../overview/analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Bernoulli numbers](../../overview/general-algebra/number-theory/bernoulli-numbers.md)
- [Characteristic p](../../overview/general-algebra/field-theory/characteristic-p.md)
- [Derivative at a point](../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Euclidean domain](../../overview/general-algebra/divisibility-in-integral-domains/euclidean-domain.md)
- [Fourier Series](../part-04/fourier-series.md)
- [Lebesgue measure (Measures and integral calculus)](../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)
- [Polynomial derivative](../../undergraduate/ring-theory/polynomial-rings/polynomial-derivative.md)
- [Polynomial functions](../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/polynomial-functions.md)

## Sources

- [Mathlib documentation: `hasSum_zeta_two`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/ZetaValues.html#hasSum_zeta_two)
- [Source of `hasSum_zeta_two` in Mathlib/NumberTheory/ZetaValues.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/ZetaValues.lean#L453)
- [Freek Wiedijk's 100 theorems, no. 14](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L73)
- [1000+ theorems list: Q810431](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L906)
- [1000+ theorems project: Q810431](https://1000-plus.github.io/all.html?length=-1#Q810431)
- [Wikipedia: Basel problem](https://en.wikipedia.org/wiki/Basel_problem)
- [Wikidata: Q810431](https://www.wikidata.org/wiki/Q810431)
