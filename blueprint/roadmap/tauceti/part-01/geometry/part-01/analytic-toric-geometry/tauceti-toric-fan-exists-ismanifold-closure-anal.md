---
declaration: theorem
origin: cited
lean: TauCeti.Toric.Fan.exists_isManifold_closure_analyticConeOrbit_isSmoothEmbedding
statement: formalized
proof: formalized
---

# TauCeti.Toric.Fan.exists_isManifold_closure_analyticConeOrbit_isSmoothEmbedding

The closure of the torus orbit of a cone `σ`, on its actual subtype with the subspace
topology, admits a complex manifold structure of dimension `rank N - dim σ` for which the
inclusion is a holomorphic smooth embedding. This closure is the intersection of the boundary
components of the rays of `σ`, so these components meet in a closed embedded complex submanifold
of the expected codimension.

```lean
TauCeti.Toric.Fan.exists_isManifold_closure_analyticConeOrbit_isSmoothEmbedding.{u} {N V : Type u}
  [AddCommGroup N] [AddCommGroup V] [_root_.Module ℝ V] {i : N →+ V} (Φ : TauCeti.Toric.Fan i)
  (hΦ : Φ.IsRegular) (σ : ↑Φ.cones) :
  ∃ C,
    IsManifold
        (modelWithCornersSelf ℂ
          (Fin (Module.finrank ℤ N - Module.finrank ℝ ↥(Submodule.span ℝ ↑↑σ)) → ℂ))
        ⊤ ↑(closure (Φ.analyticConeOrbit hΦ σ)) ∧
      Manifold.IsSmoothEmbedding
        (modelWithCornersSelf ℂ
          (Fin (Module.finrank ℤ N - Module.finrank ℝ ↥(Submodule.span ℝ ↑↑σ)) → ℂ))
        (modelWithCornersSelf ℂ (Fin (Module.finrank ℤ N) → ℂ)) ⊤ Subtype.val
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Gordan's lemma for lattice points](../scattering-diagrams-wall-crossing-and-theta-func/gordans-lemma-for-lattice-points.md)
- [TauCeti.Toric.Fan.exists_partialDiffeomorph_analyticBoundaryComponent_normalForm](tauceti-toric-fan-exists-partialdiffeomorph-anal.md)
- [Tucker's theorem](../../part-02/convex/tuckers-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Toric.Fan.exists_isManifold_closure_analyticConeOrbit_isSmoothEmbedding`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Analytic/Fan/Boundary/Manifold.html#TauCeti.Toric.Fan.exists_isManifold_closure_analyticConeOrbit_isSmoothEmbedding).

## Sources

- [Tau Ceti documentation: `TauCeti.Toric.Fan.exists_isManifold_closure_analyticConeOrbit_isSmoothEmbedding`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Analytic/Fan/Boundary/Manifold.html#TauCeti.Toric.Fan.exists_isManifold_closure_analyticConeOrbit_isSmoothEmbedding)
- [Source of `TauCeti.Toric.Fan.exists_isManifold_closure_analyticConeOrbit_isSmoothEmbedding` in TauCeti/Geometry/Toric/Analytic/Fan/Boundary/Manifold.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Toric/Analytic/Fan/Boundary/Manifold.lean#L119)
- [Tau Ceti roadmap status: Analytic toric geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/AnalyticToricGeometry/STATUS.md)
