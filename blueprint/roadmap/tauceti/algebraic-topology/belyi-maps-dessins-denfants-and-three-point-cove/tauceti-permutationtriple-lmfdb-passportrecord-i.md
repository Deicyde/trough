---
declaration: structure
origin: cited
lean: TauCeti.PermutationTriple.LMFDB.PassportRecord.IsValidAt
statement: formalized
---

# TauCeti.PermutationTriple.LMFDB.PassportRecord.IsValidAt

The record `r` is a valid row for the passport of the connected triple `t`: the triple `t` is
one of the stored triples, the certificate data of `r` are correct on the sheets of `t`, and every
other certified field is the corresponding invariant of `t`.

The aggregations `numOrbits` and `maxdegbf`, and the strings `plabel`, `primitivization` and
`autGroup`, are not constrained.

```lean
TauCeti.PermutationTriple.LMFDB.PassportRecord.IsValidAt {n : ℕ}
  (r : TauCeti.PermutationTriple.LMFDB.PassportRecord n) (t : TauCeti.ConnectedTriple n) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PermutationTriple.LMFDB.PassportRecord.IsValidAt`](https://taucetiproject.org/docs/TauCeti/Combinatorics/PermutationTriple/LMFDB/PassportRecord/Basic.html#TauCeti.PermutationTriple.LMFDB.PassportRecord.IsValidAt).

## Sources

- [Tau Ceti documentation: `TauCeti.PermutationTriple.LMFDB.PassportRecord.IsValidAt`](https://taucetiproject.org/docs/TauCeti/Combinatorics/PermutationTriple/LMFDB/PassportRecord/Basic.html#TauCeti.PermutationTriple.LMFDB.PassportRecord.IsValidAt)
- [Source of `TauCeti.PermutationTriple.LMFDB.PassportRecord.IsValidAt` in TauCeti/Combinatorics/PermutationTriple/LMFDB/PassportRecord/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/PermutationTriple/LMFDB/PassportRecord/Basic.lean#L127)
- [Tau Ceti roadmap status: Belyi maps, dessins d'enfants, and three-point covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BelyiMaps/STATUS.md)
