---
declaration: theorem
origin: cited
lean: CliffordAlgebra.range_spinToSpecialOrthogonal_eq_ker_spinorNorm
statement: formalized
proof: formalized
---

# CliffordAlgebra.range\_spinToSpecialOrthogonal\_eq\_ker\_spinorNorm

The image of the Spin action on `SO(Q)` is exactly the kernel of the spinor norm.

```lean
CliffordAlgebra.range_spinToSpecialOrthogonal_eq_ker_spinorNorm.{u, v} {K : Type u} {V : Type v}
  [Field K] [AddCommGroup V] [_root_.Module K V] [FiniteDimensional K V] [Invertible 2]
  (Q : QuadraticForm K V) (hQ : QuadraticMap.Nondegenerate) :
  (CliffordAlgebra.spinToSpecialOrthogonal Q).range = (CliffordAlgebra.spinorNorm Q hQ).ker
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.range_spinToSpecialOrthogonal_eq_ker_spinorNorm`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/SpinorNorm/Basic.html#CliffordAlgebra.range_spinToSpecialOrthogonal_eq_ker_spinorNorm).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.range_spinToSpecialOrthogonal_eq_ker_spinorNorm`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/SpinorNorm/Basic.html#CliffordAlgebra.range_spinToSpecialOrthogonal_eq_ker_spinorNorm)
- [Source of `CliffordAlgebra.range_spinToSpecialOrthogonal_eq_ker_spinorNorm` in TauCeti/LinearAlgebra/CliffordAlgebra/Spin/SpinorNorm/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/SpinorNorm/Basic.lean#L211)
- [Tau Ceti roadmap status: Orthogonal and spin groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/OrthogonalSpinGroups/STATUS.md)
