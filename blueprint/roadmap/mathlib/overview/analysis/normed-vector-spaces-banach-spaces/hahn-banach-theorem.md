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
- [Normed vector space over a normed field](normed-vector-space-over-a-normed-field.md)
- [Vector subspace](../../../undergraduate/linear-algebra/fundamentals/vector-subspace.md)

## Proof depends on

- [Dual vector space](../../linear-algebra/duality/dual-vector-space.md)
- [Finite set](../../data-structures/sets/finite-set.md)
- [The Triangle Inequality](../../../hundred-theorems/part-04/the-triangle-inequality.md)
- [Topological ring](../../topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `exists_extension_norm_eq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Module/HahnBanach.html#exists_extension_norm_eq)
- [Source of `exists_extension_norm_eq` in Mathlib/Analysis/Normed/Module/HahnBanach.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Normed/Module/HahnBanach.lean#L40)
- [Mathlib overview: Analysis › Normed vector spaces/Banach spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L288)
- [1000+ theorems list: Q866116](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L1009)
- [1000+ theorems project: Q866116](https://1000-plus.github.io/all.html?length=-1#Q866116)
- [Wikipedia: Hahn–Banach theorem](https://en.wikipedia.org/wiki/Hahn%E2%80%93Banach_theorem)
- [Wikidata: Q866116](https://www.wikidata.org/wiki/Q866116)
