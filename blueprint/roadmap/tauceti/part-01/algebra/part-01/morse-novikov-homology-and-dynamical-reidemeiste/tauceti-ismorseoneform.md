---
declaration: structure
origin: cited
lean: TauCeti.IsMorseOneForm
statement: formalized
---

# TauCeti.IsMorseOneForm

A smooth closed real one-form is Morse if each zero admits a local primitive with a
nondegenerate critical point there. This does not require Morse--Smale transversality or
nondegeneracy of periodic orbits.

```lean
TauCeti.IsMorseOneForm.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2} {M : Type u_3}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 1 M] (α : TauCeti.RoughForm I M ℝ 1) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsMorseOneForm`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/OneForm/Basic.html#TauCeti.IsMorseOneForm).

## Sources

- [Tau Ceti documentation: `TauCeti.IsMorseOneForm`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/OneForm/Basic.html#TauCeti.IsMorseOneForm)
- [Source of `TauCeti.IsMorseOneForm` in TauCeti/Geometry/Manifold/Morse/OneForm/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Morse/OneForm/Basic.lean#L55)
- [Tau Ceti roadmap status: Morse–Novikov homology and dynamical Reidemeister torsion](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MorseNovikov/STATUS.md)
