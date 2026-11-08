---
declaration: theorem
origin: cited
lean: TauCeti.SplitK0.spectralRadius_fusionMatrix
statement: formalized
proof: formalized
---

# TauCeti.SplitK0.spectralRadius_fusionMatrix

The value of the Frobenius–Perron character on a simple class `S` is the spectral radius of
the fusion matrix of `S`.

```lean
TauCeti.SplitK0.spectralRadius_fusionMatrix.{w, w', v, u} (k : Type w') [Field k] [IsAlgClosed k]
  {C : Type u} [CategoryTheory.Category.{v, u} C] [CategoryTheory.Abelian C]
  [CategoryTheory.MonoidalCategory C] [CategoryTheory.MonoidalPreadditive C]
  [CategoryTheory.RigidCategory C] [CategoryTheory.Linear k C] [CategoryTheory.MonoidalLinear k C]
  [TauCeti.IsFiniteSemisimpleCategory C] [∀ (X Y : C), FiniteDimensional k (X ⟶ Y)]
  [CategoryTheory.Simple (CategoryTheory.MonoidalCategoryStruct.tensorUnit C)]
  [CategoryTheory.EssentiallySmall.{w, v, u} C] [Fintype (TauCeti.SimpleClasses C)]
  (S : TauCeti.SimpleClasses C) :
  spectralRadius ℂ ((TauCeti.fusionMatrix k S).map Nat.cast) =
    ENNReal.ofReal ((TauCeti.SplitK0.frobeniusPerronChar k C) ((TauCeti.SplitK0.simpleBasis C) S))
```

## Depends on

- [TauCeti.fusionCoeff](tauceti-fusioncoeff.md)
- [TauCeti.SplitK0.simpleBasis](tauceti-splitk0-simplebasis.md)

## Proof depends on

- [Frobenius reciprocity in multiplicity form](../other-results/frobenius-reciprocity-in-multiplicity-form.md)
- [The Frobenius–Perron character](the-frobenius-perron-character.md)
- [Perron–Frobenius](../../linear-algebra/matrix/perron-frobenius.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SplitK0.spectralRadius_fusionMatrix`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Semisimple/FrobeniusPerron.html#TauCeti.SplitK0.spectralRadius_fusionMatrix).

## Sources

- [Tau Ceti documentation: `TauCeti.SplitK0.spectralRadius_fusionMatrix`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Semisimple/FrobeniusPerron.html#TauCeti.SplitK0.spectralRadius_fusionMatrix)
- [Source of `TauCeti.SplitK0.spectralRadius_fusionMatrix` in TauCeti/CategoryTheory/Semisimple/FrobeniusPerron.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CategoryTheory/Semisimple/FrobeniusPerron.lean#L148)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PivotalSpherical/STATUS.md)
