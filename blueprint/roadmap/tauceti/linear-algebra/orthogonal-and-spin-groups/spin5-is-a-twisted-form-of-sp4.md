---
declaration: theorem
origin: cited
lean: CliffordAlgebra.exists_injective_spinGroup_symplecticGroup_of_finrank_eq_five
statement: formalized
proof: formalized
---

# `Spin₅` is a twisted form of `Sp₄`

For a nondegenerate quadratic form on a
five-dimensional space and any separably closed extension `L / K`, there are a splitting
`e : C₀ ⊗ L ≃ M₄(L)` carrying reversal to the symplectic adjoint and an injective homomorphism
`f : Spin(Q) → Sp₄(L)` with `e⁻¹ (f s)` the scalar extension of `s`. Its image consists of exactly
those symplectic matrices `g` for which `e⁻¹ g` comes from `C₀`, so `Spin(Q)` is the group
`Sp(C₀, σ)` of `K`-rational points of `Sp₄(L)` for the `K`-structure `C₀ ⊆ C₀ ⊗ L`.

```lean
CliffordAlgebra.exists_injective_spinGroup_symplecticGroup_of_finrank_eq_five.{u_1, u_2, u_4}
  {K : Type u_1} {V : Type u_2} [Field K] [AddCommGroup V] [_root_.Module K V] [Invertible 2]
  (L : Type u_4) [Field L] [Algebra K L] [IsSepClosed L] (Q : QuadraticForm K V)
  (hQ : QuadraticMap.Nondegenerate) (hV : Module.finrank K V = 5) :
  ∃ e f,
    Function.Injective ⇑f ∧
      (∀ (s : ↥(spinGroup Q)), ↑(e.symm ↑(f s)) = (CliffordAlgebra.ofBaseChangeAux L Q) ↑s) ∧
        ∀ (g : ↥(Matrix.symplecticGroup (Fin 2) L)),
          g ∈ f.range ↔
            ∃ y ∈ CliffordAlgebra.even Q, (CliffordAlgebra.ofBaseChangeAux L Q) y = ↑(e.symm ↑g)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Artin--Wedderburn over a separably closed field](../../algebra/central-simple/artin-wedderburn-over-a-separably-closed-field.md)
- [Skolem–Noether for matrix algebras over a local semiring](../matrix/skolem-noether-for-matrix-algebras-over-a-local.md)
- [Spin is the even unitary group in dimensions one to five](spin-is-the-even-unitary-group-in-dimensions-one.md)
- [The structure theorem in operator form](../../representation-theory/spin/the-structure-theorem-in-operator-form.md)

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.exists_injective_spinGroup_symplecticGroup_of_finrank_eq_five`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/LowRank/Symplectic.html#CliffordAlgebra.exists_injective_spinGroup_symplecticGroup_of_finrank_eq_five).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.exists_injective_spinGroup_symplecticGroup_of_finrank_eq_five`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/LowRank/Symplectic.html#CliffordAlgebra.exists_injective_spinGroup_symplecticGroup_of_finrank_eq_five)
- [Source of `CliffordAlgebra.exists_injective_spinGroup_symplecticGroup_of_finrank_eq_five` in TauCeti/LinearAlgebra/CliffordAlgebra/Spin/LowRank/Symplectic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/LowRank/Symplectic.lean#L230)
- [Tau Ceti roadmap status: Orthogonal and spin groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/OrthogonalSpinGroups/STATUS.md)
