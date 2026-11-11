---
declaration: theorem
origin: cited
lean: TopCat.GlueData.IsCompatible.maximalAtlas_chartedSpace_eq
statement: formalized
proof: formalized
---

# Uniqueness of the glued manifold structure

A `C^n` manifold structure on the glued space
for which every canonical map is a `C^n` local diffeomorphism has the same maximal atlas as
`D.chartedSpace H`.

```lean
TopCat.GlueData.IsCompatible.maximalAtlas_chartedSpace_eq.{u, u_1, u_2, u_3} {D : TopCat.GlueData}
  {𝕜 : Type u_1} [NontriviallyNormedField 𝕜] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  {H : Type u_3} [TopologicalSpace H] {I : ModelWithCorners 𝕜 E H} {n : WithTop ℕ∞}
  [(i : D.J) → ChartedSpace H ↑(D.U i)] [(ij : D.J × D.J) → ChartedSpace H ↑(D.V ij)]
  [∀ (i : D.J), IsManifold I n ↑(D.U i)] (h : D.IsCompatible I n) {c : ChartedSpace H ↑D.glued}
  (hc : IsManifold I n ↑D.glued)
  (hιc : ∀ (i : D.J), IsLocalDiffeomorph I I n ⇑(CategoryTheory.ConcreteCategory.hom (D.ι i))) :
  IsManifold.maximalAtlas I n ↑D.glued = IsManifold.maximalAtlas I n ↑D.glued
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TopCat.GlueData.IsCompatible.maximalAtlas_chartedSpace_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Gluing/GlueData.html#TopCat.GlueData.IsCompatible.maximalAtlas_chartedSpace_eq).

## Sources

- [Tau Ceti documentation: `TopCat.GlueData.IsCompatible.maximalAtlas_chartedSpace_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Gluing/GlueData.html#TopCat.GlueData.IsCompatible.maximalAtlas_chartedSpace_eq)
- [Source of `TopCat.GlueData.IsCompatible.maximalAtlas_chartedSpace_eq` in TauCeti/Geometry/Manifold/Gluing/GlueData.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Gluing/GlueData.lean#L239)
- [Tau Ceti roadmap status: Complex manifolds: transport, quotients, bundles, and gluing](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexManifolds/STATUS.md)
