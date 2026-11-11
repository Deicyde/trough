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
- [Source of `TauCeti.SplitK0.simpleBasis` in TauCeti/CategoryTheory/Semisimple/GrothendieckRing.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Semisimple/GrothendieckRing.lean#L121)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PivotalSpherical/STATUS.md)
