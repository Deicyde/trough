# Turán's theorem

**Turán's theorem**. `turanGraph n r` is, up to isomorphism, the unique
`r + 1`-cliquefree Turán-maximal graph on `n` vertices.

```lean
SimpleGraph.isTuranMaximal_iff_nonempty_iso_turanGraph.{u_1} {V : Type u_1} [Fintype V]
  {G : SimpleGraph V} [DecidableRel G.Adj] {r : ℕ} (hr : 0 < r) :
  G.IsTuranMaximal r ↔ Nonempty (G ≃g SimpleGraph.turanGraph (Fintype.card V) r)
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)
- [Simple graph](simple-graph.md)

## Proof depends on

- [Finite](../pigeonhole-principles/finite.md)
- [Integer](../../general-algebra/numbers/integer.md)

## Sources

- [Mathlib documentation: `SimpleGraph.isTuranMaximal_iff_nonempty_iso_turanGraph`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SimpleGraph/Extremal/Turan.html#SimpleGraph.isTuranMaximal_iff_nonempty_iso_turanGraph)
- [Source of `SimpleGraph.isTuranMaximal_iff_nonempty_iso_turanGraph` in Mathlib/Combinatorics/SimpleGraph/Extremal/Turan.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/SimpleGraph/Extremal/Turan.lean#L290)
- [Mathlib overview: Combinatorics › Graph theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L529)
- [1000+ theorems list: Q1047749](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1224)
- [1000+ theorems project: Q1047749](https://1000-plus.github.io/all.html?length=-1#Q1047749)
- [Wikipedia: Turán's theorem](https://en.wikipedia.org/wiki/Tur%C3%A1n's_theorem)
- [Wikidata: Q1047749](https://www.wikidata.org/wiki/Q1047749)
