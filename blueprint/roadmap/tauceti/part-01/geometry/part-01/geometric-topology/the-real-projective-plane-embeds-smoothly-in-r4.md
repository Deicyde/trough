---
declaration: theorem
origin: cited
lean: Projectivization.isSmoothEmbedding_projectivePlaneEmbedding
statement: formalized
proof: formalized
---

# The real projective plane embeds smoothly in `ℝ⁴`

The map
`Projectivization.projectivePlaneEmbedding` is a `C^r` embedding of `ℝP²` in
`EuclideanSpace ℝ (Fin 4)` for every `r ≥ 1`, including the analytic order.

```lean
Projectivization.isSmoothEmbedding_projectivePlaneEmbedding {r : WithTop ℕ∞} (hr : 1 ≤ r) :
  Manifold.IsSmoothEmbedding (modelWithCornersSelf ℝ (Fin 2 → ℝ))
    (modelWithCornersSelf ℝ (EuclideanSpace ℝ (Fin 4))) r Projectivization.projectivePlaneEmbedding
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inverse function theorem for a converging family](../../../analysis/part-03/calculus/part-01/the-inverse-function-theorem-for-a-converging-fa.md)
- [ModelWithCorners.restrictScalars](../complex-manifolds-transport-quotients-bundles-an/modelwithcorners-restrictscalars.md)

## Lean

Formalized in Tau Ceti as [`Projectivization.isSmoothEmbedding_projectivePlaneEmbedding`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Projectivization/ProjectivePlane.html#Projectivization.isSmoothEmbedding_projectivePlaneEmbedding).

## Sources

- [Tau Ceti documentation: `Projectivization.isSmoothEmbedding_projectivePlaneEmbedding`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Projectivization/ProjectivePlane.html#Projectivization.isSmoothEmbedding_projectivePlaneEmbedding)
- [Source of `Projectivization.isSmoothEmbedding_projectivePlaneEmbedding` in TauCeti/Geometry/Manifold/Projectivization/ProjectivePlane.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Projectivization/ProjectivePlane.lean#L395)
- [Tau Ceti roadmap status: Geometric topology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricTopology/STATUS.md)
