---
declaration: theorem
origin: cited
lean: CliffordAlgebra.range_spinToSpecialOrthogonal_eq_ker_spinorNorm
statement: formalized
proof: formalized
---

# CliffordAlgebra.range_spinToSpecialOrthogonal_eq_ker_spinorNorm

The image of the Spin action on `SO(Q)` is exactly the kernel of the spinor norm.

```lean
CliffordAlgebra.range_spinToSpecialOrthogonal_eq_ker_spinorNorm.{u, v} {K : Type u} {V : Type v}
  [Field K] [AddCommGroup V] [_root_.Module K V] [FiniteDimensional K V] [Invertible 2]
  (Q : QuadraticForm K V) (hQ : QuadraticMap.Nondegenerate) :
  (CliffordAlgebra.spinToSpecialOrthogonal Q).range = (CliffordAlgebra.spinorNorm Q hQ).ker
```

## Depends on

- [CliffordAlgebra.orthogonalSpinorNorm](cliffordalgebra-orthogonalspinornorm.md)

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.range_spinToSpecialOrthogonal_eq_ker_spinorNorm`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/SpinorNorm/Basic.html#CliffordAlgebra.range_spinToSpecialOrthogonal_eq_ker_spinorNorm).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.range_spinToSpecialOrthogonal_eq_ker_spinorNorm`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/SpinorNorm/Basic.html#CliffordAlgebra.range_spinToSpecialOrthogonal_eq_ker_spinorNorm)
- [Source of `CliffordAlgebra.range_spinToSpecialOrthogonal_eq_ker_spinorNorm` in TauCeti/LinearAlgebra/CliffordAlgebra/Spin/SpinorNorm/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/SpinorNorm/Basic.lean#L211)
- [Tau Ceti roadmap status: Orthogonal and spin groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/OrthogonalSpinGroups/STATUS.md)
