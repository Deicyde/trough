---
declaration: theorem
origin: cited
lean: TauCeti.TreeWalk.card_closedTreeWalk
statement: formalized
proof: formalized
---

# TauCeti.TreeWalk.card_closedTreeWalk

There are `catalan k` closed walks of length `2 * k` in first-visit labelling that visit
`k + 1` vertices and traverse every edge exactly twice.

```lean
TauCeti.TreeWalk.card_closedTreeWalk (k : ℕ) :
  Nat.card (TauCeti.TreeWalk.ClosedTreeWalk k) = catalan k
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.TreeWalk.card_closedTreeWalk`](https://taucetiproject.org/docs/TauCeti/Combinatorics/TreeWalk/Basic.html#TauCeti.TreeWalk.card_closedTreeWalk).

## Sources

- [Tau Ceti documentation: `TauCeti.TreeWalk.card_closedTreeWalk`](https://taucetiproject.org/docs/TauCeti/Combinatorics/TreeWalk/Basic.html#TauCeti.TreeWalk.card_closedTreeWalk)
- [Source of `TauCeti.TreeWalk.card_closedTreeWalk` in TauCeti/Combinatorics/TreeWalk/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Combinatorics/TreeWalk/Basic.lean#L817)
- [Tau Ceti roadmap status: Random matrices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RandomMatrices/STATUS.md)
