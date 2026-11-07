---
declaration: def
origin: cited
lean: TauCeti.zigzagBraidTensorLocalizerMorphism
statement: formalized
---

# TauCeti.zigzagBraidTensorLocalizerMorphism

The positive braid tensor functor defines a morphism of the quasi-isomorphism localizer.

```lean
TauCeti.zigzagBraidTensorLocalizerMorphism.{u, v, w} (k : Type w) [CommRing k] {V : Type u}
  (G : SimpleGraph V) [Finite V] (i : V) :
  CategoryTheory.LocalizerMorphism
    (HomologicalComplex.quasiIso
      (TauCeti.GradedModuleCat ((TauCeti.zigzagAlgebraInternalGrading k G).piece ℤ))
      (ComplexShape.up ℤ))
    (HomologicalComplex.quasiIso
      (TauCeti.GradedModuleCat ((TauCeti.zigzagAlgebraInternalGrading k G).piece ℤ))
      (ComplexShape.up ℤ))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.zigzagBraidTensorLocalizerMorphism`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Braid/Module/QuasiIso.html#TauCeti.zigzagBraidTensorLocalizerMorphism).

## Sources

- [Tau Ceti documentation: `TauCeti.zigzagBraidTensorLocalizerMorphism`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Braid/Module/QuasiIso.html#TauCeti.zigzagBraidTensorLocalizerMorphism)
- [Source of `TauCeti.zigzagBraidTensorLocalizerMorphism` in TauCeti/RepresentationTheory/Quiver/Zigzag/Braid/Module/QuasiIso.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Quiver/Zigzag/Braid/Module/QuasiIso.lean#L135)
- [Tau Ceti roadmap status: Zigzag, preprojective, and Ginzburg algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ZigzagPreprojective/STATUS.md)
