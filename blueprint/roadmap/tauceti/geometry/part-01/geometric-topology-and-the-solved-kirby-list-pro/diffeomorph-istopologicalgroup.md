---
declaration: theorem
origin: cited
lean: Diffeomorph.isTopologicalGroup
statement: formalized
proof: formalized
---

# Diffeomorph.isTopologicalGroup

Self-diffeomorphisms of a compact Hausdorff manifold with a locally compact model space
form a topological group for the weak Whitney topology.

```lean
Diffeomorph.isTopologicalGroup.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜]
  {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {H : Type u_3} [TopologicalSpace H]
  {I : ModelWithCorners 𝕜 E H} {M : Type u_4} [TopologicalSpace M] [ChartedSpace H M]
  {n : WithTop ℕ∞} [CompactSpace M] [LocallyCompactSpace E] [IsManifold I n M] [T2Space M] :
  IsTopologicalGroup (Diffeomorph I I M M n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Diffeomorph.isTopologicalGroup`](https://taucetiproject.org/docs/TauCeti/Geometry/Diffeomorphism/Inversion.html#Diffeomorph.isTopologicalGroup).

## Sources

- [Tau Ceti documentation: `Diffeomorph.isTopologicalGroup`](https://taucetiproject.org/docs/TauCeti/Geometry/Diffeomorphism/Inversion.html#Diffeomorph.isTopologicalGroup)
- [Source of `Diffeomorph.isTopologicalGroup` in TauCeti/Geometry/Diffeomorphism/Inversion.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Diffeomorphism/Inversion.lean#L239)
- [Tau Ceti roadmap status: Geometric topology and the solved Kirby-list problems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricTopology/STATUS.md)
