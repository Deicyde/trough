---
declaration: theorem
origin: cited
lean: TauCeti.relativePropertyT_inl_slTwo
statement: formalized
proof: formalized
---

# Kazhdan–Margulis theorem

the pair `(ℤ² ⋊ SL(2, ℤ), ℤ²)` has relative property (T) in
every Hilbert-space universe `u`.

```lean
TauCeti.relativePropertyT_inl_slTwo.{u} : SemidirectProduct.inl.range.RelativePropertyT
```

## Depends on

- [Subgroup.RelativePropertyT](../../approximation-deformation-and-rigidity-of-finite/subgroup-relativepropertyt.md)

## Proof depends on

- [Burger's theorem](burgers-theorem.md)
- [Sanov's theorem](../../free-group/sanovs-theorem.md)
- [TauCeti.Amenable](../../amenable-groups/tauceti-amenable.md)
- [TauCeti.not_amenable_of_injective_freeGroup](../../amenable-groups/tauceti-not-amenable-of-injective-freegroup.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.relativePropertyT_inl_slTwo`](https://taucetiproject.org/docs/TauCeti/GroupTheory/PropertyT/SpecialLinear.html#TauCeti.relativePropertyT_inl_slTwo).

## Sources

- [Tau Ceti documentation: `TauCeti.relativePropertyT_inl_slTwo`](https://taucetiproject.org/docs/TauCeti/GroupTheory/PropertyT/SpecialLinear.html#TauCeti.relativePropertyT_inl_slTwo)
- [Source of `TauCeti.relativePropertyT_inl_slTwo` in TauCeti/GroupTheory/PropertyT/SpecialLinear.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/PropertyT/SpecialLinear.lean#L740)
