---
declaration: theorem
origin: cited
lean: Bundle.isSubmersion_proj
statement: formalized
proof: formalized
---

# Bundle.isSubmersion\_proj

The projection of a fibre bundle is a submersion.

```lean
Bundle.isSubmersion_proj.{u_1, u_2, u_3, u_4, u_5, u_6} {𝕜 : Type u_1} {B : Type u_2} {F : Type u_3}
  {EB : Type u_4} {HB : Type u_5} [NontriviallyNormedField 𝕜] {n : WithTop ℕ∞}
  [NormedAddCommGroup F] [NormedSpace 𝕜 F] {V : B → Type u_6}
  [TopologicalSpace (Bundle.TotalSpace F V)] [(x : B) → TopologicalSpace (V x)]
  [NormedAddCommGroup EB] [NormedSpace 𝕜 EB] [TopologicalSpace HB] {IB : ModelWithCorners 𝕜 EB HB}
  [TopologicalSpace B] [ChartedSpace HB B] [FiberBundle F V] [IsManifold IB n B]
  [IsManifold (IB.prod (modelWithCornersSelf 𝕜 F)) n (Bundle.TotalSpace F V)] :
  Manifold.IsSubmersion (IB.prod (modelWithCornersSelf 𝕜 F)) IB n Bundle.TotalSpace.proj
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Bundle.isSubmersion_proj`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/Submersion.html#Bundle.isSubmersion_proj).

## Sources

- [Tau Ceti documentation: `Bundle.isSubmersion_proj`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/Submersion.html#Bundle.isSubmersion_proj)
- [Source of `Bundle.isSubmersion_proj` in TauCeti/Geometry/Manifold/VectorBundle/Submersion.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/VectorBundle/Submersion.lean#L86)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SymplecticGeometry/STATUS.md)
