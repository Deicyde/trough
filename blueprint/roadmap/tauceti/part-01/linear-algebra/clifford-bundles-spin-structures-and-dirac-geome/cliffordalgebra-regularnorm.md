---
declaration: def
origin: cited
lean: CliffordAlgebra.regularNorm
statement: formalized
---

# CliffordAlgebra.regularNorm

The intrinsic Euclidean norm of a real Clifford element for negative definite `Q`.
It is the square root of its scalar-part squared length.

```lean
CliffordAlgebra.regularNorm.{u_1} {V : Type u_1} [AddCommGroup V] [_root_.Module ℝ V]
  (Q : QuadraticForm ℝ V) (x : CliffordAlgebra Q) : ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.regularNorm`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Regular/Norm.html#CliffordAlgebra.regularNorm).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.regularNorm`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Regular/Norm.html#CliffordAlgebra.regularNorm)
- [Source of `CliffordAlgebra.regularNorm` in TauCeti/LinearAlgebra/CliffordAlgebra/Regular/Norm.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/CliffordAlgebra/Regular/Norm.lean#L38)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SpinGeometry/STATUS.md)
