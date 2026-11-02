---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: exists_extension_norm_eq
mathlib_file: Mathlib/Analysis/Normed/Module/HahnBanach.lean
---

# Hahn-Banach theorem

**Hahn-Banach theorem** for continuous linear functions over `𝕜`
satisfying `IsRCLikeNormedField 𝕜`.

```lean
exists_extension_norm_eq.{u_1, u_2} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜]
  [IsRCLikeNormedField 𝕜] {E : Type u_2} [SeminormedAddCommGroup E] [NormedSpace 𝕜 E]
  (p : Subspace 𝕜 E) (f : StrongDual 𝕜 ↥p) : ∃ g, (∀ (x : ↥p), g ↑x = f x) ∧ ‖g‖ = ‖f‖
```

## Depends on

- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Completeness](../../topology/uniform-notions/completeness.md)
- [Dual of a normed space](dual-of-a-normed-space.md)
- [Field $\R$ of real numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-r-of-real-numbers.md)
- [Induced topology](../../topology/general-topology/part-01/induced-topology.md)
- [Metric structure](../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Normed vector space over a normed field](normed-vector-space-over-a-normed-field.md)
- [Ordered ring](../../general-algebra/rings/ordered-ring.md)
- [Permutation group of a type](../../general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Vector subspace](../../../undergraduate/linear-algebra/fundamentals/vector-subspace.md)

## Proof depends on

- [Dual vector space](../../linear-algebra/duality/dual-vector-space.md)
- [Finite set](../../data-structures/sets/finite-set.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)
- [The Triangle Inequality](../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological ring](../../topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `exists_extension_norm_eq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Module/HahnBanach.html#exists_extension_norm_eq)
- [Source of `exists_extension_norm_eq` in Mathlib/Analysis/Normed/Module/HahnBanach.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Normed/Module/HahnBanach.lean#L40)
- [Mathlib overview: Analysis › Normed vector spaces/Banach spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L288)
- [1000+ theorems list: Q866116](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1009)
- [1000+ theorems project: Q866116](https://1000-plus.github.io/all.html?length=-1#Q866116)
- [Wikipedia: Hahn–Banach theorem](https://en.wikipedia.org/wiki/Hahn%E2%80%93Banach_theorem)
- [Wikidata: Q866116](https://www.wikidata.org/wiki/Q866116)
