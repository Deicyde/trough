---
declaration: theorem
origin: cited
lean: TauCeti.markoffGraph_isTree
statement: formalized
proof: formalized
---

# The positive Markoff graph is a tree

Its vertices are the ordered positive Markoff
triples, and two of them are adjacent when they are related by a Vieta move.

```lean
TauCeti.markoffGraph_isTree : TauCeti.markoffGraph.IsTree
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Markoff's theorem](../../part-03/other-results/markoffs-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.markoffGraph_isTree`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Markoff/Tree.html#TauCeti.markoffGraph_isTree).

## Sources

- [Tau Ceti documentation: `TauCeti.markoffGraph_isTree`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Markoff/Tree.html#TauCeti.markoffGraph_isTree)
- [Source of `TauCeti.markoffGraph_isTree` in TauCeti/NumberTheory/Markoff/Tree.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Markoff/Tree.lean#L222)
- [Tau Ceti roadmap status: Classical arithmetic, sequences, polynomials and reciprocity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ClassicalArithmeticCompletion/STATUS.md)
