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

- [The finite-field generation theorem](the-finite-field-generation-theorem.md)
- [The rank-one Bruhat decomposition `Sz(q) = B ∪ B w B`, for `m ≠ 0`](the-rank-one-bruhat-decomposition-sz-q-b-b-w-b-f.md)
- [Tits's simplicity theorem](../tits-system/titss-simplicity-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ValidLieTypeIndex.isSimpleGroup_suzuki`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/CFSG/BasicProperties/Suzuki.html#TauCeti.ValidLieTypeIndex.isSimpleGroup_suzuki).

## Sources

- [Tau Ceti documentation: `TauCeti.ValidLieTypeIndex.isSimpleGroup_suzuki`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/CFSG/BasicProperties/Suzuki.html#TauCeti.ValidLieTypeIndex.isSimpleGroup_suzuki)
- [Source of `TauCeti.ValidLieTypeIndex.isSimpleGroup_suzuki` in TauCeti/GroupTheory/SpecificGroups/CFSG/BasicProperties/Suzuki.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/SpecificGroups/CFSG/BasicProperties/Suzuki.lean#L31)
