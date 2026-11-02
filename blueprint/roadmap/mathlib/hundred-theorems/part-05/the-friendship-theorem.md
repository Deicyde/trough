---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Theorems100.friendship_theorem
mathlib_file: Archive/Wiedijk100Theorems/FriendshipGraphs.lean
---

# The Friendship Theorem

**Friendship theorem**: We wish to show that a friendship graph has a politician (a vertex
adjacent to all others). We proceed by contradiction, and assume the graph has no politician.
We have already proven that a friendship graph with no politician is `d`-regular for some `d`,
and now we do casework on `d`.
If the degree is at most 2, we observe by casework that it has a politician anyway.
If the degree is at least 3, the graph cannot exist.

```lean
Theorems100.friendship_theorem.{u} {V : Type u} [Fintype V] {G : SimpleGraph V}
  (hG : Theorems100.Friendship G) [Nonempty V] : Theorems100.ExistsPolitician G
```

## Depends on

- [Finite set](../../overview/data-structures/sets/finite-set.md)
- [Set](../../overview/data-structures/sets/set.md)
- [Simple graph](../../overview/combinatorics/graph-theory/simple-graph.md)

## Proof depends on

- [Adjacency matrix](../../overview/combinatorics/graph-theory/adjacency-matrix.md)
- [Algebra of endomorphisms of a vector space](../../undergraduate/linear-algebra/fundamentals/algebra-of-endomorphisms-of-a-vector-space.md)
- [Bezout’s Theorem](../part-03/bezouts-theorem.md)
- [Cantor’s Theorem](../part-04/cantors-theorem.md)
- [Cardinal](../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Characteristic polynomial](../../overview/linear-algebra/endomorphism-polynomials/characteristic-polynomial.md)
- [Congruence in $\Z$](../../undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in.md)
- [Existence of bases](../../undergraduate/linear-algebra/fundamentals/existence-of-bases.md)
- [Field](../../overview/general-algebra/field-theory/field.md)
- [Frobenius morphism](../../overview/general-algebra/field-theory/frobenius-morphism.md)
- [Isomorphism with $K^n$](../../overview/linear-algebra/finite-dimensional-vector-spaces/isomorphism-with-k-n.md)
- [Kernel of a linear map](../../undergraduate/linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Local ring](../../overview/general-algebra/rings/local-ring.md)
- [Orbit](../../undergraduate/group-theory/basic-definitions/orbit.md)
- [Order of an element](../../undergraduate/group-theory/basic-definitions/order-of-an-element.md)
- [Ordered ring](../../overview/general-algebra/rings/ordered-ring.md)
- [Polynomial functions](../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-etc/polynomial-functions.md)
- [Prime numbers](../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)
- [Schroeder-Bernstein Theorem](../part-02/schroeder-bernstein-theorem.md)
- [Subgroup](../../overview/general-algebra/group-theory/part-01/subgroup.md)
- [Sum of subspaces](../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)
- [Tensor product of algebras](../../overview/general-algebra/algebras-over-a-ring/tensor-product-of-algebras.md)

## Sources

- [Mathlib documentation: `Theorems100.friendship_theorem`](https://leanprover-community.github.io/mathlib4_docs/Archive/Wiedijk100Theorems/FriendshipGraphs.html#Theorems100.friendship_theorem)
- [Source of `Theorems100.friendship_theorem` in Archive/Wiedijk100Theorems/FriendshipGraphs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Archive/Wiedijk100Theorems/FriendshipGraphs.lean#L325)
- [Freek Wiedijk's 100 theorems, no. 83](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L425)
- [1000+ theorems list: Q5504427](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L3240)
- [1000+ theorems project: Q5504427](https://1000-plus.github.io/?length=-1#Q5504427)
- [Wikipedia: Friendship theorem](https://en.wikipedia.org/wiki/Friendship_theorem)
- [Wikidata: Q5504427](https://www.wikidata.org/wiki/Q5504427)
