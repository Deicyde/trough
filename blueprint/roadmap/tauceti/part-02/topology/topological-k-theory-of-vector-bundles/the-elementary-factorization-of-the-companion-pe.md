---
declaration: theorem
origin: cited
lean: TauCeti.companionPencil_eq_mul
statement: formalized
proof: formalized
---

# The elementary factorization of the companion pencil

For a polynomial of degree at most
`d`, the companion pencil is `diagonal (1, …, 1, p(z))` multiplied on the left by the elementary
row operations with multipliers `(divX^[d - k] p)(z)` and on the right by the upper
unitriangular matrix `1 - z • N`.

```lean
TauCeti.companionPencil_eq_mul.{u_1} {A : Type u_1} [Ring A] {d : ℕ} {p : Polynomial A}
  (hp : p.natDegree ≤ d) (z : A) :
  TauCeti.companionPencil d p z =
    (TauCeti.lastRowTransvection d fun k => Polynomial.eval z (Polynomial.divX^[d - ↑k] p)) *
        Matrix.diagonal (Fin.snoc 1 (Polynomial.eval z p)) *
      (1 - z • TauCeti.superdiagonalShift (d + 1))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.companionPencil_eq_mul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/CompanionPencil.html#TauCeti.companionPencil_eq_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.companionPencil_eq_mul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/CompanionPencil.html#TauCeti.companionPencil_eq_mul)
- [Source of `TauCeti.companionPencil_eq_mul` in TauCeti/LinearAlgebra/Matrix/CompanionPencil.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/Matrix/CompanionPencil.lean#L107)
- [Tau Ceti roadmap status: Topological K-theory of vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TopologicalKTheory/STATUS.md)
