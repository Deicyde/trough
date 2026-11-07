---
declaration: abbrev
origin: cited
lean: CategoryTheory.Functor.proIsomorphisms
statement: formalized
---

# CategoryTheory.Functor.proIsomorphisms

The *pro-isomorphisms* of diagrams `J ⥤ C`: the morphisms whose kernel and cokernel are
pro-zero (`proIsomorphisms_iff`). This is Mathlib's class `ObjectProperty.isoModSerre` of
isomorphisms modulo the Serre class of pro-zero diagrams, so pro-isomorphisms are stable under
composition and retracts and satisfy two-out-of-three.

```lean
CategoryTheory.Functor.proIsomorphisms.{v₁, v₂, u₁, u₂} (J : Type u₁)
  [CategoryTheory.Category.{v₁, u₁} J] (C : Type u₂) [CategoryTheory.Category.{v₂, u₂} C]
  [CategoryTheory.Abelian C] : CategoryTheory.MorphismProperty (CategoryTheory.Functor J C)
```

## Depends on

- [CategoryTheory.Functor.IsProZero](categorytheory-functor-isprozero.md)

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Functor.proIsomorphisms`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Functor/ProZero.html#CategoryTheory.Functor.proIsomorphisms).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Functor.proIsomorphisms`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Functor/ProZero.html#CategoryTheory.Functor.proIsomorphisms)
- [Source of `CategoryTheory.Functor.proIsomorphisms` in TauCeti/CategoryTheory/Functor/ProZero.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CategoryTheory/Functor/ProZero.lean#L167)
- [Tau Ceti roadmap status: Enhanced derived categories of sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EnhancedDerivedSheaves/STATUS.md)
