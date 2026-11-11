---
declaration: def
origin: cited
lean: CliffordAlgebra.orthogonalSpinorNorm
statement: formalized
---

# CliffordAlgebra.orthogonalSpinorNorm

The Clifford norm modulo squares, descended through the Lipschitz action to `O(Q)`.

```lean
CliffordAlgebra.orthogonalSpinorNorm.{u, v} {K : Type u} {V : Type v} [Field K] [AddCommGroup V]
  [_root_.Module K V] [FiniteDimensional K V] [Invertible 2] (Q : QuadraticForm K V)
  (hQ : QuadraticMap.Nondegenerate) :
  ↥(TauCeti.QuadraticMap.orthogonalGroup Q) →* Kˣ ⧸ Subgroup.square Kˣ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.orthogonalSpinorNorm`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/SpinorNorm/Basic.html#CliffordAlgebra.orthogonalSpinorNorm).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.orthogonalSpinorNorm`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/SpinorNorm/Basic.html#CliffordAlgebra.orthogonalSpinorNorm)
- [Source of `CliffordAlgebra.orthogonalSpinorNorm` in TauCeti/LinearAlgebra/CliffordAlgebra/Spin/SpinorNorm/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/SpinorNorm/Basic.lean#L97)
- [Tau Ceti roadmap status: Orthogonal and spin groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/OrthogonalSpinGroups/STATUS.md)
