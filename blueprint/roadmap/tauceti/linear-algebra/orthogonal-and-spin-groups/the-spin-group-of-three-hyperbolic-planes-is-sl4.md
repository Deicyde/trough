---
declaration: abbrev
origin: cited
lean: TauCeti.hyperbolicSixSpinEquivSpecialLinear
statement: formalized
---

# The Spin group of three hyperbolic planes is `SL₄(K)`

This is
`TauCeti.spinGroupEquivSpecialLinearGroupOfFinrankEqSix` for the canonical split polarization, so a
Spin element goes to the matrix of its even half-spin action in
`TauCeti.spinSixHalfSpinStandardBasis`. By `TauCeti.coe_hyperbolicSixSpinEquivSpecialLinear_apply`
it is the restriction of `TauCeti.hyperbolicSixEvenUnitaryEquivGeneralLinear` to Spin, so `Spin(Q)`
is the determinant-one subgroup of the reverse-unitary group `U(C₀, σ) ≅ GL₄(K)`. Over `ℚ`, three
hyperbolic planes give the split rational six-dimensional form, with `U(C₀, σ) ≅ GL₄(ℚ)` and
`Spin(Q) ≅ SL₄(ℚ)`.

```lean
TauCeti.hyperbolicSixSpinEquivSpecialLinear.{u_1} (K : Type u_1) [Field K] [NeZero 2] :
  ↥(spinGroup (TauCeti.splitEvenForm K 3)) ≃* Matrix.SpecialLinearGroup (Fin 4) K
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The even structure theorem](../../representation-theory/spin/the-even-structure-theorem.md)
- [The structure theorem in operator form](../../representation-theory/spin/the-structure-theorem-in-operator-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hyperbolicSixSpinEquivSpecialLinear`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/LowRank/Six/SpecialLinear.html#TauCeti.hyperbolicSixSpinEquivSpecialLinear).

## Sources

- [Tau Ceti documentation: `TauCeti.hyperbolicSixSpinEquivSpecialLinear`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/LowRank/Six/SpecialLinear.html#TauCeti.hyperbolicSixSpinEquivSpecialLinear)
- [Source of `TauCeti.hyperbolicSixSpinEquivSpecialLinear` in TauCeti/LinearAlgebra/CliffordAlgebra/Spin/LowRank/Six/SpecialLinear.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/LowRank/Six/SpecialLinear.lean#L1017)
- [Tau Ceti roadmap status: Orthogonal and spin groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/OrthogonalSpinGroups/STATUS.md)
