---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: SimpleGraph.tutte
mathlib_file: Mathlib/Combinatorics/SimpleGraph/Tutte.lean
---

# Tutte theorem

**Tutte's theorem**

A graph has a perfect matching if and only if: For every subset `u` of vertices, removing this
subset induces at most `u.ncard` components of odd size. This is formally stated using the
predicate `IsTutteViolator`, which is satisfied exactly when this condition does not hold.

```lean
SimpleGraph.tutte.{u_1} {V : Type u_1} {G : SimpleGraph V} [Finite V] :
  (∃ M, M.IsPerfectMatching) ↔ ∀ (u : Set V), ¬G.IsTutteViolator u
```

## Depends on

- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Matching](../../../overview/combinatorics/graph-theory/matching.md)
- [Natural number](../../../overview/general-algebra/numbers/natural-number.md)
- [Ring morphism](../../../overview/general-algebra/rings/ring-morphism.md)

## Proof depends on

- [Degree-sum formula](../../../overview/combinatorics/graph-theory/degree-sum-formula.md)

## Sources

- [Mathlib documentation: `SimpleGraph.tutte`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SimpleGraph/Tutte.html#SimpleGraph.tutte)
- [Source of `SimpleGraph.tutte` in Mathlib/Combinatorics/SimpleGraph/Tutte.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/SimpleGraph/Tutte.lean#L311)
- [1000+ theorems list: Q510197](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L511)
- [1000+ theorems project: Q510197](https://1000-plus.github.io/all.html?length=-1#Q510197)
- [Wikipedia: Tutte theorem](https://en.wikipedia.org/wiki/Tutte_theorem)
- [Wikidata: Q510197](https://www.wikidata.org/wiki/Q510197)
