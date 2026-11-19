---
declaration: theorem
origin: cited
lean: TauCeti.existsUnique_transitiveGroupLabel_five
statement: formalized
proof: formalized
---

# TauCeti.existsUnique_transitiveGroupLabel_five

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
- [Source of `TauCeti.existsUnique_transitiveGroupLabel_five` in TauCeti/GroupTheory/Perm/TransitiveGroupLabel/Classification.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/Perm/TransitiveGroupLabel/Classification.lean#L828)
- [Tau Ceti roadmap status: Galois groups of polynomials](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/PolynomialGaloisGroups/STATUS.md)
