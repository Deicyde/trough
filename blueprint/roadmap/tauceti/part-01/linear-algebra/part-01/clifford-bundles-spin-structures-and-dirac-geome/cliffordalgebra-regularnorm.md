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
- [Source of `CliffordAlgebra.regularNorm` in TauCeti/LinearAlgebra/CliffordAlgebra/Regular/Norm.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/CliffordAlgebra/Regular/Norm.lean#L38)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpinGeometry/STATUS.md)
