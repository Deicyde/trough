---
declaration: def
origin: cited
lean: ModelWithCorners.restrictScalars
statement: formalized
---

# ModelWithCorners.restrictScalars

Regard a boundaryless model over another scalar field, preserving both coordinate maps
and the caller's normed-space structure.

```lean
ModelWithCorners.restrictScalars.{u_1, u_2, u_3, u_4} (𝕜 : Type u_1) {𝕜' : Type u_2}
  [NontriviallyNormedField 𝕜] [NontriviallyNormedField 𝕜'] {E : Type u_3} [NormedAddCommGroup E]
  [NormedSpace 𝕜 E] [NormedSpace 𝕜' E] {H : Type u_4} [TopologicalSpace H]
  (I : ModelWithCorners 𝕜' E H) [I.Boundaryless] : ModelWithCorners 𝕜 E H
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ModelWithCorners.restrictScalars`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/ModelWithCorners/RestrictScalars/Basic.html#ModelWithCorners.restrictScalars).

## Sources

- [Tau Ceti documentation: `ModelWithCorners.restrictScalars`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/ModelWithCorners/RestrictScalars/Basic.html#ModelWithCorners.restrictScalars)
- [Source of `ModelWithCorners.restrictScalars` in TauCeti/Geometry/Manifold/ModelWithCorners/RestrictScalars/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/ModelWithCorners/RestrictScalars/Basic.lean#L37)
- [Tau Ceti roadmap status: Complex manifolds: transport, quotients, bundles, and gluing](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexManifolds/STATUS.md)
