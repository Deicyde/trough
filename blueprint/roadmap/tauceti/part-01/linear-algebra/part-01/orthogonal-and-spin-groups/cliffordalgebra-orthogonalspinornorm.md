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
- [Source of `CliffordAlgebra.orthogonalSpinorNorm` in TauCeti/LinearAlgebra/CliffordAlgebra/Spin/SpinorNorm/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/SpinorNorm/Basic.lean#L97)
- [Tau Ceti roadmap status: Orthogonal and spin groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/OrthogonalSpinGroups/STATUS.md)
