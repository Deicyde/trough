---
declaration: def
origin: cited
lean: TauCeti.Toric.Fan.algebraicConeOrbitTorusHomeomorph
statement: formalized
---

# Algebraic orbits are quotient tori

The torus orbit of a cone `σ` in the complex points
of the toric scheme of a regular fan, with the subspace topology, is homeomorphic to the torus of
the quotient lattice `N ⧸ N_σ`.

```lean
TauCeti.Toric.Fan.algebraicConeOrbitTorusHomeomorph {N V : Type} [AddCommGroup N] [AddCommGroup V]
  [_root_.Module ℝ V] {i : N →+ V} {Φ : TauCeti.Toric.Fan i} (hΦ : Φ.IsRegular) (σ : ↑Φ.cones) :
  ↑(TauCeti.Toric.Fan.AlgebraicComplexPoint.coneOrbit Φ σ) ≃ₜ
    TauCeti.Toric.ComplexTorus (N ⧸ TauCeti.Toric.coneSublattice i ↑σ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Gordan's lemma for lattice points](../scattering-diagrams-wall-crossing-and-theta-func/gordans-lemma-for-lattice-points.md)
- [Tucker's theorem](../../part-02/convex/tuckers-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Toric.Fan.algebraicConeOrbitTorusHomeomorph`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Analytic/Fan/Comparison/Orbit.html#TauCeti.Toric.Fan.algebraicConeOrbitTorusHomeomorph).

## Sources

- [Tau Ceti documentation: `TauCeti.Toric.Fan.algebraicConeOrbitTorusHomeomorph`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Analytic/Fan/Comparison/Orbit.html#TauCeti.Toric.Fan.algebraicConeOrbitTorusHomeomorph)
- [Source of `TauCeti.Toric.Fan.algebraicConeOrbitTorusHomeomorph` in TauCeti/Geometry/Toric/Analytic/Fan/Comparison/Orbit.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Toric/Analytic/Fan/Comparison/Orbit.lean#L83)
- [Tau Ceti roadmap status: Analytic toric geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/AnalyticToricGeometry/STATUS.md)
