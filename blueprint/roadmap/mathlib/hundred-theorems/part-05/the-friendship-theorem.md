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
- [Natural number](../../overview/general-algebra/numbers/natural-number.md)
- [Set](../../overview/data-structures/sets/set.md)
- [Simple graph](../../overview/combinatorics/graph-theory/simple-graph.md)

## Proof depends on

- [Adjacency matrix](../../overview/combinatorics/graph-theory/adjacency-matrix.md)
- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Euclid's' algorithm](../../overview/general-algebra/divisibility-in-integral-domains/euclids-algorithm.md)
- [Field](../../overview/general-algebra/field-theory/field.md)
- [Irreducible element](../../overview/general-algebra/divisibility-in-integral-domains/irreducible-element.md)
- [Ordered ring](../../overview/general-algebra/rings/ordered-ring.md)
- [Ring structure $\Z$](../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)

## Sources

- [Mathlib documentation: `Theorems100.friendship_theorem`](https://leanprover-community.github.io/mathlib4_docs/Archive/Wiedijk100Theorems/FriendshipGraphs.html#Theorems100.friendship_theorem)
- [Source of `Theorems100.friendship_theorem` in Archive/Wiedijk100Theorems/FriendshipGraphs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Archive/Wiedijk100Theorems/FriendshipGraphs.lean#L325)
- [Freek Wiedijk's 100 theorems, no. 83](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L425)
- [1000+ theorems list: Q5504427](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L3240)
- [1000+ theorems project: Q5504427](https://1000-plus.github.io/?length=-1#Q5504427)
- [Wikipedia: Friendship theorem](https://en.wikipedia.org/wiki/Friendship_theorem)
- [Wikidata: Q5504427](https://www.wikidata.org/wiki/Q5504427)
