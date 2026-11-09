---
declaration: theorem
origin: cited
lean: IsSimpleRing.exists_algEquiv_matrix_of_isSepClosed
statement: formalized
proof: formalized
---

# Artin--Wedderburn over a separably closed field

A finite-dimensional central simple
`K`-algebra is a full matrix algebra over `K`.

```lean
IsSimpleRing.exists_algEquiv_matrix_of_isSepClosed.{u, u_1} (K : Type u_1) [Field K] [IsSepClosed K]
  (A : Type u) [Ring A] [Algebra K A] [Algebra.IsCentral K A] [IsSimpleRing A]
  [FiniteDimensional K A] :
  ∃ n, ∃ (_ : NeZero n), Module.finrank K A = n ^ 2 ∧ Nonempty (A ≃ₐ[K] Matrix (Fin n) (Fin n) K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Wedderburn-Artin for central simple algebras](wedderburn-artin-for-central-simple-algebras.md)

## Lean

Formalized in Tau Ceti as [`IsSimpleRing.exists_algEquiv_matrix_of_isSepClosed`](https://taucetiproject.org/docs/TauCeti/Algebra/CentralSimple/SeparablyClosed.html#IsSimpleRing.exists_algEquiv_matrix_of_isSepClosed).

## Sources

- [Tau Ceti documentation: `IsSimpleRing.exists_algEquiv_matrix_of_isSepClosed`](https://taucetiproject.org/docs/TauCeti/Algebra/CentralSimple/SeparablyClosed.html#IsSimpleRing.exists_algEquiv_matrix_of_isSepClosed)
- [Source of `IsSimpleRing.exists_algEquiv_matrix_of_isSepClosed` in TauCeti/Algebra/CentralSimple/SeparablyClosed.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/CentralSimple/SeparablyClosed.lean#L107)
