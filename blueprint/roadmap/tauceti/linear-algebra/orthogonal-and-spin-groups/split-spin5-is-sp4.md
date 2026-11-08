---
declaration: theorem
origin: cited
lean: CliffordAlgebra.exists_spinGroupEquivSymplecticGroup_of_finrank_eq_five
statement: formalized
proof: formalized
---

# Split `Spin₅` is `Sp₄`

For a nondegenerate quadratic form on a five-dimensional space
whose even Clifford algebra splits, `C₀ ≃ M₄(K)`, the group `Spin(Q)` is isomorphic to the
symplectic group `Sp₄(K)`.

```lean
CliffordAlgebra.exists_spinGroupEquivSymplecticGroup_of_finrank_eq_five.{u_1, u_2} {K : Type u_1}
  {V : Type u_2} [Field K] [AddCommGroup V] [_root_.Module K V] [Invertible 2]
  (Q : QuadraticForm K V) (hQ : QuadraticMap.Nondegenerate) (hV : Module.finrank K V = 5)
  (hsplit : Nonempty (↥(CliffordAlgebra.even Q) ≃ₐ[K] Matrix (Fin 4) (Fin 4) K)) :
  Nonempty (↥(spinGroup Q) ≃* ↥(Matrix.symplecticGroup (Fin 2) K))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Skolem–Noether for matrix algebras over a local semiring](../matrix/skolem-noether-for-matrix-algebras-over-a-local.md)
- [Spin is the even unitary group in dimensions one to five](spin-is-the-even-unitary-group-in-dimensions-one.md)

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.exists_spinGroupEquivSymplecticGroup_of_finrank_eq_five`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/LowRank/Symplectic.html#CliffordAlgebra.exists_spinGroupEquivSymplecticGroup_of_finrank_eq_five).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.exists_spinGroupEquivSymplecticGroup_of_finrank_eq_five`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/LowRank/Symplectic.html#CliffordAlgebra.exists_spinGroupEquivSymplecticGroup_of_finrank_eq_five)
- [Source of `CliffordAlgebra.exists_spinGroupEquivSymplecticGroup_of_finrank_eq_five` in TauCeti/LinearAlgebra/CliffordAlgebra/Spin/LowRank/Symplectic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/LowRank/Symplectic.lean#L189)
- [Tau Ceti roadmap status: Orthogonal and spin groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/OrthogonalSpinGroups/STATUS.md)
