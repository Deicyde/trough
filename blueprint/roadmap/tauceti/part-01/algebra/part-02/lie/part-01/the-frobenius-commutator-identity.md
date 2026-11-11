---
declaration: theorem
origin: cited
lean: TauCeti.LieAlgebra.ad_pow_expChar_pow
statement: formalized
proof: formalized
---

# The Frobenius commutator identity

In exponential characteristic `p`, taking the
`p ^ n`-th power in the algebra `A` and iterating the commutator `p ^ n` times in
`Module.End R A` give the same endomorphism.

```lean
TauCeti.LieAlgebra.ad_pow_expChar_pow.{u_1, u_2} {R : Type u_1} {A : Type u_2} [CommRing R] [Ring A]
  [Algebra R A] (p : ℕ) [ExpChar A p] (a : A) (n : ℕ) :
  (LieAlgebra.ad R A) (a ^ p ^ n) = (LieAlgebra.ad R A) a ^ p ^ n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LieAlgebra.ad_pow_expChar_pow`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/AdjointAction/Frobenius.html#TauCeti.LieAlgebra.ad_pow_expChar_pow).

## Sources

- [Tau Ceti documentation: `TauCeti.LieAlgebra.ad_pow_expChar_pow`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/AdjointAction/Frobenius.html#TauCeti.LieAlgebra.ad_pow_expChar_pow)
- [Source of `TauCeti.LieAlgebra.ad_pow_expChar_pow` in TauCeti/Algebra/Lie/AdjointAction/Frobenius.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/AdjointAction/Frobenius.lean#L72)
