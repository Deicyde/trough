---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: tendsto_subseq_of_bounded
mathlib_file: Mathlib/Topology/MetricSpace/Sequences.lean
---

# Bolzano-Weierstrass theorem

A version of **Bolzano-Weierstrass**: in a proper metric space (e.g. $ℝ^n$),
every bounded sequence has a converging subsequence.

```lean
tendsto_subseq_of_bounded.{u_1} {X : Type u_1} [PseudoMetricSpace X] [ProperSpace X] {s : Set X}
  (hs : Bornology.IsBounded s) {x : ℕ → X} (hx : ∀ (n : ℕ), x n ∈ s) :
  ∃ a ∈ closure s, ∃ φ, StrictMono φ ∧ Filter.Tendsto (x ∘ φ) Filter.atTop (nhds a)
```

## Depends on

- [Bornology](../../../overview/analysis/topological-vector-spaces/bornology.md)
- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Compactness in terms of filters](../../../overview/topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Order](../real-numbers/order.md)
- [Uniform space](../../../overview/topology/uniform-notions/uniform-space.md)

## Proof depends on

- [Bolzano–Weierstrass theorem](../../../thousand-plus/analysis/26-real-functions/part-01/bolzano-weierstrass-theorem.md)

## Sources

- [Mathlib documentation: `tendsto_subseq_of_bounded`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/MetricSpace/Sequences.html#tendsto_subseq_of_bounded)
- [Source of `tendsto_subseq_of_bounded` in Mathlib/Topology/MetricSpace/Sequences.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/MetricSpace/Sequences.lean#L37)
- [Mathlib undergraduate list: Single Variable Real Analysis › Topology of R](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L292)
