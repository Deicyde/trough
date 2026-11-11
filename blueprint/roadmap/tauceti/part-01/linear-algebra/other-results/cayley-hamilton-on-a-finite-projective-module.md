---
declaration: theorem
origin: cited
lean: LinearMap.exists_aeval_reflect_projectiveCharpolyRev_eq_zero
statement: formalized
proof: formalized
---

# Cayley–Hamilton on a finite projective module

For some `n` bounding the degree of the
reversed characteristic polynomial `Q` of `f`, the reflection `X ^ n · Q(1/X)` of `Q` kills `f`;
it is monic (`monic_reflect_projectiveCharpolyRev`).

```lean
LinearMap.exists_aeval_reflect_projectiveCharpolyRev_eq_zero.{u_1, u_2} {R : Type u_1}
  {M : Type u_2} [CommRing R] [AddCommGroup M] [_root_.Module R M] [Module.Finite R M]
  [Module.Projective R M] (f : Module.End R M) :
  ∃ n,
    (LinearMap.projectiveCharpolyRev f).natDegree ≤ n ∧
      (Polynomial.aeval f) (Polynomial.reflect n (LinearMap.projectiveCharpolyRev f)) = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.exists_aeval_reflect_projectiveCharpolyRev_eq_zero`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Charpoly/Projective.html#LinearMap.exists_aeval_reflect_projectiveCharpolyRev_eq_zero).

## Sources

- [Tau Ceti documentation: `LinearMap.exists_aeval_reflect_projectiveCharpolyRev_eq_zero`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Charpoly/Projective.html#LinearMap.exists_aeval_reflect_projectiveCharpolyRev_eq_zero)
- [Source of `LinearMap.exists_aeval_reflect_projectiveCharpolyRev_eq_zero` in TauCeti/LinearAlgebra/Charpoly/Projective.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/Charpoly/Projective.lean#L251)
