---
declaration: theorem
origin: cited
lean: TauCeti.existsUnique_transitiveGroupLabel_five
statement: formalized
proof: formalized
---

# TauCeti.existsUnique\_transitiveGroupLabel\_five

A transitive subgroup of the symmetric group on five points carries exactly one label, one of
`5T1`, …, `5T5`.

```lean
TauCeti.existsUnique_transitiveGroupLabel_five (G : Subgroup (Equiv.Perm (Fin 5)))
  [MulAction.IsPretransitive (↥G) (Fin 5)] : ∃! j, TauCeti.TransitiveGroupLabel j G
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.existsUnique_transitiveGroupLabel_five`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Perm/TransitiveGroupLabel/Classification.html#TauCeti.existsUnique_transitiveGroupLabel_five).

## Sources

- [Tau Ceti documentation: `TauCeti.existsUnique_transitiveGroupLabel_five`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Perm/TransitiveGroupLabel/Classification.html#TauCeti.existsUnique_transitiveGroupLabel_five)
- [Source of `TauCeti.existsUnique_transitiveGroupLabel_five` in TauCeti/GroupTheory/Perm/TransitiveGroupLabel/Classification.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/Perm/TransitiveGroupLabel/Classification.lean#L803)
- [Tau Ceti roadmap status: Galois groups of polynomials](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/PolynomialGaloisGroups/STATUS.md)
