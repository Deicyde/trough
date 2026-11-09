---
declaration: def
origin: cited
lean: TestFunction.dualEquivDistribution
statement: formalized
---

# Maps on vector-valued tests are operator-valued distributions

For a finite-dimensional
real normed space `F` and a real normed space `V`, the continuous linear maps from the `F`-valued
test functions on `Ω` to `V` correspond to the `F →L[ℝ] V`-valued distributions on `Ω`: a map `T`
corresponds to the distribution `ψ ↦ (v ↦ T (ψ • v))`. Both spaces carry the topology of uniform
convergence on compact sets, and the correspondence is a homeomorphism for these topologies.

```lean
TestFunction.dualEquivDistribution.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {Ω : TopologicalSpace.Opens E} {F : Type u_2} [NormedAddCommGroup F]
  [NormedSpace ℝ F] [FiniteDimensional ℝ F] {V : Type u_3} [NormedAddCommGroup V] [NormedSpace ℝ V]
  {n : ℕ∞} :
  CompactConvergenceCLM (RingHom.id ℝ) (TestFunction Ω F n) V ≃L[ℝ] Distribution Ω (F →L[ℝ] V) n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TestFunction.dualEquivDistribution`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TestFunction/DualEquiv.html#TestFunction.dualEquivDistribution).

## Sources

- [Tau Ceti documentation: `TestFunction.dualEquivDistribution`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TestFunction/DualEquiv.html#TestFunction.dualEquivDistribution)
- [Source of `TestFunction.dualEquivDistribution` in TauCeti/Analysis/Distribution/TestFunction/DualEquiv.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Distribution/TestFunction/DualEquiv.lean#L125)
- [Tau Ceti roadmap status: Integral currents, geometric homology and minimizing hypersurfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricCurrents/STATUS.md)
