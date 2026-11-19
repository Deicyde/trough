---
declaration: theorem
origin: cited
lean: CliffordAlgebra.realCliffordSpecialOrthogonalTwoContinuousMulEquivCircle_spinToSpecialOrthogonal
statement: formalized
proof: formalized
---

# The real Spin double cover in dimension two is the squaring map of the circle

Under the
identifications of `Spin(2)` and `SO(2)` with the circle group, the Spin projection is `z ↦ z²`:
the Spin element `cos θ - sin θ e₀e₁` acts on the plane as the rotation by the angle `2θ`. The
projection is stated as `spinToSpecialOrthogonal`, the simp normal form of the covering map
`realCliffordSpinProjectionZero 2`.

```lean
CliffordAlgebra.realCliffordSpecialOrthogonalTwoContinuousMulEquivCircle_spinToSpecialOrthogonal
  (x : ↥(CliffordAlgebra.realCliffordSpinGroupZero 2)) :
  CliffordAlgebra.realCliffordSpecialOrthogonalTwoContinuousMulEquivCircle
      ((CliffordAlgebra.spinToSpecialOrthogonal (TauCeti.realCliffordForm 2 0)) x) =
    CliffordAlgebra.realCliffordSpinTwoContinuousMulEquivCircle x ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [CliffordAlgebra.orthogonalSpinorNorm](../orthogonal-and-spin-groups/cliffordalgebra-orthogonalspinornorm.md)
- [CliffordAlgebra.range_spinToSpecialOrthogonal_eq_ker_spinorNorm](../orthogonal-and-spin-groups/cliffordalgebra-range-spintospecialorthogonal-eq.md)

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.realCliffordSpecialOrthogonalTwoContinuousMulEquivCircle_spinToSpecialOrthogonal`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/CliffordAlgebra/Spin/Real/Two.html#CliffordAlgebra.realCliffordSpecialOrthogonalTwoContinuousMulEquivCircle_spinToSpecialOrthogonal).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.realCliffordSpecialOrthogonalTwoContinuousMulEquivCircle_spinToSpecialOrthogonal`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/CliffordAlgebra/Spin/Real/Two.html#CliffordAlgebra.realCliffordSpecialOrthogonalTwoContinuousMulEquivCircle_spinToSpecialOrthogonal)
- [Source of `CliffordAlgebra.realCliffordSpecialOrthogonalTwoContinuousMulEquivCircle_spinToSpecialOrthogonal` in TauCeti/Topology/Algebra/CliffordAlgebra/Spin/Real/Two.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/CliffordAlgebra/Spin/Real/Two.lean#L427)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpinGeometry/STATUS.md)
