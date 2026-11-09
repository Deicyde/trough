---
declaration: def
origin: cited
lean: CliffordAlgebra.conjStar
statement: formalized
---

# CliffordAlgebra.conjStar

The conjugate-linear Clifford involution of the complexified Clifford algebra: Clifford
conjugation `star = reverse ∘ involute` followed by complex conjugation of the coefficients. It
is an involutive anti-automorphism (`CliffordAlgebra.conjStar_mul`,
`CliffordAlgebra.conjStar_conjStar`) negating the real vectors.

```lean
CliffordAlgebra.conjStar.{u_1} {V : Type u_1} [AddCommGroup V] [_root_.Module ℝ V]
  (Q : QuadraticForm ℝ V) :
  CliffordAlgebra (QuadraticForm.baseChange ℂ Q) →ₗ⋆[ℂ]
    CliffordAlgebra (QuadraticForm.baseChange ℂ Q)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.conjStar`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Complexification.html#CliffordAlgebra.conjStar).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.conjStar`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Complexification.html#CliffordAlgebra.conjStar)
- [Source of `CliffordAlgebra.conjStar` in TauCeti/LinearAlgebra/CliffordAlgebra/Complexification.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/CliffordAlgebra/Complexification.lean#L196)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SpinGeometry/STATUS.md)
