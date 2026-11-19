---
declaration: def
origin: cited
lean: TauCeti.frobeniusPerronDim
statement: formalized
---

# TauCeti.frobeniusPerronDim

The **Frobenius–Perron dimension** of an object of a fusion category: the value of the
Frobenius–Perron character `TauCeti.SplitK0.frobeniusPerronChar` at the class of the object.

```lean
TauCeti.frobeniusPerronDim.{w, w', v, u} (k : Type w') [Field k] [IsAlgClosed k] {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Abelian C] [CategoryTheory.MonoidalCategory C]
  [CategoryTheory.MonoidalPreadditive C] [CategoryTheory.RigidCategory C]
  [CategoryTheory.Linear k C] [TauCeti.IsFiniteSemisimpleCategory C]
  [∀ (X Y : C), FiniteDimensional k (X ⟶ Y)]
  [CategoryTheory.Simple (CategoryTheory.MonoidalCategoryStruct.tensorUnit C)]
  [CategoryTheory.EssentiallySmall.{w, v, u} C] [Finite (TauCeti.SimpleClasses C)] (X : C) : ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Collatz–Wielandt bound](collatz-wielandt-bound.md)
- [Perron–Frobenius theorem for irreducible matrices, existence](perron-frobenius-theorem-for-irreducible-matrice.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.frobeniusPerronDim`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Semisimple/FrobeniusPerron.html#TauCeti.frobeniusPerronDim).

## Sources

- [Tau Ceti documentation: `TauCeti.frobeniusPerronDim`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Semisimple/FrobeniusPerron.html#TauCeti.frobeniusPerronDim)
- [Source of `TauCeti.frobeniusPerronDim` in TauCeti/CategoryTheory/Semisimple/FrobeniusPerron.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Semisimple/FrobeniusPerron.lean#L196)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PivotalSpherical/STATUS.md)
