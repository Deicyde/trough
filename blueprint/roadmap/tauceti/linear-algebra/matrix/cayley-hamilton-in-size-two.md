---
declaration: theorem
origin: cited
lean: Matrix.sq_eq_trace_smul_sub_det_smul_one_fin_two, Matrix.Represents.aeval_charpoly_eq_zero, Matrix.pow_add_two_fin_two
statement: formalized
proof: formalized
---

# Cayley–Hamilton in size two

a `2 × 2` matrix `A` satisfies
`A ^ 2 = (trace A) • A - (det A) • 1`.

```lean
Matrix.sq_eq_trace_smul_sub_det_smul_one_fin_two.{u_1} {R : Type u_1} [CommRing R]
  (A : Matrix (Fin 2) (Fin 2) R) : A ^ 2 = A.trace • A - A.det • 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.sq_eq_trace_smul_sub_det_smul_one_fin_two`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Trace/FinTwo.html#Matrix.sq_eq_trace_smul_sub_det_smul_one_fin_two).

## Other forms

**Cayley–Hamilton along a representation.** Formalized in Tau Ceti as [`Matrix.Represents.aeval_charpoly_eq_zero`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Charpoly/LinearMap.html#Matrix.Represents.aeval_charpoly_eq_zero).

```lean
Matrix.Represents.aeval_charpoly_eq_zero.{u_1, u_2, u_3} {ι : Type u_1} [Fintype ι] [DecidableEq ι]
  {R : Type u_2} {M : Type u_3} [CommRing R] [AddCommGroup M] [_root_.Module R M] {b : ι → M}
  (hb : Submodule.span R (Set.range b) = ⊤) {A : Matrix ι ι R} {f : Module.End R M}
  (h : Matrix.Represents b A f) : (Polynomial.aeval f) A.charpoly = 0
```

**Cayley–Hamilton in size two, as a recurrence for the powers of a `2 × 2` matrix.** Formalized in Tau Ceti as [`Matrix.pow_add_two_fin_two`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Trace/FinTwo.html#Matrix.pow_add_two_fin_two).

```lean
Matrix.pow_add_two_fin_two.{u_1} {R : Type u_1} [CommRing R] (A : Matrix (Fin 2) (Fin 2) R)
  (n : ℕ) : A ^ (n + 2) = A.trace • A ^ (n + 1) - A.det • A ^ n
```

## Sources

- [Tau Ceti documentation: `Matrix.sq_eq_trace_smul_sub_det_smul_one_fin_two`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Trace/FinTwo.html#Matrix.sq_eq_trace_smul_sub_det_smul_one_fin_two)
- [Source of `Matrix.sq_eq_trace_smul_sub_det_smul_one_fin_two` in TauCeti/LinearAlgebra/Matrix/Trace/FinTwo.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/Matrix/Trace/FinTwo.lean#L91)
