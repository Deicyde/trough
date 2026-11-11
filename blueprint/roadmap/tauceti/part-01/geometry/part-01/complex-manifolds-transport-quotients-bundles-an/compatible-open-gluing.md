---
declaration: theorem
origin: cited
lean: TopCat.GlueData.IsCompatible.isManifold
statement: formalized
proof: formalized
---

# Compatible open gluing

If the pieces of `D` are `C^n` manifolds whose atlases are
compatible with those of the overlaps, then the glued space is a `C^n` manifold.

```lean
TopCat.GlueData.IsCompatible.isManifold.{u, u_1, u_2, u_3} {D : TopCat.GlueData} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {H : Type u_3}
  [TopologicalSpace H] {I : ModelWithCorners 𝕜 E H} {n : WithTop ℕ∞}
  [(i : D.J) → ChartedSpace H ↑(D.U i)] [(ij : D.J × D.J) → ChartedSpace H ↑(D.V ij)]
  [∀ (i : D.J), IsManifold I n ↑(D.U i)] (h : D.IsCompatible I n) : IsManifold I n ↑D.glued
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TopCat.GlueData.IsCompatible.isManifold`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Gluing/GlueData.html#TopCat.GlueData.IsCompatible.isManifold).

## Sources

- [Tau Ceti documentation: `TopCat.GlueData.IsCompatible.isManifold`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Gluing/GlueData.html#TopCat.GlueData.IsCompatible.isManifold)
- [Source of `TopCat.GlueData.IsCompatible.isManifold` in TauCeti/Geometry/Manifold/Gluing/GlueData.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Gluing/GlueData.lean#L153)
- [Tau Ceti roadmap status: Complex manifolds: transport, quotients, bundles, and gluing](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexManifolds/STATUS.md)
