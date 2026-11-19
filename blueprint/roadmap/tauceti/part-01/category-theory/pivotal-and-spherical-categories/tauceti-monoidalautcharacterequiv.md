---
declaration: def
origin: cited
lean: TauCeti.monoidalAutCharacterEquiv
statement: formalized
---

# TauCeti.monoidalAutCharacterEquiv

Monoidal natural automorphisms of the identity are the characters of the universal grading
group, as groups. The forward map extracts the scalar on each simple object; the inverse
extends a character to every object using finite semisimplicity.

```lean
TauCeti.monoidalAutCharacterEquiv.{v, u, u_1} (k : Type u_1) [Field k] [IsAlgClosed k] {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Abelian C] [CategoryTheory.MonoidalCategory C]
  [CategoryTheory.MonoidalPreadditive C] [CategoryTheory.Linear k C]
  [CategoryTheory.MonoidalLinear k C]
  [hfin : ∀ (X : C) [CategoryTheory.Simple X], FiniteDimensional k (X ⟶ X)]
  [TauCeti.IsFiniteSemisimpleCategory C]
  [CategoryTheory.Simple (CategoryTheory.MonoidalCategoryStruct.tensorUnit C)] :
  CategoryTheory.Aut (CategoryTheory.LaxMonoidalFunctor.of (CategoryTheory.Functor.id C)) ≃*
    (TauCeti.universalGradingGroup C →* kˣ)
```

## Depends on

- [Schur's lemma as an identification of algebras](../preadditive/schurs-lemma-as-an-identification-of-algebras.md)
- [TauCeti.universalGradingGroup](tauceti-universalgradinggroup.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.monoidalAutCharacterEquiv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Grading/Classification.html#TauCeti.monoidalAutCharacterEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.monoidalAutCharacterEquiv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Grading/Classification.html#TauCeti.monoidalAutCharacterEquiv)
- [Source of `TauCeti.monoidalAutCharacterEquiv` in TauCeti/CategoryTheory/Monoidal/Grading/Classification.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Monoidal/Grading/Classification.lean#L65)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PivotalSpherical/STATUS.md)
