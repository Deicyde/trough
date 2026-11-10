---
declaration: theorem
origin: cited
lean: Matrix.GeneralLinearGroup.innerAut_surjective
statement: formalized
proof: formalized
---

# Skolem–Noether for matrix algebras over a local semiring

every algebra automorphism of a
matrix algebra over a commutative local semiring, in particular over a field, is inner.

```lean
Matrix.GeneralLinearGroup.innerAut_surjective.{u_1, u_2} {n : Type u_1} [Fintype n] [DecidableEq n]
  (K : Type u_2) [CommSemiring K] [IsLocalRing K] :
  Function.Surjective ⇑Matrix.GeneralLinearGroup.innerAut
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.GeneralLinearGroup.innerAut_surjective`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/GeneralLinearGroup/InnerAut.html#Matrix.GeneralLinearGroup.innerAut_surjective).

## Sources

- [Tau Ceti documentation: `Matrix.GeneralLinearGroup.innerAut_surjective`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/GeneralLinearGroup/InnerAut.html#Matrix.GeneralLinearGroup.innerAut_surjective)
- [Source of `Matrix.GeneralLinearGroup.innerAut_surjective` in TauCeti/LinearAlgebra/Matrix/GeneralLinearGroup/InnerAut.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/Matrix/GeneralLinearGroup/InnerAut.lean#L228)
