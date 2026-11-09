---
declaration: theorem
origin: cited
lean: IsSimpleRing.exists_algEquiv_matrix_centralDivisionRing
statement: formalized
proof: formalized
---

# Wedderburn-Artin for central simple algebras

A finite-dimensional central simple
`K`-algebra `A` is isomorphic to a matrix algebra over a finite-dimensional **central** division
`K`-algebra `D`, and then `finrank K A = n ^ 2 * finrank K D`.

Mathlib's `IsSimpleRing.exists_algEquiv_matrix_divisionRing_finite` supplies everything except the
centrality of `D`, which comes from `TauCeti.Algebra.IsCentral.of_matrix`.

```lean
IsSimpleRing.exists_algEquiv_matrix_centralDivisionRing.{u, u_1} (K : Type u_1) [Field K]
  (A : Type u) [Ring A] [Algebra K A] [Algebra.IsCentral K A] [IsSimpleRing A]
  [FiniteDimensional K A] :
  ∃ n,
    ∃ (_ : NeZero n),
      ∃ D x x_1,
        ∃ (_ : Algebra.IsCentral K D) (_ : FiniteDimensional K D),
          Module.finrank K A = n ^ 2 * Module.finrank K D ∧
            Nonempty (A ≃ₐ[K] Matrix (Fin n) (Fin n) D)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsSimpleRing.exists_algEquiv_matrix_centralDivisionRing`](https://taucetiproject.org/docs/TauCeti/Algebra/CentralSimple/Wedderburn.html#IsSimpleRing.exists_algEquiv_matrix_centralDivisionRing).

## Sources

- [Tau Ceti documentation: `IsSimpleRing.exists_algEquiv_matrix_centralDivisionRing`](https://taucetiproject.org/docs/TauCeti/Algebra/CentralSimple/Wedderburn.html#IsSimpleRing.exists_algEquiv_matrix_centralDivisionRing)
- [Source of `IsSimpleRing.exists_algEquiv_matrix_centralDivisionRing` in TauCeti/Algebra/CentralSimple/Wedderburn.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/CentralSimple/Wedderburn.lean#L85)
