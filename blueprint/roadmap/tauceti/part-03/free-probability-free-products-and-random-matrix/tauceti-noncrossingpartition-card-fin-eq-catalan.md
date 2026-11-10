---
declaration: theorem
origin: cited
lean: TauCeti.NoncrossingPartition.card_fin_eq_catalan
statement: formalized
proof: formalized
---

# TauCeti.NoncrossingPartition.card_fin_eq_catalan

There are `catalan n` noncrossing partitions of the `n` ordered positions of `Fin n`.

```lean
TauCeti.NoncrossingPartition.card_fin_eq_catalan (n : ℕ) :
  Fintype.card (TauCeti.NoncrossingPartition Finset.univ) = catalan n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NoncrossingPartition.card_fin_eq_catalan`](https://taucetiproject.org/docs/TauCeti/Combinatorics/NoncrossingPartition/Catalan.html#TauCeti.NoncrossingPartition.card_fin_eq_catalan).

## Sources

- [Tau Ceti documentation: `TauCeti.NoncrossingPartition.card_fin_eq_catalan`](https://taucetiproject.org/docs/TauCeti/Combinatorics/NoncrossingPartition/Catalan.html#TauCeti.NoncrossingPartition.card_fin_eq_catalan)
- [Source of `TauCeti.NoncrossingPartition.card_fin_eq_catalan` in TauCeti/Combinatorics/NoncrossingPartition/Catalan.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/NoncrossingPartition/Catalan.lean#L452)
- [Tau Ceti roadmap status: Free probability, free products, and random matrix models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FreeProbability/STATUS.md)
