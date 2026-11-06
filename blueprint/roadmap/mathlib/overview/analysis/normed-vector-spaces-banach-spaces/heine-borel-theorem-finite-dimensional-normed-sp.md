# Heine-Borel theorem (finite-dimensional normed spaces are proper)

Any finite-dimensional vector space over a locally compact field is proper.
We do not register this as an instance to avoid an instance loop when trying to prove the
properness of `𝕜`, and the search for `𝕜` as an unknown metavariable. Declare the instance
explicitly when needed.

```lean
FiniteDimensional.proper.{u, v} (𝕜 : Type u) [NontriviallyNormedField 𝕜] (E : Type v)
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] [LocallyCompactSpace 𝕜] [FiniteDimensional 𝕜 E] :
  ProperSpace E
```

## Depends on

- [Compactness in terms of filters](../../topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Finite-dimensionality](../../linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Normed vector space over a normed field](normed-vector-space-over-a-normed-field.md)

## Proof depends on

- [Basis](../../linear-algebra/fundamentals/basis.md)
- [Cardinal](../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Continuous linear map](../../topology/topological-algebra/continuous-linear-map.md)
- [Equivalence of norms in finite dimension](equivalence-of-norms-in-finite-dimension.md)
- [Field $\R$ of real numbers](../../../undergraduate/ring-theory/field-theory/field-r-of-real-numbers.md)
- [Heine-Borel theorem (proper metric space version)](../../topology/metric-spaces/heine-borel-theorem-proper-metric-space-version.md)
- [Linear independence](../../../undergraduate/linear-algebra/fundamentals/linear-independence.md)
- [Local ring](../../general-algebra/rings/local-ring.md)
- [Ordered ring](../../general-algebra/rings/ordered-ring.md)
- [Topological ring](../../topology/topological-algebra/topological-ring.md)
- [Topology on a normed vector space](topology-on-a-normed-vector-space.md)

## Sources

- [Mathlib documentation: `FiniteDimensional.proper`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Module/FiniteDimension.html#FiniteDimensional.proper)
- [Source of `FiniteDimensional.proper` in Mathlib/Analysis/Normed/Module/FiniteDimension.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Normed/Module/FiniteDimension.lean#L542)
- [Mathlib overview: Analysis › Normed vector spaces/Banach spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L283)
- [Mathlib undergraduate list: Topology › Normed vector spaces on $\R$ and $\C$](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L434)
