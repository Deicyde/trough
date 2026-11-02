---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: tendsto_subseq_of_frequently_bounded, tendsto_subseq_of_bounded
mathlib_file: Mathlib/Topology/MetricSpace/Sequences.lean
---

# Bolzano–Weierstrass theorem (1000+ theorems)

Mathlib records this with 2 declarations.

`tendsto_subseq_of_frequently_bounded`: A version of **Bolzano-Weierstrass**: in a proper metric space (e.g. $ℝ^n$),
every bounded sequence has a converging subsequence. This version assumes only
that the sequence is frequently in some bounded set.

```lean
tendsto_subseq_of_frequently_bounded.{u_1} {X : Type u_1} [PseudoMetricSpace X] [ProperSpace X]
  {s : Set X} (hs : Bornology.IsBounded s) {x : ℕ → X} (hx : ∃ᶠ (n : ℕ) in Filter.atTop, x n ∈ s) :
  ∃ a ∈ closure s, ∃ φ, StrictMono φ ∧ Filter.Tendsto (x ∘ φ) Filter.atTop (nhds a)
```

`tendsto_subseq_of_bounded`: A version of **Bolzano-Weierstrass**: in a proper metric space (e.g. $ℝ^n$),
every bounded sequence has a converging subsequence.

```lean
tendsto_subseq_of_bounded.{u_1} {X : Type u_1} [PseudoMetricSpace X] [ProperSpace X] {s : Set X}
  (hs : Bornology.IsBounded s) {x : ℕ → X} (hx : ∀ (n : ℕ), x n ∈ s) :
  ∃ a ∈ closure s, ∃ φ, StrictMono φ ∧ Filter.Tendsto (x ∘ φ) Filter.atTop (nhds a)
```

## Depends on

- [Bornology](../../../../overview/analysis/topological-vector-spaces/bornology.md)
- [Closure](../../../../overview/topology/general-topology/part-01/closure.md)
- [Compactness in terms of filters](../../../../overview/topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Order (Real numbers)](../../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)
- [Uniform space](../../../../overview/topology/uniform-notions/uniform-space.md)

## Proof depends on

- [Ordered ring](../../../../overview/general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `tendsto_subseq_of_frequently_bounded`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/MetricSpace/Sequences.html#tendsto_subseq_of_frequently_bounded)
- [Source of `tendsto_subseq_of_frequently_bounded` in Mathlib/Topology/MetricSpace/Sequences.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/MetricSpace/Sequences.lean#L27)
- [Mathlib documentation: `tendsto_subseq_of_bounded`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/MetricSpace/Sequences.html#tendsto_subseq_of_bounded)
- [Source of `tendsto_subseq_of_bounded` in Mathlib/Topology/MetricSpace/Sequences.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/MetricSpace/Sequences.lean#L37)
- [1000+ theorems list: Q468391](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L465)
- [1000+ theorems project: Q468391](https://1000-plus.github.io/all.html?length=-1#Q468391)
- [Wikipedia: Bolzano–Weierstrass theorem](https://en.wikipedia.org/wiki/Bolzano%E2%80%93Weierstrass_theorem)
- [Wikidata: Q468391](https://www.wikidata.org/wiki/Q468391)
