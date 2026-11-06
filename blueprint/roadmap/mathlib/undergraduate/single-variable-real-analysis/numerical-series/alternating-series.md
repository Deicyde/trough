# Alternating series

The **alternating series test** for antitone sequences.

```lean
Antitone.tendsto_alternating_series_of_tendsto_zero {f : ℕ → ℝ} (hfa : Antitone f)
  (hf0 : Filter.Tendsto f Filter.atTop (nhds 0)) :
  ∃ l, Filter.Tendsto (fun n => ∑ i ∈ Finset.range n, (-1) ^ i * f i) Filter.atTop (nhds l)
```

## Depends on

- [Bornology](../../../overview/analysis/topological-vector-spaces/bornology.md)
- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Order](../real-numbers/order.md)

## Proof depends on

- [Completeness of R](../topology-of-r/completeness-of-r.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)
- [Topology on a normed vector space](../../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `Antitone.tendsto_alternating_series_of_tendsto_zero`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecificLimits/Normed.html#Antitone.tendsto_alternating_series_of_tendsto_zero)
- [Source of `Antitone.tendsto_alternating_series_of_tendsto_zero` in Mathlib/Analysis/SpecificLimits/Normed.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/SpecificLimits/Normed.lean#L963)
- [Mathlib undergraduate list: Single Variable Real Analysis › Numerical series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L305)
