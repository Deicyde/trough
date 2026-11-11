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
- [Source of `TauCeti.symmetricSphericalCategory` in TauCeti/CategoryTheory/Monoidal/Pivotal/Symmetric.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Monoidal/Pivotal/Symmetric.lean#L113)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PivotalSpherical/STATUS.md)
