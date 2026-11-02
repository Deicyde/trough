---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Complex.tendsto_tsum_powerSeries_nhdsWithin_stolzCone, Real.tendsto_tsum_powerSeries_nhdsWithin_lt
mathlib_file: Mathlib/Analysis/Complex/AbelLimit.lean
---

# Abel's theorem

Mathlib records this with 2 declarations.

`Complex.tendsto_tsum_powerSeries_nhdsWithin_stolzCone`: **Abel's limit theorem**. Given a power series converging at 1, the corresponding function
is continuous at 1 when approaching 1 within any fixed Stolz cone.

```lean
Complex.tendsto_tsum_powerSeries_nhdsWithin_stolzCone {f : ℕ → ℂ} {l : ℂ}
  (h : Filter.Tendsto (fun n => ∑ i ∈ Finset.range n, f i) Filter.atTop (nhds l)) {s : ℝ}
  (hs : 0 < s) :
  Filter.Tendsto (fun z => ∑' (n : ℕ), f n * z ^ n) (nhdsWithin 1 (Complex.stolzCone s)) (nhds l)
```

`Real.tendsto_tsum_powerSeries_nhdsWithin_lt`: **Abel's limit theorem**. Given a real power series converging at 1, the corresponding function
is continuous at 1 when approaching 1 from the left.

```lean
Real.tendsto_tsum_powerSeries_nhdsWithin_lt {f : ℕ → ℝ} {l : ℝ}
  (h : Filter.Tendsto (fun n => ∑ i ∈ Finset.range n, f i) Filter.atTop (nhds l)) :
  Filter.Tendsto (fun x => ∑' (n : ℕ), f n * x ^ n) (nhdsWithin 1 (Set.Iio 1)) (nhds l)
```

## Depends on

- [Field $\C$ of complex numbers](../../../../undergraduate/ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Infinite sum](../../../../overview/topology/topological-algebra/infinite-sum.md)
- [Metric space](../../../../overview/topology/metric-spaces/metric-space.md)
- [Ordered ring](../../../../overview/general-algebra/rings/ordered-ring.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Characteristic zero](../../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Completeness of R](../../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Continuous linear map](../../../../overview/topology/topological-algebra/continuous-linear-map.md)
- [Hausdorff space](../../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Limits of sequences](../../../../undergraduate/topology/topology-and-metric-spaces/limits-of-sequences.md)
- [Metric structure](../../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Normed vector space over a normed field](../../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Ring structure $\Z$](../../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)
- [The Triangle Inequality](../../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological ring](../../../../overview/topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `Complex.tendsto_tsum_powerSeries_nhdsWithin_stolzCone`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/AbelLimit.html#Complex.tendsto_tsum_powerSeries_nhdsWithin_stolzCone)
- [Source of `Complex.tendsto_tsum_powerSeries_nhdsWithin_stolzCone` in Mathlib/Analysis/Complex/AbelLimit.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Complex/AbelLimit.lean#L240)
- [Mathlib documentation: `Real.tendsto_tsum_powerSeries_nhdsWithin_lt`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/AbelLimit.html#Real.tendsto_tsum_powerSeries_nhdsWithin_lt)
- [Source of `Real.tendsto_tsum_powerSeries_nhdsWithin_lt` in Mathlib/Analysis/Complex/AbelLimit.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Complex/AbelLimit.lean#L262)
- [1000+ theorems list: Q318767](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L360)
- [1000+ theorems project: Q318767](https://1000-plus.github.io/?length=-1#Q318767)
- [Wikipedia: Abel's theorem](https://en.wikipedia.org/wiki/Abel's_theorem)
- [Wikidata: Q318767](https://www.wikidata.org/wiki/Q318767)
