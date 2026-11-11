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
- [Source of `Subgroup.relativePropertyT_top_of_finite` in TauCeti/GroupTheory/PropertyT/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/PropertyT/Basic.lean#L79)
- [Tau Ceti roadmap status: Approximation, deformation and rigidity of finite factors](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FactorRigidity/STATUS.md)
