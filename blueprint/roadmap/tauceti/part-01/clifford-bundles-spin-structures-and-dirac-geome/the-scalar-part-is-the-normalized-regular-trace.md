---
declaration: theorem
origin: cited
lean: CliffordAlgebra.trace_mulLeft_eq_two_pow_mul_scalarTrace
statement: formalized
proof: formalized
---

# The scalar part is the normalized regular trace

over a field in which `2` is invertible,
for every quadratic form on a finite-dimensional space,
`trace (x * ·) = 2 ^ finrank K V * scalarTrace Q x`. Every such form has an orthogonal basis, so
`CliffordAlgebra.trace_mulLeft_eq_finrank_mul_scalarTrace` applies.

```lean
CliffordAlgebra.trace_mulLeft_eq_two_pow_mul_scalarTrace.{u, v} {K : Type u} {V : Type v} [Field K]
  [AddCommGroup V] [_root_.Module K V] [Invertible 2] [FiniteDimensional K V]
  {Q : QuadraticForm K V} (x : CliffordAlgebra Q) :
  (LinearMap.trace K (CliffordAlgebra Q)) (LinearMap.mulLeft K x) =
    2 ^ Module.finrank K V * (CliffordAlgebra.scalarTrace Q) x
```

## Depends on

- [CliffordAlgebra.scalarTrace](cliffordalgebra-scalartrace.md)

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.trace_mulLeft_eq_two_pow_mul_scalarTrace`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/ScalarTrace/Basic.html#CliffordAlgebra.trace_mulLeft_eq_two_pow_mul_scalarTrace).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.trace_mulLeft_eq_two_pow_mul_scalarTrace`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/ScalarTrace/Basic.html#CliffordAlgebra.trace_mulLeft_eq_two_pow_mul_scalarTrace)
- [Source of `CliffordAlgebra.trace_mulLeft_eq_two_pow_mul_scalarTrace` in TauCeti/LinearAlgebra/CliffordAlgebra/ScalarTrace/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/CliffordAlgebra/ScalarTrace/Basic.lean#L246)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SpinGeometry/STATUS.md)
