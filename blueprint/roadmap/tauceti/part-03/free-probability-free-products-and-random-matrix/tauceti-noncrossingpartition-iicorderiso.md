---
declaration: def
origin: cited
lean: TauCeti.NoncrossingPartition.iicOrderIso
statement: formalized
---

# TauCeti.NoncrossingPartition.iicOrderIso

The lower interval `[0_s, π]` of the lattice of noncrossing partitions of `s` is isomorphic
to the product of the lattices of noncrossing partitions of the parts of `π`: a noncrossing
partition `σ ≤ π` corresponds to its restrictions to the parts of `π`, and a family of noncrossing
partitions of the parts corresponds to their juxtaposition.

```lean
TauCeti.NoncrossingPartition.iicOrderIso.{u_1} {α : Type u_1} [LinearOrder α] {s : Finset α}
  (π : TauCeti.NoncrossingPartition s) :
  ↑(Set.Iic π) ≃o ((B : ↥(↑π).parts) → TauCeti.NoncrossingPartition ↑B)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NoncrossingPartition.iicOrderIso`](https://taucetiproject.org/docs/TauCeti/Combinatorics/NoncrossingPartition/Interval.html#TauCeti.NoncrossingPartition.iicOrderIso).

## Sources

- [Tau Ceti documentation: `TauCeti.NoncrossingPartition.iicOrderIso`](https://taucetiproject.org/docs/TauCeti/Combinatorics/NoncrossingPartition/Interval.html#TauCeti.NoncrossingPartition.iicOrderIso)
- [Source of `TauCeti.NoncrossingPartition.iicOrderIso` in TauCeti/Combinatorics/NoncrossingPartition/Interval.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/NoncrossingPartition/Interval.lean#L56)
- [Tau Ceti roadmap status: Free probability, free products, and random matrix models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FreeProbability/STATUS.md)
