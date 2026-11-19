---
declaration: theorem
origin: cited
lean: Subgroup.relativePropertyT_top_of_finite
statement: formalized
proof: formalized
---

# Subgroup.relativePropertyT_top_of_finite

A finite group has property (T).

```lean
Subgroup.relativePropertyT_top_of_finite.{u, v} {G : Type v} [Group G] [Finite G] :
  ⊤.RelativePropertyT
```

## Depends on

- [Subgroup.RelativePropertyT](subgroup-relativepropertyt.md)

## Proof depends on

- [ContRepresentation.HasAlmostInvariantVectors](contrepresentation-hasalmostinvariantvectors.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.relativePropertyT_top_of_finite`](https://taucetiproject.org/docs/TauCeti/GroupTheory/PropertyT/Basic.html#Subgroup.relativePropertyT_top_of_finite).

## Sources

- [Tau Ceti documentation: `Subgroup.relativePropertyT_top_of_finite`](https://taucetiproject.org/docs/TauCeti/GroupTheory/PropertyT/Basic.html#Subgroup.relativePropertyT_top_of_finite)
- [Source of `Subgroup.relativePropertyT_top_of_finite` in TauCeti/GroupTheory/PropertyT/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/PropertyT/Basic.lean#L79)
- [Tau Ceti roadmap status: Approximation, deformation and rigidity of finite factors](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FactorRigidity/STATUS.md)
