---
declaration: def
origin: cited
lean: TauCeti.SplitK0.simpleBasis
statement: formalized
---

# TauCeti.SplitK0.simpleBasis

The classes of the simple representatives form a `ℤ`-basis of split `K₀`.

```lean
TauCeti.SplitK0.simpleBasis.{w, v, u} (C : Type u) [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Abelian C] [TauCeti.IsFiniteSemisimpleCategory C]
  [CategoryTheory.EssentiallySmall.{w, v, u} C] :
  Module.Basis (TauCeti.SimpleClasses C) ℤ (TauCeti.SplitK0 C)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SplitK0.simpleBasis`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Semisimple/GrothendieckRing.html#TauCeti.SplitK0.simpleBasis).

## Sources

- [Tau Ceti documentation: `TauCeti.SplitK0.simpleBasis`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Semisimple/GrothendieckRing.html#TauCeti.SplitK0.simpleBasis)
- [Source of `TauCeti.SplitK0.simpleBasis` in TauCeti/CategoryTheory/Semisimple/GrothendieckRing.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CategoryTheory/Semisimple/GrothendieckRing.lean#L121)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PivotalSpherical/STATUS.md)
