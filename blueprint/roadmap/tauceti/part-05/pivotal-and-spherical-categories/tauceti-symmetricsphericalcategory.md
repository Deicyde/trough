---
declaration: theorem
origin: cited
lean: TauCeti.symmetricSphericalCategory
statement: formalized
proof: formalized
---

# TauCeti.symmetricSphericalCategory

The canonical pivotal structure on a symmetric rigid category is spherical.

```lean
TauCeti.symmetricSphericalCategory.{v, u} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.MonoidalCategory C] [CategoryTheory.SymmetricCategory C]
  [CategoryTheory.RigidCategory C] : TauCeti.SphericalCategory C
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.symmetricSphericalCategory`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/Symmetric.html#TauCeti.symmetricSphericalCategory).

## Sources

- [Tau Ceti documentation: `TauCeti.symmetricSphericalCategory`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/Symmetric.html#TauCeti.symmetricSphericalCategory)
- [Source of `TauCeti.symmetricSphericalCategory` in TauCeti/CategoryTheory/Monoidal/Pivotal/Symmetric.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CategoryTheory/Monoidal/Pivotal/Symmetric.lean#L113)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PivotalSpherical/STATUS.md)
