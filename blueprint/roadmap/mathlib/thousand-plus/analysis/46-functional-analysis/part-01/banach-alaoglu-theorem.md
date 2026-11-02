---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: WeakDual.isCompact_polar
mathlib_file: Mathlib/Analysis/Normed/Module/WeakDual.lean
---

# Banach–Alaoglu theorem

The **Banach-Alaoglu theorem**: the polar set of a neighborhood `s` of the origin in a
normed space `E` is a compact subset of `WeakDual 𝕜 E`.

```lean
WeakDual.isCompact_polar.{u_1, u_3} (𝕜 : Type u_1) {E : Type u_3} [NontriviallyNormedField 𝕜]
  [SeminormedAddCommGroup E] [NormedSpace 𝕜 E] [ProperSpace 𝕜] {s : Set E} (s_nhds : s ∈ nhds 0) :
  IsCompact (WeakDual.polar 𝕜 s)
```

## Depends on

- [Associative algebra over a commutative ring](../../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Compactness in terms of filters](../../../../overview/topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Dual of a normed space](../../../../overview/analysis/normed-vector-spaces-banach-spaces/dual-of-a-normed-space.md)
- [Normed vector space over a normed field](../../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Topological ring](../../../../overview/topology/topological-algebra/topological-ring.md)

## Proof depends on

- [Closure](../../../../overview/topology/general-topology/part-01/closure.md)
- [Metric structure](../../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Ordered ring](../../../../overview/general-algebra/rings/ordered-ring.md)
- [Ring structure $\Z$](../../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)
- [Weak-* topology for dualities](../../../../overview/analysis/topological-vector-spaces/weak-topology-for-dualities.md)

## Sources

- [Mathlib documentation: `WeakDual.isCompact_polar`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Module/WeakDual.html#WeakDual.isCompact_polar)
- [Source of `WeakDual.isCompact_polar` in Mathlib/Analysis/Normed/Module/WeakDual.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Normed/Module/WeakDual.lean#L312)
- [1000+ theorems list: Q537618](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L545)
- [1000+ theorems project: Q537618](https://1000-plus.github.io/?length=-1#Q537618)
- [Wikipedia: Banach–Alaoglu theorem](https://en.wikipedia.org/wiki/Banach%E2%80%93Alaoglu_theorem)
- [Wikidata: Q537618](https://www.wikidata.org/wiki/Q537618)
