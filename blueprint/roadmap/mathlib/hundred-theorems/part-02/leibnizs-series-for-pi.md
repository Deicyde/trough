---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Real.tendsto_sum_pi_div_four
mathlib_file: Mathlib/Analysis/Real/Pi/Leibniz.lean
---

# Leibniz’s Series for Pi

**Leibniz's series for `π`**. The alternating sum of odd number reciprocals is `π / 4`,
proved by using Abel's limit theorem to extend the Maclaurin series of `arctan` to 1.

```lean
Real.tendsto_sum_pi_div_four :
  Filter.Tendsto (fun k => ∑ i ∈ Finset.range k, (-1) ^ i / (2 * ↑i + 1)) Filter.atTop
    (nhds (Real.pi / 4))
```

## Depends on

- [Bornology](../../overview/analysis/topological-vector-spaces/bornology.md)
- [Cos (extension of trigonometric functions to the complex plane)](../../undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md)
- [Uniform space](../../overview/topology/uniform-notions/uniform-space.md)

## Proof depends on

- [Abel's theorem](../../thousand-plus/analysis/26-real-functions/part-01/abels-theorem.md)
- [Alternating series](../../undergraduate/single-variable-real-analysis/numerical-series/alternating-series.md)
- [Order topology](../../overview/topology/topological-algebra/order-topology.md)
- [Sin (extension of trigonometric functions to the complex plane)](../../undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/sin.md)

## Sources

- [Mathlib documentation: `Real.tendsto_sum_pi_div_four`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Pi/Leibniz.html#Real.tendsto_sum_pi_div_four)
- [Source of `Real.tendsto_sum_pi_div_four` in Mathlib/Analysis/Real/Pi/Leibniz.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Real/Pi/Leibniz.lean#L22)
- [Freek Wiedijk's 100 theorems, no. 26](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L127)
