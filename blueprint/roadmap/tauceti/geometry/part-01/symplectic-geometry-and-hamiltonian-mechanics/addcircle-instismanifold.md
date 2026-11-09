---
declaration: theorem
origin: cited
lean: AddCircle.instIsManifold
statement: formalized
proof: formalized
---

# AddCircle.instIsManifold

The circle `AddCircle p` is an analytic manifold modelled on `ℝ`.

```lean
AddCircle.instIsManifold (p : ℝ) [Fact (0 < p)] {n : WithTop ℕ∞} :
  IsManifold (modelWithCornersSelf ℝ ℝ) n (AddCircle p)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Homeomorph.pullbackChartedSpace](../complex-manifolds-transport-quotients-bundles-an/homeomorph-pullbackchartedspace.md)

## Lean

Formalized in Tau Ceti as [`AddCircle.instIsManifold`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Instances/AddCircle.html#AddCircle.instIsManifold).

## Sources

- [Tau Ceti documentation: `AddCircle.instIsManifold`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Instances/AddCircle.html#AddCircle.instIsManifold)
- [Source of `AddCircle.instIsManifold` in TauCeti/Geometry/Manifold/Instances/AddCircle.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Instances/AddCircle.lean#L265)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SymplecticGeometry/STATUS.md)
