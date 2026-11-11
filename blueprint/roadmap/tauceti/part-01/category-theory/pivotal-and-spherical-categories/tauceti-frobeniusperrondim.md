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
  [CategoryTheory.Linear k C] [CategoryTheory.MonoidalLinear k C]
  [TauCeti.IsFiniteSemisimpleCategory C] [∀ (X Y : C), FiniteDimensional k (X ⟶ Y)]
  [CategoryTheory.Simple (CategoryTheory.MonoidalCategoryStruct.tensorUnit C)]
  [CategoryTheory.EssentiallySmall.{w, v, u} C] [Finite (TauCeti.SimpleClasses C)] (X : C) : ℝ
```

## Depends on

- [TauCeti.SplitK0.simpleBasis](tauceti-splitk0-simplebasis.md)

## Proof depends on

- [Frobenius reciprocity in multiplicity form](../other-results/frobenius-reciprocity-in-multiplicity-form.md)
- [The Frobenius–Perron character](the-frobenius-perron-character.md)
- [TauCeti.fusionCoeff](tauceti-fusioncoeff.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.frobeniusPerronDim`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Semisimple/FrobeniusPerron.html#TauCeti.frobeniusPerronDim).

## Sources

- [Tau Ceti documentation: `TauCeti.frobeniusPerronDim`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Semisimple/FrobeniusPerron.html#TauCeti.frobeniusPerronDim)
- [Source of `TauCeti.frobeniusPerronDim` in TauCeti/CategoryTheory/Semisimple/FrobeniusPerron.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Semisimple/FrobeniusPerron.lean#L196)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PivotalSpherical/STATUS.md)
