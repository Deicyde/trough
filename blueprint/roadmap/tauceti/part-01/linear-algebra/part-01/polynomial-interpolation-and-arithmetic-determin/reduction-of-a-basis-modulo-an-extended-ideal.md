---
declaration: def
origin: cited
lean: Module.Basis.quotient
statement: formalized
---

# Reduction of a basis modulo an extended ideal

For an arbitrary ideal `J` of `R`, the
classes of a basis of `A` over `R` form a basis of `A ⧸ J A` over `R ⧸ J`: the base change of `b`
to `R ⧸ J`, transported along `Algebra.TensorProduct.quotIdealMapEquivQuotTensor`.

```lean
Module.Basis.quotient.{u_1, u_2, u_4} {R : Type u_1} {A : Type u_2} {ι : Type u_4} [CommRing R]
  [CommRing A] [Algebra R A] (b : Module.Basis ι R A) (J : Ideal R) :
  Module.Basis ι (R ⧸ J) (A ⧸ Ideal.map (algebraMap R A) J)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Module.Basis.quotient`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Basis/ExtendedIdeal.html#Module.Basis.quotient).

## Sources

- [Tau Ceti documentation: `Module.Basis.quotient`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Basis/ExtendedIdeal.html#Module.Basis.quotient)
- [Source of `Module.Basis.quotient` in TauCeti/LinearAlgebra/Basis/ExtendedIdeal.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/Basis/ExtendedIdeal.lean#L87)
- [Tau Ceti roadmap status: Polynomial interpolation and arithmetic determinants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ArithmeticInterpolationDeterminants/STATUS.md)
