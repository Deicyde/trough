---
declaration: structure
origin: cited
lean: PolynomialLaw.IsMultiplicative
statement: formalized
---

# PolynomialLaw.IsMultiplicative

A polynomial law `f : A →ₚₗ[R] B` between `R`-algebras is multiplicative if `f 1 = 1` and
`f (x * y) = f x * f y` for every commutative `R`-algebra `S` and all `x y : S ⊗[R] A`. See
`IsMultiplicative.toFun_one` and `IsMultiplicative.toFun_mul` for algebras in other universes.

```lean
PolynomialLaw.IsMultiplicative.{u, u_1, u_2} {R : Type u} [CommSemiring R] {A : Type u_1}
  {B : Type u_2} [Semiring A] [Algebra R A] [Semiring B] [Algebra R B] (f : A →ₚₗ[R] B) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`PolynomialLaw.IsMultiplicative`](https://taucetiproject.org/docs/TauCeti/RingTheory/PolynomialLaw/Multiplicative.html#PolynomialLaw.IsMultiplicative).

## Sources

- [Tau Ceti documentation: `PolynomialLaw.IsMultiplicative`](https://taucetiproject.org/docs/TauCeti/RingTheory/PolynomialLaw/Multiplicative.html#PolynomialLaw.IsMultiplicative)
- [Source of `PolynomialLaw.IsMultiplicative` in TauCeti/RingTheory/PolynomialLaw/Multiplicative.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/PolynomialLaw/Multiplicative.lean#L68)
- [Tau Ceti roadmap status: Derived module algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DerivedModuleAlgebra/STATUS.md)
