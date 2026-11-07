---
declaration: def
origin: cited
lean: CliffordAlgebra.scalarTrace
statement: formalized
---

# CliffordAlgebra.scalarTrace

The **scalar part** of an element of a Clifford algebra: its degree-zero component under the
module isomorphism `CliffordAlgebra.equivExterior` with the exterior algebra.

```lean
CliffordAlgebra.scalarTrace.{u, v} {R : Type u} {M : Type v} [CommRing R] [AddCommGroup M]
  [_root_.Module R M] [Invertible 2] (Q : QuadraticForm R M) : CliffordAlgebra Q →ₗ[R] R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.scalarTrace`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/ScalarTrace/Basic.html#CliffordAlgebra.scalarTrace).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.scalarTrace`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/ScalarTrace/Basic.html#CliffordAlgebra.scalarTrace)
- [Source of `CliffordAlgebra.scalarTrace` in TauCeti/LinearAlgebra/CliffordAlgebra/ScalarTrace/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/CliffordAlgebra/ScalarTrace/Basic.lean#L100)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SpinGeometry/STATUS.md)
