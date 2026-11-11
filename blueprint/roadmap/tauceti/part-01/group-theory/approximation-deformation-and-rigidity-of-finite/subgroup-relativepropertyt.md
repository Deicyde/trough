---
declaration: def
origin: cited
lean: Subgroup.RelativePropertyT
statement: formalized
---

# Subgroup.RelativePropertyT

A subgroup has relative property (T) if every unitary representation with almost invariant
vectors on a complex Hilbert space in universe `u` has a nonzero vector fixed by this subgroup.

```lean
Subgroup.RelativePropertyT.{u, v} {G : Type v} [Group G] (Λ : Subgroup G) : Prop
```

## Depends on

- [ContRepresentation.HasAlmostInvariantVectors](contrepresentation-hasalmostinvariantvectors.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.RelativePropertyT`](https://taucetiproject.org/docs/TauCeti/GroupTheory/PropertyT/Basic.html#Subgroup.RelativePropertyT).

## Sources

- [Tau Ceti documentation: `Subgroup.RelativePropertyT`](https://taucetiproject.org/docs/TauCeti/GroupTheory/PropertyT/Basic.html#Subgroup.RelativePropertyT)
- [Source of `Subgroup.RelativePropertyT` in TauCeti/GroupTheory/PropertyT/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/PropertyT/Basic.lean#L35)
- [Tau Ceti roadmap status: Approximation, deformation and rigidity of finite factors](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FactorRigidity/STATUS.md)
