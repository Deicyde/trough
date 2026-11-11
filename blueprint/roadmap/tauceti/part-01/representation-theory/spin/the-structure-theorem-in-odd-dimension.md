---
declaration: theorem
origin: cited
lean: CliffordAlgebra.nonempty_algEquiv_matrix_prod_of_finrank_eq_two_mul_add_one
statement: formalized
proof: formalized
---

# The structure theorem in odd dimension

over a separably closed field of characteristic not
two, the Clifford algebra of a nondegenerate quadratic form on a space of dimension `2 * l + 1` is
the product of two copies of the matrix algebra `M_{2^l}(F)`.

This is the odd-dimensional companion of
`CliffordAlgebra.nonempty_algEquiv_matrix_of_finrank_eq_two_mul`, and the two blocks are not an
artefact of the proof: the product displayed here has `(1, 0)` as a central idempotent other than
`0` and `1`, so the algebra is not simple, whereas in even dimension it is
(`TauCeti.SpinPolarizationData.isSimpleRing_cliffordAlgebra`).

```lean
CliffordAlgebra.nonempty_algEquiv_matrix_prod_of_finrank_eq_two_mul_add_one.{u, v} {F : Type u}
  [Field F] [NeZero 2] {V : Type v} [AddCommGroup V] [_root_.Module F V] {Q : QuadraticForm F V}
  [IsSepClosed F] {l : ℕ} (hQ : QuadraticMap.Nondegenerate) (hV : Module.finrank F V = 2 * l + 1) :
  Nonempty
    (CliffordAlgebra Q ≃ₐ[F]
      Matrix (Fin (2 ^ l)) (Fin (2 ^ l)) F × Matrix (Fin (2 ^ l)) (Fin (2 ^ l)) F)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.nonempty_algEquiv_matrix_prod_of_finrank_eq_two_mul_add_one`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/OddStructure.html#CliffordAlgebra.nonempty_algEquiv_matrix_prod_of_finrank_eq_two_mul_add_one).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.nonempty_algEquiv_matrix_prod_of_finrank_eq_two_mul_add_one`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/OddStructure.html#CliffordAlgebra.nonempty_algEquiv_matrix_prod_of_finrank_eq_two_mul_add_one)
- [Source of `CliffordAlgebra.nonempty_algEquiv_matrix_prod_of_finrank_eq_two_mul_add_one` in TauCeti/RepresentationTheory/Spin/OddStructure.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Spin/OddStructure.lean#L181)
