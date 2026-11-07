---
declaration: theorem
origin: cited
lean: Module.End.mk_trace_homogeneousSubmoduleMapₛₗ_mul_reverse_charpoly_of_pow_eq_one
statement: formalized
proof: formalized
---

# Module.End.mk\_trace\_homogeneousSubmoduleMapₛₗ\_mul\_reverse\_charpoly\_of\_pow\_eq\_one

**The graded trace formula for an endomorphism of finite order** of a finite-dimensional
vector space over an arbitrary field: if `f ^ n = 1` with `n` nonzero in `K`, then
`(∑ₘ tr(f | Symᵐ V) tᵐ) * det(1 - t f) = 1`.

No eigenvalue of `f` need lie in `K`: over an algebraic closure `f` becomes diagonalizable, and
both factors commute with scalar extension
(`Module.End.trace_homogeneousSubmoduleMapₛₗ_baseChange`, `LinearMap.charpoly_baseChange`).

```lean
Module.End.mk_trace_homogeneousSubmoduleMapₛₗ_mul_reverse_charpoly_of_pow_eq_one.{u_1, u_2}
  {K : Type u_1} {V : Type u_2} [Field K] [AddCommGroup V] [_root_.Module K V]
  [FiniteDimensional K V] {f : Module.End K V} {n : ℕ} (hn : ↑n ≠ 0) (hf : f ^ n = 1) :
  (PowerSeries.mk fun m =>
        (LinearMap.trace K ↥(TauCeti.SymmetricAlgebra.homogeneousSubmodule K V m))
          (TauCeti.SymmetricAlgebra.homogeneousSubmoduleMapₛₗ f m)) *
      ↑(LinearMap.charpoly f).reverse =
    1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Module.End.mk_trace_homogeneousSubmoduleMapₛₗ_mul_reverse_charpoly_of_pow_eq_one`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/SymmetricAlgebra/Trace.html#Module.End.mk_trace_homogeneousSubmoduleMap%E2%82%9B%E2%82%97_mul_reverse_charpoly_of_pow_eq_one).

## Sources

- [Tau Ceti documentation: `Module.End.mk_trace_homogeneousSubmoduleMapₛₗ_mul_reverse_charpoly_of_pow_eq_one`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/SymmetricAlgebra/Trace.html#Module.End.mk_trace_homogeneousSubmoduleMap%E2%82%9B%E2%82%97_mul_reverse_charpoly_of_pow_eq_one)
- [Source of `Module.End.mk_trace_homogeneousSubmoduleMapₛₗ_mul_reverse_charpoly_of_pow_eq_one` in TauCeti/LinearAlgebra/SymmetricAlgebra/Trace.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/SymmetricAlgebra/Trace.lean#L202)
- [Tau Ceti roadmap status: Finite reflection invariants, degrees, and Weyl exponents](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ReflectionInvariantTheory/STATUS.md)
