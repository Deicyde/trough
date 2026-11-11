---
declaration: theorem
origin: cited
lean: CliffordAlgebra.nonempty_algEquiv_matrix_of_finrank_eq_two_mul
statement: formalized
proof: formalized
---

# The structure theorem over a separably closed field

the Clifford algebra of a
nondegenerate quadratic form on a `2l`-dimensional space is the matrix algebra `M_{2^l}(F)`.

The isomorphism is not canonical — it is read in a basis of the spinor module of a polarization,
and neither the polarization nor the basis is unique — so the statement is `Nonempty`. The
polarization-dependent isomorphism itself is
`TauCeti.SpinPolarizationData.cliffordEquivMatrix`.

```lean
CliffordAlgebra.nonempty_algEquiv_matrix_of_finrank_eq_two_mul.{u, v} {F : Type u} [Field F]
  [NeZero 2] {V : Type v} [AddCommGroup V] [_root_.Module F V] [FiniteDimensional F V]
  {Q : QuadraticForm F V} [IsSepClosed F] {l : ℕ} (hQ : QuadraticMap.Nondegenerate)
  (hV : Module.finrank F V = 2 * l) :
  Nonempty (CliffordAlgebra Q ≃ₐ[F] Matrix (Fin (2 ^ l)) (Fin (2 ^ l)) F)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The structure theorem](the-structure-theorem.md)

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.nonempty_algEquiv_matrix_of_finrank_eq_two_mul`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/Structure.html#CliffordAlgebra.nonempty_algEquiv_matrix_of_finrank_eq_two_mul).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.nonempty_algEquiv_matrix_of_finrank_eq_two_mul`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/Structure.html#CliffordAlgebra.nonempty_algEquiv_matrix_of_finrank_eq_two_mul)
- [Source of `CliffordAlgebra.nonempty_algEquiv_matrix_of_finrank_eq_two_mul` in TauCeti/RepresentationTheory/Spin/Structure.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Spin/Structure.lean#L441)
