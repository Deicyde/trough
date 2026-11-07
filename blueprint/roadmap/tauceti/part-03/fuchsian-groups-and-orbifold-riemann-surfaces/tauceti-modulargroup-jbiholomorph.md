---
declaration: def
origin: cited
lean: TauCeti.ModularGroup.jBiholomorph
statement: formalized
---

# TauCeti.ModularGroup.jBiholomorph

The normalized modular invariant identifies the compactified level-one modular quotient
biholomorphically with the Riemann sphere.

```lean
TauCeti.ModularGroup.jBiholomorph :
  Diffeomorph (modelWithCornersSelf ℂ ℂ) (modelWithCornersSelf ℂ ℂ)
    psl2zToPSL2R.range.CompactifiedQuotient (OnePoint ℂ) ↑⊤
```

## Depends on

- [A degree-one map is a biholomorphism](a-degree-one-map-is-a-biholomorphism.md)
- [Subgroup.CompactifiedQuotient](subgroup-compactifiedquotient.md)

## Proof depends on

- [Descent of an invariant map to the orbit space](../../part-02/complex-manifolds-transport-quotients-bundles-an/descent-of-an-invariant-map-to-the-orbit-space.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ModularGroup.jBiholomorph`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/LevelOne/Sphere.html#TauCeti.ModularGroup.jBiholomorph).

## Sources

- [Tau Ceti documentation: `TauCeti.ModularGroup.jBiholomorph`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/LevelOne/Sphere.html#TauCeti.ModularGroup.jBiholomorph)
- [Source of `TauCeti.ModularGroup.jBiholomorph` in TauCeti/Analysis/Complex/Fuchsian/LevelOne/Sphere.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Fuchsian/LevelOne/Sphere.lean#L179)
- [Tau Ceti roadmap status: Fuchsian groups and orbifold Riemann surfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FuchsianOrbifolds/STATUS.md)
