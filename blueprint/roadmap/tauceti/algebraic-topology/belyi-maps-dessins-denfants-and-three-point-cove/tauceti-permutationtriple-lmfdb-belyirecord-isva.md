---
declaration: structure
origin: cited
lean: TauCeti.PermutationTriple.LMFDB.BelyiRecord.IsValidFor
statement: formalized
---

# TauCeti.PermutationTriple.LMFDB.BelyiRecord.IsValidFor

A row is valid for the passport `P` when its stored degree is the degree, its stored orbit
size is its number of stored embedding entries, it stores at least one triple, every stored
triple denotes a connected triple with passport `P`, its stored cycle notation writes the stored
triples position by position, the stored partitions are those of `P`, and the stored genus is the
genus of every stored triple.

The labels, the base field, the equations, and the embedding values are not constrained.

```lean
TauCeti.PermutationTriple.LMFDB.BelyiRecord.IsValidFor {n : ℕ}
  (r : TauCeti.PermutationTriple.LMFDB.BelyiRecord n) (P : TauCeti.PassportSpec n) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PermutationTriple.LMFDB.BelyiRecord.IsValidFor`](https://taucetiproject.org/docs/TauCeti/Combinatorics/PermutationTriple/LMFDB/BelyiRecord/Basic.html#TauCeti.PermutationTriple.LMFDB.BelyiRecord.IsValidFor).

## Sources

- [Tau Ceti documentation: `TauCeti.PermutationTriple.LMFDB.BelyiRecord.IsValidFor`](https://taucetiproject.org/docs/TauCeti/Combinatorics/PermutationTriple/LMFDB/BelyiRecord/Basic.html#TauCeti.PermutationTriple.LMFDB.BelyiRecord.IsValidFor)
- [Source of `TauCeti.PermutationTriple.LMFDB.BelyiRecord.IsValidFor` in TauCeti/Combinatorics/PermutationTriple/LMFDB/BelyiRecord/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/PermutationTriple/LMFDB/BelyiRecord/Basic.lean#L352)
- [Tau Ceti roadmap status: Belyi maps, dessins d'enfants, and three-point covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BelyiMaps/STATUS.md)
