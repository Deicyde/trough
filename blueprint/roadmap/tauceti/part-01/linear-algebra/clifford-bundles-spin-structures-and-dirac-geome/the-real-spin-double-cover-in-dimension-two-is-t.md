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
- [Source of `CliffordAlgebra.realCliffordSpecialOrthogonalTwoContinuousMulEquivCircle_spinToSpecialOrthogonal` in TauCeti/Topology/Algebra/CliffordAlgebra/Spin/Real/Two.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/CliffordAlgebra/Spin/Real/Two.lean#L427)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SpinGeometry/STATUS.md)
