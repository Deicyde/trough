---
declaration: def
origin: cited
lean: CliffordAlgebra.spinGroupEquivNeg
statement: formalized
---

# CliffordAlgebra.spinGroupEquivNeg

The Spin groups of `Q` and `-Q` are isomorphic, through Mathlib's identification
`evenEquivEvenNeg` of their even Clifford algebras. A product of two vectors `ι Q a * ι Q b` goes to
`-(ι (-Q) a * ι (-Q) b)`, and the vector actions agree.

```lean
CliffordAlgebra.spinGroupEquivNeg.{u, v} {R : Type u} {M : Type v} [CommRing R] [AddCommGroup M]
  [_root_.Module R M] (Q : QuadraticForm R M) [Invertible 2] : ↥(spinGroup Q) ≃* ↥(spinGroup (-Q))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.spinGroupEquivNeg`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/Neg.html#CliffordAlgebra.spinGroupEquivNeg).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.spinGroupEquivNeg`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/Neg.html#CliffordAlgebra.spinGroupEquivNeg)
- [Source of `CliffordAlgebra.spinGroupEquivNeg` in TauCeti/LinearAlgebra/CliffordAlgebra/Spin/Neg.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/Neg.lean#L144)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SpinGeometry/STATUS.md)
