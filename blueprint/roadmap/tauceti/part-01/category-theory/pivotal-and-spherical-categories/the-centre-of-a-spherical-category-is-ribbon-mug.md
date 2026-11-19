---
declaration: theorem
origin: cited
lean: CategoryTheory.Center.ribbonCategory_of_sphericalCategory
statement: formalized
proof: formalized
---

# The centre of a spherical category is ribbon (Müger)

For a spherical category `C` whose
centre is a split finite semisimple category with simple unit, the twist induced on `Center C` by
its braiding and its pivotal structure is ribbon. The twist is the one built from the pivotal
structure induced from `C`, not an arbitrary twist of the centre, and the abelian, linear, rigid
and pivotal structures of the centre are the canonical ones.

The simple unit of the centre and the finite-dimensionality of the endomorphisms of its simple
objects are found by instance search when `C` has a simple unit and finite-dimensional
endomorphism spaces (`CategoryTheory.Center.instSimpleUnit`,
`CategoryTheory.Center.instFiniteDimensionalHom`).

```lean
CategoryTheory.Center.ribbonCategory_of_sphericalCategory.{v, u, u_1} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.MonoidalCategory C]
  [CategoryTheory.RigidCategory C] [TauCeti.PivotalCategory C] (k : Type u_1) [Field k]
  [IsAlgClosed k] [TauCeti.SphericalCategory C] [CategoryTheory.Abelian C]
  [CategoryTheory.MonoidalPreadditive C] [CategoryTheory.Linear k C]
  [CategoryTheory.MonoidalLinear k C] [TauCeti.IsFiniteSemisimpleCategory (CategoryTheory.Center C)]
  [CategoryTheory.Simple
      (CategoryTheory.MonoidalCategoryStruct.tensorUnit (CategoryTheory.Center C))]
  [hfin : ∀ (X : CategoryTheory.Center C) [CategoryTheory.Simple X], FiniteDimensional k (X ⟶ X)] :
  TauCeti.RibbonCategory (CategoryTheory.Center C)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Freyd–Yetter identity](../other-results/the-freyd-yetter-identity.md)
- [Schur's lemma for an exact pairing with simple left member](../diagrammatic-coherence-for-monoidal-categories-a/schurs-lemma-for-an-exact-pairing-with-simple-le.md)

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Center.ribbonCategory_of_sphericalCategory`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Center/Ribbon.html#CategoryTheory.Center.ribbonCategory_of_sphericalCategory).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Center.ribbonCategory_of_sphericalCategory`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Center/Ribbon.html#CategoryTheory.Center.ribbonCategory_of_sphericalCategory)
- [Source of `CategoryTheory.Center.ribbonCategory_of_sphericalCategory` in TauCeti/CategoryTheory/Monoidal/Center/Ribbon.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Monoidal/Center/Ribbon.lean#L72)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PivotalSpherical/STATUS.md)
