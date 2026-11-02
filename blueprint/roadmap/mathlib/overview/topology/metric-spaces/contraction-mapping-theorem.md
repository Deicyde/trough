---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ContractingWith.exists_fixedPoint
mathlib_file: Mathlib/Topology/MetricSpace/Contracting.lean
---

# Contraction mapping theorem

Banach fixed-point theorem, contraction mapping theorem, `EMetricSpace` version.
A contracting map on a complete metric space has a fixed point.
We include more conclusions in this theorem to avoid proving them again later.

The main API for this theorem are the functions `efixedPoint` and `fixedPoint`,
and lemmas about these functions.

```lean
ContractingWith.exists_fixedPoint.{u_1} {α : Type u_1} [EMetricSpace α] {K : NNReal} {f : α → α}
  [CompleteSpace α] (hf : ContractingWith K f) (x : α) (hx : edist x (f x) ≠ ⊤) :
  ∃ y,
    Function.IsFixedPt f y ∧
      Filter.Tendsto (fun n => f^[n] x) Filter.atTop (nhds y) ∧
        ∀ (n : ℕ), edist (f^[n] x) y ≤ edist x (f x) * ↑K ^ n / (1 - ↑K)
```

## Depends on

- [Completeness](../uniform-notions/completeness.md)
- [Lipschitz continuity](lipschitz-continuity.md)

## Proof depends on

- [Cauchy sequence](../uniform-notions/cauchy-sequence.md)
- [Continuous function](../general-topology/part-01/continuous-function.md)
- [Hausdorff space](../general-topology/part-01/hausdorff-space.md)

## Sources

- [Mathlib documentation: `ContractingWith.exists_fixedPoint`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/MetricSpace/Contracting.html#ContractingWith.exists_fixedPoint)
- [Source of `ContractingWith.exists_fixedPoint` in Mathlib/Topology/MetricSpace/Contracting.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/MetricSpace/Contracting.lean#L90)
- [Mathlib overview: Topology › Metric spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L266)
- [Mathlib undergraduate list: Topology › Topology and Metric Spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L421)
- [1000+ theorems list: Q220680](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L239)
- [1000+ theorems project: Q220680](https://1000-plus.github.io/all.html?length=-1#Q220680)
- [Wikipedia: Banach fixed-point theorem](https://en.wikipedia.org/wiki/Banach_fixed-point_theorem)
- [Wikidata: Q220680](https://www.wikidata.org/wiki/Q220680)
