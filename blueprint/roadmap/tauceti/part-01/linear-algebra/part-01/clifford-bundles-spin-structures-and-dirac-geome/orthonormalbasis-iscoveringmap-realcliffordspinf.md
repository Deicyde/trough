---
declaration: theorem
origin: cited
lean: OrthonormalBasis.isCoveringMap_realCliffordSpinFrameProjection
statement: formalized
proof: formalized
---

# OrthonormalBasis.isCoveringMap_realCliffordSpinFrameProjection

The frame projection is a covering map.

```lean
OrthonormalBasis.isCoveringMap_realCliffordSpinFrameProjection.{u_1} {V : Type u_1}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] {Q : QuadraticForm ℝ V} {n : ℕ}
  (b : OrthonormalBasis (Fin n) ℝ V) (hQ : ∀ (v : V), Q v = ‖v‖ ^ 2) :
  IsCoveringMap ⇑(b.realCliffordSpinFrameProjection hQ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [CliffordAlgebra.orthogonalSpinorNorm](../orthogonal-and-spin-groups/cliffordalgebra-orthogonalspinornorm.md)
- [CliffordAlgebra.range_spinToSpecialOrthogonal_eq_ker_spinorNorm](../orthogonal-and-spin-groups/cliffordalgebra-range-spintospecialorthogonal-eq.md)

## Lean

Formalized in Tau Ceti as [`OrthonormalBasis.isCoveringMap_realCliffordSpinFrameProjection`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/CliffordAlgebra/Spin/Real/Frame.html#OrthonormalBasis.isCoveringMap_realCliffordSpinFrameProjection).

## Sources

- [Tau Ceti documentation: `OrthonormalBasis.isCoveringMap_realCliffordSpinFrameProjection`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/CliffordAlgebra/Spin/Real/Frame.html#OrthonormalBasis.isCoveringMap_realCliffordSpinFrameProjection)
- [Source of `OrthonormalBasis.isCoveringMap_realCliffordSpinFrameProjection` in TauCeti/Topology/Algebra/CliffordAlgebra/Spin/Real/Frame.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/CliffordAlgebra/Spin/Real/Frame.lean#L144)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpinGeometry/STATUS.md)
