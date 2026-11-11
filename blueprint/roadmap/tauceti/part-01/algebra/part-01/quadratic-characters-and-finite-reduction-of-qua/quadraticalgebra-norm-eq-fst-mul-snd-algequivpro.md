---
declaration: theorem
origin: cited
lean: QuadraticAlgebra.norm_eq_fst_mul_snd_algEquivProdOfSq
statement: formalized
proof: formalized
---

# QuadraticAlgebra.norm_eq_fst_mul_snd_algEquivProdOfSq

In the unit-square splitting, the norm is the product of the two coordinates.

```lean
QuadraticAlgebra.norm_eq_fst_mul_snd_algEquivProdOfSq.{u_1} {R : Type u_1} [CommRing R]
  [Invertible 2] {a : R} (u : Rˣ) (ha : a = ↑u ^ 2) (z : QuadraticAlgebra R a 0) :
  QuadraticAlgebra.norm z =
    ((QuadraticAlgebra.algEquivProdOfSq u ha) z).1 * ((QuadraticAlgebra.algEquivProdOfSq u ha) z).2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`QuadraticAlgebra.norm_eq_fst_mul_snd_algEquivProdOfSq`](https://taucetiproject.org/docs/TauCeti/Algebra/QuadraticAlgebra/Split.html#QuadraticAlgebra.norm_eq_fst_mul_snd_algEquivProdOfSq).

## Sources

- [Tau Ceti documentation: `QuadraticAlgebra.norm_eq_fst_mul_snd_algEquivProdOfSq`](https://taucetiproject.org/docs/TauCeti/Algebra/QuadraticAlgebra/Split.html#QuadraticAlgebra.norm_eq_fst_mul_snd_algEquivProdOfSq)
- [Source of `QuadraticAlgebra.norm_eq_fst_mul_snd_algEquivProdOfSq` in TauCeti/Algebra/QuadraticAlgebra/Split.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/QuadraticAlgebra/Split.lean#L111)
- [Tau Ceti roadmap status: Quadratic characters and finite reduction of quadratic orders](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuadraticCharactersAndReduction/STATUS.md)
