---
declaration: theorem
origin: cited
lean: AddCircle.isLocalDiffeomorph_coe
statement: formalized
proof: formalized
---

# AddCircle.isLocalDiffeomorph\_coe

The quotient map `ℝ → AddCircle p` is an analytic local diffeomorphism.

```lean
AddCircle.isLocalDiffeomorph_coe (p : ℝ) [Fact (0 < p)] (n : WithTop ℕ∞) :
  IsLocalDiffeomorph (modelWithCornersSelf ℝ ℝ) (modelWithCornersSelf ℝ ℝ) n QuotientAddGroup.mk
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Homeomorph.pullbackChartedSpace](../../part-02/complex-manifolds-transport-quotients-bundles-an/homeomorph-pullbackchartedspace.md)
- [Homeomorph.pullbackDiffeomorph](../../part-02/complex-manifolds-transport-quotients-bundles-an/homeomorph-pullbackdiffeomorph.md)

## Lean

Formalized in Tau Ceti as [`AddCircle.isLocalDiffeomorph_coe`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Instances/AddCircle.html#AddCircle.isLocalDiffeomorph_coe).

## Sources

- [Tau Ceti documentation: `AddCircle.isLocalDiffeomorph_coe`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Instances/AddCircle.html#AddCircle.isLocalDiffeomorph_coe)
- [Source of `AddCircle.isLocalDiffeomorph_coe` in TauCeti/Geometry/Manifold/Instances/AddCircle.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Instances/AddCircle.lean#L303)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SymplecticGeometry/STATUS.md)
