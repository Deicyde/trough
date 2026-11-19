---
declaration: theorem
origin: cited
lean: TauCeti.IsPseudoUnitary.existsUnique_pivotalCategory
statement: formalized
proof: formalized
---

# TauCeti.IsPseudoUnitary.existsUnique_pivotalCategory

A pseudo-unitary complex pivotal fusion category has a unique pivotal structure whose left
dimensions are the Frobenius–Perron dimensions of all objects. This structure is spherical.

```lean
TauCeti.IsPseudoUnitary.existsUnique_pivotalCategory.{w, v, u} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Abelian C] [CategoryTheory.MonoidalCategory C]
  [CategoryTheory.MonoidalPreadditive C] [CategoryTheory.RigidCategory C]
  [CategoryTheory.Linear ℂ C] [CategoryTheory.MonoidalLinear ℂ C]
  [TauCeti.IsFiniteSemisimpleCategory C] [∀ (X Y : C), FiniteDimensional ℂ (X ⟶ Y)]
  [CategoryTheory.Simple (CategoryTheory.MonoidalCategoryStruct.tensorUnit C)]
  [CategoryTheory.EssentiallySmall.{w, v, u} C] [Fintype (TauCeti.SimpleClasses C)]
  [original : TauCeti.PivotalCategory C] [TauCeti.IsPseudoUnitary C] :
  ∃! P,
    (∀ (X : C),
        TauCeti.leftDim X =
          ↑(TauCeti.frobeniusPerronDim ℂ X) •
            CategoryTheory.CategoryStruct.id (CategoryTheory.MonoidalCategoryStruct.tensorUnit C)) ∧
      TauCeti.SphericalCategory C
```

## Depends on

- [TauCeti.frobeniusPerronDim](tauceti-frobeniusperrondim.md)

## Proof depends on

- [Collatz–Wielandt bound](collatz-wielandt-bound.md)
- [The Freyd–Yetter identity](../other-results/the-freyd-yetter-identity.md)
- [Frobenius reciprocity in multiplicity form](../other-results/frobenius-reciprocity-in-multiplicity-form.md)
- [Perron–Frobenius](perron-frobenius.md)
- [Perron–Frobenius theorem for irreducible matrices, existence](perron-frobenius-theorem-for-irreducible-matrice.md)
- [Schur's lemma as an identification of algebras](../preadditive/schurs-lemma-as-an-identification-of-algebras.md)
- [TauCeti.universalGradingGroup](tauceti-universalgradinggroup.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsPseudoUnitary.existsUnique_pivotalCategory`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/PseudoUnitary/Existence.html#TauCeti.IsPseudoUnitary.existsUnique_pivotalCategory).

## Sources

- [Tau Ceti documentation: `TauCeti.IsPseudoUnitary.existsUnique_pivotalCategory`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/PseudoUnitary/Existence.html#TauCeti.IsPseudoUnitary.existsUnique_pivotalCategory)
- [Source of `TauCeti.IsPseudoUnitary.existsUnique_pivotalCategory` in TauCeti/CategoryTheory/Monoidal/Pivotal/PseudoUnitary/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Monoidal/Pivotal/PseudoUnitary/Existence.lean#L159)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PivotalSpherical/STATUS.md)
