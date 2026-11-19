---
declaration: theorem
origin: cited
lean: ContinuousAlternatingMap.exists_orthonormal_norm_eq
statement: formalized
proof: formalized
---

# ContinuousAlternatingMap.exists_orthonormal_norm_eq

An alternating map attains its norm on an orthonormal frame whenever the degree
is at most the dimension.

```lean
ContinuousAlternatingMap.exists_orthonormal_norm_eq.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [NormedAddCommGroup F]
  [NormedSpace ℝ F] {k : ℕ} (ω : E [⋀^Fin k]→L[ℝ] F) (hk : k ≤ Module.finrank ℝ E) :
  ∃ v, Orthonormal ℝ v ∧ ‖ω v‖ = ‖ω‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [ContinuousAlternatingMap.opNorm_le_iff_le_orthonormal](continuousalternatingmap-opnorm-le-iff-le-orthon.md)

## Lean

Formalized in Tau Ceti as [`ContinuousAlternatingMap.exists_orthonormal_norm_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Instances/Stiefel/Comass.html#ContinuousAlternatingMap.exists_orthonormal_norm_eq).

## Sources

- [Tau Ceti documentation: `ContinuousAlternatingMap.exists_orthonormal_norm_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Instances/Stiefel/Comass.html#ContinuousAlternatingMap.exists_orthonormal_norm_eq)
- [Source of `ContinuousAlternatingMap.exists_orthonormal_norm_eq` in TauCeti/Geometry/Manifold/Instances/Stiefel/Comass.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Instances/Stiefel/Comass.lean#L31)
- [Tau Ceti roadmap status: Calibrations, volume minimization and special Lagrangian geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CalibratedGeometry/STATUS.md)
