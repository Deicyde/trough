---
declaration: theorem
origin: cited
lean: TauCeti.Cocharacter.exists_mem_unipotent_mem_levi
statement: formalized
proof: formalized
---

# The dynamic Levi decomposition, on points

every point of the dynamic parabolic is a
point of its unipotent part times a point of its Levi part.

```lean
TauCeti.Cocharacter.exists_mem_unipotent_mem_levi.{u_1, u_2, u_3} {R : Type u_1} {H : Type u_2}
  {A : Type u_3} [CommSemiring R] [Semiring H] [CommSemiring A] [Algebra R A] [HopfAlgebra R H]
  {l : H →ₐc[R] LaurentPolynomial R} {g : WithConv (H →ₐ[R] A)}
  (hg : g ∈ TauCeti.Cocharacter.parabolic A l) :
  ∃ u ∈ TauCeti.Cocharacter.unipotent A l, ∃ z ∈ TauCeti.Cocharacter.levi A l, g = u * z
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Cocharacter.exists_mem_unipotent_mem_levi`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Dynamic/Parabolic.html#TauCeti.Cocharacter.exists_mem_unipotent_mem_levi).

## Sources

- [Tau Ceti documentation: `TauCeti.Cocharacter.exists_mem_unipotent_mem_levi`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Dynamic/Parabolic.html#TauCeti.Cocharacter.exists_mem_unipotent_mem_levi)
- [Source of `TauCeti.Cocharacter.exists_mem_unipotent_mem_levi` in TauCeti/Algebra/AlgebraicGroup/Dynamic/Parabolic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/AlgebraicGroup/Dynamic/Parabolic.lean#L584)
