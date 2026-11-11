---
declaration: theorem
origin: cited
lean: TauCeti.ValidLieTypeIndex.isSimpleGroup_suzuki
statement: formalized
proof: formalized
---

# The Suzuki groups on the classification list are simple

```lean
TauCeti.ValidLieTypeIndex.isSimpleGroup_suzuki {m : ℕ}
  (hv : (TauCeti.LieTypeIndex.suzuki m).Valid) :
  IsSimpleGroup (TauCeti.ValidLieTypeIndex.Group ⟨TauCeti.LieTypeIndex.suzuki m, hv⟩)
```

## Depends on

- [The ambient group of a valid Lie-type index](../stating-the-classification-of-finite-simple-grou/the-ambient-group-of-a-valid-lie-type-index.md)
- [TauCeti.ValidLieTypeIndex.Group](../stating-the-classification-of-finite-simple-grou/tauceti-validlietypeindex-group.md)

## Proof depends on

- [Cauchy--Binet for `2 × 2` minors](../../linear-algebra/matrix/cauchy-binet-for-2-2-minors.md)
- [The finite-field generation theorem](../other-results/the-finite-field-generation-theorem.md)
- [The rank-one Bruhat decomposition `Sz(q) = B ∪ B w B`, for `m ≠ 0`](the-rank-one-bruhat-decomposition-sz-q-b-b-w-b-f.md)
- [The Tits system of rank one on `Sz(q)`, for `m ≠ 0`](the-tits-system-of-rank-one-on-sz-q-for-m-0.md)
- [Tits's simplicity theorem](../tits-system/titss-simplicity-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ValidLieTypeIndex.isSimpleGroup_suzuki`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/CFSG/BasicProperties/Suzuki.html#TauCeti.ValidLieTypeIndex.isSimpleGroup_suzuki).

## Sources

- [Tau Ceti documentation: `TauCeti.ValidLieTypeIndex.isSimpleGroup_suzuki`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/CFSG/BasicProperties/Suzuki.html#TauCeti.ValidLieTypeIndex.isSimpleGroup_suzuki)
- [Source of `TauCeti.ValidLieTypeIndex.isSimpleGroup_suzuki` in TauCeti/GroupTheory/SpecificGroups/CFSG/BasicProperties/Suzuki.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/SpecificGroups/CFSG/BasicProperties/Suzuki.lean#L31)
- [Tau Ceti roadmap status: Finiteness and simplicity of the groups on the CFSG list](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CFSGBasicProperties/STATUS.md)
