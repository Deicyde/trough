---
declaration: theorem
origin: cited
lean: TauCeti.ValidLieTypeIndex.finite
statement: formalized
proof: formalized
---

# Every Lie-type group on the classification list is finite

The candidate group of a valid
Lie-type index is the derived subgroup of the finite Steinberg fixed points modulo its centre.

```lean
TauCeti.ValidLieTypeIndex.finite (d : TauCeti.ValidLieTypeIndex) : Finite d.Group
```

## Depends on

- [TauCeti.ValidLieTypeIndex.Group](../stating-the-classification-of-finite-simple-grou/tauceti-validlietypeindex-group.md)

## Proof depends on

- [The ambient group of a valid Lie-type index](../stating-the-classification-of-finite-simple-grou/the-ambient-group-of-a-valid-lie-type-index.md)
- [Cauchy--Binet for `2 × 2` minors](../../linear-algebra/matrix/cauchy-binet-for-2-2-minors.md)
- [The finite-coordinate fixed-point criterion](the-finite-coordinate-fixed-point-criterion.md)
- [TauCeti.F4ShortRoot.PrimeField.specialIsogeny_specialIsogeny](../stating-the-classification-of-finite-simple-grou/tauceti-f4shortroot-primefield-specialisogeny-sp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ValidLieTypeIndex.finite`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/CFSG/BasicProperties/LieTypeFinite.html#TauCeti.ValidLieTypeIndex.finite).

## Sources

- [Tau Ceti documentation: `TauCeti.ValidLieTypeIndex.finite`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/CFSG/BasicProperties/LieTypeFinite.html#TauCeti.ValidLieTypeIndex.finite)
- [Source of `TauCeti.ValidLieTypeIndex.finite` in TauCeti/GroupTheory/SpecificGroups/CFSG/BasicProperties/LieTypeFinite.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/SpecificGroups/CFSG/BasicProperties/LieTypeFinite.lean#L144)
- [Tau Ceti roadmap status: Finiteness and simplicity of the groups on the CFSG list](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CFSGBasicProperties/STATUS.md)
